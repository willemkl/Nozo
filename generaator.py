import random

def generaator():

    m = int(input("Ridade arv: "))
    n = int(input("Veergude arv: "))

    maatriks = []

    i = 0
    while i < m:
        maatriks.append([])
        j = 0
        while j < n:
            maatriks[i].append(random.randint(0, 10))
            j += 1
        i += 1
    
    return maatriks, m, n