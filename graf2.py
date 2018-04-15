size = int(raw_input("rozmiar tablicy: "))
tab = [[None] * size for i in range(size)]

# pomocnicza macierz sasiedztwa, jak jej nie bedzie to poprosi o uzupelnienie danych
tab = [[0, 1, 0, 0, 0],
       [1, 0, 0, 1, 0],
       [0, 0, 0, 0, 0],
       [0, 1, 0, 0, 1],
       [0, 0, 0, 1, 0]]

#jak cos puste to uzupelnic
for x in range(0, size):
    for y in range(x, size):
        if x == y:
            tab[x][y] = 0
        elif tab[x][y] == None:
            print(tab[x])
            print "wartosc [", x, "][", y, "]"
            tab[x][y] = int(input())
            tab[y][x] = tab[x][y]

# wyswietlenie tablicy
for x in range(0, size):
    print(tab[x])

# wypisanie wszystkich stopni
stopnie = [0 for i in range(size)]
for x in range(0, size):
    for y in range(0, size):
        if tab[x][y] == 1:
            stopnie[x] = int(stopnie[x] + 1)

# podliczenie parzystych
parzyste = 0
for x in range(0, size):
    if not stopnie[x] % 2:
        parzyste += 1

"""
kod na przeszukanie zachlanne - jak obejelo wszystkie wierzczolki to spojny
"""
# poszukiwanie zachlanne rekurencyjne
def search(wierzcholek):
    if not odwiedzone.__contains__(wierzcholek):
        odwiedzone.append(wierzcholek)
        for x in range(0, size):
            if tab[x][wierzcholek] == 1:
                search(x)

odwiedzone = []

search(0)

if odwiedzone.__len__() != size:
    spojny = False
else:
    spojny = True

"""
eulerowski - spojny, wszystkie wierzcholki parzystego stopnia
"""
if size == parzyste and spojny:
    print ">Eulerowski"


"""
pol-eulerowski - - spojny, wszystkie wierzcholki parzystego stopnia oprocz max 2
0 1 2
"""
if (size == parzyste or size == parzyste + 1 or size == parzyste + 2) and spojny:
    print ">Pol-Eulerowski"


"""
nie spojny - dfs/bfs nei przejdzie po wszystkich wierzcholkach
"""
if spojny == False:
    print ">Nie Spojny"


"""
nie eulerowski i nie pol eulerowski
"""
if parzyste + 2 < size:
    print ">Nie Eulerowski ani Pol-Eulerowski"
