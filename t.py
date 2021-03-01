# def chatroom_status(lista):
#     if len(lista) == 0:
#         return 'No one online'
#     elif len(lista) == 1:
#         return lista[0] + ' online'
#     elif len(lista) == 2:
#         return lista[0] + ' and ' + lista[1] + ' online'
#     elif len(lista)>2:
#         return lista[0] + ', ' + lista[1] + ' and '+ str(len(lista)-2) + ' more online'

# print(chatroom_status([]))
# print(chatroom_status(['tizio']))
# print(chatroom_status(['tizio','caio']))
# print(chatroom_status(['tizio','caio','sempronio']))

# def missing_num(lista):
#     controllo = [1,2,3,4,5,6,7,8,9,10]
#     for i in range(len(controllo)):
#         if controllo[i] not in lista:
#             return controllo[i]

# print(missing_num([2,3,7,8,10,4,5,6,1]))

# def add_indexes(lista):
#     new_list=list()
#     for i in range(len(lista)):
#          new_num = i + lista[i]
#          new_list.append(new_num)
#     return new_list

# print(add_indexes([5,4,0,2,1,0]))

# def index_of_caps(stringa):
#     indexes_list = list()
#     for c in range(len(stringa)):
#         if stringa[c].isupper():
#             indexes_list.append(c)
#     return indexes_list

# print(index_of_caps('aaAaaAaaA'))

# def name_shuffle(stringa):
#     temp = stringa.split()
#     if len(temp) == 2:
#         new_name = temp[1] + ' ' + temp[0]
#         return new_name
#     elif len(temp) == 3:
#         new_name = temp[1] + ' ' + temp[2] + ' ' + temp[0]
#         return new_name
#     else:
#         return 'Ma che cazzo di nome hai?!'

# print(name_shuffle('Franco Rossi'))
# print(name_shuffle('Franco De Rossi'))
# print(name_shuffle('Franco Mario De Rossi'))

# def numbers_sum(lista):
#     somma = 0
#     for i in range(len(lista)):
#         if type(lista[i]) == int:
#             somma += lista[i]
#     return somma

# print(numbers_sum([True,'co',5,False,'ca',5]))

# class Calculator():

#     def __init__(self):
#         self.stato=0

#     def add(self,n1,n2):
#         return n1+n2
    
#     def subtract(self,n1,n2):
#         return n1-n2

#     def multiply(self,n1,n2):
#         return n1*n2

#     def divide(self,n1,n2):
#         return int(n1/n2)

# c = Calculator()

# print(c.add(10,5))
# print(c.subtract(10,5))
# print(c.multiply(10,5))
# print(c.divide(10,5))

# def get_indices(lista,index):
#     new_list = list()
#     for i in range(len(lista)):
#         if lista[i] == index:
#             new_list.append(i)
#     return new_list

# print(get_indices(['a',4,'a',4],5))
# print(get_indices(['a',4,'a',4],4))
# print(get_indices(['a',4,'a',4],'a'))

# def number_length(num):
#     somma=0
#     temp = str(num)
#     for i in range(len(temp)): # più efficiente --> for n in str(num):
#         if temp[i].isdigit():
#             somma +=1
#     return somma

# print(number_length('0909jj'))
# print(number_length(5))
# print(number_length(56))
# print(number_length(567))

# def combinations(*args):
#     prod = 1
#     for i in range(len(args)):
#         if args[i] == 0:
#             continue
#         else:
#             prod *= args[i]
#     return prod

# print(combinations(2,3))
# print(combinations(3,7,4))
# print(combinations(2,3,4,5))
# print(combinations(2,3,0,4,5))
