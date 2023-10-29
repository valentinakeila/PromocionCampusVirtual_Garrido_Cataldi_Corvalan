
class Carrera:
    def __init__(self, nombre:str, cant_anios: int ):
        self.__nombre = nombre
        self.__cant_anios = 2
        self.__cursos = []

    def __str__(self):
        return "Nombre" + self.__nombre + "Cantidad de años" + self.__cant_anios

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def cant_anios(self):
        return self.__cant_anios

    @cant_anios.setter
    def cant_anios(self, valor):
        self.__cant_anios = valor

    @property
    def cursos(self):
        return self.__cursos

    @cursos.setter
    def cursos(self, valor):
        self.__cursos = valor
