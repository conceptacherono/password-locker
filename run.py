import string
from random import *
from user import User
from credentials import Credentials
def create_user(firstname,lastname,username,userpassword):
    newuser= User(firstname,lastname,username,userpassword)
    return newuser
def save_user(user):
    user.save_user()
def delete_user(user):
    user.delete_user()
def find_user(number):
    return User.find_by_number(number)
def display_users():
    return User.display_users()
def create_account(accountusername,accountname,accountpassword):
    newaccount= Credentials(accountusername,accountname,accountpassword)
    return newaccount
def save_account(user):
    user.save_account()
def delete_account(user):
    user.dele_account(user)
def find_account(number):
    return Credentials.find_by_number (number)
def display_accounts():
    return Credentials.display_accounts()
def main():
    while  True:
        print('Welcome to password locker,write new or log to start')
        print('new -or- log')  
        option=input()
        if option == 'new':
            print('Create account')
            print("-"*10)
            print('Enter your First Name')
            firstname=input()
            print('Enter your Last Name')
            lastname=input()
            print('Set your username')
            username=input()
            print('Set your password')
            userpassword=input()
            save_user(create_user(firstname,lastname,username,userpassword))
            print('Your account was created successfully.Details....')
            print("-"*10)
            print(f"Name: {firstname} {lastname} \nUsername: {username} \nPassword {userpassword}")
            print("\nUse Login to your account with your details")
            print("-"*10)
            print("\n \n")
            #for user in display_users():
            
        elif option == "log":
            print('Your username')
            logInUsername=input()
            print('your password')
            logInPassword=input()
            if find_user(logInPassword):
                print('\n')
                print('you can create multipe accounts (AC) and also view them (VC)')
                print("-"*60)
                print('AC -or- VC')
                choose=input()
                print('\n')
                if choose == 'AC':
                    print('Add your cred Account')
                    print("-"*25)
                    accountusername=logInUsername
                    print('Acoount Name')
                    accountname=input()
                    print('\n')
                    print("Generate automatic password(G) or Create new password(C)?")
                    decision=input()
                    if decision=="G":
                        characters=string.ascli_letters + string.digits
                        accountpassword="".join(choice(characters)for x in range(randit(6,16)))
                        print(f"Password: {accountpassword}")
                    elif decision=="C":
                            print('enter your password')
                            accountpassword=input()
                    else:
                        print("please put in a valid choice")
                    save_account(create_account(accountusername,accountname,accountpassword))
                    print('\n')
                    print(f'Username:{accountusername} \nAccount Name: {accountname} \nPassword: {accountpassword}') 
                elif choose == "VC":
                    if find_account(accountusername):
                        print('Here is a list of your created accounts: ')
                        print("-"*25)
                        for user in display_accounts():
                            print(f'Account: {user.accountname} \nPassword: {user.accountpassword} \n\n ')
                        else:
                            print('invalid creds!')
                    else:
                        print('PLEASE TRY AGAIN')
                        print('\n')
                else:
                    print('Incorrect INFO please try again! Thankyou')
                    print('\n')
            else:
                print('Kindly choose a valid option')
                print('\n')
if _name_ == '_main_':
    main()                                        







