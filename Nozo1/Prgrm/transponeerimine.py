def transponeerimine(maatriks):
    transp_maatriks = []
    # tühi maatriks
    for i in range(len(maatriks)):
        transp_maatriks.append([])
        for j in range(len(maatriks)):
            transp_maatriks[i].append(0)
    # transponeerimine
    for i in range(len(maatriks)):
        for j in range(len(maatriks)):
            transp_maatriks[i][j] = maatriks[j][i]
    
    return transp_maatriks