import abc

__author__ = 'Bruno'


class IFilter:
    """
    Class IFilter
    """
    __metaclass__ = abc.ABCMeta

    nextFilter = None

    @abc.abstractmethod
    def execute(self):
        """
        Execute a process
        :return: Void
        """
        raise NotImplementedError


class SessionFilter(IFilter):
    """
    A Session's filter
    """

    def execute(self):
        print('Session Filter started')
        valid_session = True
        if not valid_session:
            raise Exception('Invalid Session')
        else:
            print('Valid Session')
        if self.nextFilter is not None:
            print('Next Filter')
            self.nextFilter.execute()


class SecurityFilter(IFilter):
    """
    Security's filter
    """

    def execute(self):
        print('Security Filter started')
        secure = True
        if not secure:
            raise Exception("Insecure session")
        else:
            print('Is secure')
        if self.nextFilter is not None:
            print('Next Filter')
            self.nextFilter.execute()


class AjaxCallFilter(IFilter):
    """
    Ajax's call filter
    """

    def execute(self):
        print('Ajax call Filter started')
        ajax = False
        if ajax:
            print('Ajax call')
        else:
            print('Not Ajax call')
        if self.nextFilter is not None:
            print('Next Filter')
            self.nextFilter.execute()
