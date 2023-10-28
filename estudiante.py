import random
from usuario import Usuario
from cursos import Cursos


class Estudiante(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, anio_inscripcion: int):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = self.__generar_legajo()
        self.__anio_inscripcion_carrera = anio_inscripcion
        self.__mis_cursos = []

    def __str__(self):
        return (super().__str__() + " Legajo: " + self.__legajo, " Año de inscripcion: " +
                self.__anio_inscripcion_carrera)  # Esto funciona ignorar el warning jeje

    # El diagrama UML pide de parametro crear un curso pero el enunciado pide mostrar una lista de los cursos
    # ya existentes y seleccionar el deseado a agregar al atributo mis_cursos
    # decidimos hacer esta funcionalidad en el programa principal siguiendo las pautas del enunciado
    # @classmethod
    # def matricular_en_curso(cls, self, curso: Cursos):

    # Hice diferente la asignacion del legajo para que se genere automaticamente igual que el año
    @classmethod
    def __generar_legajo(cls):
        return random.randint(100000, 999999)

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, valor):
        return self._apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        self._email = valor

    @property
    def contrasenia(self):
        return self._contrasenia

    @contrasenia.setter
    def contrasenia(self, valor):
        self._contrasenia = valor

    @property
    def legajo(self):
        return self.__legajo

    @legajo.setter
    def legajo(self, valor: int):
        self.__legajo = valor

    @property
    def anio_inscripcion_carrera(self):
        return self.__anio_inscripcion_carrera

    @anio_inscripcion_carrera.setter
    def anio_inscripcion_carrera(self, valor):
        self.__anio_inscripcion_carrera = valor

    @property
    def mis_cursos(self):
        return self.__mis_cursos

    @mis_cursos.setter
    def mis_cursos(self,valor):
        self.__mis_cursos = valor

        # decorador classmethod, parametro cls, cuando el profe haga dictar curso esto agregara cursos a su lista
        # mis_cursos,



