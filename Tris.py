import numpy as np 
global matrice
matrice = np.zeros(shape=(3,3))
print(matrice)

def controlloVittoria():
    """Check if the conditions for victory are met"""

    if matrice[0][0]==matrice[0][1]==matrice[0][2]==1:
        return False
        print('Vittoria!')
    elif matrice[1][0]==matrice[1][1]==matrice[1][2]==1:
        print('Vittoria!')
        return False
    elif matrice[2][0]==matrice[2][1]==matrice[2][2]==1:
        print('Vittoria!')
        return False
    elif matrice[0][0]==matrice[1][0]==matrice[2][0]==1:
        print('Vittoria!')
        return False
    elif matrice[0][1]==matrice[1][1]==matrice[2][1]==1:
        print('Vittoria!')
        return False
    elif matrice[0][2]==matrice[1][2]==matrice[2][2]==1:
        print('Vittoria!')
        return False
    elif matrice[0][0]==matrice[1][1]==matrice[2][2]==1:
        print('Vittoria!')
        return False
    elif matrice[2][0]==matrice[1][1]==matrice[0][2]==1:
        print('Vittoria!')
        return False
    elif matrice[0][0]==matrice[0][1]==matrice[0][2]==2:
        print('Vittoria!')
        return False
    elif matrice[1][0]==matrice[1][1]==matrice[1][2]==2:
        print('Vittoria!')
        return False
    elif matrice[2][0]==matrice[2][1]==matrice[2][2]==2:
        print('Vittoria!')
        return False
    elif matrice[0][0]==matrice[1][0]==matrice[2][0]==2:
        print('Vittoria!')
        return False
    elif matrice[0][1]==matrice[1][1]==matrice[2][1]==2:
        print('Vittoria!')
        return False
    elif matrice[0][2]==matrice[1][2]==matrice[2][2]==2:
        print('Vittoria!')
        return False
    elif matrice[0][0]==matrice[1][1]==matrice[2][2]==2:
        print('Vittoria!')
        return False
    elif matrice[2][0]==matrice[1][1]==matrice[0][2]==2:
        print('Vittoria!')
        return False
    else:
        return True

def mossa():
    """Game flow"""

    while controlloVittoria():
        giocatore = input('Nome giocatore:\n')
        if giocatore == '1':
            selezione_riga = int(input('Quale riga scegli:\n'))
            selezione_colonna = int(input('Quale colonna scegli:\n'))
            if matrice[selezione_riga,selezione_colonna]==0:
                matrice[selezione_riga,selezione_colonna]= 1
                print(matrice)
            else:
                print("E' occupato, effettua un'altra scelta")
                selezione_riga = int(input('Quale riga scegli:\n'))
                selezione_colonna = int(input('Quale colonna scegli:\n'))
                if matrice[selezione_riga,selezione_colonna]== 0:
                    matrice[selezione_riga,selezione_colonna]= 1
                    print(matrice)
        elif giocatore == '2':
            selezione_riga = int(input('Quale riga scegli:\n'))
            selezione_colonna = int(input('Quale colonna scegli:\n'))
            if matrice[selezione_riga,selezione_colonna]==0:
                matrice[selezione_riga,selezione_colonna]= 2
                print(matrice)
            else:
                print("E' occupato, effettua un'altra scelta")
                selezione_riga = int(input('Quale riga scegli:\n'))
                selezione_colonna = int(input('Quale colonna scegli:\n'))
                if matrice[selezione_riga,selezione_colonna]== 0:
                    matrice[selezione_riga,selezione_colonna]= 2
                    print(matrice)
    
mossa()
