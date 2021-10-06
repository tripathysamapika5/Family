import sys
import os

project_dir = os.getcwd()
sys.path.append(project_dir)

import unittest
from src.main.family.person import Person
from src.main.family.familyTree import FamilyTree
from src.main.util.gender import Gender
from src.main.util.exceptions import InvalidMemberInTree, InvalidMotherForChildAddition

class TestFamilyTree(unittest.TestCase):    
    familyTree = FamilyTree()
    
    kamdev = Person('Kamdev', Gender.male)
    familyTree.updateMemeberToTree(kamdev)
    
    familyTree.addSpouse('Kamdev', 'Bilasini','Female')
    
    familyTree.addChild('Bilasini', 'Kailash', 'Male')
    familyTree.addChild('Bilasini', 'Keshab', 'Male')
    familyTree.addChild('Bilasini', 'Kalyani', 'Female')
    familyTree.addChild('Bilasini', 'Kanan', 'Female')
    
        
    def testGetMemberFromTree(self):
        with self.assertRaises(InvalidMemberInTree):
            TestFamilyTree.familyTree.getMemberFromTree('Samapika')
        
        self.assertTrue(TestFamilyTree.familyTree.getMemberFromTree('Kamdev') == TestFamilyTree.kamdev)
        
    def testAddSpouse(self):
        self.assertTrue(TestFamilyTree.kamdev.getSpouse().getName() == 'Bilasini')
        bilasini = TestFamilyTree.familyTree.getMemberFromTree('Bilasini')
        self.assertTrue(bilasini.getSpouse().getName() == 'Kamdev')
    
    def testAddChild(self):
        bilasini = TestFamilyTree.familyTree.getMemberFromTree('Bilasini')
        
        kailash = TestFamilyTree.familyTree.getMemberFromTree('Kailash')
        keshab = TestFamilyTree.familyTree.getMemberFromTree('Keshab')
        kalyani = TestFamilyTree.familyTree.getMemberFromTree('Kalyani')
        kanan = TestFamilyTree.familyTree.getMemberFromTree('Kanan')
        
        self.assertTrue(bilasini.getChildren() == [kailash, keshab, kalyani, kanan])
        self.assertTrue(TestFamilyTree.kamdev.getChildren() == [kailash, keshab, kalyani, kanan])
        
        self.assertTrue(kailash.getFather() == TestFamilyTree.kamdev)
        self.assertTrue(kailash.getMother() == bilasini)

        self.assertTrue(keshab.getFather() == TestFamilyTree.kamdev)
        self.assertTrue(keshab.getMother() == bilasini)

        self.assertTrue(kalyani.getFather() == TestFamilyTree.kamdev)
        self.assertTrue(kalyani.getMother() == bilasini)

        self.assertTrue(kanan.getFather() == TestFamilyTree.kamdev)
        self.assertTrue(kanan.getMother() == bilasini)
        
        with self.assertRaises(InvalidMotherForChildAddition):
            TestFamilyTree.familyTree.addChild('Kamdev', 'Kailash', 'Male')
        
    def testGetSonsAndGetSonNames(self):
        kalyani = TestFamilyTree.familyTree.getMemberFromTree('Kalyani')
        kanan = TestFamilyTree.familyTree.getMemberFromTree('Kanan')
        
        self.assertTrue(TestFamilyTree.familyTree.getDaughters(TestFamilyTree.kamdev) == [kalyani, kanan])
        self.assertTrue(TestFamilyTree.familyTree.getDaughterNames('Kamdev') == ['Kalyani', 'Kanan'])
        
        bilasini = TestFamilyTree.familyTree.getMemberFromTree('Bilasini')

        self.assertTrue(TestFamilyTree.familyTree.getDaughters(bilasini) == [kalyani, kanan])
        self.assertTrue(TestFamilyTree.familyTree.getDaughterNames('Bilasini') == ['Kalyani', 'Kanan'])  
        
        self.assertTrue(TestFamilyTree.familyTree.getDaughters(kalyani) == [])     
        self.assertTrue(TestFamilyTree.familyTree.getDaughterNames('Kalyani') is None)   
        
    def testGetDaughtersAndGetDaughterNames(self):
        kailash = TestFamilyTree.familyTree.getMemberFromTree('Kailash')
        keshab = TestFamilyTree.familyTree.getMemberFromTree('Keshab')
        
        self.assertTrue(TestFamilyTree.familyTree.getSons(TestFamilyTree.kamdev) == [kailash, keshab])
        self.assertTrue(TestFamilyTree.familyTree.getSonNames('Kamdev') == ['Kailash', 'Keshab'])

        bilasini = TestFamilyTree.familyTree.getMemberFromTree('Bilasini')

        self.assertTrue(TestFamilyTree.familyTree.getSons(bilasini) == [kailash, keshab])
        self.assertTrue(TestFamilyTree.familyTree.getSonNames('Bilasini') == ['Kailash', 'Keshab'])        

        self.assertTrue(TestFamilyTree.familyTree.getDaughters(kailash) == [])     
        self.assertTrue(TestFamilyTree.familyTree.getDaughterNames('Kailash') is None)
        
    def testGetSiblings(self):
           
        kailash = TestFamilyTree.familyTree.getMemberFromTree('Kailash')
        keshab = TestFamilyTree.familyTree.getMemberFromTree('Keshab')
        kalyani = TestFamilyTree.familyTree.getMemberFromTree('Kalyani')
        kanan = TestFamilyTree.familyTree.getMemberFromTree('Kanan')
        
        self.assertTrue(TestFamilyTree.familyTree.getSiblings(kailash) == [keshab, kalyani, kanan])
        self.assertTrue(TestFamilyTree.familyTree.getSiblings(kalyani) == [kailash, keshab, kanan])

        self.assertTrue(TestFamilyTree.familyTree.getSiblingNames('Kailash') == ['Keshab', 'Kalyani', 'Kanan'])
        self.assertTrue(TestFamilyTree.familyTree.getSiblingNames('Kalyani') == ['Kailash', 'Keshab', 'Kanan'])
        
        self.assertTrue(TestFamilyTree.familyTree.getSiblings(TestFamilyTree.kamdev) is None)
        self.assertTrue(TestFamilyTree.familyTree.getSiblingNames('Kamdev') is None)

    def testGetPaternalUncles(self):
        familyTree = FamilyTree()
    
        kamdev = Person('Kamdev', Gender.male)
        familyTree.updateMemeberToTree(kamdev)
        
        familyTree.addSpouse('Kamdev', 'Bilasini','Female')
        
        familyTree.addChild('Bilasini', 'Kailash', 'Male')
        familyTree.addChild('Bilasini', 'Keshab', 'Male')
        familyTree.addChild('Bilasini', 'Kalyani', 'Female')
        familyTree.addChild('Bilasini', 'Kanan', 'Female')
        familyTree.addChild('Bilasini', 'Bisha', 'Male')
        
        familyTree.addSpouse('Kailash', 'Pramila', 'Female')
        familyTree.addSpouse('Keshab', 'Jhunu', 'Female')
        familyTree.addSpouse('Kalyani', 'Santosh', 'Male')
        familyTree.addSpouse('Kanan', 'Babu', 'Male')
        
        familyTree.addChild('Pramila', 'Samapika', 'Female')
        familyTree.addChild('Jhunu', 'Safu', 'Male')
        familyTree.addChild('Kalyani', 'Swati', 'Female')
        familyTree.addChild('Kanan', 'Sanu', 'Male')
        
        self.assertTrue(familyTree.getPaternalUncleNames('Safu') == ['Kailash','Bisha'])
        self.assertTrue(familyTree.getPaternalUncleNames('Swati') == None)

    def testGetPaternalAunts(self):
        familyTree = FamilyTree()
    
        kamdev = Person('Kamdev', Gender.male)
        familyTree.updateMemeberToTree(kamdev)
        
        familyTree.addSpouse('Kamdev', 'Bilasini','Female')
        
        familyTree.addChild('Bilasini', 'Kailash', 'Male')
        familyTree.addChild('Bilasini', 'Keshab', 'Male')
        familyTree.addChild('Bilasini', 'Kalyani', 'Female')
        familyTree.addChild('Bilasini', 'Kanan', 'Female')
        familyTree.addChild('Bilasini', 'Bisha', 'Male')
        
        familyTree.addSpouse('Kailash', 'Pramila', 'Female')
        familyTree.addSpouse('Keshab', 'Jhunu', 'Female')
        familyTree.addSpouse('Kalyani', 'Santosh', 'Male')
        familyTree.addSpouse('Kanan', 'Babu', 'Male')
        
        familyTree.addChild('Pramila', 'Samapika', 'Female')
        familyTree.addChild('Jhunu', 'Safu', 'Male')
        familyTree.addChild('Kalyani', 'Swati', 'Female')
        familyTree.addChild('Kanan', 'Sanu', 'Male')
        
        self.assertTrue(familyTree.getPaternalAuntNames('Safu') == ['Kalyani','Kanan'])
        self.assertTrue(familyTree.getPaternalAuntNames('Swati') == None)

    def testGetMaternalUncles(self):
        familyTree = FamilyTree()
    
        kamdev = Person('Kamdev', Gender.male)
        familyTree.updateMemeberToTree(kamdev)
        
        familyTree.addSpouse('Kamdev', 'Bilasini','Female')
        
        familyTree.addChild('Bilasini', 'Kailash', 'Male')
        familyTree.addChild('Bilasini', 'Keshab', 'Male')
        familyTree.addChild('Bilasini', 'Kalyani', 'Female')
        familyTree.addChild('Bilasini', 'Kanan', 'Female')
        
        familyTree.addSpouse('Kailash', 'Pramila', 'Female')
        familyTree.addSpouse('Keshab', 'Jhunu', 'Female')
        familyTree.addSpouse('Kalyani', 'Santosh', 'Male')
        familyTree.addSpouse('Kanan', 'Babu', 'Male')
        
        familyTree.addChild('Pramila', 'Samapika', 'Female')
        familyTree.addChild('Jhunu', 'Safu', 'Male')
        familyTree.addChild('Kalyani', 'Swati', 'Female')
        familyTree.addChild('Kanan', 'Sanu', 'Male')
        
        self.assertTrue(familyTree.getMaternalUncleNames('Swati') == ['Kailash','Keshab'])
        self.assertTrue(familyTree.getMaternalUncleNames('Safu') == None)

    def testGetMaternalAunts(self):
        familyTree = FamilyTree()
    
        kamdev = Person('Kamdev', Gender.male)
        familyTree.updateMemeberToTree(kamdev)
        
        familyTree.addSpouse('Kamdev', 'Bilasini','Female')
        
        familyTree.addChild('Bilasini', 'Kailash', 'Male')
        familyTree.addChild('Bilasini', 'Keshab', 'Male')
        familyTree.addChild('Bilasini', 'Kalyani', 'Female')
        familyTree.addChild('Bilasini', 'Kanan', 'Female')
        familyTree.addChild('Bilasini', 'Kapuri', 'Female')
        
        familyTree.addSpouse('Kailash', 'Pramila', 'Female')
        familyTree.addSpouse('Keshab', 'Jhunu', 'Female')
        familyTree.addSpouse('Kalyani', 'Santosh', 'Male')
        familyTree.addSpouse('Kanan', 'Babu', 'Male')
        
        familyTree.addChild('Pramila', 'Samapika', 'Female')
        familyTree.addChild('Jhunu', 'Safu', 'Male')
        familyTree.addChild('Kalyani', 'Swati', 'Female')
        familyTree.addChild('Kanan', 'Sanu', 'Male')
        
        self.assertTrue(familyTree.getMaternalAuntNames('Swati') == ['Kanan','Kapuri'])
        self.assertTrue(familyTree.getMaternalAuntNames('Safu') == None)
        
    def testGetSisterInLaw(self):
        familyTree = FamilyTree()
    
        kamdev = Person('Kamdev', Gender.male)
        familyTree.updateMemeberToTree(kamdev)
        
        familyTree.addSpouse('Kamdev', 'Bilasini','Female')
        
        familyTree.addChild('Bilasini', 'Kailash', 'Male')
        familyTree.addChild('Bilasini', 'Keshab', 'Male')
        familyTree.addChild('Bilasini', 'Kalyani', 'Female')
        familyTree.addChild('Bilasini', 'Kanan', 'Female')
        familyTree.addChild('Bilasini', 'Kapuri', 'Female')
        
        familyTree.addSpouse('Kailash', 'Pramila', 'Female')
        familyTree.addSpouse('Keshab', 'Jhunu', 'Female')
        familyTree.addSpouse('Kalyani', 'Santosh', 'Male')
        familyTree.addSpouse('Kanan', 'Babu', 'Male')
        
        familyTree.addChild('Pramila', 'Samapika', 'Female')
        familyTree.addChild('Jhunu', 'Safu', 'Male')
        familyTree.addChild('Kalyani', 'Swati', 'Female')
        familyTree.addChild('Kanan', 'Sanu', 'Male')
        
        self.assertTrue(familyTree.getSisterInLawNames('Jhunu') == ['Kalyani','Kanan','Kapuri'])
        self.assertTrue(familyTree.getSisterInLawNames('Pramila') == ['Kalyani','Kanan','Kapuri'])
        self.assertTrue(familyTree.getSisterInLawNames('Keshab') == ['Pramila'])
        self.assertTrue(familyTree.getSisterInLawNames('Swati') == None)
        
        x = Person('X', Gender.male)
        familyTree.updateMemeberToTree(x)
        
        familyTree.addParent('Jhunu', 'Y', 'Female')
        familyTree.addChild('Y', 'Suka', 'Male')
        familyTree.addChild('Y', 'Sunu', 'Female')
        familyTree.addSpouse('Suka', 'Rani', 'Female')
        self.assertTrue(familyTree.getSisterInLawNames('Jhunu') == ['Kalyani','Kanan','Kapuri','Rani'])
        self.assertTrue(familyTree.getSisterInLawNames('Pramila') == ['Kalyani','Kanan','Kapuri'])
        self.assertTrue(familyTree.getSisterInLawNames('Keshab') == ['Sunu','Pramila'])
        self.assertTrue(familyTree.getSisterInLawNames('Swati') == None)

    def testGetBrotherInLaw(self):
        familyTree = FamilyTree()
    
        kamdev = Person('Kamdev', Gender.male)
        familyTree.updateMemeberToTree(kamdev)
        
        familyTree.addSpouse('Kamdev', 'Bilasini','Female')
        
        familyTree.addChild('Bilasini', 'Kailash', 'Male')
        familyTree.addChild('Bilasini', 'Keshab', 'Male')
        familyTree.addChild('Bilasini', 'Kalyani', 'Female')
        familyTree.addChild('Bilasini', 'Kanan', 'Female')
        familyTree.addChild('Bilasini', 'Jatadhari', 'Male')
        
        familyTree.addSpouse('Kailash', 'Pramila', 'Female')
        familyTree.addSpouse('Keshab', 'Jhunu', 'Female')
        familyTree.addSpouse('Kalyani', 'Santosh', 'Male')
        familyTree.addSpouse('Kanan', 'Babu', 'Male')
        
        familyTree.addChild('Pramila', 'Samapika', 'Female')
        familyTree.addChild('Jhunu', 'Safu', 'Male')
        familyTree.addChild('Kalyani', 'Swati', 'Female')
        familyTree.addChild('Kanan', 'Sanu', 'Male')
        
        self.assertTrue(familyTree.getBrotherInLawNames('Jhunu') == ['Kailash','Jatadhari'])
        self.assertTrue(familyTree.getBrotherInLawNames('Pramila') == ['Keshab','Jatadhari'])
        self.assertTrue(familyTree.getBrotherInLawNames('Keshab') == ['Santosh','Babu'])
        self.assertTrue(familyTree.getBrotherInLawNames('Kailash') == ['Santosh','Babu'])
        self.assertTrue(familyTree.getBrotherInLawNames('Swati') == None)
        
        x = Person('X', Gender.male)
        familyTree.updateMemeberToTree(x)
        
        familyTree.addParent('Jhunu', 'Y', 'Female')
        familyTree.addChild('Y', 'Suka', 'Male')
        familyTree.addSpouse('Suka', 'Rani', 'Female')
        familyTree.addChild('Y', 'Sunu', 'Female')
        familyTree.addSpouse('Sunu', 'Muna', 'Male')
        self.assertTrue(familyTree.getBrotherInLawNames('Keshab') == ['Suka','Santosh','Babu'])
        self.assertTrue(familyTree.getBrotherInLawNames('Jhunu') == ['Kailash','Jatadhari','Muna'])

        
if __name__ == '__main__':
    unittest.main()