#!usr/bin/python3
__author__ = 'josue'

class Nodo():
    def __init__(self):
        self.datos = None
        self.siguiente = None

    def comparar(self, datosNodo):
        if self.datos > datosNodo:
            return 1
        elif self.datos < datosNodo:
            return -1
        else:
            return 0


