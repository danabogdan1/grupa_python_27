print("hello world!")
print("This is a change")
print("Another change here")

var1 = True



# if statements:

# calculator: 9 + 8 -> 1
# decizii / alegeri

populatie_brasov = 300000
nou_nascuti_curent = 35000

populatie_brasov = populatie_brasov + nou_nascuti_curent

if populatie_brasov > 310000:
    print("populatia brasovului a crescut considerabil.")
    print("felicitari")
    if populatie_brasov> 330000:
        print("populatia a crescut cu mai mult de 10%.")
else:
    print("nu se nasc destui copii sa mentinem societatea curenta.")


lista2 = [0, 6, 7, 10, 90, 100, 33, 88, 5, 13]

#vrem sa printam toate numerele pare

# a + b
# a / b, a // b -> rezultatul impartirii

nr_pare = []
nr_impare = []
for nr in lista2:
    if nr % 2 == 0:
        nr_pare.append(nr)
    else:
        nr_impare.append(nr)

print("Nr pare:")
print(nr_pare)

print("Nr impare:")
print(nr_impare)

# Expresii logice

for nr in lista2:
    if nr % 2 == 0 and nr % 5 == 0:
        print("Nr urmator este par si mutiplu de 5")
        print(nr)


