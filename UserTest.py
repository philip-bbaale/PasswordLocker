import unittest
from User import Users

class TestUser(unittest.TestCase):
    def setUp(self):
        self.newlogin = Users("pipbbaale","2001","putlocker")

    def test_init(self):
        self.assertEqual(self.newlogin.username,"pipbbaale")
        self.assertEqual(self.newlogin.password,"2001")
        self.assertEqual(self.newlogin.accountType,"putlocker")

    def test_save_user_account(self):
        self.newlogin.save_user_account()
        self.assertEqual(len(Users.userLogin_list),1)

    def tearDown(self):
        Users.userLogin_list = []

    def test_save_multiple_user_accounts(self):
        self.newlogin.save_user_account()
        test_user = Users("namesusing","passusing","accountusing")
        test_user.save_user_account()
        self.assertEqual(len(Users.userLogin_list),2)

    def test_user_accounts_exist(self):
        self.newlogin.save_user_account()
        test_user = Users("namesusing","passusing","accountusing")
        test_user.save_user_account()
        user_account_exists = Users.user_account_exists("namesusing")
        self.assertTrue(user_account_exists)

    def test_display_users_acounts(self):
        self.assertEqual(Users.display_user_accounts(),Users.userLogin_list)



if __name__ == '__main__':
    unittest.main()