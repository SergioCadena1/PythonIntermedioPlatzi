import string


def divisor(num):
    """List comprehensions"""
    list_divisor = [i for i in range (1,num+1) if num % i == 0]
    print(list_divisor)

    """Ciclo"""
    list_divisor1 =[]
    for i in range (1, num+1):
        if num % i == 0:
            list_divisor1.append(i)
    print(list_divisor1)
    return list_divisor1


def run():
    try:     
        num = int(input("Digite el numero a revisar : "))
        if num <0:
            raise Exception("debes ingresar un numero positivo")
        divisor(num)
    except ValueError:
        print("solo se aceptan numeros")
    except Exception as ve:
        print(ve)

    print("Termino el programa")

if __name__ == "__main__":
    run()



# assert len(string) >0, "No se puede ingresar cadena vacia"