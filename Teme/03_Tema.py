
# Creati un program care are ca scop un meniu. Meniul se va selecta prin introducerea de la tastaura a unui numar intre 1 si 5 captat intr-o variabila. Printati in terminal acest mesaj:
# """1 – Afisare lista de cumparaturi
# 2 – Adaugare element
# 3 – Stergere element
# 4 – Sterere lista de cumparaturi
# 5 - Cautare in lista de cumparaturi “””
# Apoi folosindu-va de o constructie if-elif-else afisati: - daca utilizatorul scrie de la
# tastaura 1 afisati “Afisare lista de cumparaturi” - daca utilizatorul scrie de la tastaura 2
# afisati “Adugare element” - daca utilizatorul scrie de la tastaura 3 afisati “Stergere
# element” - daca utilizatorul scrie de la tastaura 4 afisati “Sterere lista de cumparaturit”
# - daca utilizatorul scrie de la tastaura 5 afisati “Adaugare element” - daca utilizatorul
# scrie altceva de la tastaura afisati “Alegerea nu exista. Reincercati”
# Implementati logica pentru toate aceste operatii, optional folosind functii.

lista_cumparaturi = []

var1 = "1 - Afisare lista de cumparaturi"
print(var1)
var2 = "2 – Adaugare element"
print(var2)
var3 = "3 – Stergere element"
print(var3)
var4 = "4 – Stergere lista de cumparaturi"
print(var4)
var5 = "5 - Cautare in lista de cumparaturi"
print(var5)

optiune_meniu = int(input("Alege o optiune din meniu: "))


var1 = "1 - Afisare lista de cumparaturi"
print(var1)
var2 = "2 – Adaugare element"
print(var2)
var3 = "3 – Stergere element"
print(var3)
var4 = "4 – Stergere lista de cumparaturi"
print(var4)
var5 = "5 - Cautare in lista de cumparaturi"
print(var5)

if optiune_meniu == 1:
    print(lista_cumparaturi)
elif optiune_meniu == 2:
    produs = input("Adaugare produs")
    lista_cumparaturi.append(produs)
    print(lista_cumparaturi)
elif optiune_meniu == 3:
    produs = input("Sterge produs:")
    lista_cumparaturi.remove(produs)
    print(lista_cumparaturi)
elif optiune_meniu == 4:
    input("Lista de cumparaturi stearsa")
elif optiune_meniu == 5:
    input("Ce produs cauti?")
else:
    input("Alegerea nu exista. Reincercati")


print(lista_cumparaturi)


