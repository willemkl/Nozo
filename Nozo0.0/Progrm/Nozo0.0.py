from generaator import *
from väljund import *
from lõng_list import *
from korrutamine import *
from transponeerimine import *
from skaalar import *
from liitmine_lahutamine import *

def tegevus(tehe):
    vastus = []
    if "*" in tehe:
        i = tehe.index("*")
        es_liidetav = lõng_list(tehe[:i])
        te_liidetav = lõng_list(tehe[i+1:])
        vastus = korrutamine(tegevus(es_liidetav),tegevus(te_liidetav))
    else:
        vastus = tehe
    
    return vastus

print("Tehtemärgid: +, -, *, transponeerida")
k_sisend = input("Sisesta oma tehe: ")

väljund(tegevus(k_sisend))