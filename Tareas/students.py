from mongoengine import *


class Students(Document):
    name = StringField(required=True)
    email = StringField(required=True)
    passw = StringField(required=True)

    def guardar(self, name=None, email=None, passw=None):
        return Students(name=name,email=email,passw=passw).save()

    def guardarStudent(self, student=None):
        return student.save()

    def consultarByName(self, name):
        return Students.objects(name=name)

    def consultar(self):
        return Students.objects()

    def actualizar(self, name, student):
        user = Students.objects(name=name).first()
        if not user:
            print(f'dato no encontrado: {name}')
            return -1
        user.update(name=student.name, email=student.email, passw=student.passw)
        return user

    def eliminar(self, name):
        t = Students.objects(name=name).delete()
        return Students.objects()

    def __str__(self):
        return f'{self.name,self.email,self.passw}'