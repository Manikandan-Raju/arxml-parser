from xml.etree import ElementTree
from typing import List
from .container import Container
from .export_database import get_database

import logging
logging.basicConfig(level=logging.INFO)


class arxml_parsing:

    def __init__(self, arxml_path, db_path) -> None:
        """Constructor for arxml_parsing"""
        self.arxml_path = arxml_path
        self.schema = "http://autosar.org/schema/r4.0"
        self.namespace = {"as": self.schema}
        self.root = ElementTree.parse(self.arxml_path)
        self.database: List[Container] = []
        self.extract_containers()
        get_database(self.database,db_path)

    def extract_containers(self):
        ecu_name = self.root.find(
            "as:AR-PACKAGES/as:AR-PACKAGE/as:SHORT-NAME", self.namespace
        ).text
        ELEMENTS = "as:AR-PACKAGES/as:AR-PACKAGE/as:ELEMENTS/as:ECUC-MODULE-CONFIGURATION-VALUES"
        for ele in self.root.findall(ELEMENTS, self.namespace):
            config_value = next(
                iter(c.text for c in ele if c.tag == f"{{{self.schema}}}SHORT-NAME")
            )
            CONTAINER_VALUE = "as:CONTAINERS/as:ECUC-CONTAINER-VALUE"
            for cont in ele.findall(CONTAINER_VALUE, self.namespace):
                container_name = next(
                    iter(
                        c.text for c in cont if c.tag == f"{{{self.schema}}}SHORT-NAME"
                    )
                )
                definition_ref = next(
                    iter(
                        c.text
                        for c in cont
                        if c.tag == f"{{{self.schema}}}DEFINITION-REF"
                    )
                )
                SUB_CONTAINERS = "as:SUB-CONTAINERS/as:ECUC-CONTAINER-VALUE"
                sub_cont = cont.find("as:SUB-CONTAINERS", self.namespace)
                if sub_cont is not None:
                    for sub_cont in cont.findall(SUB_CONTAINERS, self.namespace):
                        sub_container_name = next(
                            iter(
                                c.text
                                for c in sub_cont
                                if c.tag == f"{{{self.schema}}}SHORT-NAME"
                            )
                        )
                        sub_definition_ref = next(
                            iter(
                                c.text
                                for c in sub_cont
                                if c.tag == f"{{{self.schema}}}DEFINITION-REF"
                            )
                        ).split("/")[-1]
                        container = Container(
                            ecu_name,
                            config_value,
                            container_name,
                            definition_ref,
                            sub_container_name,
                            sub_definition_ref,
                        )
                        self.database.append(container)
                else:
                    container = Container(
                        ecu_name,
                        config_value,
                        container_name,
                        definition_ref,
                        None,
                        None,
                    )
                    self.database.append(container)
        logging.info("Containers and sub containers extracted")

