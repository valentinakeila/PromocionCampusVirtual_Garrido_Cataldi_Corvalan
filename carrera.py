
class Carrera:
    def __init__(self, nombre:str, cant_anios: int ):
        self.__nombre = nombre
        self.__cant_anios = 2

    def __str__(self):
        return "Nombre" + self.__nombre + "Cantidad de años" + self.__cant_anios