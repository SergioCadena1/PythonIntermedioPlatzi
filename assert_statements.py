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
    num = (input("Digite el numero a revisar : "))
    assert num.isnumeric() and int(num)>0,"Recuerda que solo se aceptan numeros y deben ser positivos"
    divisor(int(num))

    print("Termino el programa")

if __name__ == "__main__":
    run()
# assert len(string) >0, "No se puede ingresar cadena vacia"