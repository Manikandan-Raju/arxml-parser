import argparse
import os
from app.arxml_parsing import arxml_parsing

import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    cmd_parser = argparse.ArgumentParser(allow_abbrev=False)
    cmd_parser.add_argument(
        "--arxml",
        type=str,
        nargs="?",
        default="AutosarFile.arxml",
        help="Enter ARXML path",
    )
    cmd_parser.add_argument(
        "--excel", type=str, nargs="?", default="db/", help="Enter Excel path"
    )
    args = cmd_parser.parse_args()

    if os.path.isfile(str(args.arxml)) and os.path.isdir(str(args.excel)):
        logging.info("Starting ARXML Parser tool")
        arxml_parsing(args.arxml, args.excel)
    else:
        logging.error("%s and %s not proper",args.arxml, args.excel)
    logging.info("DONE")
