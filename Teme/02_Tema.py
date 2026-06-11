# Scrieti un program care primeste o lista de dictionare de persoane, si returneaza intr-o alta lista, doar persoanele care au varsta mai mare de 25 de ani, si care au greutatea peste 60 kg.
# # Lista sa aiba cel putin 5 persoane. Logica acestui filtru sa o puneti intr-o functie, sa poata fi refolosita.
#
# Exemplu lista persoane:
# cetateni = [
#     19304843895738: {
#         "Nume": "Marius Moga",
#         "Varsta": 32,
#         "Adresa": "Brasov, Jud Brasov",
#         "Greutate": 75,
#     },
#     193048438345345: {
#         "Nume": "Matei Luca",
#         "Varsta": 30,
#         "Greutate": 59,
#     }
# ]

cetateni = [
    {
        "CNP": 1930484389573,
        "Nume": "Marius Moga",
        "Varsta": 32,
        "Adresa": "Brasov, Jud Brasov",
        "Greutate": 75,
    },
    {
        "CNP": 1920484383453,
        "Nume": "Matei Luca",
        "Varsta": 30,
        "Greutate": 59,
    },
    {
        "CNP": 2790716060799,
        "Nume": "Daniela Rusu",
        "Varsta": 20,
        "Greutate": 61,
    },
    {
        "CNP": 2790716060791,
        "Nume": "Marius Rus",
        "Varsta": 53,
        "Greutate": 62,
    },
    {
        "CNP": 2901555555555,
        "Nume": "Ioana Pop",
        "Varsta": 40,
        "Greutate": 59,
    }
]

def filtreaza_cetateni(lista_cetateni):
    res = []
    for persoana in lista_cetateni:
        if persoana["Varsta"] > 25 and persoana["Greutate"] > 60:
            res.append(persoana)
    return res

lista_cetateni_filtrata = filtreaza_cetateni(cetateni)
print(lista_cetateni_filtrata)













