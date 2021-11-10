def skalaar(maatriks,skalaar):
    # korrutamine skalaariga
    for i in range(len(maatriks)):
        for j in range(len(maatriks[0])):
            maatriks[i][j] = maatriks[i][j]*skalaar
    return maatriks