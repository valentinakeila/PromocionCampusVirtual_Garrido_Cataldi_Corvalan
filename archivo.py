from datetime import *
class Archivo:
    def __init__(self, nombre: str, formato: str, ):
        self.__nombre = nombre
        self.__fecha = datetime.today()
        self.__formato = "PDF"

    def __str__(self):
        return "Nombre" + self.__nombre + "Fecha" + self.__fecha + "Formato:" + self.__formato