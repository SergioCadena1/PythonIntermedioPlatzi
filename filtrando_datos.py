DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    all_python_devs = [i["name"] for i in DATA if i["language"] == "python"]
    print(all_python_devs)

    all_platzi_workers = [i["name"] for i in DATA if i["organization"] == "Platzi"]
    print(all_platzi_workers)

    all_adults = [i["name"] for i in DATA if i["age"] >= 18]
    print(all_adults)
    
    all_teens = [i["name"] for i in DATA if i["age"] < 18]
    print(all_teens)
   
    for i in all_platzi_workers:
        print(i)

    print("")

    for i in all_python_devs:
        print(i)


    """FILTER"""

    print("Adultos con filter")
    all_adults_filter = list(filter(lambda x : x["age"] >= 18, DATA))
    # print(all_adults_filter)
    
    """Combinando las High Order Functions"""

    all_adults_name_combined = list(map(lambda x: x["name"],all_adults_filter))
    print(all_adults_name_combined)
    print("")
    for i in all_adults_name_combined:
        print(i)


    old_people = list(map(lambda x: x | {"old": x["age"] >= 70} , DATA))


    for i in old_people:
        print(i)



if __name__ == "__main__":
    run()