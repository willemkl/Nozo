def skalaar(maatriks,skalaar):
    if isinstance(maatriks, list):
        # korrutamine skalaariga
        for i in range(len(maatriks)):
            for j in range(len(maatriks[0])):
                maatriks[i][j] = maatriks[i][j]*skalaar
        return maatriks
    else:
        for i in range(len(skalaar)):
            for j in range(len(skalaar[0])):
                skalaar[i][j] = skalaar[i][j]*maatriks
        return skalaar