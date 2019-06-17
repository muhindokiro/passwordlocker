#!/usr/bin/env python3.6
from account import User

def create_account(fname,lname,phone,email,password,platform):
    '''
    Function to create a new account
    '''
    new_account = User(fname,lname,phone,email,password,platform)
    return new_account

def save_accounts(account):
    '''
    Function to save account
    '''
    account.save_account()

def del_account(account):
    '''
    Function to delete a account
    '''
    account.delete_account()

def find_account(text):
    '''
    Function that finds an account by platform and returns the account
    '''
    return User.find_by_platform(text)

def check_existing_accounts(text):
    '''
    Function that check if an account exists with that platform and returns a Boolean
    '''
    return User.account_exist(text)

def display_accounts():
    '''
    Function that returns all saved accounts
    '''
    return User.display_accounts()

def main():
            print("Hello Welcome to your account list. What is your name?")
            user_name = input()
            
            print(f"Hello {user_name}. what would you like to do?")
            print('\n')

            while True:
                    print("Use these short codes : cc - create a new account, dc - display accounts, fc -find an account, ex -exit the account list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Account")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Phone number ...")
                            p_number = input()

                            print("Email address ...")
                            e_address = input()

                            print("Password ...")
                            password = input()

                            print("Platform (facebook,twitter e.t.c) ...")
                            platform = input()


                            save_accounts(create_account(f_name,l_name,p_number,e_address,password,platform)) # create and save new account.
                            print ('\n')
                            print(f"New Account {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_accounts():
                                    print("Here is a list of all your accounts")
                                    print('\n')

                                    for account in display_accounts():
                                            print(f"{account.first_name} {account.last_name} .....{account.platform}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any accounts saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the platform account you want to search for")

                            search_platform = input()
                            if check_existing_accounts(search_platform):
                                    search_account = find_account(search_platform)
                                    print(f"{search_account.first_name} {search_account.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number..{search_account.phone_number}")
                                    print(f"Email address..{search_account.email}")
                                    print(f"Password..{search_account.password}")
                            else:
                                    print("That account does not exist")

                    elif short_code == "ex":
                            print("Thank you for using this application ;) ")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()
