
import sys
import os

project_dir = os.getcwd()
sys.path.append(project_dir)

import unittest
from src.main.family.person import Person
from src.main.family.familyTree import ShanFamilyTree
from src.main.util.gender import Gender
from src.main.util.commonUtilities import CommonUtilities
from src.main.util.exceptions import *
import logging


def main():
    try:
        inputFilePath = CommonUtilities.getInputFilePath(sys.argv)
        actions = CommonUtilities.readInputFileToActions(inputFilePath)

        shanFamilyTree = ShanFamilyTree()
        CommonUtilities.performActions(shanFamilyTree, actions)

    except CommandLineArgumentNotAvailable:
        logging.exception("Input file path is not provided.. \nplease run the code with input file path as first argument..")
    except InvalidFilePath:
        logging.exception("Path is invalid")
        
if __name__ == '__main__':
    main()