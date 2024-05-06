import tkinter as tk
from tkinter import *
import random


okno = Tk()
okno.title("piškvorky")
okno.geometry("250x250")


# nastavenie tlačidla po stlačení
def occupied1():
    button1.config(text="X")
    button1["state"] = "disabled"
    hrac_tahy.append(button1)
    Kontrola()
def occupied2():
    button2.config(text="X")
    button2["state"] = "disabled"
    hrac_tahy.append(button2)
    Kontrola()
def occupied3():
    button3.config(text="X")
    button3["state"] = "disabled"
    hrac_tahy.append(button3)
    Kontrola()
def occupied4():
    button4.config(text="X")
    button4["state"] = "disabled"
    hrac_tahy.append(button4)
    Kontrola()
def occupied5():
    button5.config(text="X")
    button5["state"] = "disabled"
    hrac_tahy.append(button5)
    Kontrola()
def occupied6():
    button6.config(text="X")
    button6["state"] = "disabled"
    hrac_tahy.append(button6)
    Kontrola()
def occupied7():
    button7.config(text="X")
    button7["state"] = "disabled"
    hrac_tahy.append(button7)
    Kontrola()
def occupied8():
    button8.config(text="X")
    button8["state"] = "disabled"
    hrac_tahy.append(button8)
    Kontrola()
def occupied9():
    button9.config(text="X")
    button9["state"] = "disabled"
    hrac_tahy.append(button9)
    Kontrola()


# vytvorenie tlačidiel a príkazov v nich
button1 = tk.Button(okno, command=occupied1, text="", width=5, height=2)
button1.place(x=50,y=0)
button2 = tk.Button(okno, command=occupied2, text="", width=5, height=2)
button2.place(x=100,y=0)
button3 = tk.Button(okno, command=occupied3, text="", width=5, height=2)
button3.place(x=150,y=0)
button4 = tk.Button(okno, command=occupied4, text="", width=5, height=2)
button4.place(x=50,y=40)
button5 = tk.Button(okno, command=occupied5, text="", width=5, height=2)
button5.place(x=100,y=40)
button6 = tk.Button(okno, command=occupied6, text="", width=5, height=2)
button6.place(x=150,y=40)
button7 = tk.Button(okno, command=occupied7, text="", width=5, height=2)
button7.place(x=50,y=80)
button8 = tk.Button(okno, command=occupied8, text="", width=5, height=2)
button8.place(x=100,y=80)
button9 = tk.Button(okno, command=occupied9, text="", width=5, height=2)
button9.place(x=150,y=80)

# vytvorenie zoznamu tlačidiel
buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

pc_tahy = []
hrac_tahy =[]

y1 = [button1, button2, button3]
y2 = [button4, button5, button6]
y3 = [button7, button8, button9]

x1 = [button1, button4, button7]
x2 = [button2, button5, button8]
x3 = [button3, button6, button9]

uhl1 = [button1, button5, button9]
uhl2 = [button7, button5, button3]


def tah_PC():
    volne_tlacidla = [tl for tl in buttons if tl["state"] != "disabled"]     # vytvaram zoznam-list volnych tlacidiel
    tlacidlo = random.choice(volne_tlacidla)                                # vyberam tlacidlo y listu
    #print("vybrane nahodne tlacidlo: ", tlacidlo)
    if tlacidlo:
        if len([tl for tl in volne_tlacidla if tl["state"] != "disabled"]) == 8:  #ak pocet volnych tlacidiel je rovný 8:
            tlacidlo = random.choice(volne_tlacidla)
            tlacidlo.config(text="O", bg="lightblue")
            tlacidlo["state"] = "disabled"
            Kontrola()
        else:
            Logika()

def Logika():    #Hlavny program
    if len([tl for tl in x1 if tl.cget("text") == "O"]) == 2:       # kONTROLA VYHRY HRACA
        tl = random.choice(x1)
        for tl in x1:
            if tl["state"] != "disabled":
                tl.config(text="O", bg="lightblue")
                tl["state"] = "disabled"
                return Kontrola()

    else:
        pass

    if len([tl for tl in x2 if tl.cget("text") == "O"]) == 2:
        tl = random.choice(x2)
        for tl in x2:
            if tl["state"] != "disabled":
                tl.config(text="O", bg="lightblue")
                tl["state"] = "disabled"
                return Kontrola()

    else:
        pass

    if len([tl for tl in x3 if tl.cget("text") == "O"]) == 2:
        tl = random.choice(x3)
        for tl in x3:
            if tl["state"] != "disabled":
                tl.config(text="O", bg="lightblue")
                tl["state"] = "disabled"
                return Kontrola()

    else:
        pass



