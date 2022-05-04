import random
import os


def limpiar_pantalla():
    os.system("cls")

def read():
    words = []
    with open ("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
    palabra_aleatoria = random.choice(words)
    return palabra_aleatoria

def palabra_guiones(palabra_aleatoria):
    letras = []
    for i in palabra_aleatoria:
        letras.append(i)
    longitud = len(palabra_aleatoria)
    palabra_guion = []
    for i in range (longitud):
        palabra_guion.append("_")
    juego_terminado = False
    intentos = 10
    
    while(juego_terminado == False):
        letra = input("digite una letra: ")
        adivine_alguna = False
    
        for i in range (longitud):
            if (letras[i] == letra):
                palabra_guion[i] = letra
                adivine_alguna = True
                if(palabra_guion == letras):
                    print("Felicitaciones ganaste")
                    juego_terminado = True
        print(palabra_guion)

        if adivine_alguna == False:
            print("no adivinaste ninguna letra")
            intentos = intentos - 1 
            print("Te quedan " + str(intentos) + " intentos")
            limpiar_pantalla()
            if intentos == 0:
                print("Lo siento no lograste adivinar la letra ':(' ")
                juego_terminado = True

        

def run():
    limpiar_pantalla()
    palabra_guiones(read())


if __name__ == "__main__":
    run()