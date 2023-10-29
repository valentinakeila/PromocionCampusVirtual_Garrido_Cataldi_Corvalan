from datetime import *
class Archivo:
    def __init__(self, nombre: str, formato: str ):
        self.__nombre = nombre
        self.__fecha = datetime.today()
        self.__formato = formato

    def __str__(self):
        return "Nombre" + self.__nombre + "Fecha" + self.__fecha + "Formato:" + self.__formato

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor
    
    @property
    def fecha(self):
        return self.__fecha 
    @fecha.setter
    def fecha(self, valor):
        self.__fecha = valor

    @property
    def formato(self):
        return self.__formato
    
    @formato.setter
    def formato(self, valor):
        self.__formato = valor