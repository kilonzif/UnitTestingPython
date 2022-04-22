import unittest #importing unittest module from python 

from contact import Contact #importing our Contact class from our contact file

class TestContact(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact = Contact("John","Doe",'011234567','john.doe@mail.com')
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_contact.firstName,"John")
        self.assertEqual(self.new_contact.lastName,"Doe")
        self.assertEqual(self.new_contact.phoneNo,"011234567")
        self.assertEqual(self.new_contact.email,"john.doe@mail.com")
    
    def test_fullName(self):
        '''
        Testing the fullName property function  
        '''
        firstP = self.new_contact.fullName
        self.assertEqual(firstP,'John Doe')

    def test_saveContact(self):
        '''
        Testing the save_contact() function 
        '''
        self.new_contact.save_contact() # saving the new contact
        self.assertEqual(len(Contact.contact_list),1)

#if unit tests pass
if __name__ == '__main__':
    unittest.main()
