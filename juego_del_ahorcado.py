import random


def read():
    words = []
    with open ("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
    palabra_aleatoria = random.choice(words)
    print(palabra_aleatoria)    
    return palabra_aleatoria

def cambio_de_palabra(palabra_aleatoria):
    print(palabra_aleatoria)
    letras = []
    for i in palabra_aleatoria:
        letras.append(i)
    print(letras)
    for i in letras:
        letra_user = input("Escriba una letra")
        if letra_user == i:
            print("si existe")



def run():
    cambio_de_palabra(read())

if __name__ == "__main__":
    run()