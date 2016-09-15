"""Testing Command Line Interface"""

import argparse

# The Following code provides --help and --version functionality
#  To test it in terminal: python cliTesting.py --help (or --version)

parser = argparse.ArgumentParser(description='***Welcome to MegaResearch Inc. AmesWeather***', prog='MegaResearch', add_help=False)
parser.add_argument('--version', action='version', version='2.0')
parser.add_argument('--help', action='help', help='show this help message and exit')

args = parser.parse_args()
