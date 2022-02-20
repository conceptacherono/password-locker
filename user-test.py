import unittest
from user import User

class Testuser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
         unittest.TestCase: TestCase class that helps in creating test cases
    '''

def setUp(self):
    '''
    Set up method to run before each test cases.
    '''
    self.new_user = user("Concepta","Cherono","2022") # create contact object
def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_user.user_name,"Concepta")


    self.assertEqual(self.new_user.password,"2022")
def test_save_user(self):
    '''
    test_save_user test case to test if the user object is saved into the user list
    '''
    self.new_user.save_user() # saving the new contact
    self.assertEqual(len(user.user_list),1)
def test_delete_user(self):
    '''
    test_selete_contact to test if we can remove a contact from our contact list
    '''
    self.new_contact.save_contact()
    test_user = user("Test","user","0768549788","test@user.com") # new contact
    test_user.save_user()

    self.new_user.delete_user() #deleting a contact object
    self.assertEqual(len(user.user_list),1)
if _name_ == '_main_':
    unittest.main()
