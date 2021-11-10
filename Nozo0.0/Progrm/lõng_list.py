def lõng_list(lõng):
    numbrid = "0123456789"
    list_lõng = list(lõng)
    rida = []
    maatriks = []
    # muudab sõnes kujus maatriksi listiks
    for i in range(len(list_lõng)):
        # paneb numbri paika
        if list_lõng[i] in numbrid:
            # vaatab, kas arv on negatiivne
            if list_lõng[i-1] == "-":
                rida.append(int("-" + list_lõng[i]))
            # kui pole negatiivne
            else:
                rida.append(int(list_lõng[i]))
        # sisestab rea maatriksisse
        elif list_lõng[i] == "]" and list_lõng[i-1] != "]":
            maatriks.append(rida)
            rida = []
    return maatriks