from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia

    @abstractmethod  # se obliga a sobreescribir el metodo para no repetir codigo
    def __str__(self):
        return "Nombre: " + self._nombre + " Apellido: " + self._apellido + " Email: " + self._email + " Contraseña: " + self._contrasenia

    def validar_credenciales(self, email: str, contrasenia: str):
        if self._email == email and self._contrasenia == contrasenia:
            return True, "Credenciales correctas"
        return False, "Credenciales incorrectas"
