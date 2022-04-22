
class Contact:
    '''
    Contact class
    '''

    contact_list=[] #list to save the contact objects

    def __init__(self,firstName,lastName,phoneNo,email):
        '''
        Initialization constructor to instantiate the class properties 
        '''
        self.firstName=firstName
        self.lastName=lastName
        self.phoneNo = phoneNo
        self.email=email

    @property
    def fullName(self):
        '''
        fullName property method that concatinates and formats first and last name
        '''
        return '{} {}'.format(self.firstName,self.lastName)

    def save_contact(self):
        '''
        save_contact method saves contact objects into contact_list

        '''
        self.contact_list.append(self)



# def main():
#     contact_obj = Contact("John","Doe",'011234567','john.doe@mail.com')
#     print(contact_obj.email)


# if __name__ == '__main__':
#     main()



        