from mongoengine import *


class Students(Document):
    name = StringField(required=True)
    email = StringField(required=True)
    passw = StringField(required=True)

    def guardar(self, name=None, email=None, passw=None):
        return Students(name=name,email=email,passw=passw).save()

    def consultarByName(self, name):
        return Students.objects(name=name).first()

    def consultar(self):
        return Students.objects().first()

    def actualizar(self, name, student):
        user = Students.objects(name=name).first()
        if not user:
            print(f'dato no encontrado: {name}')
            return -1
        # user.update(email=record['email'])
        user.update(name=student[0], email=student[1], passw=student[2])
        return Students.objects(name=student[0]).first()

    def eliminar(self, name):
        t = Students.objects(name=name).delete()
        return t