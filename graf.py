# macierz sasiedztwa
tab = [[0, 1, 0, 0, 0],
       [1, 0, 1, 1, 1],
       [0, 1, 0, 1, 0],
       [0, 1, 1, 0, 1],
       [0, 1, 0, 1, 0]]

size = tab.__len__()
k = 0

# wyswietlenie tablicy
for x in range(0, size):
    print(tab[x])

# przejscie po kazdym elemencie
for x in range(0, size):
    for y in range(x + 1, size):
        if tab[x][y] == 1:
            k += 1

print "wierzcholki: ",  size
print "krawedzie: ", k