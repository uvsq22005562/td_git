import tkinter as tk
import math

A = [[], []]
p = 0
s = 0


def reset():
    """fonction reset"""
    global A, s, p
    A = [[], []]
    p = 0
    s = 0
    pass


def resetlow():
    """fonction reset"""
    global A, s, p
    A = [[], []]
    p = 0
    s = 0
    pass


def ajout0():
    """ajout de chiffre ou de signe"""
    global A
    A[p].append(0)
    affiche()
    pass


def ajout1():
    """ajout de chiffre ou de signe"""
    global A
    A[p].append(1)
    affiche()
    pass


def ajout2():
    """ajout de chiffre ou de signe"""
    global A
    A[p].append(2)
    affiche()
    pass


def ajout3():
    """ajout de chiffre ou de signe"""
    global A
    A[p].append(3)
    affiche()
    pass


def ajout4():
    """ajout de chiffre ou de signe"""
    global A
    A[p].append(4)
    affiche()
    pass


def ajout5():
    """ajout de chiffre ou de signe"""
    global A
    A[p].append(5)
    affiche()
    pass


def ajout6():
    """ajout de chiffre ou de signe"""
    global A
    A[p].append(6)
    affiche()
    pass


def ajout7():
    """ajout de chiffre ou de signe"""
    global A
    A[p].append(7)
    affiche()
    pass


def ajout8():
    """ajout de chiffre ou de signe"""
    global A
    A[p].append(8)
    affiche()
    pass


def ajout9():
    """ajout de chiffre ou de signe"""
    global A
    A[p].append(9)
    affiche()
    pass


def signedivide():
    """change le signe en division"""
    global s, p
    s = 1
    affiche()
    p = 1
    pass


def signemultiplie():
    """change le signe en multiplier"""
    global s, p
    s = 2
    affiche()
    p = 1
    pass


def signesomme():
    """change le signe en somme"""
    global s, p
    s = 3
    affiche()
    p = 1
    pass


def signesoustraction():
    """change le en soustraction"""
    global s, p
    s = 4
    affiche()
    p = 1
    pass


def signepower():
    """change le signe en puissance"""
    global s, p
    s = 5
    affiche()
    p = 1
    pass


def power2():
    """fais la puissance de 2"""
    global A, p
    if p == 1:
        ERROR()
    else:
        A[0] = str(A[0])
        A[0] = float(A[0]) ** 2
        affichage(A[0])
    pass


def sqrt():
    """fais la racine du nombre"""
    global A, p
    if p == 1:
        ERROR()
    else:
        A[0] = str(A[0])
        A[0] = math.sqrt(float(A[0]))
        affichag(A[0])
    pass


def affiche():
    global A, s, p
    B = 0
    if p == 0:
        B = str(A[0])
        affichage.config(text = str(B))
        if s != 0:
            if s == 1:
                B = B + "/"
            elif s == 2:
                B = B + "*"
            elif s == 3:
                B = B + "+"
            elif s == 4:
                B = B + "^"

    elif p == 1:
        C = str(A[0])
        D = str(A[1])
        if s == 1:
            B = C + "/" + D
        elif s == 2:
            B = C + "*" + D
        elif s == 3:
            B = C + "+" + D
        elif s == 4:
            B = C + "^" + D
    
    affichage.config(text = B)

    pass


racine = tk.Tk()
couleur1 = '#6ac1c2'
couleur2 = '#db8417'
couleur3 = '#ffff8e'
couleur4 = '#316258'

# ----- création des widgets -----
affichage = tk.Label(racine, text='', height='3', font=('courier', '8'))
boutton_0 = tk.Button(racine, text='0', height='2', width='4', bg=couleur1, command=ajout0)
boutton_1 = tk.Button(racine, text='1', height='2', width='4', bg=couleur1, command=ajout1)
boutton_2 = tk.Button(racine, text='2', height='2', width='4', bg=couleur1, command=ajout2)
boutton_3 = tk.Button(racine, text='3', height='2', width='4', bg=couleur1, command=ajout3)
boutton_4 = tk.Button(racine, text='4', height='2', width='4', bg=couleur1, command=ajout4)
boutton_5 = tk.Button(racine, text='5', height='2', width='4', bg=couleur1, command=ajout5)
boutton_6 = tk.Button(racine, text='6', height='2', width='4', bg=couleur1, command=ajout6)
boutton_7 = tk.Button(racine, text='7', height='2', width='4', bg=couleur1, command=ajout7)
boutton_8 = tk.Button(racine, text='8', height='2', width='4', bg=couleur1, command=ajout8)
boutton_9 = tk.Button(racine, text='9', height='2', width='4', bg=couleur1, command=ajout9)
boutton_clear = tk.Button(racine, text='C',
                          height='2', width='4', bg=couleur2)
boutton_addition = tk.Button(racine, text='+',
                             height='2', width='4', bg=couleur3)
boutton_soustraction = tk.Button(racine, text='-',
                                 height='2', width='4', bg=couleur3)
boutton_multiplication = tk.Button(racine, text='x',
                                   height='2', width='4', bg=couleur3)
boutton_division = tk.Button(racine, text='/',
                             height='2', width='4', bg=couleur3)
boutton_calcul = tk.Button(racine, text='=',
                           height='2', width='4', bg=couleur4)
boutton_point = tk.Button(racine, text='.', height='2', width='4', bg=couleur3)
boutton_carre = tk.Button(racine, text='²', height='2', width='4', bg=couleur3, command=power2)
boutton_racine_carre = tk.Button(racine, text='sqrt',
                                 height='2', width='4', bg=couleur3, command=sqrt)
boutton_exposant = tk.Button(racine, text='^',
                             height='2', width='4', bg=couleur3)

# ----- placement des widgets -----
affichage.grid(column=0, row=0, columnspan=4)
boutton_1.grid(column=0, row=1)
boutton_2.grid(column=1, row=1)
boutton_3.grid(column=2, row=1)
boutton_4.grid(column=0, row=2)
boutton_5.grid(column=1, row=2)
boutton_6.grid(column=2, row=2)
boutton_7.grid(column=0, row=3)
boutton_8.grid(column=1, row=3)
boutton_9.grid(column=2, row=3)
boutton_clear.grid(column=0, row=4)
boutton_0.grid(column=1, row=4)
boutton_calcul.grid(column=3, row=5)
boutton_addition.grid(column=3, row=1)
boutton_soustraction.grid(column=3, row=2)
boutton_multiplication.grid(column=3, row=3)
boutton_division.grid(column=3, row=4)
boutton_point.grid(column=2, row=4)
boutton_carre.grid(column=0, row=5)
boutton_racine_carre.grid(column=1, row=5)
boutton_exposant.grid(column=2, row=5)


racine.mainloop()

