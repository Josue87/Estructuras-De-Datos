#!usr/bin/python3
__author__ = 'josue'
from Lista import Lista
import random

def main():
    lista = Lista()


    for i in range(0,10):
        num = random.randrange(0,30)
        if(num < 14):
	        lista.insertarPrimero(num)
        elif(num%2 == 0):
	        lista.insertarUltimo(num)
        else:
	        lista.insertarOrdenado(num)

    print("-------------------------------------------")
    print("|           Probando la lista             |")
    print("-------------------------------------------\n")
    tam = lista.longitud()
    print("Lista con longitud ",tam,"\n")
    lista.visualizar()
    print("Intentando borrar datos...\n")
    for i in range(3):
        borrado(lista)
    lista.ordenar()
    tam2 = lista.longitud()
    if(tam==tam2):
        print("No se han borrado datos\n")
    else:
        print("Se borraron ",(tam-tam2)," elementos\n")
         
    print("Lista ordenada con longitud ",tam2)
    lista.visualizar()

def borrado(lista):
    num = random.randrange(0,30)

    if(lista.existe(num)):
        if(random.randrange(1,3) == 1):
            print("Eliminando 1 aparición de ",num," de la lista")
            lista.eliminar(num,1)
        else:
            print("Eliminando todas las apariciones de ",num," de la lista")
            lista.eliminar(num,2)
    else:
        print(num," no existe en la lista -> no se elimina")
        

if __name__ == '__main__':
    main()
