import unittest
from template.army import Warrior, Archer, SpellCaster

__author__ = 'Bruno'


class TestTemplate(unittest.TestCase):
    def test(self):
        warrior = Warrior()
        archer = Archer()
        spell_caster = SpellCaster()
        print("------------------Warrior-------------------")
        warrior.attack()
        print("------------------Archer--------------------")
        archer.attack()
        print("---------------SpellCaster------------------")
        spell_caster.attack()


if __name__ == '__main__':
    unittest.main()
