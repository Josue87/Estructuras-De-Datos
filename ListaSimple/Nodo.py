#!usr/bin/python3
__author__ = 'josue'

class Nodo():
    def __init__(self):
        self.datos = None
        self.sig = None

    def comparar(self, n):
        if self.datos > n:
            return 1
        elif self.datos < n:
            return -1
        else:
            return 0
