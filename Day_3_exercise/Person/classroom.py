class Person(object):
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    def getfirstname(self):
        return self.firstname
    
    def getlastname(self):
        return self.lastname
    
    def __str__(self):
        return (self.firstname + ' ' + self.lastname)
    
class Student(Person):
    def __init__(self,firstname,lastname,subject):
        Person.__init__(self,firstname,lastname)
        self.subject = subject
    def subject(self):
        return self.subject
    def printNameSubject(self):
        print(self.firstname + " " + self.lastname + ", " + self.subject)
        
class Teacher(Person):
    def __init__(self,firstname,lastname,subject):
        Person.__init__(self,firstname,lastname)
        self.subject = subject
    def subject(self):
        return self.subject
    def printNameSubject(self):
        print(self.firstname + " " + self.lastname + ", " + self.subject)