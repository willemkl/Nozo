from generaator import *
from väljund import *
from lõng_list2 import *
from korrutamine import *
from transponeerimine import *
from skalaar import *
from liitmine_lahutamine import *

def tegevus(tehe):
    vastus = []
    # korrutamine
    if "*" in tehe and "s*" not in tehe:
        i = tehe.index("*")
        es = lõng_list(tehe[:i])
        te = lõng_list(tehe[i+1:])
        vastus = korrutamine(es,te)
    # liitmine
    elif "+" in tehe:
        i = tehe.index("+")
        es = lõng_list(tehe[:i])
        te = lõng_list(tehe[i+1:])
        vastus = liitmine(es,te)
    # lahutamine
    elif "-" in tehe:
        i = tehe.index("-")
        es = lõng_list(tehe[:i])
        te = lõng_list(tehe[i+1:])
        vastus = lahutamine(es,te)
    # transponeerimine
    elif "transp" in tehe:
        i = tehe.index("transp")
        m = lõng_list(tehe[i:])
        vastus = transponeerimine(m)
    # skalaariga korrutamine
    elif "s*" in tehe:
        i = tehe.index("s*")
        s = int(tehe[:i])
        m = lõng_list(tehe[i+2:])
        vastus = skalaar(m,s)
    else:
        vastus = tehe
    return vastus

print("Teha saab üht tüüpi tehteid.")
print("Maatriksi kuju: [[0,0],[0,0]]")
print("Tehtemärgid: +(liitmine), -(lahutamine), *(korrutamine), transp(transponeerimine), s*(skalaariga korrutamine)")
print("Näidissisend(liitmine, lahutamine analoogne): [[2,0],[4,0]]+[[0,2],[6,7]]")
print("Näidissisend(korrutamine): [[2,0]]*[[0,2],[6,7]]")
print("Näidissisend(transponeerimine): transp[[0,2],[6,7]]")
print("Näidissisend(skalaariga korrutamine): 2s*[[0,2],[6,7]]")
k_sisend = input("Sisesta oma tehe: ")

väljund(tegevus(k_sisend))