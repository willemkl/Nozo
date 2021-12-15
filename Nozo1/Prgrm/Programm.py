from väljund import *
from lõng_list2 import *
from lõng_list3 import *
from korrutamine import *
from transponeerimine import *
from skalaar import *
from liitmine_lahutamine import *
from Nozo0_1 import *

import tkinter as tk

def vajuta():
    tekst = väljund(pohi(sisend.get()))
    silt.configure(text=tekst)

aken = tk.Tk()
aken.title("Maatriksid")

silt = tk.Label(aken, text = "",font=("Oswald Bold", 20))
silt2 = tk.Label(aken, text = "Tehtemärgid: +(liitmine), -(lahutamine), *(korrutamine), t(transponeerimine), s*(skalaariga korrutamine).",font=("Oswald Bold", 10))
silt3 = tk.Label(aken, text = "Näidissisend(liitmine, lahutamine ja korrutamine analoogne): [[2,0],[4,0]]+[[0,2],[6,7]].",font=("Oswald Bold", 10))
silt4 = tk.Label(aken, text = "Näidissisend(skalaariga korrutamine): 2s*[[0,2],[6,7]].",font=("Oswald Bold", 10))
silt5 = tk.Label(aken, text = "Näidissisend(transponeerimine): t[[0,2],[6,7]].",font=("Oswald Bold", 10))

aken.geometry('860x500')

silt.grid(column=0,row=0)
silt2.grid(column=0,row=2)
silt3.grid(column=0,row=3)
silt4.grid(column=0,row=4)
silt5.grid(column=0,row=5)


nupp = tk.Button(aken, text="Arvuta!", command=vajuta)
nupp.grid(column=1,row=1)

sisend = tk.Entry(aken,width=57,font=("Oswald", 15))
sisend.grid(column=0,row=1)

aken.mainloop()