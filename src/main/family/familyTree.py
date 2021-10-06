
import sys
import os

project_dir = os.getcwd()
sys.path.append(project_dir)

from src.main.family.person import Person
from src.main.util.gender import Gender
from src.main.util.exceptions import InvalidMemberInTree, InvalidMotherForChildAddition
import logging

class FamilyTree:
    
    def __init__(self):
        self.rootMember = None
        self.name_to_person_mapping = {}    
        
    def updateMemeberToTree(self, person):
        '''
        It will add a new member to the tree
        '''
        self.name_to_person_mapping[person.getName()] = person
        
    def getMemberFromTree(self, personName):
        '''
        It will return a member from the tree
        '''
        person = self.name_to_person_mapping.get(personName)
        if not person:
            raise InvalidMemberInTree("Member : {} is not found in FamilyTree".format(personName))
        
        return person
    
    def addSpouse(self,personName, spouseName, spouseGenderName):
        '''
        This method sets the spouse of a person
        '''
        # getting the person and spouse instance
        person = self.getMemberFromTree(personName)
        spouseGender = Gender.getGender(spouseGenderName)
        spouse = Person(spouseName,spouseGender)
        
        # setting the spouse for each other
        person.setSpouse(spouse)
        spouse.setSpouse(person)
        
        # setting the children for each other
        spouse.setChildren(person.getChildren())
        person.setChildren(spouse.getChildren())
        
        all_children = person.getChildren()
        
        if person.isMale():
            father = person
            mother = spouse
        else:
            father = spouse
            mother = person
        
        # setting the parents for them
        for child in all_children:
            child.setParent(father, mother)
            
        # adding the spouse to the map
        self.updateMemeberToTree(spouse)


    def addChild(self, motherName, childName, childGenderName):
        '''
        It will add a child to the tree through its mother
        '''
        # finds out father , mother instance and creates child instance
        mother = self.getMemberFromTree(motherName) 
        if mother.isMale():
            raise InvalidMotherForChildAddition("{} is male. Hence child addition failed".format(motherName))
        
        childGender = Gender.getGender(childGenderName)
        child = Person(childName,childGender)
        father = mother.getSpouse()
        
        # sets child for mother
        mother.setChild(child)
        child.setParent(mother = mother)
        
        # sets child for father
        if father:
            father.setChild(child)
            child.setParent(father = father)
        
        # adding new member child to tree
        self.updateMemeberToTree(child)
        
        return True
        
    def addParent(self, childName, parentName, parentGenderName):
        '''
        It adds a parent to the child
        '''
        child = self.getMemberFromTree(childName) 
        parentGender = Gender.getGender(parentGenderName)
        parent = Person(parentName,parentGender)
        
        father,mother = None,None
        if parent.isMale():
            father = parent
            if child.getMother():
                mother = child.getMother()
                self.addSpouse(mother.getName(), father.getName(), 'Male')
        else:
            mother = parent 
            if child.getFather():
                father = child.getFather()
                self.addSpouse(father.getName(), mother.getName(), 'Female')
                
        self.updateMemeberToTree(parent)

        if mother:
            mother.setChild(child)
            child.setParent(mother = mother)
        
        # sets child for father
        if father:
            father.setChild(child)
            child.setParent(father = father)
            
        return True
        
        
    def getSons(self, person):
        '''
        It returns a list of all son instances of a person instance
        '''
        return  [child for child in person.getChildren() if child.isMale()]

                
    def getSonNames(self, personName):
        '''
        It returns a list of all son names of a person
        '''
        person = self.getMemberFromTree(personName)    
        sons = self.getSons(person)
        
        if not sons:
            return None
        else:
            return Person.getNames(sons)

        
    def getDaughters(self, person):
        '''
        It returns a list of all names of daughters of a person 
        '''
        return  [child for child in person.getChildren() if child.isFemale()]

    def getDaughterNames(self, personName):
        '''
        It returns a list of all daughter names of a person
        '''
        person = self.getMemberFromTree(personName)
        daughters = self.getDaughters(person)
        
        if not daughters:
            return None
        else:
            return Person.getNames(daughters)


    
    def getSiblings(self, person):
        '''
        It returns all sibling instances of a person instance
        '''
        parent = person.getFather()
        if not parent:
            parent = person.getMother()
        
        if parent:
            return [sibling for sibling in  parent.getChildren() if sibling != person]
        else:
            return None
    
    def getSiblingNames(self, personName):
        '''
        It returns all sibling names of a person
        '''
        person = self.getMemberFromTree(personName)
        siblings = self.getSiblings(person)
        
        if not siblings:
            return None
        else:
            return Person.getNames(siblings)
    
    def getPaternalUncle(self, person):
        '''
        It returns all patrernal uncle instances of a person instance
        '''
        father = person.getFather()
        
        if father:
            fatherSiblings = self.getSiblings(father)
            if fatherSiblings:        
                return [uncle for uncle in  fatherSiblings if uncle != father and uncle.isMale()]
            else:
                return None
        else:
            return None
        
        
    
    def getPaternalUncleNames(self, personName):
        '''
        It returns all paternal uncle names of a person
        '''
        person = self.getMemberFromTree(personName)
        paternalUncles = self.getPaternalUncle(person)
        
        if not paternalUncles:
            return None
        else:
            return Person.getNames(paternalUncles)
        
    def getPaternalAunt(self, person):
        '''
        It returns all paternal aunt instances of a person instance
        '''

        father = person.getFather()
        
        if father:
            fatherSiblings = self.getSiblings(father)
            if fatherSiblings:
                return [aunt for aunt in  fatherSiblings if aunt.isFemale()]
            else:
                return None
        else:
            return None

    def getPaternalAuntNames(self, personName):
        '''
        It returns all paternal aunt names of a person
        '''

        person = self.getMemberFromTree(personName)
        paternalAunts = self.getPaternalAunt(person)
        
        if not paternalAunts:
            return None
        else:
            return Person.getNames(paternalAunts)
   

    def getMaternalUncle(self, person):
        '''
        It returns all maternal uncle instances of a person instance
        '''
        mother = person.getMother()
        if mother:
            motherSiblings = self.getSiblings(mother)
            if motherSiblings:
                return [uncle for uncle in  motherSiblings if uncle.isMale()]
            else:
                return None
        else:
            return None

    def getMaternalUncleNames(self, personName):
        '''
        It returns all maternal uncle names of a person
        '''

        person = self.getMemberFromTree(personName)
        maternalUncles = self.getMaternalUncle(person)
        
        if not maternalUncles:
            return None
        else:
            return Person.getNames(maternalUncles)


    def getMaternalAunt(self, person):
        '''
        It returns all maternal aunt instances of a person instance
        '''
        mother = person.getMother()
        if mother:
            motherSiblings = self.getSiblings(mother)
            if motherSiblings:
                return [aunt for aunt in  motherSiblings if aunt.isFemale() and aunt != mother]
            else:
                return None
        else:
            return None

    def getMaternalAuntNames(self, personName):
        '''
        It returns all maternal aunt names of a person
        '''
        person = self.getMemberFromTree(personName)
        maternalAunts = self.getMaternalAunt(person)
        
        if not maternalAunts:
            return None
        else:
            return Person.getNames(maternalAunts)

        
    def getSisterInLaw(self, person):
        '''
        It returns all sister in laws instances of a person instance
        '''
        spouse = person.getSpouse()
        spouseSisters = []
        siblingWives = []
        
        if spouse:
            spouseSiblings = self.getSiblings(spouse)
            if spouseSiblings:
                spouseSisters = [sibling for sibling in  spouseSiblings if sibling != spouse and sibling.isFemale()]
            
        personSiblings = self.getSiblings(person)
        
        if personSiblings:
            siblingWives = [sibling.getSpouse() for sibling in personSiblings if sibling.isMale() and sibling != person]
        
        sistersInLaws = spouseSisters + siblingWives
        
        if sistersInLaws:
            return sistersInLaws
        else:
            return None

    def getSisterInLawNames(self, personName):
        '''
        It returns all sister in laws names of a person
        '''
        person = self.getMemberFromTree(personName)
        sisterInLaws = self.getSisterInLaw(person)
        
        if not sisterInLaws:
            return None
        else:
            return Person.getNames(sisterInLaws)


    def getBrotherInLaw(self, person):
        '''
        It returns all brother in laws instances of a person instance
        '''
        spouse = person.getSpouse()
        spouseBrothers = []
        siblingHusbands = []
        
        if spouse:
            spouseSiblings = self.getSiblings(spouse)
            if spouseSiblings:
                spouseBrothers = [sibling for sibling in  spouseSiblings if sibling != spouse and sibling.isMale()]
        
        personSiblings = self.getSiblings(person)
        
        if personSiblings:
            siblingHusbands = [sibling.getSpouse() for sibling in personSiblings if sibling.isFemale() and sibling != person]
        
        brotherInLaw = spouseBrothers + siblingHusbands
        
        if brotherInLaw:
            return brotherInLaw
        else:
            return None

    def getBrotherInLawNames(self, personName):
        '''
        It returns all brother in laws names of a person
        '''
        person = self.getMemberFromTree(personName)
        brotheInLaws = self.getBrotherInLaw(person)
        
        if not brotheInLaws:
            return None
        else:
            return Person.getNames(brotheInLaws)


