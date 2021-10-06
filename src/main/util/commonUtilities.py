
import sys
import os

project_dir = os.getcwd()
sys.path.append(project_dir)

from src.main.util.exceptions import CommandLineArgumentNotAvailable, InvalidFilePath, InvalidMemberInTree, InvalidMotherForChildAddition
from src.main.family.familyTree import ShanFamilyTree
import copy

class CommonUtilities:
    
    @staticmethod
    def getInputFilePath(cliArguments):
        if len(cliArguments) < 2 :
            raise CommandLineArgumentNotAvailable('Command line argumemt not found !')
        else:
            inputFilePath = cliArguments[1]
            if not os.path.exists(inputFilePath):
                raise InvalidFilePath('Path: {} is invalid'.format(inputFilePath))
        
        return inputFilePath 
    
    @staticmethod
    def readFile(inputFilePath):
        with open(inputFilePath) as f:
            lines = f.readlines()
        return lines
     
    @staticmethod
    def readInputFileToActions(inputFilePath):
        actions = []
        for line in CommonUtilities.readFile(inputFilePath):
            words = line.split(' ')
            action = {}
            if words[0].upper() == 'ADD_CHILD':
                action['method'] = 'addChild'
                action['motherName'] = words[1]
                action['childName'] =  words[2]
                action['childGenderName'] =  words[3]
                
            elif words[0].upper() == 'GET_RELATIONSHIP':
                action['personName'] =  words[1]
                if words[2].upper() == 'PATERNAL-UNCLE':
                    action['method'] = 'getPaternalUncleNames'
                elif words[2].upper() == 'MATERNAL-UNCLE':
                    action['method'] = 'getMaternalUncleNames'
                elif words[2].upper() == 'PATERNAL-AUNT':
                    action['method'] = 'getPaternalAuntNames'
                elif words[2].upper() == 'MATERNAL-AUNT':
                    action['method'] = 'getMaternalAuntNames'
                elif words[2].upper() == 'SISTER-IN-LAW':
                    action['method'] = 'getSisterInLawNames'
                elif words[2].upper() == 'BROTHER-IN-LAW':
                    action['method'] = 'getBrotherInLawNames'
                elif words[2].upper() == 'SON':
                    action['method'] = 'getSonNames'
                elif words[2].upper() == 'DAUGHTER':
                    action['method'] = 'getDaughterNames'
                elif words[2].upper() == 'SIBLINGS':
                    action['method'] = 'getSiblingNames'
                    
            actions.append(action)
        return actions
    
    @staticmethod
    def listToString(inputList):
        return ' '.join([str(item) for item in inputList])

    @staticmethod
    def printResult(result):
        if result == True:
            print('CHILD_ADDITION_SUCCEEDED')
        elif isinstance(result, list):
            print(CommonUtilities.listToString(result))
        elif result is None:
            print('NONE')
            
    @staticmethod
    def runMethod(obj, methodName, arguments):
        try:
            result = getattr(obj, methodName)(**arguments)
            CommonUtilities.printResult(result)
        except InvalidMemberInTree:
            print('PERSON_NOT_FOUND')
        except InvalidMotherForChildAddition:
            print('CHILD_ADDITION_FAILED')
                
    @staticmethod
    def performActions(shanFamilyTreeObj, actions):
        for action in actions:
            methodName = action['method']
            arguments = copy.deepcopy(action)
            del arguments['method']
            CommonUtilities.runMethod(shanFamilyTreeObj, methodName, arguments)
            
        
