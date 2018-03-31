
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
    for y in range(0, size):
        if tab[x][y] == 1:
            k += 1

k = k/2
w = size

print("wierzcholki: ", w)
print("krawedzie: ", k)