from generaator import *

def liitmine(maatriks_1,maatriks_2):
    summa=[]
    # kas kaks maatriksit on sama ridade ja veergude arvuga
    if len(maatriks_1) == len(maatriks_2) and len(maatriks_1[0]) == len(maatriks_2[0]):
        for i in range(len(maatriks_1)):
            # lisame tühja rea
            summa.append([])
            for j in range(len(maatriks_1[0])):
                # lisame tühja elemendi
                summa[i].append(0)
                # muudame tühja elemedi kahe maatriksi vastavate elementide summaks
                summa[i][j] = maatriks_1[i][j] + maatriks_2[i][j]
        return summa
    else:
        return False

def lahutamine(maatriks_1,maatriks_2):
    summa=[]
    # kas kaks maatriksit on sama ridade ja veergude arvuga
    if len(maatriks_1) == len(maatriks_2) and len(maatriks_1[0]) == len(maatriks_2[0]):
        for i in range(len(maatriks_1)):
            # lisame tühja rea
            summa.append([])
            for j in range(len(maatriks_1[0])):
                # lisame tühja elemendi
                summa[i].append(0)
                # muudame tühja elemedi kahe maatriksi vastavate elementide vaheks
                summa[i][j] = maatriks_1[i][j] - maatriks_2[i][j]
        return summa
    else:
        return False