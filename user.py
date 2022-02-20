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
                      

class Credentials:
    '''
    class that generates new instances of credentials
    '''
    accounts=[]
    def _init_(self,accountusername,accountname,accountpassword):
        '''
        _init_ method that helps us define properties for our objectsself
        '''
        self.accountusername= accountusername
        self.accountname= accountname
        self.accountpassword= accountpassword
    def save_account(self):
        '''
        save_account method saves user info into accounts
         '''
        Credentials.accounts.append(self)
    def delete_account(self):
        '''
        delete_account method deletes a saved credential from accounts
        '''
        Credentials.accounts.append(self)
    @classmethod
    def display_accounts(cls):
        '''
        method that returns a list of the account
        '''
        for account in cls.accounts:
                return cls.accounts
    @classmethod
    def find_by_number(cls,number):
        '''
        method that takes in a number and returns a contact that matches that number
        '''
        for accounts in cls.accounts:
            if account.accountusername == number:
                return account
                

































