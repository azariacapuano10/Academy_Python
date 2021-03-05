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

def inserisci_numero():
    
        selezione_riga = int(input('Quale riga scegli:\n'))
        selezione_colonna = int(input('Quale colonna scegli:\n'))
        if matrice_sudoku[selezione_riga][selezione_colonna]==0:
            numero_da_inserire = int(input('Che numero vuoi inserire?\n'))
            matrice_sudoku[selezione_riga][selezione_colonna] = numero_da_inserire
            for i in range(9):
                print(matrice_sudoku[i])
        else:
            print("E' occupato, effettua un'altra scelta")
            selezione_riga = int(input('Quale riga scegli:\n'))
            selezione_colonna = int(input('Quale colonna scegli:\n'))
            if matrice_sudoku[selezione_riga,selezione_colonna]== 0:
                numero_da_inserire = int(input('Che numero vuoi inserire?\n'))
                matrice_sudoku[selezione_riga][selezione_colonna]= numero_da_inserire
                for i in range(9):
                    print(matrice_sudoku[i])