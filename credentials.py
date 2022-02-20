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
            if accounts.accountusername == number:
                return accounts