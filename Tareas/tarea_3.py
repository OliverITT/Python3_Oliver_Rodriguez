from Tareas.student import Student
import Tareas.StudentIO_T3 as IO
nombres = ["Mary","Christine","Stacy","Donna B Barefield","Ann D Wilhelm"]
emails = ["kailyn_wilkins@yahoo.com","antone1977@hotmail.com","celestino.crem@gmail.com","elias1989@gmail.com","nakia1976@gmail.com"]
paswords = ["614-751-0124","313-385-4925","401-275-3281","716-258-6655","316-794-9842"]


students =[]

for n,e,p in zip(nombres,emails,paswords):
    students.append(Student(n, e, p))

IO.writeStudentsP(students)

newstd  = Student("peyton","peyton@gmail.com","112")

IO.updateStudetP('Stacy',newstd)
newstd = Student("Dot","dot@gmail.com","412")
IO.insertStudentP(newstd)

lectura = IO.readStudentsP()

for i in lectura:
   print(i.getName())
print(len(lectura))

#shelve
IO.writeStudentsS(students)
IO.insertStudentS(Student("uno","dos","tres"))

IO.updateStudetS("uno", Student("Mildred","quinn1981@yahoo.com","513-375-5536"))

t = IO.readStudentsS()
for i in t:
    print(i.getName())

print(len(t))