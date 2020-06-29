from mongoengine import *
from Tareas.students import Students


if __name__ == '__main__':

    db = connect('padts')

    test = Students()
    test.switch_collection('estudiantes')
    #guardar dato
    test.guardar('oliver', 'preuba', 'insert')
    #consultar
    t = test.consultarByName(name='oliver')
    studenttem = ['oliver643','otra', 'cosa']
    #actualizar
    h=test.actualizar(name='oliver',student=studenttem)
    print(h)
    #eliminar
    test.eliminar(name='oliver')
    print(t)
    #consultar todo
    e = test.consultar()
    print(e)
    test.guardar(name='Mildred',email='qwe',passw='ease')
    test.guardar(name='Mildred', email='qwe', passw='ease')
    test.guardar(name='Mildred', email='qwe', passw='ease')
    test.guardar(name='Mildred', email='qwe', passw='ease')




