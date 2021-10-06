import sys
import os

project_dir = os.getcwd()
sys.path.append(project_dir)
print(project_dir)

from src.main.util.gender import Gender

class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.spouse = None
        self.children = []
        self.parent = {'father' :None, 'mother' : None}
    
    def getName(self):
        '''
        This method returns the name of the person.
        Input : NA
        '''
        return self.name
    
    def getGender(self):
        '''
        This method returns the gender.
        Input : NA
        '''    
        return self.gender
    
    def setSpouse(self, spouse):
        '''
        This method sets the spouse of a person
        Input : spouse(type : Person)
        '''
        self.spouse = spouse
        
    def getSpouse(self):
        '''
        This method will return spouse of the person
        Input : NA
        '''
        return self.spouse

    def setChild(self, child):
        '''
        This method will add a child to the person
        Input : child object
        '''
        self.children.append(child)
    
    def setChildren(self, childrenList):
        '''
        This method will add a set of children to the person
        Input : iterable of children
        '''
        for child in childrenList:
            self.setChild(child)
    
    def getChildren(self):
        '''
        It will return a list of childrens belonging to the person
        Input : NA
        '''
        return self.children

    def setParent(self, father = None, mother = None):
        '''
        It will set the parents of the person
        Input : Person object for father and mother
        '''
        if father:
            self.parent['father'] = father
        if mother:
            self.parent['mother'] = mother

    def getParent(self):
        '''
        It will return the parents of the object
        Input : NA
        '''
        return self.parent  
    
    def getFather(self):
        '''
        It will return the father
        ''' 
        return self.parent.get('father')
    
    def getMother(self):
        '''
        It will return the mother
        ''' 
        return self.parent.get('mother')
    
    def isMale(self):
        '''
        Checks if the gender of the person is male or not
        returns True/False
        '''
        return self.getGender() == Gender.male
                
    def isFemale(self):
        '''
        Checks if the gender of the person is female or not
        returns True/False
        '''
        return self.getGender() == Gender.female


     
    @staticmethod
    def isValidPerson(person):
        '''
        It checks if an instance is valid person instance or not
        Input : instance
        output : True/False (boolean)
        '''
        return isinstance(person, Person)

    @staticmethod
    def getNames(people):
        '''
        It will return a list of names for a list of people
        '''
        return [person.getName() for person in people]