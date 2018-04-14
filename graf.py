# # macierz sasiedztwa
# tab = [[0, 1, 0, 0, 0],
#        [1, 0, 1, 1, 1],
#        [0, 1, 0, 1, 0],
#        [0, 1, 1, 0, 1],
#        [0, 1, 0, 1, 0]]

size = int(raw_input("rozmiar tablicy: "))
tab = [[None] * size for i in range(size)]

st = []
k = 0
i = 0

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

# przejscie po tablicy
for x in range(0, size):
    st.append(i)
    i = 0
    for y in range(0, size):
        if tab[x][y] == 1:
            k += 1
            i += 1
st.append(i)

# wyswietlenie wartosci
print "wierzcholki: ",  size
print "krawedzie: ", k
for x in range(1, st.__len__()):
    print "stopien wierzcholka [", x, "] =", st[x]
st.sort()
print "stopien grafu: ", st[st.__len__() - 1]