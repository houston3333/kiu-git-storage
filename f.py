import abc


class GUIFactory(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def createButton(self,color):
        pass
    
    @abc.abstractmethod
    def createCheckbox(self,color):
        pass



class WinFactory(GUIFactory):

    def create_product_a(self):
        return createButton()

    def create_product_b(self):
        return createCheckbox()


class MacFactory(GUIFactory):
    
    def create_product_a(self):
        return createButton()

    def create_product_b(self):
        return createCheckbox()


class AbstractButton(metaclass=abc.ABCMeta):
    def __init__(self, color):
        self.color = color
    

class createButton(AbstractButton):
   
    def TouchButton(self):
        print('Кнопка нажата')


class createCheckbox(AbstractButton):

    def check(self):
        print('Галочка поставлена')



def main():
    for factory in (WinFactory(), MacFactory()):
        product_a = factory.create_product_a() 
        product_b = factory.create_product_b()

        product_a.TouchButton()
        product_b.check()


if __name__ == "__main__":
    main()