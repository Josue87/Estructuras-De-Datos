#!usr/bin/python3
__author__ = 'josue'
from Nodo import Nodo

class Lista():
    def __init__(self):
        self.lista = None

    def insertarPrimero(self, datosAInsertar):
        nodo = Nodo()
        nodo.datos = datosAInsertar
        if self.esVacia():
            nodo.siguiente = None
        else:
            nodo.siguiente = self.lista
        self.lista = nodo

    def insertarUltimo(self, datosAInsertar):
        nodo = Nodo()
        nodo.datos = datosAInsertar
        nodo.siguiente = None
        if self.esVacia():
            self.lista = nodo
        else:
            copiaLista = self.lista
            while copiaLista.siguiente!=None:
                copiaLista = copiaLista.siguiente
            copiaLista.siguiente = nodo

    def insertarOrdenado(self, datosAInsertar): # si la lista esta desordenada, no hace maravillas
        nodo = Nodo()
        nodo.datos = datosAInsertar
        if self.esVacia():
            nodo.siguiente = None
            self.lista = nodo
        else:
            copiaLista = self.lista
            listaAuxiliar = None
            while  (copiaLista!=None) and (nodo.comparar(copiaLista.datos)>=0): # el orden de la comprobacion importa
                listaAuxiliar = copiaLista
                copiaLista = copiaLista.siguiente
            nodo.siguiente = copiaLista
            if listaAuxiliar == None: 
                self.lista = nodo
            else:
                listaAuxiliar.siguiente = nodo

    def eliminar(self, datosABorrar, modo = 1): # si modo es distinto a 1 se eliminan todas las apariciones, si no la primera
        copiaLista = self.lista
        listaAuxiliar = None
        encontrado = False
        while(copiaLista!=None and not encontrado):
            encontrado = (copiaLista.comparar(datosABorrar) == 0)
            if not encontrado:
                listaAuxiliar = copiaLista
                copiaLista = copiaLista.siguiente
        if encontrado:
            if listaAuxiliar == None:
                self.lista = copiaLista.siguiente
            else:
                    listaAuxiliar.siguiente = copiaLista.siguiente
            nodoABorrar = copiaLista
            copiaLista = copiaLista.siguiente
            del nodoABorrar
            if modo != 1:
                while(copiaLista!=None):
                    if(copiaLista.comparar(datosABorrar) == 0):
                        if listaAuxiliar == None:
                            self.lista = copiaLista.siguiente
                        else:
                            listaAuxiliar.siguiente = copiaLista.siguiente
                        nodoABorrar = copiaLista
                        copiaLista = copiaLista.siguiente
                        del nodoABorrar
                    else:
                        listaAuxiliar = copiaLista
                        copiaLista = copiaLista.siguiente


    def ordenar(self):
        if self.longitud()>1: 
            copiaLista = self.lista
            while copiaLista != None:
                listaAuxiliar = copiaLista.siguiente
                mirarNodo = copiaLista
                while listaAuxiliar != None:
                    if mirarNodo.comparar(listaAuxiliar.datos)>0: 
                        mirarNodo = listaAuxiliar
                    listaAuxiliar = listaAuxiliar.siguiente
                if mirarNodo!=copiaLista: 
                    datos = mirarNodo.datos
                    mirarNodo.datos = copiaLista.datos
                    copiaLista.datos = datos
                copiaLista = copiaLista.siguiente



    def existe(self,datosNodo):
        copiaLista = self.lista
        while copiaLista!=None:
            if copiaLista.comparar(datosNodo) == 0:
                return True
            copiaLista = copiaLista.siguiente
        return False



    def primero(self):
        if self.esVacia():
            return None
        else:
            return self.lista.datos

    def esVacia(self):
        return self.lista == None

    def longitud(self):
        copiaLista = self.lista
        cont = 0
        while copiaLista!=None:
            cont += 1
            copiaLista = copiaLista.siguiente
        return cont

    def visualizar(self):
        copiaLista = self.lista
        cont = 0
        while copiaLista!=None:
            print(copiaLista.datos, end=" ")
            cont +=1
            if cont%12 == 0:
                print()
            copiaLista = copiaLista.siguiente
        print()
