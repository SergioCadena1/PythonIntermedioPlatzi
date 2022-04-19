from ast import For
from multiprocessing.sharedctypes import Value


def run():
    my_List = [1, 'hello', True, 4.5]
    my_dict = {"firstname":"Sergio",
               "lastname":"Cadena"
               }
    super_list = [
        {"firstname":"Sergio","lastname":"Cadena"},
        {"firstname":"Laura","lastname":"Santacruz"},
        {"firstname":"Vaneso","lastname":"Cadena"},
        {"firstname":"Nicolle","lastname":"Ortega"},
        {"firstname":"Alexander","lastname":"Otalora"},        
        {"firstname":"Milton","lastname":"heladas"},

    ]
    super_dict = {
        "natural_nums":[1, 2, 3, 4, 5],
        "integer_nums":[-1, -2, 0, 1, 2],
        "floating_nums":[-1.56, -2.54, 0.87, 1.21, 2.35],
        "animals":["Elefant","Jirafa","Dogs", "Cats", "Parots"],
    }

    print("Diccionario\n")
    for key, Value in super_dict.items():
        print("para la llave: " + str(key) + " los valores son : " + str(Value))

    # forma simple de imprimir una lista
    for l in super_list:
         print(l)

    print("\nLista\n")
    
    # forma mas presentable 
    for l in super_list:
        print(l["firstname"], l["lastname"])


if __name__ == '__main__':
    run()