from multiprocessing.sharedctypes import Value
from optparse import Values

def run():
    
    """El siguiente codigo muestra, como se deben imprimir los primeros 100 numeros que no son divisibles 
    entre 3 y este numero se eleva al cuadrado y se guardan en una lista, """
    # squares = []
    # for i in range(1,101):
    #     if (i % 3 != 0):
    #         squares.append(i**2)
    #     else:
    #         pass    
    
    
    # print(squares)
    
    # number_of_elements = len(squares)
    # print(number_of_elements)


    """ List Comprenhensions"""
    
    squares = [i**2 for i in range(1,101) if i % 3 != 0]
    impar = [i for i in range (1,11) if i % 2 != 0]
    suma = sum(impar)

    print(f"la suma es {suma}")
    print(impar)
    

    print(squares)

    """Reto de la clase"""

    common_multiples=[i for i in range(0,100000) if i % 4 == 0 and i % 6 ==0  and i % 9==0 and i% 7==0]
    print(common_multiples)

if __name__ == "__main__":
    run()