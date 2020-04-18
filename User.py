class Credentials:
    """
    Class that generates new instances of usersLogin.
    """

    userLogin_list = []

    def __init__(self,username,password,accountType):
        self.username = username
        self.password = password
        self.accountType = accountType

    def save_user_account(self):
        Credentials.userLogin_list.append(self)

    @classmethod
    def user_account_exists(cls,username):
        for user in cls.userLogin_list:
            if user.username == username:
                return True
        return False

    @classmethod
    def display_user_accounts(cls):
        return cls.userLogin_list

class User: