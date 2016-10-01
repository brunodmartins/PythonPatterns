"""
Date: 30/09/2016
Test module
@author: BrunoDM2943
"""
from unittest import TestCase
from mediator.chatroom import *

class TestMediator(TestCase):
    """
    Test class
    """

    def test_chat(self):
        chat = Chat()
        bruno = Member(chat, 'Bruno')
        leh = Member(chat, 'Leh')
        dog = Member(chat, 'Dog')
        bruno.send_message('Love u Leh <3')
        dog.send_message('Bark!')
        leh.send_message('Love u too Bruno <3')

        for m in [bruno,leh,dog]:
            print(m.name + ' messages')
            for msg in m.messages:
                print(msg)
