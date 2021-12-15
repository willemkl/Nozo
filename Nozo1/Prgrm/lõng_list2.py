# muudab järjendi maatriksiks(listiks)
def lõng_list(lõng):
    numbrid_miinus = "-0123456789"
    arv = ""
    rida = []
    maatriks = []
    # loeb järjendi läbi
    for i in range(len(lõng)):
        # "[" ei ole vaja vaadata
        if lõng[i] == "[":
            continue
        else:
            # loome arvu
            if lõng[i] in numbrid_miinus:
                arv = arv + lõng[i]
            # asetame arvu ritta
            elif lõng[i] == "," and lõng[i+1] != "[":
                rida.append(int(arv))
                arv = ""
            # asetame arvu ritta ja rea maatriksisse
            if lõng[i] == "]" and lõng[i-1] != "]":
                rida.append(int(arv))
                arv = ""
                maatriks.append(rida)
                rida = []
    return maatriks