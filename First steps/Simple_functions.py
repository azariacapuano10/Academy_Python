def chatroom_status(lista):
    """Print the number of users online in a chatroom"""

    if len(lista) == 1:
        print(lista[0],'online')
    elif len(lista) == 2:
        print(lista[0],'and', lista[1],'online')
    elif len(lista) == 0:
        print('no one online')
    elif len(lista) > 2:
        print(lista[0],',', lista[1],'and',len(lista)-2,'online')

    

def missing_num(lista):
    """Takes a list of numbers between 1 and 10(excluding one number) and returns the missing number"""

    controllo = [1,2,3,4,5,6,7,8,9,10]
    for i in range(0,10):
        if controllo[i] not in lista:
            return controllo[i]

def add_indexes(lista):
    """Given a list of numbers, create a function which returns the list but with each element's index in the list addedd to itself"""

    for i in range(0,len(lista)):
        lista[i] = lista[i] + i
    return lista

def index_of_caps(stringa):
"""Create a function that takes a single string as argument and returns an oredered list containinf indices of all capital letters in the string"""

    lista = list()
    for i in range(len(stringa)):
        if stringa[i].isupper():
            lista.append(i)
            lista.sort()
    return lista

def name_shuffle(stringa):
"""Create a function that takes a string (will be a person's first and last name) and returns a string with the first and last name swapped"""

    temp = stringa.split()
    return temp[1] + ' ' +temp[0]
    
def numbers_sum(lista):
    """Returns the sum of all the integer elements in the list"""

    somma = 0
    for i in range(0,len(lista)):
        if type(lista[i]) == int:
            somma += lista[i]
    return somma

def get_indices(lista,index):
    """Returns the indices of all occurrences of an item in the list"""

    lista_index=list()
    for i in range(0,len(lista)):
        if lista[i] == index:
            lista_index.append(i)
    return lista_index

def number_length(num):
    """Takes a number num and returns its length"""

    somma=0
    for n in str(num):
        if n.isdigit():
            somma+=1
    return somma

def combinations(*args):
    """Takes a variable number of arguments, each argument representing the number of itmes in a group, and returns the number of permutations of items that you could get by taking one item from each group"""

    lista = list()
    comb = 1
    for x in range(0, len(args)):
        num = args[x]
        lista.append(num)
    for y in range(0,len(lista)):
        comb *= lista[y]
    return comb
