import unittest
from chainOfResponsability import webFilters

__author__ = 'Bruno'


class Test(unittest.TestCase):
    def test(self):
        session_filter = webFilters.SessionFilter()
        security_filter = webFilters.SecurityFilter()
        ajax_call_filter = webFilters.AjaxCallFilter()
        session_filter.nextFilter = security_filter
        security_filter.nextFilter = ajax_call_filter
        ajax_call_filter.nextFilter = None
        session_filter.execute()


if __name__ == '__main__':
    unittest.main()
