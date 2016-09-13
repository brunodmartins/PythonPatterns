from command.LoginButtonGUI import User, LoginButton, LoginCommand

__author__ = 'Bruno'

import unittest


class MyTestCase(unittest.TestCase):
    def test(self):
        user = User()
        button = LoginButton(LoginCommand(user))
        user.login = "root"
        user.password = 123456
        button.on_press()


if __name__ == '__main__':
    unittest.main()
