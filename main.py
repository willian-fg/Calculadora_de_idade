from tkinter import *
#from tkinter import ttk

#cores
cor1 = "#3b3b3b"   #cinza escuro
cor2 = '#333333'    #preto
cor3 = '#ffffff'    #Branco
cor4 = '#ffcc58'     #Laranja


janela = Tk()
janela.title('Calculadora de idade')
janela.geometry('310x400')

#frames
frame_cima = Frame(janela, width=310, height=140, pady=0, padx=0, relief='flat', bg=cor2)
frame_cima.grid(row=0, column=0)
frame_baixo = Frame(janela, width=310, height=300, pady=0, padx=0, relief='flat', bg=cor1)
frame_baixo.grid(row=1, column=0)

#Labels do frame superior
l_calculadora = Label(frame_cima, text='Calculadora', width=25, height=1, padx=3, relief='flat', pady=0,
                      anchor='center', font='Ivy 15 bold', bg=cor2, fg=cor3)
l_calculadora.place(x=0, y=30)
l_idade = Label(frame_cima, text='DE IDADE', width=11, height=1, relief='flat', pady=0, anchor='center',
                font='Arial 35 bold', bg=cor2, fg=cor4)
l_idade.place(x=0, y=70)

janela.mainloop()
