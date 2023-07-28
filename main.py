import datetime
from datetime import *
from tkinter import *
from tkcalendar import DateEntry

# from tkinter import ttk

# cores
cor1 = "#3b3b3b"  # cinza escuro
cor2 = '#333333'  # preto
cor3 = '#ffffff'  # Branco
cor4 = '#ffcc58'  # Laranja

janela = Tk()
janela.title('Calculadora de idade')
janela.geometry('310x400')

# frames
frame_cima = Frame(janela, width=310, height=140, pady=0, padx=0, relief='flat', bg=cor2)
frame_cima.grid(row=0, column=0)
frame_baixo = Frame(janela, width=310, height=300, pady=0, padx=0, relief='flat', bg=cor1)
frame_baixo.grid(row=1, column=0)

# Labels do frame superior
l_calculadora = Label(frame_cima, text='Calculadora', width=25, height=1, padx=3, relief='flat', pady=0,
                      anchor='center', font='Ivy 15 bold', bg=cor2, fg=cor3)
l_calculadora.place(x=0, y=30)
l_idade = Label(frame_cima, text='DE IDADE', width=11, height=1, relief='flat', pady=0, anchor='center',
                font='Arial 35 bold', bg=cor2, fg=cor4)
l_idade.place(x=0, y=70)


# Funções

def calcular_idade():
    inicial = cal_1.get()
    final = cal_2.get()

    d1 = datetime.strptime(inicial, '%m/%d/%Y')
    d2 = datetime.strptime(final, '%m/%d/%Y')
    sub_meses = abs(d1.month - d2.month)
    sub_dias = abs(d1.day - d2.day)
    sub_anos = abs(d1.year - d2.year)

    l_app_anos['text'] = sub_anos
    l_app_meses['text'] = sub_meses
    l_app_dias['text'] = sub_dias


# label frame inferior


l_data_inicial = Label(frame_baixo, text='Data Atual', width=25, height=1, padx=0, relief='flat', pady=0, anchor='nw',
                       font='Ivy 11', bg=cor1, fg=cor3)
l_data_inicial.place(x=40, y=30)
cal_1 = DateEntry(frame_baixo, width=13, bg="darkblue", fg=cor3, borderwidth=2, date_pattern="mm/dd/y", y=2021)
cal_1.place(x=190, y=30)

l_data_de_nascimento = Label(frame_baixo, text='Data de Nascimento', width=25, height=1, padx=0, relief='flat', pady=0,
                             anchor='nw', font='Ivy 11', bg=cor1, fg=cor3)
l_data_de_nascimento.place(x=40, y=75)
cal_2 = DateEntry(frame_baixo, width=13, bg="darkblue", fg=cor3, borderwidth=2, date_pattern="mm/dd/y", y=2021)
cal_2.place(x=190, y=70)

l_app_anos = Label(frame_baixo, text='--', width=0, height=1, relief='flat', padx=0, pady=0, anchor='center',
                   font='Ivy 25 bold', bg=cor1, fg=cor3)
l_app_anos.place(x=60, y=135)
l_app__anos_nome = Label(frame_baixo, text='Anos', width=0, height=1, relief='flat', padx=0, pady=0, anchor='center',
                         font='Ivy 11 bold', bg=cor1, fg=cor3)
l_app__anos_nome.place(x=60, y=175)

l_app_meses = Label(frame_baixo, text='--', width=0, height=1, relief='flat', padx=0, pady=0, anchor='center',
                    font='Ivy 25 bold', bg=cor1, fg=cor3)
l_app_meses.place(x=140, y=135)
l_app__meses_nome = Label(frame_baixo, text='Meses', width=0, height=1, relief='flat', padx=0, pady=0, anchor='center',
                          font='Ivy 11 bold', bg=cor1, fg=cor3)
l_app__meses_nome.place(x=140, y=175)

l_app_dias = Label(frame_baixo, text='--', width=0, height=1, relief='flat', padx=0, pady=0, anchor='center',
                   font='Ivy 25 bold', bg=cor1, fg=cor3)
l_app_dias.place(x=220, y=135)
l_app_dias_nome = Label(frame_baixo, text='dias', width=0, height=1, relief='flat', padx=0, pady=0, anchor='center',
                        font='Ivy 11 bold', bg=cor1, fg=cor3)
l_app_dias_nome.place(x=220, y=175)

# Botões

b_calcular = Button(frame_baixo, text='Calcular', width=20, height=1, relief='raised', padx=0, pady=0,
                    overrelief='ridge', font='Ivy 10 bold', bg=cor1, fg=cor3, command=calcular_idade)
b_calcular.place(x=70, y=225)

janela.mainloop()
