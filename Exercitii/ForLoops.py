list1 = ["apples", "oranges", "cherries"]       #instructiunea iterativa for se foloseste pentru a parcurge elementele unei secvente (sir, lista sau tuplu)
tup1 = (12, 14, 16)                             
for item in list1:
    print(item)

for item in tup1:
    print(item)

for i in range(0,10):    #generarea unei secvente numerice se realizeaza prin intermediul functiei range()
    print(i)              #nu se printeaza ultimul numar


for i in range(0,11,2):
    print(i)


#sa se scrie primii 10 multiplii ai lui 5
for i in range(0,51,5):
    print(i)

for i in range(0,5):
    for j in range(0,3):
        print(i*j)

n = 100
for i in range(n):
    count = 0
    if  n % i == 0:
        count += 1
    if count == 2:
        print("e nr prim")
    else:
        print("nu e nr prim")

