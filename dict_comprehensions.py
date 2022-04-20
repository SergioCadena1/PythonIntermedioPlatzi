def run():
    """Este codigo pone los numeros de 1 al 100 como Keys y 
    los numeros de 1 al 100 elevados al cubo como values"""
    # my_dict={}

    # for key in range (1,101):
    #     if (key % 3 != 0):
    #         my_dict[key] = key**3
    # print(my_dict)

    # my_dict={key:key**3 for key in range (1,101) if (key % 3 != 0)}
    # print(my_dict)    

    

    my_dict_test={key:round(key**(1/2),2) for key in range(1,1001)}
    print(my_dict_test)

if __name__ == "__main__":
    run()

    