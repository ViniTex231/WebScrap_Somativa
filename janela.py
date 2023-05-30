from tkinter import *
from tkinter import ttk
from conexao import cursor
from main import Web

janela = Tk()

class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.botoes()
        self.lista_frame2()
        self.clear_list()
        self.combobox()
        janela.mainloop()

    def tela(self):
        self.janela.title("Busca Preço")
        self.janela.configure(background='#bdbcb3')
        self.janela.geometry('700x500')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=700, height=500)

    def frames(self):
        self.frame_0 = Frame(self.janela, bg='#D9D9D9', highlightthickness=0.5, highlightbackground='#9c9a92')
        self.frame_0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.11)

        self.frame_1 = Frame(self.janela, bg='#D9D9D9', highlightthickness=0.5, highlightbackground='#9c9a92')
        self.frame_1.place(relx=0.03, rely=0.15, relwidth=0.94, relheight=0.11)

        self.frame_2 = Frame(self.janela, bg='#D9D9D9', highlightthickness=0.5, highlightbackground='#9c9a92')
        self.frame_2.place(relx=0.03, rely=0.50, relwidth=0.94, relheight=0.45)

    def combobox(self):
        names = ["Springer", "Elgin", "Gree", "LG", "Samsung"]
        self.cb_marcas = ttk.Combobox(self.frame_1, values=names)
        self.cb_marcas.pack()
        self.cb_marcas.place(relx=0.03, rely=0.35, relwidth=0.1, relheight=0.50)
        self.cb_label = Label(self.frame_1, width=15, height=2, text="Marca", font=('Arial 10'), anchor='w')
        self.cb_label.place(relx=0.03, rely=0.10, relwidth=0.1, relheight=0.23)

    def botoes(self):
        self.btBuscar = Button(self.frame_1, text="Buscar", command=self.select_list)
        self.btBuscar.place(relx=0.15, rely=0.30, relwidth=0.1, relheight=0.50)

        self.btLimpar = Button(self.frame_1, text="Limpar", command=self.clear_list)
        self.btLimpar.place(relx=0.27, rely=0.30, relwidth=0.1, relheight=0.50)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, columns=('col1', 'col2', 'col3'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='Descrição')
        self.listaCli.heading('#2', text='Valor')

        self.listaCli.column('#0', width=5)
        self.listaCli.column('#1', width=500)
        self.listaCli.column('#2', width=100)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)

    def select_list(self):

        marca_a = self.cb_marcas.get().lower()
        cursor.execute(f"SHOW TABLES LIKE '{marca_a}'")
        list_tabel = cursor.fetchone() is not None

        if list_tabel:
            n_marcas = self.list_tabela(marca_a)
            for modelo in n_marcas:
                self.listaCli.insert("", "end", values=modelo)
        else:
            Web(marca_a)

    def list_tabela(self, tabela):
        cursor.execute(f"SELECT * FROM {tabela}")
        linhas = cursor.fetchall()
        return linhas

    def clear_list(self):
        self.listaCli.delete(*self.listaCli.get_children())


janela_main = Aplicacao()
