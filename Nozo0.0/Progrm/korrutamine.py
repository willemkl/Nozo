def korrutamine(maatriks_1, maatriks_2):
    m_1 = len(maatriks_1)
    n_1 = len(maatriks_1[0])
    m_2 = len(maatriks_2)
    n_2 = len(maatriks_2[0])
    maatriks = []
    # kas saab korrutada?
    if n_1 == m_2:
        # tühja maatriksi loomine
        for i in range(m_1):
            maatriks.append([])
            for j in range(n_2):
                maatriks[i].append(0)
        # elementidele vastavate rea ja veeru elementide korrutiste summeerimine
        for i in range(m_1):
            for j in range(n_2):
                for k in range(n_1):
                    maatriks[i][j] += maatriks_1[i][k]*maatriks_2[k][j]
        return maatriks
    else:
        return False