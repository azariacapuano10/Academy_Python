controllo = list() #creazione controllo
for i in range(1,10):
    controllo.append(i)

matrice_sudoku = [] #creazione matrice
for r in range(9):
    lista = list()
    matrice_sudoku.append(lista)
    for c in range(9):
        num = ' '
        lista.append(num)

for i in range(9): #print matrice
    print(matrice_sudoku[i])

def inserisci_numero():
    while controllo_vittoria():
        selezione_riga = int(input('Quale riga scegli:\n'))
        selezione_colonna = int(input('Quale colonna scegli:\n'))
        if matrice_sudoku[selezione_riga][selezione_colonna]== ' ':
            numero_da_inserire = int(input('Che numero vuoi inserire?\n'))
            matrice_sudoku[selezione_riga][selezione_colonna] = numero_da_inserire
            for i in range(9):
                print(matrice_sudoku[i])
        else:
            print("E' occupato, effettua un'altra scelta")
            selezione_riga = int(input('Quale riga scegli:\n'))
            selezione_colonna = int(input('Quale colonna scegli:\n'))
            if matrice_sudoku[selezione_riga,selezione_colonna]== ' ':
                numero_da_inserire = int(input('Che numero vuoi inserire?\n'))
                matrice_sudoku[selezione_riga][selezione_colonna]= numero_da_inserire
                for i in range(9):
                    print(matrice_sudoku[i])

def controllo_vittoria():
    cont_quadranti = 0
    cont_righe = 0
    cont_colonne = 0
    lista_controllo_colonne = list() #controllo colonne
    for r in range(9):
        lista = list()
        lista_controllo_colonne.append(lista)

    for c in range(9): 
        lista_controllo_colonne[c]
        for i,j in zip(range(9), range(9)): 
            lista_controllo_colonne[c].append(matrice_sudoku[i][j])

    
    if set(lista_controllo_colonne[0]) == set(controllo):
        cont_colonne += 1
    elif set(lista_controllo_colonne[1]) == set(controllo):
        cont_colonne += 1
    elif set(lista_controllo_colonne[2]) == set(controllo):
        cont_colonne += 1
    elif set(lista_controllo_colonne[3]) == set(controllo):
        cont_colonne += 1
    elif set(lista_controllo_colonne[4]) == set(controllo):
        cont_colonne += 1
    elif set(lista_controllo_colonne[5]) == set(controllo):
        cont_colonne += 1
    elif set(lista_controllo_colonne[6]) == set(controllo):
        cont_colonne += 1
    elif set(lista_controllo_colonne[7]) == set(controllo):
        cont_colonne += 1
    elif set(lista_controllo_colonne[8]) == set(controllo):
        cont_colonne += 1


    lista_controllo_righe = list() #controllo righe
    for r in range(9):
        lista = list()
        lista_controllo_righe.append(lista)
    
    for r in range(9): 
        lista_controllo_righe[r] = matrice_sudoku[r]

    if set(lista_controllo_righe[0]) == set(controllo):
        cont_righe += 1
    elif set(lista_controllo_righe[1]) == set(controllo):
        cont_righe += 1
    elif set(lista_controllo_righe[2]) == set(controllo):
        cont_righe += 1
    elif set(lista_controllo_righe[3]) == set(controllo):
        cont_righe += 1
    elif set(lista_controllo_righe[4]) == set(controllo):
        cont_righe += 1
    elif set(lista_controllo_righe[5]) == set(controllo):
        cont_righe += 1
    elif set(lista_controllo_righe[6]) == set(controllo):
        cont_righe += 1
    elif set(lista_controllo_righe[7]) == set(controllo):
        cont_righe += 1
    elif set(lista_controllo_righe[8]) == set(controllo):
        cont_righe += 1


    lista_controllo_quadrato1 = list() #controllo quadranti
    for i in range(3):
        for j in range(3):
            lista_controllo_quadrato1.append(matrice_sudoku[i][j])

    lista_controllo_quadrato2 = list()
    for i in range(3):
        for j in range(3,6):
            lista_controllo_quadrato2.append(matrice_sudoku[i][j])

    lista_controllo_quadrato3 = list()
    for i in range(3):
        for j in range(6,9):
            lista_controllo_quadrato3.append(matrice_sudoku[i][j])

    lista_controllo_quadrato4 = list()
    for i in range(3,6):
        for j in range(3):
            lista_controllo_quadrato4.append(matrice_sudoku[i][j])

    lista_controllo_quadrato5 = list()
    for i in range(3,6):
        for j in range(3,6):
            lista_controllo_quadrato5.append(matrice_sudoku[i][j])

    lista_controllo_quadrato6 = list()
    for i in range(3,6):
        for j in range(6,9):
            lista_controllo_quadrato6.append(matrice_sudoku[i][j])

    lista_controllo_quadrato7 = list()
    for i in range(6,9):
        for j in range(3):
            lista_controllo_quadrato7.append(matrice_sudoku[i][j])

    lista_controllo_quadrato8 = list()
    for i in range(6,9):
        for j in range(3,6):
            lista_controllo_quadrato8.append(matrice_sudoku[i][j])

    lista_controllo_quadrato9 = list()
    for i in range(6,9):
        for j in range(6,9):
            lista_controllo_quadrato9.append(matrice_sudoku[i][j])

    
    if set(lista_controllo_quadrato1) == set(controllo):
        cont_quadranti += 1
    elif set(lista_controllo_quadrato2) == set(controllo):
        cont_quadranti += 1
    elif set(lista_controllo_quadrato3) == set(controllo):
        cont_quadranti += 1
    elif set(lista_controllo_quadrato4) == set(controllo):
        cont_quadranti += 1
    elif set(lista_controllo_quadrato5) == set(controllo):
        cont_quadranti += 1
    elif set(lista_controllo_quadrato6) == set(controllo):
        cont_quadranti += 1
    elif set(lista_controllo_quadrato7) == set(controllo):
        cont_quadranti += 1
    elif set(lista_controllo_quadrato8) == set(controllo):
        cont_quadranti += 1
    elif set(lista_controllo_quadrato9) == set(controllo):
        cont_quadranti += 1


    if cont_colonne == cont_quadranti == cont_righe == 9:
        print('Hai vinto!')
        return False
    else:
        return True