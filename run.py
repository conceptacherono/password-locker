from email.policy import default
import random
from user import User


def main():

    while True:
        print("Welcome to password locker")
        print('/n')
        print("Select a short code to navigate through:to create new user 'new':To login to your account 'log' or 'go' to exit")
        short_code =input().lower()
        print('/n')

        if short_code == 'new':
            print('create username')
            created_user_name = input()

            print('create password')
            created_user_password = input()

            print('confirm password')
            confirm_password = input()

            while confirm_password != created_user_password:
                print('password do not match!')
                print('enter correct password')
                created_user_password = input()
                print('confirm your password')
                confirm_password = input()
            else:
                print(f'congratulations {created_user_name}! account created successfully')
                print('/n')
                print('login')
                print('Username')
                entered_username = input()
                print('your password')
                entered_password = input()

            while entered_username != created_user_name or entered_password != created_user_password:
                print('Invalid username or password')
                print('Username')
                entered_username = input()
                print('your password')
                entered_password = input()

            else:
                print('Welcome! {entered_username} to your account')
                print('/n')  

        elif short_code == 'log':
            print('welcome')
            print('Enter user name')
            default_user_name = input()


            print('Enter password')
            default_user_password = input()
            print('/n')
            while default_user_name != 'testuser' or default_user_password != '0000':
                print('wrong userName or password. Username 'testuser' and password  '0000'')
                print('Enter user name')
                default_user_name

                print('Enter password')
                default_user_password = input()
                print('/n')
            else:
                print('login success')
                print('/n')
                print('/n')

        elif short_code == 'go':
            break
        else:
            print('Enter valid code to continue')

                        
                


        





