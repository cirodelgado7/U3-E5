from zope.interface import Interface


class IElemento(Interface):

    def insertarElemento(elemento, indice):
        pass

    def agregarElemento(elemento):
        pass

    def mostrarElemento(indice):
        pass