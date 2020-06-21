try:
    import cPickle as pickle
except ImportError:
    import pickle
import shelve


def writeStudentsP(student):
    file = open("student.db", "wb")
    pickle.Pickler(file,4).dump(student)
    file.close()


def readStudentsP():
    try:
        file = open("student.db", "rb")
    except Exception:
        print("Error al abrir el archivo")
    unpik = pickle.Unpickler(file)
    return unpik.load()

def updateStudetP(name, student):
    temp = readStudentsP()
    for i in range(len(temp)):
        if temp[i].getName() == name:
            temp[i]= student
    writeStudentsP(temp)

def insertStudentP(student):
    temp = readStudentsP()
    file = open("student.db", "wb")
    temp.append(student)
    writeStudentsP(temp)
    file.close()



def writeStudentsS(student):
    with shelve.open("student") as s:
        for i in range(len(student)):
            s[student[i].getName()]=student[i]

def readStudentsS():
    l=[]
    with shelve.open("student") as s:
        for i in s.keys():
            l.append(s[i])
    return l

def updateStudetS(key, student):
    with shelve.open("student") as s:
        s[key] = student

def insertStudentS(student):
    with shelve.open("student") as s:
        s[student.getName()] = student
