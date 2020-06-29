from mongoengine import *
from Tareas.students import Students


if __name__ == '__main__':
    db = connect('padts')
    estudiante = Students()
    estudiante.switch_collection('estudiante')
    estudiante.guardarStudent(Students(name='Elizabeth', email='correo@', passw='123ps'))
    estudiante.guardarStudent(Students(name='Alcapone', email='correo@', passw='123ps'))
    estudiante.guardarStudent(Students(name='Diana', email='correo@', passw='123ps'))
    estudiante.guardarStudent(Students(name='Carlos', email='correo@', passw='123ps'))
    estudiante.guardarStudent(Students(name='Ragnar', email='correo@', passw='123ps'))

    t = estudiante.consultarByName(name='Elizabeth')
    print(t)
    y = estudiante.actualizar(name='Alcapone', student=Students(name='Benito', email='correo@', passw='123ps'))
    print(y)
    g = estudiante.eliminar(name='Benito')
    print(g[0].id)



