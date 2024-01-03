from tkinter import *
from tkinter  import ttk
#import random 


root = Tk()
root.title("Creation de Comptre")
root.geometry("700x500")

account_type_var = StringVar()
account_type_var.set("courant Epargne")
def desactive():
    
    #Obtenez la valeur du bouton radio sélectionné
    account_type = account_type_var.get()
     #Si c'est un compte courant, activez la case de saisie du taux d'intérêt
    if account_type == "Courant":
      entryM.config(state=NORMAL)
      entrytaux.config(state=DISABLED)
    else:
      entryM.config(state=DISABLED)
      entrytaux.config(state=NORMAL)

nbr = 0
numero = Label(root,text = "Numero : ")
numero.place (x=10,y=10)
nbr1= Label(root,text=nbr)
nbr1.place(x=100,y=10)

Proprietaire = Label(root,text="Proprietaire :")
Proprietaire.place( x=10 , y=40)
entryPro= Entry(root)
entryPro.place(x=100,y=40,width=200)

Solde= Label(root,text="Solde initial :")
Solde.place( x=10 , y=70)
eurro= Label(root, text="Euro €")
eurro.place(x=300,y=70)
entrysold= Entry(root)
entrysold.place(x=100,y=70,width=200)

Type = Label(root,text="Type :")
Type.place(x=10 ,y=100)
Courant = Radiobutton(root,text="Courant",value="Courant",variable=account_type_var,command=desactive)
Courant.place(x=90,y=100)
Epargne = Radiobutton(root,text="Epargne",value="Epargne",variable=account_type_var,command=desactive)
Epargne.place(x=170,y=100)


Taux = Label(root,text="Taux Interet :")
Taux.place( x=10 , y=140)
P= Label(root, text="%")
P.place(x=300,y=140)
entrytaux= Entry(root)
entrytaux.place(x=100,y=140,width=200)

M = Label(root,text="M.Decouvert :")
M.place( x=10 , y=170)
entryM= Entry(root)
entryM.place(x=100,y=170,width=200)


def ajouter ():
   global nbr
   nbr = nbr + 1 
   nbr1.config(text=nbr)
   Proprietaire = entryPro.get()
   solde = entrysold.get()
   type = account_type_var.get()
   Taux  = entrytaux.get()
   mautant = entryM.get()
   
   table.insert('','end',values=(nbr,Proprietaire,solde,type,Taux,mautant))



table =ttk.Treeview(root, columns=(1,2,3,4,5,6),height=5,show="headings")
table.place(x=10,y=300,width=800,height=200)

table.heading(1,text="numero")
table.heading(2,text="Proprietaire")
table.heading(3,text="solde")
table.heading(4,text="type")
table.heading(5,text="taux interet")
table.heading(6,text="montant decovert")

table.column(1,width=30)
table.column(2,width=50)
table.column(3,width=40)
table.column(4,width=40)
table.column(5,width=70)
table.column(6,width=80)

button = Button(root,text="Creation de compte" ,command=ajouter)
button.place(x=100,y=200,height=30,width=170)


root.mainloop()