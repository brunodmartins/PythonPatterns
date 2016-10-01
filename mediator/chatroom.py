"""
Date: 29/09/2016
@author: bruno
"""
import abc


class IChat:
    """
    IChat interface defining operation
    """
    __metaclass__ = abc.ABCMeta

    def send_message(self, member, message):
        """
        Notify all members in
        the chat room
        :param member: The rementent
        :param message: The message
        """
        raise NotImplementedError

    def join_chat(self, member):
        """
        Add a member to the chat
        :param member: The member to join
        """
        raise NotImplementedError

    def leave_chat(self, member):
        """
        Leaves the chat
        :param member: The member to leave
        """
        raise NotImplementedError


class Chat(IChat):
    """
    The chat implementation
    """

    def __init__(self):
        """
        Constructor
        """
        self.members = []

    def send_message(self, member, message):
        """
        Notify all members in
        the chat room
        :param member: The rementent
        :param message: The message
        """
        lst = [m for m in self.members if m.name != member.name]
        for m in lst:
            m.receive_message(member.name + ' typed: ' + message)

    def join_chat(self, member):
        """
        Add a member to the chat
        :param member: The member to join
        """
        self.members.append(member)
        self.send_message(member, member.name + ' joined the chat')

    def leave_chat(self, member):
        """
        Leaves the chat
        :param member: The member to leave
        """
        self.members.remove(member)
        self.send_message(member, member.name + ' leaved the chat')


class Member:
    """
    The member class
    """

    def __init__(self, chat_room, name):
        """
        Constructor
        :param chat_room: The chat
        :param name: The member's name
        """
        self.chat_room = chat_room
        self.name = name
        self.messages = []
        self.chat_room.join_chat(self)

    def send_message(self, message):
        """
        Sends a message
        """
        self.messages.append('Me: ' + message)
        self.chat_room.send_message(self, message)

    def receive_message(self, message):
        """
        Receives a message
        """
        self.messages.append(message)

    def __str__(self):
        """
        String representation
        """
        return self.name
