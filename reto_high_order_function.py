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

    print("All_python_devs")
    all_python_devs = list(filter(lambda x: x["language"] == "python",DATA))
    all_python_devs = list(map(lambda x : x["name"],all_python_devs))

    for i in all_python_devs:
        print(i)

    print("\nAll_Platzi_workers")
    all_platzi_workers = list(filter(lambda x : x["organization"] == "Platzi",DATA))
    all_platzi_workers = list(map(lambda x : x["name"],all_platzi_workers))

    for i in all_platzi_workers:
        print(i)

    print("\nAll_Adults")
    all_adults = [i["name"] for i in DATA if i["age"] >= 18]
    for i in all_adults:
        print(i)
    
    print("\nOld_people")
    # old_people = list(map(lambda x: x | {"old": x["age"] >= 70} , DATA))
    old_people = [i | {"old": i["age"] >= 70} for i in DATA ]
    print(old_people)

if __name__ == "__main__":
    run()


