
print("hello world")
print("This is a change")
print("Another change here")

var1 = True


# if statements:

#calculator: 9+8 -> 17
#decizii / alegeri


populatie_brasov = 300000
nou_nascuti_brasov = 35000

populatie_brasov = populatie_brasov + nou_nascuti_brasov

if populatie_brasov > 310000:
    print("Populatia Brasovului a crescut considerabil.")
    print("Felicitari!")
    if populatie_brasov > 335000:
        print("Populatia Brasovului a crescut cu peste 10%.")
else:
    print("Nu se nasc destui copii.")


lista2 = [6, 7, 10, 90, 100, 33, 88, 5, 13, 0]

nr_pare = []
nr_impare = []

# vrem sa printam toate numerele pare

for nr in lista2:
    if  nr % 2 ==0 and nr % 5 == 0:
        print(nr)
        nr_pare.append(nr)
    else:
        nr_impare.append(nr)

print("Numerele pare sunt:")
print(nr_pare)
print("Numerele impare sunt:")
print(nr_impare)
