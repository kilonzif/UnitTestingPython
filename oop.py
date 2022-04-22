#OOP

#properties
   # methods/functions

#object - instance of the class

#this -> JavaScript

class Student:    
    '''This class is a class docstring'''
    def __init__(self,studentName, studentAge, studentRegNo, studentCourse):
        self.studentName=studentName
        self.studentAge = studentAge
        self.studentRegNo = studentRegNo
        self.studentCourse = studentCourse

    def getCourse(self):

        '''This function prints the course the student is studying'''

        print("This student is studying " + self.studentCourse) #comment


#create object 
studentOne = Student('Michael',21,1001,'Engineering')

print(studentOne.getCourse())








    



