import tkinter as tk

racine = tk.Tk()
couleur1 = '#6ac1c2'
couleur2 = '#db8417'
couleur3 = '#ffff8e'
couleur4 = '#316258'

# ----- création des widgets -----
affichage = tk.Label(racine, text='', height='3', font=('courier', '8'))
boutton_0 = tk.Button(racine, text='0', height='2', width='4', bg=couleur1)
boutton_1 = tk.Button(racine, text='1', height='2', width='4', bg=couleur1)
boutton_2 = tk.Button(racine, text='2', height='2', width='4', bg=couleur1)
boutton_3 = tk.Button(racine, text='3', height='2', width='4', bg=couleur1)
boutton_4 = tk.Button(racine, text='4', height='2', width='4', bg=couleur1)
boutton_5 = tk.Button(racine, text='5', height='2', width='4', bg=couleur1)
boutton_6 = tk.Button(racine, text='6', height='2', width='4', bg=couleur1)
boutton_7 = tk.Button(racine, text='7', height='2', width='4', bg=couleur1)
boutton_8 = tk.Button(racine, text='8', height='2', width='4', bg=couleur1)
boutton_9 = tk.Button(racine, text='9', height='2', width='4', bg=couleur1)
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
                                 height='2', width='4', bg=couleur3)
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
