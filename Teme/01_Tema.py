#Creati o variabila care contine o lista de siruri de caractere:
#"ERR-Value Error-ER:10"
#"INF-Program launch Info-CD:5"
#"WRN-Low memory-WR:11"

#Si alta variabila, cu alte siruri de caractere:
#"INF-Program exit-CD:14"
#"WRN-Low disk space-WR:99"
#"WRN-Bandwith reached-WR:87"

#Treceti prin toate sirurile de caractere, extrageti valorile de la ERR, INF, WRN, si creati urmatorul text formatat, din sirurile de caracter date, de exemplu:

#Rezultatul ar trebui sa arate astfel:
#[ERROR]
#Mesaj: Value Error
#Cod: 10

#[INFO]
#Mesaj: Program launch Info
#Cod: 5

#[WARNING]
#Mesaj: Low memory
#Cod: 11

#Faceti asta pentru amandoua variabile, care contin acele siruri de caracter.

var1 = ["ERR-Value Error-ER:10", "INF-Program launch Info-CD:5", "WRN-Low memory-WR:11"]
var2 = ["INF-Program exit-CD:14", "WRN-Low disk space-WR:99", "WRN-Bandwith reached-WR:87"]

# Solutia 1

for s in var1 + var2:
    if s.split("-")[0] == 'ERR':
        print("[ERROR]")
    else:
        if s.split("-")[0] == "INF":
            print("[INFO]")
        else:
            print("[WARNING]")
    print("Mesaj:", s.split("-")[1])
    print("Cod:", s.split("-")[2].split(":")[1])
    print()


# Solutia 2

for s in var1 + var2:
    print(s.split("-")[0].replace("ERR", "[ERROR]").replace("INF", "[INFO]").replace("WRN", "[WARNING]"))
    print("Mesaj:", s.split("-")[1])
    print("Cod:", s.split("-")[2].split(":")[1])
    print()