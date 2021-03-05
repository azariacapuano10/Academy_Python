controllo = list() #creazione controllo
for i in range(1,10):
    controllo.append(i)

matrice_sudoku = [] #creazione matrice
for r in range(9):
    lista = list()
    matrice_sudoku.append(lista)
    for c in range(9):
        num = int()
        lista.append(num)

for i in range(9): #print matrice
    print(matrice_sudoku[i])