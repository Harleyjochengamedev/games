import tkinter as tk
from tkinter import font

def xouo():
    controle = True
    numero = 1
    if controle:
        rotulo["text"] = "O"
        numero+=1
    else:
        rotulo["text"] = "X"
        numero+=1

tela = tk.Tk()
for linha in range(3):
    for coluna in range(3):
        frame = tk.Frame(master=tela,relief=tk.RAISED,borderwidth=1)
        frame.grid(row=linha,column=coluna,padx=5,pady=5)
        rotulo = tk.Label(master=frame,text=f'Linha:{linha} \n Coluna:{coluna}')
        botao = tk.Button(master=frame,command=xouo, text="clique aqui")
        rotulo.pack()
        botao.pack()
tela.mainloop()