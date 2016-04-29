import unittest
from memento import saves

__author__ = 'Bruno'


class Test(unittest.TestCase):

    def test_save_file(self):
        save1 = saves.SaveFile()
        m = saves.MemoryCard()
        self.assertTrue(save1.name, 'save_file');
        m.add_save(save1.save_file())
        save1.name = 'bla'
        self.assertTrue(save1.name, 'bla');
        save1.return_save(m.get_save(0))
        self.assertTrue(save1.name, 'save_file');

if __name__ == '__main__':
    unittest.main()