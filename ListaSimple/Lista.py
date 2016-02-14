#!usr/bin/python3
__author__ = 'josue'
from Nodo import Nodo

class Lista():
    def __init__(self):
        self.lista = None

    def insertarPrimero(self, dat):
        nodo = Nodo()
        nodo.datos = dat
        if self.esVacia():
            nodo.sig = None
        else:
            nodo.sig = self.lista
        self.lista = nodo

    def insertarUltimo(self, dat):
        nodo = Nodo()
        nodo.datos = dat
        nodo.sig = None
        if self.esVacia():
            self.lista = nodo
        else:
            l = self.lista
            while l.sig!=None:
                l = l.sig
            l.sig = nodo

    def insertarOrdenado(self, dat): # si la lista esta desordenada, no hace maravillas
        nodo = Nodo()
        nodo.datos = dat
        if self.esVacia():
            nodo.sig = None
            self.lista = nodo
        else:
            l1 = self.lista
            l2 = None
            while  (l1!=None) and (nodo.comparar(l1.datos)>=0): # el orden de la comprobación importa
                l2 = l1
                l1 = l1.sig
            nodo.sig = l1
            if l2 == None: 
                self.lista = nodo
            else:
                l2.sig = nodo

    def eliminar(self, n, modo = 1): # si modo es distinto a 1 se eliminan todas las apariciones, si no la primera
        l = self.lista
        laux = None
        encontrado = False
        while(l!=None and not encontrado):
            encontrado = (l.comparar(n) == 0)
            if not encontrado:
                laux = l
                l = l.sig
        if encontrado:
            if laux == None:
                self.lista = l.sig
            else:
                    laux.sig = l.sig
            aux = l
            l = l.sig
            del aux
            if modo != 1:
                while(l!=None):
                    if(l.comparar(n) == 0):
                        if laux == None:
                            self.lista = l.sig
                        else:
                            laux.sig = l.sig
                        aux = l
                        l = l.sig
                        del aux
                    else:
                        laux = l
                        l = l.sig


    def ordenar(self):
        if self.longitud()>1: 
            l = self.lista
            while l != None:
                l2 = l.sig
                aux = l
                while l2 != None:
                    if aux.comparar(l2.datos)>0: 
                        aux = l2
                    l2 = l2.sig
                if aux!=l: 
                    dat = aux.datos
                    aux.datos = l.datos
                    l.datos = dat
                l = l.sig



    def existe(self,n):
        l = self.lista
        while l!=None:
            if l.comparar(n) == 0:
                return True
            l = l.sig
        return False



    def primero(self):
        if self.esVacia():
            return None
        else:
            return self.lista.datos

    def esVacia(self):
        return self.lista == None

    def longitud(self):
        l = self.lista
        cont = 0
        while l!=None:
            cont += 1
            l = l.sig
        return cont

    def visualizar(self):
        l = self.lista
        cont = 0
        while l!=None:
            print(l.datos, end=" ")
            cont +=1
            if cont%12 == 0:
                print()
            l = l.sig
        print()



