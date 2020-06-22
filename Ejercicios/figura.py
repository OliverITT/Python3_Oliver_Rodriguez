
class Figura():

    def __int__(self, area=0, base=0, altura=0):
        self._area = area
        self._base = base
        self._altura = altura

    def getArea(self):
        return self._area

    def setArea(self, area=0):
        self._area = area

    def getBase(self):
        return self._base

    def setBase(self, base=0):
        self._base = base

    def getAltura(self):
        return self._altura

    def setAltura(self, altura=0):
        self._altura = altura

    def calArea(self):
        pass


class Triangulo(Figura):

    def __int__(self, area=0, base=0, altura=0):
        self._area = area
        self._base = base
        self._altura = altura

    def calArea(self):
        self._area = (self._base * self._altura) / 2


class Rectangulo(Figura):

    def __int__(self, area=0, base=0, altura=0):
        self._area = area
        self._base = base
        self._altura = altura

    def calArea(self):
        self._area = (self._base * self._altura)
