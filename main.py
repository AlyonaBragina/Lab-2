# Задание 1
import csv
list = []
k=0
with open('books-en.csv', encoding = 'latin-1') as f:
    data = csv.DictReader(f, delimiter=';')
    for row in data:
        list.append(row['Book-Title'])
for i in list:
    if len(i)>30:
        k+=1
print(k)
a = input('Введите фамилию: ')
with open('books-en.csv', encoding = 'latin-1') as f:
    data = csv.DictReader(f, delimiter=';')
    for row in data:
        if row['Book-Author']==a and int(row['Year-Of-Publication'])<2016:
            print(row['Book-Title'])

list_author=[]
list_title=[]
list_year=[]
list1=[]
with open('books-en.csv', encoding = 'latin-1') as f:
    data = csv.DictReader(f, delimiter=';')
    for row in data:
        list_author.append(row['Book-Author'])
        list_title.append(row['Book-Title'])
        list_year.append(row['Year-Of-Publication'])
for i in range(20):
    list1.extend([str(i+1),') ', '<',list_author[i],'>.' ,'<',list_title[i],'>-', '<',list_year[i],'>', '\n'])

file = open('result.txt', 'w')
file.writelines(list1)
file.close()
