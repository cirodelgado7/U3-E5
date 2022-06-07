from zope.interface import implementer
from Interface import IElemento


@implementer(IElemento)
class Coleccion:
    __comienzo = None

    def __init__(self):
        self.__comienzo = None

    def insertarElemento(self, indice, elemento):
        '''Codigo para insertar un nodo'''

    def agregarElemento(self, elemento):
        '''Codigo para agregar un nodo al final'''

    def mostrarElemento(self, indice):
        '''Codigo para mostrar un nodo'''
