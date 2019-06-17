class User:
    """
    Class that generates new instances of accounts
    """
    account_list = [] # Empty account list

    def __init__(self,first_name,last_name,number,email,password,platform):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
        self.password = password
        self.platform = platform

    def save_account(self):

        '''
        save_account method saves an account objects into account_list
        '''

        User.account_list.append(self)

    def delete_account(self):

        '''
        delete_account method deletes a saved account from the account_list
        '''

        User.account_list.remove(self)    

    @classmethod
    def find_by_platform(cls,text):
        '''
        Method that takes in a platform and returns an account that was created in that platform.

        Args:
            text: Platform to search for
        Returns :
            User of person that matches the platform.
        '''

        for account in cls.account_list:
            if account.platform == text:
                return account

    @classmethod
    def account_exist(cls,text):
        '''
        Method that checks if an account exists from the account list.
        Args:
            text: Platform to search if it exists
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for account in cls.account_list:
            if account.platform == text:
                    return True

        return False

    @classmethod
    def display_accounts(cls):
        '''
        method that returns the account list
        '''
        return cls.account_list

    @classmethod
    def copy_email(cls,text):
        account_found = User.find_by_platform(text)
        pyperclip.copy(account_found.email)


    
    

    