class ShanFamilyTree(FamilyTree):
    def __init__(self):
        super().__init__()
        shan = Person('King Shan', Gender.male)
        super().updateMemeberToTree(shan)
        
        anga = Person('Queen Anga', Gender.female)
        super().addSpouse('King Shan', 'Queen Anga', 'Female')
    
        super().addChild('Queen Anga', 'Chit', 'Male')
        super().addChild('Queen Anga', 'Ish', 'Male')
        super().addChild('Queen Anga', 'Vich', 'Male')
        super().addChild('Queen Anga', 'Aras', 'Male')
        super().addChild('Queen Anga', 'Satya', 'Female')
        
        super().addSpouse('Chit', 'Amba', 'Female')
        super().addSpouse('Vich', 'Lika', 'Female')
        super().addSpouse('Aras', 'Chitra', 'Female')
        super().addSpouse('Satya', 'Vyan', 'Male')
        
        super().addChild('Amba', 'Dritha', 'Female')
        super().addChild('Amba', 'Tritha', 'Female')
        super().addChild('Amba', 'Vritha', 'Male')
        super().addChild('Lika', 'Vila', 'Female')
        super().addChild('Lika', 'Chika', 'Female')
        super().addChild('Chitra', 'Jnki', 'Female')
        super().addChild('Chitra', 'Ahit', 'Male')
        super().addChild('Satya', 'Atya', 'Female')
        super().addChild('Satya', 'Asva', 'Male')
        super().addChild('Satya', 'Vyas', 'Male')
        
        super().addSpouse('Dritha', 'Jaya', 'Male')
        super().addSpouse('Jnki', 'Arit', 'Male')
        super().addSpouse('Asva', 'Satvy', 'Female')
        super().addSpouse('Vyas', 'Krpi', 'Female')
        
        super().addChild('Dritha', 'Yodhan', 'Male')
        super().addChild('Jnki', 'Laki', 'Male')
        super().addChild('Jnki', 'Lavnya', 'Female')
        super().addChild('Satvy', 'Vasa', 'Male')
        super().addChild('Krpi', 'Kriya', 'Male')
        super().addChild('Krpi', 'Krithi', 'Female')
        
        
        


        
        
        
                
if __name__ == '__main__':
    shanFamilyTree  = ShanFamilyTree() 
    #print(Person.getNames(shanFamilyTree.name_to_person_mapping['King Shan'].getChildren()))
    print(shanFamilyTree.getSonNames('King Shan'))
    
    shanFamilyTree.addChild('Chitra', 'Aria', 'Female')
    print(shanFamilyTree.getMaternalAuntNames('Lavnya'))
    print(shanFamilyTree.getSiblingNames('Aria'))
    
    #shanFamilyTree.addChild('Pjali', 'Srutak', 'Male')
    #shanFamilyTree.addChild('Asva', 'Vani', 'Female')
    print(shanFamilyTree.getSiblingNames('Vasa'))
    print(shanFamilyTree.getSisterInLawNames('Atya'))
    #shanFamilyTree.addChild('Satya', 'Yaya', 'Female')
    print(shanFamilyTree.getSisterInLawNames('Satvy'))
          
