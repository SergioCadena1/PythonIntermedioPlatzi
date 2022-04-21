def no_aceptable(num):
    try:
        if num < 0:
            raise ValueError("Solo puedes escribir numeros positivos") #solo con numeros negativos
        else:
            return False
    except ValueError as ve:
        print(ve)
    return False

def continuar(num):
    for i in range(1,11):
        print(str(i) + "|" + " x " + "|" + " = " + str(i*num))
        return True

def run():
    try:
        num = int(input("Escribe un numero: "))
        another = no_aceptable(num)
        other = continuar(num)
        #usando la funcion de no aceptable
        if another == False:
            return False
        #usando la funcion continuar
        elif other == True:
            return True
    except ValueError:
        print("Solo puedes escribir numeros") #exception con letras o caracteres de strings
# calc = continuar(num)
# if calc:
# return True
# else:
# return False
if __name__ == "__main__":
    run()