#!/bin/bash

exec python3 manipulate_string.py  --string "He Is A gOoD bOy" &
exec python3 parser_gui.py --arxml ./AutosarFile.xml --excel ~ 