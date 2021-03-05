import random
import copy

# Creazione matrice vuota
matrice_sudoku = [] 
for r in range(9):
    lista = list()
    matrice_sudoku.append(lista)
    for c in range(9):
        num = ' '
        lista.append(num)

# Creazione suduku random partendo da base
matrice_sudoku=[[1,2,3,4,5,6,7,8,9],[4,5,6,7,8,9,1,2,3],[7,8,9,1,2,3,4,5,6],[2,3,1,6,4,5,8,9,7],[5,6,4,9,7,8,2,3,1],[8,9,7,3,1,2,5,6,4],[3,1,2,5,6,4,9,7,8],[6,4,5,8,9,7,3,1,2],[9,7,8,2,3,1,6,4,5]]

for i in range(40):
    num1=random.randint(1,9)
    num2=random.randint(1,9)

    for i in range(0,9):
        for e in range(0,9):
            if matrice_sudoku[i][e]==num1:
                matrice_sudoku[i][e]=num2
            elif matrice_sudoku[i][e]==num2:
                matrice_sudoku[i][e]=num1

# Creazione caselle vuote per giocare 
sudokuCopy = copy.deepcopy(matrice_sudoku)

cont=0
while cont<3:
    for i in range(0,9):
        for e in range(0,9):
            tolgo=random.randint(0,1)
            if tolgo==0 and cont<3 and matrice_sudoku[i][e]!=" ":
                matrice_sudoku[i][e]=" "
                cont+=1

# Creazione lista per controllo
controllo = list() 
for i in range(1,10):
    controllo.append(i)

def inserisci_numero():
    '''Game flow'''
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
    '''Check if the conditions for victory are met'''
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