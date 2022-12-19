#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
#Позиции хранятся в отдельном списке( пример n=4, lst1=[4,-2,1,3] - списко на основе n, а позиции элементов lst2=[3,1].


import random
 
rand_list=[]
n =int(input("Введите число N "))
for i in range(n):
    rand_list.append(random.randint(-n -1,n))
print(rand_list)
a =int(input("Укажите позицию 1 элемента <= N "))
b =int(input("Укажите позицию 2 элемента <= N "))
if a <=n and b <=n:
    print(rand_list[a -1] *rand_list[b -1])
else:
    print("Введены неверные позиции")