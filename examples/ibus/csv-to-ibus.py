#!/usr/bin/python3
import csv
import sys
from datetime import datetime

# Script to convert Natasha's Cherokee syllabary table into the format
# used by ibus-table, by Thomas Klute <thomas2.klute@uni-dortmund.de>.
#
# Licensed as CC0 (see
# https://creativecommons.org/publicdomain/zero/1.0/), use as you
# wish!
#
# Usage: ./csv-to-ibus.py < chr.csv > chr.txt

# variables for table metadata that's likely to change
desc = "Input method for Cherokee, based on Natasha's syllabary table"
author = "Thomas Klute <thomas2.klute@uni-dortmund.de>"
uuid = "fa824c40-b615-46b0-807d-b9fa311c3a1c"
# simple time based serial number, UTC to avoid any timezone confusion
serial = datetime.utcnow().strftime('%Y%m%d%H%M')
# TODO: find a nice public domain icon for Cherokee
icon = "py-mode.svg"

# file type header
print("SCIM_Generic_Table_Phrase_Library_TEXT\n"
      "VERSION_1_0\n")

# table metadata
print("BEGIN_DEFINITION\n"
      "LICENSE = CC0\n"
      "SYMBOL = \u13e3\n"
      "NAME = Cherokee\n"
      "LANGUAGES = chr\n"
      "STATUS_PROMPT = \u13e3\u13b3\u13a9")

# Just one replacement per print() to avoid mixups
print("UUID = %s" % uuid)
print("SERIAL_NUMBER = %s" % serial)
print("ICON = %s" % icon)
print("DESCRIPTION = %s" % desc)
print("AUTHOR = %s" % author)

# TODO: This should contain only characters that actually occur in the
# table. Generating the list would require either moving away from the
# stdin to stdout processing, or buffering the table output until the
# header has been written.
print('VALID_INPUT_CHARS = abcdefghijklmnopqrstuvwxyz')
# TODO: Like VALID_INPUT_CHARS this should ideally be calculated from
# the input
print("MAX_KEY_LENGTH = 3")

# This is a static replacement table, so use autocommit (just type, no
# need to confirm replacements), and no complicated stuff.
print("LAYOUT = default\n"
      "AUTO_COMMIT = TRUE\n"
      "AUTO_SELECT = FALSE\n"
      "DEF_FULL_WIDTH_PUNCT = FALSE\n"
      "DEF_FULL_WIDTH_LETTER = FALSE\n"
      "USER_CAN_DEFINE_PHRASE = FALSE\n"
      "PINYIN_MODE = FALSE\n"
      "DYNAMIC_ADJUST = FALSE\n"
      "END_DEFINITION\n")

# Create the actual table. All replacements are assigned the same
# frequency since there's only one replacement per combination of
# input characters.
print('BEGIN_TABLE')
reader = csv.DictReader(sys.stdin)
for row in reader:
    # line format (TSV): transliteration, character, frequency
    print("%s\t%s\t%d" % (row['transliteration'], row['character'], 1))
print('END_TABLE')
