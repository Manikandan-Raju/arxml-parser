from dataclasses import dataclass, field


@dataclass
class Container:
    ecu_name: str = field(default_factory=str)
    config_value: str = field(default_factory=str)
    container_name: str = field(default_factory=str)
    definition_ref: str = field(default_factory=str)
    sub_container_name: str = field(default_factory=str)
    sub_definition_ref: str = field(default_factory=str)
