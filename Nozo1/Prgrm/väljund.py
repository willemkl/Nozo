def väljund(maatriks):
    väljund = ""
    suurim = 0
    for rida in maatriks:
        for veerg in rida:
            if len(str(veerg)) > suurim:
                suurim = len(str(veerg))
#     suurim += 1
    for rida in maatriks:
        for i in range(len(rida)):
            väljund += str(rida[i]).center(suurim," ")
            if i + 1 != len(rida):
                väljund += " "
        väljund += "\n"
    return str(väljund)