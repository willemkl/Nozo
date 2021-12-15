from väljund import *
from lõng_list2 import *
from lõng_list3 import *
from korrutamine import *
from transponeerimine import *
from skalaar import *
from liitmine_lahutamine import *

sisend = "t(t(([[-1,3],[-1,5]]-[[1,1],[5,8]])*[[1,1],[1,1]])-[[1,1],[1,1]])*[[1,1],[1,1]]"

def pohi(sisend):
    tehtemärgid = "st+-*"
    kõrge = "s*"
    keskmine = "+-"
    madal = ")" # ei kasuta
    madalaim = "t" # ei kasuta

    vahetulemus = []
    ootel = []

    jär = tehe(sisend)

    vahele = ""

    for i in range(len(jär)):
        if i == vahele:
            continue
        elif isinstance(jär[i], list) or isinstance(jär[i], int):
            vahetulemus.append(jär[i])
        elif jär[i] == "(":
            ootel.append(jär[i])
        elif jär[i] in tehtemärgid:
            if len(ootel) > 0:
                for j in range(len(ootel)-1, -1, -1):
                    if jär[i] in kõrge and ootel[j] in kõrge or jär[i] in keskmine and ootel[j] in keskmine or jär[i] in keskmine and ootel[j] in kõrge:
                        if ootel[j] == "+":
                            vahetulemus.append(liitmine(vahetulemus.pop(-1),vahetulemus.pop(-1)))
                            ootel.pop(j)
                        elif ootel[j] == "-":
                            vahetulemus.append(lahutamine(vahetulemus.pop(-2),vahetulemus.pop(-1)))
                            ootel.pop(j)
                        elif ootel[j] == "s":
                            vahetulemus.append(skalaar(vahetulemus.pop(-1),vahetulemus.pop(-1)))
                            ootel.pop(j)
                        elif ootel[j] == "*":
                            vahetulemus.append(korrutamine(vahetulemus.pop(-2),vahetulemus.pop(-1)))
                            ootel.pop(j)
                        elif ootel[j] == "t":
                            vahetulemus.append(transponeerimine(vahetulemus.pop(-1)))
                            ootel.pop(j)
                    else:
                        break
            ootel.append(jär[i])
        elif jär[i] == ")":
            for l in range(len(ootel)-1, -1, -1):
                if ootel[l] == "(":
                    ootel.pop(l)
                    break
                else:
                    if ootel[l] == "+":
                        vahetulemus.append(liitmine(vahetulemus.pop(-1),vahetulemus.pop(-1)))
                        ootel.pop(l)
                    elif ootel[l] == "-":
                        vahetulemus.append(lahutamine(vahetulemus.pop(-2),vahetulemus.pop(-1)))
                        ootel.pop(l)
                    elif ootel[l] == "s":
                        vahetulemus.append(skalaar(vahetulemus.pop(-1),vahetulemus.pop(-1)))
                        ootel.pop(l)
                    elif ootel[l] == "*":
                        vahetulemus.append(korrutamine(vahetulemus.pop(-2),vahetulemus.pop(-1)))
                        ootel.pop(l)
                    elif ootel[l] == "t":
                        vahetulemus.append(transponeerimine(vahetulemus.pop(-1)))
                        ootel.pop(l)
            
    for s in range(len(ootel)-1,-1,-1):
        if ootel[s] == "+":
            vahetulemus.append(liitmine(vahetulemus.pop(-1),vahetulemus.pop(-1)))
            ootel.pop(s)
        elif ootel[s] == "-":
            vahetulemus.append(lahutamine(vahetulemus.pop(-2),vahetulemus.pop(-1)))
            ootel.pop(s)
        elif ootel[s] == "s":
            vahetulemus.append(skalaar(vahetulemus.pop(-1),vahetulemus.pop(-1)))
            ootel.pop(s)
        elif ootel[s] == "*":
            vahetulemus.append(korrutamine(vahetulemus.pop(-2),vahetulemus.pop(-1)))
            ootel.pop(s)
        elif ootel[s] == "t":
            vahetulemus.append(transponeerimine(vahetulemus.pop(-1)))
            ootel.pop(s)
    return vahetulemus[0]