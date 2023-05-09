from main import start
from tkinter import *
from tkinter import Tk

janela = Tk()

class Busca():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        #self.botoes()
        #self.labels()
        #self.inputs()
        #self.lista_frame2()
        #self.select_list()
        #self.inpIDUsuario.focus_set()
        #self.grafic()
        #self.grafic2()
        janela.mainloop()
    def tela(self):
        self.janela.title("Busca Preço")
        janela.configure(background='#fff')
        janela.geometry('700x700')
        janela.resizable(True, True)
        janela.maxsize(width=700, height=700)

    def frames(self):
        frame_0 = Frame(janela, bg='#b0afa9', highlightthickness=0.5, highlightbackground='#9c9a92')
        frame_0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.08)

x = Busca()
