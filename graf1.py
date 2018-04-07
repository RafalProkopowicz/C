# macierz sasiedztwa
tab = [[0, 1, 0, 0, 0],
       [1, 0, 1, 1, 1],
       [0, 1, 0, 1, 0],
       [0, 1, 1, 0, 1],
       [0, 1, 0, 1, 0]]

st = []
size = tab.__len__()
k = 0
i = 0

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