""" Module which contain an example attribute mixin class """

class Test_AttrMixin:
    """ The attributes defined in this class will be picked up at design-time
        when mixed with a frame like class """
    def __init__(self):
        self.name1 = 1
        self.frameTitle = 'Attr'
        self.buttonLabel = 'Mixin'
