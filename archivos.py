def read():
    numbers = []
    with open ("./archivos/numbers.txt" ,"r",encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["sergio", "laura", "alexander","nicolle","lori"]
    with open ("./archivos/names.txt" ,"w",encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")
    
def append(name):
    with open ("./archivos/names.txt" ,"a",encoding="utf-8") as f:
        f.write(name)
        f.write("\n")


def run():
    read()
    append("gono")

if __name__ == "__main__":
    run()