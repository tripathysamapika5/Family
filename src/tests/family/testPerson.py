import sys
import os

project_dir = os.getcwd()
sys.path.append(project_dir)

import unittest
from src.main.family.person import Person
from src.main.util.gender import Gender

class TestPerson(unittest.TestCase):    

    def testGetName(self):
        person = Person('Samapika','Female')
        self.assertTrue('Samapika' == person.name)   
         
    def testGetGender(self):
        person = Person('Samapika',Gender.female)
        self.assertTrue(Gender.female == person.gender)    
        person2 = Person('Samapika',None)
        self.assertTrue( person2.gender is None) 
        
    def testSetSpouseAndGetSpouse(self):
        person = Person('Samapika',Gender.female)
        spouse = Person('Rajiv',Gender.male)
        self.assertTrue( person.spouse is None) 
        person.setSpouse(spouse)
        self.assertTrue( person.spouse is spouse) 
        self.assertTrue( person.spouse == spouse) 
        self.assertTrue( person.spouse.name == 'Rajiv') 
        self.assertTrue( person.spouse.gender == Gender.male) 
        self.assertTrue( person.getSpouse() is spouse)     
        
    def testSetChildrenAndGetChildren(self):
        person = Person('Samapika',Gender.female)
        children = [Person('Bhumi',Gender.female),Person('anonymous',Gender.male)]
        person.setChildren(children)
        self.assertTrue(person.getChildren() == children)
        
    def setGetParent(self):
        person = Person('Samapika',Gender.female)
        father = Person('kailash',Gender.male)
        mother = Person('pramila',Gender.female)
        parent = {'father' : father, 'mother' : mother}
        person.setParent(father,mother)
        self.assertTrue(person.getParent() == parent)
        self.assertTrue(person.getFather() == father)
        self.assertTrue(person.getMother() == mother)
    
    def testIsMaleIsFemale(self):
        person1 = Person('Samapika',Gender.female)
        person2 = Person('Rajiv',Gender.male)
        
        self.assertTrue(person1.isFemale())
        self.assertTrue(person2.isMale())
        
        self.assertFalse(person1.isMale())
        self.assertFalse(person2.isFemale())
        
    def testGetNames(self):
        person1 = Person('Samapika',Gender.female)
        person2 = Person('Rajiv',Gender.male)
        self.assertTrue(Person.getNames([person1,person2]) == ['Samapika', 'Rajiv'])
        
                    
  
if __name__ == '__main__':
    unittest.main()

