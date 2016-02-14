#!usr/bin/python3
__author__ = 'josue'
from Lista import Lista
import random

def main():
    lista = Lista()


    for i in range(0,10):
        numero = random.randrange(0,30)
        if(numero < 14):
	        lista.insertarPrimero(numero)
        elif(numero%2 == 0):
	        lista.insertarUltimo(numero)
        else:
	        lista.insertarOrdenado(numero)

    print("-------------------------------------------")
    print("|           Probando la lista             |")
    print("-------------------------------------------\n")
    listSize = lista.longitud()
    print("Lista no ordenada con longitud ",listSize,"\n")
    lista.visualizar()
    print("\nPrueba aleatoria de borrado de 3 elementos\n")
    for i in range(3):
        borrado(lista)
    lista.ordenar()
    listSize2 = lista.longitud()
    if(listSize==listSize2):
        print("No se han borrado datos\n")
    else:
        print("Se borraron ",(listSize-listSize2)," elemento/s\n")
         
    print("Lista ordenada con longitud ",listSize2)
    lista.visualizar()

def borrado(lista):
    numero = random.randrange(0,30)

    if(lista.existe(numero)):
        if(random.randrange(1,3) == 1):
            print("Eliminando 1 aparicion de ",numero," de la lista")
            lista.eliminar(numero,1)
        else:
            print("Eliminando todas las apariciones de ",numero," de la lista")
            lista.eliminar(numero,2)
    else:
        print(numero," no existe en la lista -> no se elimina")
        

if __name__ == '__main__':
    main()
