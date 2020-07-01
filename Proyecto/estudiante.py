class Estudiante:
    _nombre = ''
    _correo = ''
    _contrasena = ''

    def __init__(self, nombre, correo, contrasena):
        self._nombre = nombre
        self._correo = correo
        self._contrasena = contrasena

    def __str__(self):
        return f'Nombre: {self._nombre}\n' \
               f'Correo: {self._correo}\n'

    def nombre(self):
        return self._nombre

    def correo(self):
        return self._correo

    def contrasena(self):
        return self._contrasena

    def actualizarNombre(self, nombre=None):
        if nombre:
            self._nombre = nombre
            return True
        else:
            return False

    def actualizarCorreo(self, correo=None):
        if correo:
            self._correo = correo
            return True
        else:
            return False

    def actualizarContrasena(self, contrasena=None):
        if contrasena:
            self._contrasena = contrasena
            return True
        else:
            return False