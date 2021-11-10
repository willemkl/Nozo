def skaalar(maatriks,skaalar):
    # korrutamine skaalariga
    for i in range(len(maatriks)):
        for j in range(len(maatriks[0])):
            maatriks[i][j] = maatriks[i][j]*skaalar
    return maatriks