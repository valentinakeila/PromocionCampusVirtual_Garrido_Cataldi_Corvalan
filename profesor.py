from usuario import Usuario

class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, titulo: str, anio_egreso: int):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        self.__mis_cursos = []

    def __str__(self):
        return super().__str__() + " Titulo: " + self.__titulo + " Año de egreso: " + self.__anio_egreso


    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,valor):
        self.nombre = valor

    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self,valor):
        self.apellido = valor


    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self,valor):
        self.email = valor


    @property
    def contrasenia(self):
        return self._contrasenia
    
    
    @contrasenia.setter
    def contrasenia(self,valor):
        self._contrasenia = valor
    
    
    
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, valor):
        self.__titulo = valor

    @property
    def anio_egreso(self):
        return self.__anio_egreso

    @anio_egreso.setter
    def anio_egreso(self, valor):
        self.__anio_egreso = valor

    @property
    def mis_cursos(self):
        return self.__mis_cursos

