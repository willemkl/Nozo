import random

def generaator():
    # maatriksi suurus
    m = int(input("Ridade arv: "))
    n = int(input("Veergude arv: "))
    maatriks = []
    # maatriksi täitmine suvaliste arvudega -9, 9
    for i in range(m):
        maatriks.append([])
        for j in range(n):
            maatriks[i].append(random.randint(-9, 9))
    return maatriks