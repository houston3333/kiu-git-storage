import abc


class AbstractFactory(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_button(self):
        pass

    @abc.abstractmethod
    def create_checkbox(self):
        pass


class MacFactory(AbstractFactory):

    color = 'white'

    def create_checkbox(self):
        return Checkbox()

    def create_button(self):
        return TouchButton()


class WindowsFactory(AbstractFactory):

    color = 'blue'

    def create_checkbox(self):
        return Checkbox()

    def create_button(self):
        return TouchButton()


class AbstractButton(metaclass=abc.ABCMeta):
    
    def init(self, color):
        self.color = color

class TouchButton(AbstractButton):

    def touch(self):
        print('Кнопка нажата')


class Checkbox(AbstractButton):

    def check(self):
        print('Галочка поставлена')
