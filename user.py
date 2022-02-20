import random
import string

class User:
    '''
    class that generates new instances of user
    '''
    userlist=[]
    def _init_(self,firstname,lastname,username,password):
        '''_init_ method that helps us define properties for our objectsself
        '''
        self.firstname=firstname
        self.lastname=lastname
        self.username=username
        self.password=password
    def save_user(self):
        '''
        save_user method saves user info into user userslist
        '''    
        User.userslist.append(self)

    def delete_user(self):
        '''
        delete_user method deletes a saved user from the userlist
        '''    
        User.userlist.remove(self)
        @classmethod
        def display_users(cls):
            '''
            method that returns info from the userlist
            '''
            return cls.userslist
        @classmethod
        def find_by_number(cls,number):
            '''
            method that takes in a username and returns a user that matches that number
            '''
            for user in cls.userslist:
                if user.password == number:
                    return user
        @classmethod
        def user_exist(cls,number):
            for user in cls.userslist:
                if user.username == number:
                    return True
                    return False           
                      

  class Credentials      





























