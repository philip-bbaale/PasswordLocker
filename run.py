#!/usr/bin/env python3
from User import Users

def create_user_account(username,password,accountType):
    new_user_account = Users(username,password,accountType)
    return new_user_account

def save_user_account(User):
    User.save_user_account()

def check_existing_user_account(username):
    return Users.user_account_exists(username)
'''
def display_user_accounts():
    return Users.display_user_accounts()

def main():
    print ("Hi there, Welcome to Password Locker. A safe place to store all your passwords")
    print ("What is your username")
    user_name = input()
    print ("Please input your password")
    user_password = input()
    print (f"Hello {user_name} \n Your password is {user_password}")

    while True:
        print("Use these short codes : nw - Create a new account locker., dp - Display account lockers.,  ex - Exit Password Locker.  ")

        short_code = input().lower()

        if short_code == 'nw':
            print("New Account Locker")
            print("-"*10)

            print ("Account Username")
            username = input()

            print("Account password")
            password = input()

            print("Account type")
            accountType = input()

            save_user_account(create_user_account(username,password,accountType))
            print ('\n')
            print(f"New Contact {accountType} {username} created")
            print ('\n')

        elif short_code == 'dp':

            if display_user_accounts():
                print("Here is a list of all your Accounts details")
                print('\n')

                for Users in display_user_accounts():
                        print(f" Account type: {Users.accountType}\n Username: {Users.username} \n Password: {Users.password}")

                print('\n')
            else:
                print('\n')
                print("You dont seem to have any Account information yet")
                print('\n')

        elif short_code == "ex":
                print("Thank you for trusting us!")
                break

        else:
                print("I really didn't get that. Please use the short codes")




if __name__ == '__main__':

    main()