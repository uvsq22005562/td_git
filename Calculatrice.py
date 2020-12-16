import tkinter as tk
import math

A = [[], []]
p = 0
s = 0


def somme(A, B):
    """ Fais la somme de 2 nombre """
    C = A + B
    return C


def divide(A, B):
    """ Fais la division de 2 nombres """
    C = A / B
    return C


def multiplie(A, B):
    """ fais la multiplication de 2 nombres"""
    C = A * B
    return C


def power(A, B):
    """ fais la puissance de 2 nombres """
    C = A ** B
    return C


def soustraction(A, B):
    """ fais la soustraction de 2 nombres """
    C = A - B
    return C


def ERROR():
    """fonction erreur"""
    reset()
    affichage.config(text = "ERROR")
    pass


def reset():
    """fonction reset"""
    global A, s, p
    A = [[], []]
    p = 0
    s = 0
    pass


def ajout(V):
    """ajout de chiffre ou de signe"""
    global A
    A[p].append(V)

    pass


def signedivide():
    """change le signe en division"""
    global s
    s = 1
    pass


def signemultiplie():
    """change le signe en multiplier"""
    global s
    s = 2
    pass


def signesomme():
    """change le signe en somme"""
    global s
    s = 3
    pass


def signesoustraction():
    """change le en soustraction"""
    global s
    s = 4
    pass


def signepower():
    """change le signe en puissance"""
    global s
    s = 5
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


def affiche(A):
    if p == 0:
        A = str(A)
        affichage.config(text = str(A[0]))
    elif p == 1:
        A[0] = str(A[0])
        A[1] = str(A[1])
        if s == 1:
            B = A[0] + "/" + A[1]
        elif s == 2:
            B = A[0] + "*" + A[1]
        elif s == 3:
            B = A[0] + "+" + A[1]
        elif s == 4:
            B = A[0] + "^" + A[1]
        affichage.config(text = B)
    else:



racine = tk.Tk()
couleur1 = '#6ac1c2'
couleur2 = '#db8417'
couleur3 = '#ffff8e'
couleur4 = '#316258'

# ----- création des widgets -----
affichage = tk.Label(racine, text='', height='3', font=('courier', '8'))
boutton_0 = tk.Button(racine, text='0', height='2', width='4', bg=couleur1, command=ajout(0))
boutton_1 = tk.Button(racine, text='1', height='2', width='4', bg=couleur1, command=ajout(1))
boutton_2 = tk.Button(racine, text='2', height='2', width='4', bg=couleur1, command=ajout(2))
boutton_3 = tk.Button(racine, text='3', height='2', width='4', bg=couleur1, command=ajout(3))
boutton_4 = tk.Button(racine, text='4', height='2', width='4', bg=couleur1, command=ajout(4))
boutton_5 = tk.Button(racine, text='5', height='2', width='4', bg=couleur1, command=ajout(5))
boutton_6 = tk.Button(racine, text='6', height='2', width='4', bg=couleur1, command=ajout(6))
boutton_7 = tk.Button(racine, text='7', height='2', width='4', bg=couleur1, command=ajout(7))
boutton_8 = tk.Button(racine, text='8', height='2', width='4', bg=couleur1, command=ajout(8))
boutton_9 = tk.Button(racine, text='9', height='2', width='4', bg=couleur1, command=ajout(9))
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
boutton_carre = tk.Button(racine, text='²', height='2', width='4', bg=couleur3)
boutton_racine_carre = tk.Button(racine, text='sqrt',
                                 height='2', width='4', bg=couleur3, command=sqrt())
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

