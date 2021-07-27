#!/usr/bin/python3
""" Cytiva SVG to PNG Exporter

This script takes all vector files of SVG format in a folder and exports them to PNG in a variety of sizes and
colours, found in 'lists.py'.

You can supply an additional 'Colour to Replace' argument using a hex colour format, such as:

-$ python3 iconGenerator.py #BADA55
-$ python3 iconGenerator.py bada55
-$ python3 iconGenerator.py 000000

"""

__author__ = "Danny Taylor"
__version__ = "0.1.0"

import codecs
import cairosvg
import glob
import os
import sys
import re
from pathlib import Path

from lists import colours, sizes


def validHexCode(hexCode):
    # CHECK IF ARGUMENT STARTS WITH A '#', ADD ONE IF NOT
    if hexCode[0] != "#":
        print("A hex colour must start with a '#' symbol, for example: #BADA55")
        print("Please try again.")
        return
        # TODO: Add a '#' automatically and avoid this error: 'invalid literal for int() with base 16'

    if len(hexCode) < 7:
        print("Error: Please try again with a 6-digit hex code, i.e. 'BADA55' or '#000000'")
        return

    # REGEX FOR HEX CODES
    regex = "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"

    # COMPILE THE REGEX
    check = re.compile(regex)

    # COMPARE THE COMPILED REGEX TO THE STRING
    if re.search(check, hexCode):
        return True
    else:
        print("Error:", hexCode, "is not a valid Hex code. Please check your input and try again.")
        return False


def main():
    # DECLARE VARIABLES
    totalIcons = 0  # Number of icons created by the script
    filepath = "../png"  # Could change in the future to an input or argument

    # CHECK IF A CUSTOM COLOUR ARGUMENT HAS BEEN PROVIDED IN THE TERMINAL
    if len(sys.argv) > 1:
        colourToReplace = sys.argv[1].upper()
        # CHECK IF PROVIDED COLOUR IS VALID OR NOT
        if not validHexCode(colourToReplace):
            return

    # USE DEFAULT COLOUR IF NO CUSTOM ONE IS PROVIDED
    else:
        colourToReplace = "#00CCC5"
        print("Using default colour: ", colourToReplace)

    # CHECK IF THERE ARE ANY SVG FILES BEFORE PROCEEDING
    if len(glob.glob("*.svg")) == 0:
        print("No SVG files found!")
        return
    else:
        # CHECK IF EXPORT FOLDER EXISTS - IF NOT, MAKE ONE
        if not os.path.exists(filepath):
            os.makedirs(filepath)

    # LOOP THROUGH EACH SVG FILE
    for file in glob.glob("*.svg"):
        with codecs.open(file, encoding='utf-8', errors='ignore') as svgFile:
            content = svgFile.read()
        print("Exporting:", file)

        # LOOP THROUGH ALL EXPORTS (SIZE AND COLOUR)
        for size in sizes:
            for colour in colours:
                newSVG = content.replace(colourToReplace, colour[1])
                newBytes = str.encode(newSVG)
                try:
                    cairosvg.svg2png(bytestring=newBytes,
                                     write_to=filepath + "/{}_{}_{}.png".format(os.path.splitext(file)[0],
                                                                                colour[0],
                                                                                size[0]),
                                     output_width=size[1])
                    totalIcons = totalIcons + 1
                except Exception as error:
                    print(error)
                    print(colour)
                pass

    # AT END OF RUN, GIVE INFORMATION ABOUT ICON QUANTITY
    print("Process complete!")
    print("Icons created: " + str(totalIcons))


if __name__ == "__main__":
    main()
