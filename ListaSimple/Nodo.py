#!usr/bin/python3
__author__ = 'josue'

class Nodo():
    def __init__(self):
        self.datos = None
        self.siguiente = None

    def comparar(self, nodo):
        if self.datos > nodo:
            return 1
        elif self.datos < nodo:
            return -1
        else:
            return 0

