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
