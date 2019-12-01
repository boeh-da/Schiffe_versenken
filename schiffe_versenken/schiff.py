# Klasse Schiff aus Aufgabe 8.2.1

class Schiff():

    def __init__(self, laenge):
        self.laenge = laenge

    @property
    def richtung(self):
        return self._richtung

    @richtung.setter
    def richtung(self, value):
        self._richtung = value

    @property
    def start_x(self):
        return self._start_x

    @start_x.setter
    def start_x(self, value):
        if self.richtung == 0:
            if 0 <= value and value+self.laenge <= 10:
                self._start_x = value
            else:
                raise Exception('Schiff nicht gültig platziert')
        elif self.richtung == 1:
            if 0 <= value <=9 :
                self._start_x = value
            else:
                raise Exception('Schiff nicht gültig platziert')

    @property
    def start_y(self):
        return self._start_y

    @start_y.setter
    def start_y(self, value):
        if self.richtung == 1:
            if 0 >= value and value+self.laenge <= 10:
                self._start_y = value
            else:
                raise Exception('Schiff nicht gültig platziert')
        elif self.richtung == 0:
            if 0 <= value <=9 :
                self._start_y = value
            else:
                raise Exception('Schiff nicht gültig platziert')   
