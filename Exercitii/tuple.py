tup = ('oranges', 'apples', 'bananas')     #structură de date care stochează o secvență ordonată de valori
print(tup)                                 #nu se pot modifica valorile dintr-un tuplu   #! nu se poate introduce alt termen in tuplu  
#tuplurile sunt scrise cu paranteze rotunde  
# !diferenta dintre tuplu si lista:  lista este mutabilă, în timp ce un tuplu este imuabil
print (tup[0])
print(tup[2:3])

tup2 = 12, 14
tup3 = tup + tup2
print(tup3)

print(len(tup))

del tup3
print(tup3)
