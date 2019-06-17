import unittest # Importing the unittest module
import pyperclip
from account import User # Importing the user class

class TestAccount(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = User("userfn","userln","0712345678","user@gmail.com","userpassword","userplatform") # create account object


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.account_list = []

    

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.first_name,"userfn")
        self.assertEqual(self.new_account.last_name,"userln")
        self.assertEqual(self.new_account.phone_number,"0712345678")
        self.assertEqual(self.new_account.email,"user@gmail.com")
        self.assertEqual(self.new_account.password,"userpassword")
        self.assertEqual(self.new_account.platform,"userplatform")


    def test_save_account(self):
        '''
        test_save_account test case to test if the contact object is saved into
         the account list
        '''
        self.new_account.save_account() # saving the new account
        self.assertEqual(len(User.account_list),1)    

    def test_save_multiple_account(self):
            '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_account.save_account()
            test_account = User("Test","user","0712345678","test@user.com","password","platform") # new account
            test_account.save_account()
            self.assertEqual(len(User.account_list),2)

    def test_delete_account(self):
            '''
            test_delete_account to test if we can remove a account from our account list
            '''
            self.new_account.save_account()
            test_account = User("Test","user","0712345678","test@user.com","password","platform") # new account
            test_account.save_account()

            self.new_account.delete_account()# Deleting a account object
            self.assertEqual(len(User.account_list),1)

    def test_find_account_by_platform(self):
        '''
        test to check if we can find a account by the platform and display information
        '''

        self.new_account.save_account()
        test_account = User("Test","user","0711223344","test@user.com","password","platform") # new account
        test_account.save_account()

        found_account = User.find_by_platform("platform")

        self.assertEqual(found_account.email,test_account.email)

    def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''

        self.new_account.save_account()
        test_account = User("Test","user","0711223344","test@user.com","password","platform") # new account
        test_account.save_account()

        account_exists = User.account_exist("platform")

        self.assertTrue(account_exists)

    def test_display_all_accounts(self):
        '''
        method that returns a list of all accounts saved
        '''

        self.assertEqual(User.display_accounts(),User.account_list)

        
    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found account
        '''

        self.new_account.save_account()
        User.copy_email("0712345678")

        self.assertEqual(self.new_account.email,pyperclip.paste())

if __name__ == '__main__':
    unittest.main()

