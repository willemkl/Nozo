from lõng_list2 import *

def tehe(sisend):
    märgid = "+-*"
    trajas = "t()"
    vahe_m = ""
    avaldis = []
    vahele = ""
    # Käib stringi läbi
    for i in range(len(sisend)):
        # Jätab vahle
        if i == vahele:
            continue
        # Kui tegu on tehtemärgiga lisab liikme ja märgi väljundisse
        elif sisend[i] in märgid and sisend[i-1] in "])":
            if vahe_m != "":
                avaldis.append(lõng_list(vahe_m))
                avaldis.append(sisend[i])
                vahe_m = ""
            else:
                avaldis.append(sisend[i])
        # Kui tegu on skalaarkorrutamisega lisab arvu ja tehtemärgi väljundisse ning tühjendab liikme
        elif sisend[i] == "s":
            try:
                avaldis.append(int(vahe_m))
                vahe_m = ""
                avaldis.append("s")
            except:
                avaldis.append(lõng_list(vahe_m))
                vahe_m = ""
                avaldis.append("s")
        # Kui tegu on transponeerimise tähisega või avava suluga lisab selle väljundisse
        elif sisend[i] in "t(":
            avaldis.append(sisend[i])
        # Lõpetav sulg, lisab maatriksi ja sulu väljundisse
        elif sisend[i] == ")":
            avaldis.append(lõng_list(vahe_m))
            vahe_m = ""
            avaldis.append(")")
        # Kui tegu on numriga lisab selle vahesse
        else:
            vahe_m += sisend[i]
    if vahe_m != "":
        try:
            # Kui tegu on skalaarkorrutisega lisab täisarvu
            avaldis.append(int(vahe_m))
        except:
            # Lisab viimase vahe väljundisse
            avaldis.append(lõng_list(vahe_m))
    return avaldis
# print(tehe("t([[-1,3],[-1,5]]-[[1,1],[5,8]])*[[1,1],[1,1]])"))