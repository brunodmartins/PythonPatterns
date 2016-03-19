import abc
__author__ = 'Bruno'


class GuiFactory(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_button(self):
        """Create one button"""
        raise NotImplementedError

    @classmethod
    def create_factory(cls, name):
        if name == 'Gnome':
            return GnomeFactory();
        else:
            return KDEFactory();


class GnomeFactory(GuiFactory):

    def create_button(self):
        return GnomeButton();


class KDEFactory(GuiFactory):

    def create_button(self):
        return KDEButton();


class Button(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def paint(self):
        """Paint something"""
        raise NotImplementedError


class GnomeButton(Button):

    def paint(self):
        print('GnomeButton');


class KDEButton(Button):

    def paint(self):
        print('KDEButton');


factory = GuiFactory.create_factory('Gnome');
button = factory.create_button();
button.paint();
factory = GuiFactory.create_factory('Kde');
button = factory.create_button();
button.paint();