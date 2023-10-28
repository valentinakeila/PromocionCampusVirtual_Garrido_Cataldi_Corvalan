import secrets


class Cursos:

    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__contrasenia_matriculacion = self.__generar_contrasenia()
        self.__alta = False #Empieza dado de baja y un profesor puede darlo de alta para dictarlo

    @classmethod
    def __generar_contrasenia(cls):
        password_length = 4
        return secrets.token_urlsafe(password_length)

    def __str__(self):
        return f"{self.__nombre}: '{self.__contrasenia_matriculacion}'"

    @property
    def alta(self):
        return self.__alta

    @alta.setter
    def alta(self,valor):
        self.__alta = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def contrasenia(self):
        return self.__contrasenia_matriculacion

    @contrasenia.setter
    def contrasenia(self, valor):
        self.__contrasenia_matriculacion = valor

# cursoMatematica = Cursos("Matematica")
# cursoLengua = Cursos("Lengua")
# cursoFisica = Cursos("Fisica")
# cursoEdF = Cursos("Educacion Fisica")
# cursoMusica = Cursos("Musica")
# cursoGeografia = Cursos("Geografia")
# cursos = [cursoMatematica,cursoLengua,cursoMusica,cursoFisica,cursoEdF,cursoGeografia]
#
#
# contador = 0
# for i in cursos:
#     if contador % 3 == 0:
#         print("\n")
#     print(i,end="    ")
#     contador = contador + 1
