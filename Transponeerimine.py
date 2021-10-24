from generaator import *

a = generaator()

m = a[1]
n = a[2]
a = a[0]

def transponeerimine(a,n,m):
    maatriks = []
    i = 0
    while i < m:
        maatriks.append([])
        j = 0
        while j < n:
            maatriks[i].append(0)
            j += 1
        i += 1
    i = 0
    while i < m:
        j = 0
        while j < n:
            maatriks[i][j] = a[j][i]
            j += 1
        i += 1
    
    return maatriks