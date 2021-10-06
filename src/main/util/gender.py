class Gender:
    male = 'Male'
    female = 'Female'
    
    
    @staticmethod
    def getGender(genderName):
        '''This method returns the gender instance based on the gender string'''
        if genderName.lower() == "male":
            return Gender.male
        elif genderName.lower()  == "female" :
            return Gender.female
        else:
            return None