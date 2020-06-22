from Ejercicios.figura import *
from Ejercicios.alumno import Student


trian = Triangulo()
trian.setBase(5)
trian.setAltura(4)
trian.calArea()
print(trian.getArea())

rect = Rectangulo()
rect.setBase(10)
rect.setAltura(5)
rect.calArea()
print(rect.getArea())

estudiambre = Student("Mildred","Mildred@gmail.com","12345")
print(estudiambre)