##################################################################################    xxxxxxxxxxx

    if len([tl for tl in y1 if tl.cget("text") == "O"]) == 2:
        tl = random.choice(y1)
        for tl in y1:
            if tl["state"] != "disabled":
                tl.config(text="O", bg="lightblue")
                tl["state"] = "disabled"
                return Kontrola()

    else:
        pass

    if len([tl for tl in y2 if tl.cget("text") == "O"]) == 2:
        tl = random.choice(y2)
        for tl in y2:
            if tl["state"] != "disabled":
                tl.config(text="O", bg="lightblue")
                tl["state"] = "disabled"
                return Kontrola()

    else:
        pass

    if len([tl for tl in y3 if tl.cget("text") == "O"]) == 2:
        tl = random.choice(y3)
        for tl in y3:
            if tl["state"] != "disabled":
                tl.config(text="O", bg="lightblue")
                tl["state"] = "disabled"
                return Kontrola()

    else:
        pass

########################################################################### yyyyyyyyyyyyy

    if len([tl for tl in uhl1 if tl.cget("text") == "O"]) == 2:
        tl = random.choice(uhl1)
        for tl in uhl1:
            if tl["state"] != "disabled":
                tl.config(text="O", bg="lightblue")
                tl["state"] = "disabled"
                return Kontrola()

    else:
        pass

    if len([tl for tl in uhl2 if tl.cget("text") == "O"]) == 2:
        tl = random.choice(uhl2)
        for tl in uhl2:
            if tl["state"] != "disabled":
                tl.config(text="O", bg="lightblue")
                tl["state"] = "disabled"
                return Kontrola()

    else:
        pass



################################################################ KONTROLA SUPERA
    if len([tl for tl in x1 if tl.cget("text") == "X"]) == 2:
        tl = random.choice(x1)
        for tl in x1:
            if tl["state"] != "disabled":
                tl.config(text="O", bg="lightblue")
                tl["state"] = "disabled"
                return Kontrola()

    else:
        pass

    if len([tl for tl in x2 if tl.cget("text") == "X"]) == 2:
        tl = random.choice(x2)
        for tl in x2:
            if tl["state"] != "disabled":
                tl.config(text="O", bg="lightblue")
                tl["state"] = "disabled"
                return Kontrola()

    else:
        pass

    if len([tl for tl in x3 if tl.cget("text") == "X"]) == 2:
        tl = random.choice(x3)
        for tl in x3:
            if tl["state"] != "disabled":
                tl.config(text="O", bg="lightblue")
                tl["state"] = "disabled"
                return Kontrola()

    else:
        pass



##################################################################################    xxxxxxxxxxx

    if len([tl for tl in y1 if tl.cget("text") == "X"]) == 2:
        tl = random.choice(y1)
        for tl in y1:
            if tl["state"] != "disabled":
                tl.config(text="O", bg="lightblue")
                tl["state"] = "disabled"
                return Kontrola()

    else:
        pass

    if len([tl for tl in y2 if tl.cget("text") == "X"]) == 2:
        tl = random.choice(y2)
        for tl in y2:
            if tl["state"] != "disabled":
                tl.config(text="O", bg="lightblue")
                tl["state"] = "disabled"
                return Kontrola()

    else:
        pass

    if len([tl for tl in y3 if tl.cget("text") == "X"]) == 2:
        tl = random.choice(y3)
        for tl in y3:
            if tl["state"] != "disabled":
                tl.config(text="O", bg="lightblue")
                tl["state"] = "disabled"
                return Kontrola()

    else:
        pass

########################################################################### yyyyyyyyyyyyy

    if len([tl for tl in uhl1 if tl.cget("text") == "X"]) == 2:
        tl = random.choice(uhl1)
        for tl in uhl1:
            if tl["state"] != "disabled":
                tl.config(text="O", bg="lightblue")
                tl["state"] = "disabled"
                return Kontrola()

    else:
        pass

    if len([tl for tl in uhl2 if tl.cget("text") == "X"]) == 2:
        tl = random.choice(uhl2)
        for tl in uhl2:
            if tl["state"] != "disabled":
                tl.config(text="O", bg="lightblue")
                tl["state"] = "disabled"
                return Kontrola()

    else:
        pass

########################################################################  kontrola dalsich stavov

    if len([tl for tl in x1 if tl.cget("text") == "O"]) >= 1 and \
            len([tl for tl in x1 if tl.cget("text") == "X"]) == 0:
        tl = random.choice(x1)
        for tl in x1:
            if tl["state"] != "disabled":
                tl.config(text="O", bg="lightblue")
                tl["state"] = "disabled"
                return Kontrola()

    else:
        pass

    if len([tl for tl in x2 if tl.cget("text") == "O"]) >= 1 and \
            len([tl for tl in x2 if tl.cget("text") == "X"]) == 0:
            tl = random.choice(x2)
            for tl in x2:
                if tl["state"] != "disabled":
                    tl.config(text="O", bg="lightblue")
                    tl["state"] = "disabled"
                    return Kontrola()

    else: pass

    if len([tl for tl in x3 if tl.cget("text") == "O"]) >= 1 and \
            len([tl for tl in x3 if tl.cget("text") == "X"]) == 0:
            tl = random.choice(x3)
            for tl in x3:
                if tl["state"] != "disabled":
                    tl.config(text="O", bg="lightblue")
                    tl["state"] = "disabled"
                    return Kontrola()

    else: pass

