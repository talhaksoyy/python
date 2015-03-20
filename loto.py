import random
k = 0
while k<8:
    i = 0
    loto = [ ]
    while i<6:
        a = random.randrange(1, 50)
        if loto.count(a) == (0):
            loto.append(a)
            i = i+1
    print(loto)
    k = k+1
