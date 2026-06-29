
# Se cere realizarea unui to-do list utilizând noțiunile învățate până în acest moment.
# În prima faza se adaugă categoriile dorite de la tastatură:
# exemplu: Introduceți categoriile de taskuri:
# posibile răspunsuri: curs, cumpărături, muncă, cadouri, etc

import json

def introducere_categorii_taskuri():
    categorii_taskuri = []

    print("Introducere categorii taskuri:")

    continua = True

    while continua:

        elem = input("Categorie: ")

        if elem in categorii_taskuri:
            print("Categoria exista deja!")
        else:
            categorii_taskuri.append(elem)

        raspuns = input("Mai adaugi? (da/nu): ")

        if raspuns.lower() == "nu":
            continua = False

    return categorii_taskuri


def save_categorii_taskuri(categorii_taskuri):
    with open("categorii_taskuri.json", "w") as f:
        json.dump(categorii_taskuri, f, indent=4)

categorii = introducere_categorii_taskuri()
save_categorii_taskuri(categorii)


# Cerințe:
# -       se va cere, pe rand, introducerea unui task de la tastatura: ex: rezolvare tema
# -       se va cere introducerea unei date limite de realizare a taskului respectiv, ex:  22.01.2022 21:30
# -       se va adăuga o persoana responsabilă cu realizarea taskului respectiv: ex: Ion Vasile
# -       se va adăuga o categorie din care taskul face parte. Ex. curs
# Atenție, categoria trebuie să existe. În cazul în care nu există, se afișează mesaj de eroare.
#
# Va exista posibilitatea de adăugare a unui număr nelimitat de taskuri, chiar si după ce utilizatorul confirmă faptul că a terminat de introdus taskurile.
# Datele se salveaza in fisiere. Vor exista doua fisiere: unul pentru categorii si unul care sa contina: taskurile, data limita, persoana responsabila, categorie

class Task:

    def __init__(self, nume, data, persoana, categorie):
        self.nume = nume
        self.data = data
        self.persoana = persoana
        self.categorie = categorie

    @staticmethod
    def save_task(taskuri):
        with open("taskuri.json", "w") as f:
            json.dump([
                {
                    "nume": task.nume,
                    "data": task.data,
                    "persoana": task.persoana,
                    "categorie": task.categorie
                }
                for task in taskuri
            ], f, indent=4)

def introducere_taskuri(categorii_taskuri):

    taskuri = []

    print("Introducere taskuri:")

    continua = True

    while continua:
        nume = input("Task: ").strip()

        if nume.lower() == "stop":
            continua = False
            continue

        exista = False
        for task in taskuri:
            if task.nume == nume:
                exista = True

        if exista:
            print("Task exista deja!")
            continue

        data = input("Data: ")
        persoana = input("Persoana: ")
        categorie = input("Categorie: ")

        if categorie not in categorii_taskuri:
            print("Categoria NU exista!")
            continue

        task_nou = Task(nume, data, persoana, categorie)
        taskuri.append(task_nou)

        raspuns = input("Mai adaugi task? (da/nu): ")

        if raspuns == "nu":
            continua = False
            continue

    return taskuri

taskuri = introducere_taskuri(categorii)

Task.save_task(taskuri)





# Cerințe suplimentare:
# Se afișează un meniu din care utilizatorul poate alege să realizeze următoarele operații:
# Listare date: în afișarea inițială a datelor se realizează o sortare în funcție de categorie.
# Sortare: se alege o opțiune din cele 8 de mai jos:
# Criteriile disponibile sunt:
# 1. sortare ascendentă task
# 2. sortare descendentă task
# 3. sortare ascendentă data
# 4. sortare descendentă data
# 5. sortare ascendentă persoana responsabilă
# 6. sortare descendentă persoană responsabilă
# 7. sortare ascendentă categorie
# 8. sortare descendentă categorie
#
# 3.Filtrare date: filtrarea datelor reprezintă de fapt o listare a datelor în funcție de anumite detalii date de la tastatură. criteriile de filtrare sunt:
# -    se cere de la tastatură câmpul după care se realizeaza filtrarea:
# 1.     Task
# 2.     Dată
# 3.     Persoană responsabilă
# 4.     Categorie
# -       după alegerea campului de la tastatură se cere introducerea unui string utilizat pentru filtrarea în lista inițială de date, astfel încât din lista inițială să rămână doar datele care conțin / încep cu valoarea introdusă
# -       se afișează lista rămasă
#
# 4.Adăugarea unui nou task în lista inițială
#
# 5.Editarea detaliilor referitoare la task, dată, persoană sau categorie dintr-un anumit task ales de utilizator de la tastatură (când se cere această opțiune, se va lista lista de taskuri cu un identificator unic pe rand, astfel încât să se știe ce informație urmează să editeze utilizatorul)
#
# 6.Ștergerea unui task din lista inițială.
#
# Atenție! Trebuie să aveți grijă că o categorie poate să existe o singură dată (nu se accepta dubluri, ex curs, cumpărături, muncă, cadouri, curs este greșit)
#
# De asemenea, la adăugarea taskurilor se va avea grijă și la compararea textelor taskurilor, dacă textul respectiv există, nu se poate adăuga.


