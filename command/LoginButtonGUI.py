import abc

__author__ = 'Bruno'


class Command:
    """
    The command's class
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self):
        """
        Executes a command
        :return:
        """
        raise NotImplementedError


class User:
    """
    User class
    """

    def __init__(self, login="", password=""):
        """
        Constructor
        """
        self.login = login;
        self.password = password;


class LoginCommand(Command):
    """
    Login's command class
    """

    def __init__(self, user=None):
        """
        Constructor
        """
        self.user = user;

    def execute(self):
        """
        Execute the command
        """
        LoginService.do_login(self.user)


class LoginService:
    """
    LoginService class
    """

    @classmethod
    def do_login(cls, user=None):
        """
        Do Login
        :param user:
        :return:
        """
        print("Login: {} - Password: {}".format(user.login, user.password))


class LoginButton:
    """
    Login's button class
    """

    def __init__(self, command=None):
        """
        Constructor
        :param command:
        :return:
        """
        self.command = command

    def on_press(self):
        """
        On press action
        """
        self.command.execute()
