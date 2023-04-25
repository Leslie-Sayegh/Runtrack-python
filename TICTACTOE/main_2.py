erreur

from tkinter import*
 
#création d'une fenêtre
window = Tk()
window.title("Morpion")
window.geometry("500x500")
window.minsize(500,500)
window.maxsize(500,500)
window.config(background = "white")
 
#frame
frame = Frame(window,bg="white")
frame.pack(expand=YES)
 
 
#commande bouton
def command(row,column):
    width = 100
    height = 100
    joueur = 1
    if joueur == 1:
        # cercle
        cercle = Canvas(frame, width=width, height=height)
        cercle.create_oval(10, 5, 90, 90, width=10, outline="blue")
        joueur += 1
        cercle.grid(row=row,column = column)
    else:
        # croix
        croix = Canvas(frame, width=width, height=height)
        croix.create_line(15, 5, 86, 100, width=10, fill='red')
        croix.create_line(80, 5, 20, 100, width=10, fill='red')
        croix.grid(row=row, column=column)
        joueur = -1
 
#titre
titre = Label(frame,text="Morpion",font=("Arial",20),fg = "black",bg = "white")
titre.grid(row=0,column=1)
 
#boutons
button_1 = Button(frame,padx = 60,pady=60,command = lambda:command(1,0))
button_1.grid(row=1,column=0)
button_2 = Button(frame,padx = 60,pady=60,command = lambda:command(1,1))
button_2.grid(row=1,column=1)
button_3 = Button(frame,padx = 60,pady=60,command = lambda:command(1,2))
button_3.grid(row=1,column=2)
button_4 = Button(frame,padx = 60,pady=60,command = lambda:command(2,0))
button_4.grid(row=2,column=0)
button_5 = Button(frame,padx = 60,pady=60,command = lambda:command(2,1))
button_5.grid(row=2,column=1)
button_6 = Button(frame,padx = 60,pady=60,command = lambda:command(2,2))
button_6.grid(row=2,column=2)
button_7 = Button(frame,padx = 60,pady=60,command = lambda:command(3,0))
button_7.grid(row=3,column=0)
button_8 = Button(frame,padx = 60,pady=60,command = lambda:command(3,1))
button_8.grid(row=3,column=1)
button_9 = Button(frame,padx = 60,pady=60,command = lambda:command(3,2))
button_9.grid(row=3,column=2)
 
 
 
#afficher la fenêtre
window.mainloop()