#////////////////////////////////////////////////////////////////////////////////////////////
#                       y - ove podmienky
#////////////////////////////////////////////////////////////////////////////////////////////

    if len([tl for tl in y1 if tl.cget("text") == "O"]) >= 1 and \
            len([tl for tl in y1 if tl.cget("text") == "X"]) == 0:

        tl = random.choice(y1)
        for tl in y1:
            if tl["state"] != "disabled":
                tl.config(text="O", bg="lightblue")
                tl["state"] = "disabled"
                return Kontrola()


    else: pass

    if len([tl for tl in y2 if tl.cget("text") == "O"]) >= 1 and \
            len([tl for tl in y2 if tl.cget("text") == "X"]) == 0:

        tl = random.choice(y2)
        for tl in y2:
            if tl["state"] != "disabled":
                tl.config(text="O", bg="lightblue")
                tl["state"] = "disabled"
                return Kontrola()


    else: pass

    if len([tl for tl in y3 if tl.cget("text") == "O"]) >= 1 and \
            len([tl for tl in y3 if tl.cget("text") == "X"]) == 0:

        tl = random.choice(y3)
        for tl in y3:
            if tl["state"] != "disabled":
                tl.config(text="O", bg="lightblue")
                tl["state"] = "disabled"
                return Kontrola()


    else: pass

#////////////////////////////////////////////////////////////////////////////
#                          uhlopriecky
#////////////////////////////////////////////////////////////////////////////

    if len([tl for tl in uhl1 if tl.cget("text") == "O"]) >= 1 and \
            len([tl for tl in uhl1 if tl.cget("text") == "X"]) == 0:

        tl = random.choice(uhl1)
        for tl in uhl1:
            if tl["state"] != "disabled":
                tl.config(text="O", bg="lightblue")
                tl["state"] = "disabled"
                return Kontrola()


    else: pass

    if len([tl for tl in uhl2 if tl.cget("text") == "O"]) >= 1 and \
            len([tl for tl in uhl2 if tl.cget("text") == "X"]) == 0:

        tl = random.choice(uhl2)
        for tl in uhl2:
            if tl["state"] != "disabled":
                tl.config(text="O", bg="lightblue")
                tl["state"] = "disabled"
                return Kontrola()


    else: print("PC sa vzdáva")


button10 = tk.Button(okno, text="PC na rade", command = tah_PC, width=10, height=2)     #tlačidlo tah PC
button10.place(x=80,y=150)


def Kontrola():
    #print("zaciatok kontroly výhry")
    if all(button.cget("text") == "X" for button in y1):       #Kontrola horizontalneho stavu
        print("Vyhráva hráč so znakom X")
        return Koniec_Hry()
    elif all(button.cget("text") == "X" for button in y2):
        print("Vyhráva hráč so znakom X")
        return Koniec_Hry()
    elif all(button.cget("text") == "X" for button in y3):
        print("Vyhráva hráč so znakom X")
        return Koniec_Hry()

    elif all(button.cget("text") == "X" for button in x1):  #Kontrola vertikalneho stavu
        print("Vyhráva hráč so znakom X")
        return Koniec_Hry()
    elif all(button.cget("text") == "X" for button in x2):
       print("Vyhráva hráč so znakom X")
       return Koniec_Hry()
    elif all(button.cget("text") == "X" for button in x3):
       print("Vyhráva hráč so znakom X")
       return Koniec_Hry()

    elif all(button.cget("text") == "X" for button in uhl1):  #Kontrola uhlopriečok
       print("Vyhráva hráč so znakom X")
       return Koniec_Hry()
    elif all(button.cget("text") == "X" for button in uhl2):
       print("Vyhráva hráč so znakom X")
       return Koniec_Hry()

    # parametre pre PC - "O"---------------------------------------------------------------------

    elif all(button.cget("text") == "O" for button in y1):       #Kontrola horizontalneho stavu pre "O"
        print("Vyhráva hráč so znakom O")
        return Koniec_Hry()
    elif all(button.cget("text") == "O" for button in y2):
        print("Vyhráva hráč so znakom O")
        return Koniec_Hry()
    elif all(button.cget("text") == "O" for button in y3):
        print("Vyhráva hráč so znakom O")
        return Koniec_Hry()

    elif all(button.cget("text") == "O" for button in x1):
        print("Vyhráva hráč so znakom O")
        return Koniec_Hry()
    elif all(button.cget("text") == "O" for button in x2):
        print("Vyhráva hráč so znakom O")
        return Koniec_Hry()
    elif all(button.cget("text") == "O" for button in x3):
        print("Vyhráva hráč so znakom O")
        return Koniec_Hry()


    elif all(button.cget("text") == "O" for button in uhl1):  #Kontrola uhlopriečok
       print("Vyhráva hráč so znakom O")
       return Koniec_Hry()
    elif all(button.cget("text") == "O" for button in uhl2):
       print("Vyhráva hráč so znakom O")
       return Koniec_Hry()


def Koniec_Hry():
    print("Koniec hry")
    for button in buttons:
        button.config(state = "disabled", bg = "lightpink")


okno.mainloop()

