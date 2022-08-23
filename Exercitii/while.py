c = 0            #while se utilizeaza pentru a repeta o instructiune atata timp cat conditia este adevarata.
while c < 5:                       # este de forma :   while conditie:
    print(c)                       #                       instructiune1
    c = c + 1                      #                 else:                   
#                                   #                       instructiune2

c = 0                        #instrctiunea break paraseste complet o bucla for sau while
while c < 5:
    print(c)
    if c == 3:
        break
    c = c + 1


c = 0
while c < 5:
    c = c + 1
    print(c)
    if c == 3:
        continue
    print(c)
