from functools import reduce


def saludo(func):
    func()

def hola():
    print("Hola!!!")

def adios():
    print("Adios!!!")

def use_list():
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]
    odd = [i for i in my_list if i % 2 != 0]
    my_list2 = [1, 2, 3, 4, 5]
    squares2 = []
    squares = [i**2 for i in my_list2]
    for i in my_list2:
        squares2.append(i**2)
    print(odd)
    print(squares)
    print(squares2)
    
"""Tengo una lambda function, que recibe cada uno de los elementos de la lista,(segundo parametro de la 
funcion filter() y al resultado que me dio lo convierto en lista con la función list del principio"""    
def use_filter():
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]
    odd = list(filter(lambda x: x%2 !=0,my_list))
    print(odd)

"""Recorre cada uno de los lugares del arreglo, los eleva al cuadrado y los ubica en una nueva lista 
llamada squares"""
def use_map():
    my_list = [1, 2, 3, 4, 5]
    squares = list(map(lambda x:x**2,my_list))
    print(squares)

"""La funcion reduce lo que hace es la operacion que yo quiera, con una lista, es decir tengo una lista n
y quiero hacer una operacion con cada uno de los items de la lista y convertir en un valor unico, 
entonces utilizo reduce para convertir una operacion en una solita"""
def use_reduce():
    my_list = [2, 2, 2, 2, 2]
    
    print("Solución normal")
    all_multiplied=1

    for i in my_list:
        all_multiplied = all_multiplied*i

    print(all_multiplied)

    print("Solución Reduce()")
    mult = reduce(lambda a , b : a * b, my_list)
    print(mult)
    

saludo(hola)
print("")
saludo(use_list)
print("")
saludo(use_filter)
print("")
saludo(adios)
print("")
saludo(use_map)
print("")
saludo(use_reduce)
