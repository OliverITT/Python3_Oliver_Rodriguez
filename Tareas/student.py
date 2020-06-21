
class Student():

    def __init__(self,name=None,email=None,passw=None):
        self._name= name
        self._email = email
        self._passw = passw

    def getName(self):
        return self._name

    def setName(self,name):
        self._name = name

    def getEmail(self):
        return self._email

    def setEmail(self,email):
        self._email = email

    def getPassw(self):
        return self._passw

    def setPassw(self, passw):
        self._passw = passw
