from tkinter import Tk, Entry, Label, Button, Frame, messagebox, filedialog, ttk, Scrollbar, VERTICAL, HORIZONTAL
import pandas as pd
import tkinter as tk
import sqlalchemy
import psycopg2
from sqlalchemy import create_engine
import datetime
from tkinter import *


class Register(tk.Frame):
    def __init__(self, window, *args, **kwargs):
        tk.Frame.__init__(self, window)
        self.wind = window
        self.wind.title('ABM')
        menubar = Menu(self.wind)
        self.wind.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="App Informativa", command=self.openAppInformativa)
        filemenu.add_command(label="Callback SMS Notifica", command=self.openCallbackSMS)
        filemenu.add_command(label="callbackhvc", command=self.opencallbackhvc)
        filemenu.add_command(label="cms17", command=self.opencms17)
        filemenu.add_command(label="cms 19", command=self.opencms19)
        filemenu.add_command(label="Integraci�n EBS", command=self.openIntegracionEBS)
        filemenu.add_command(label="Llamadas molestosas", command=self.openLlamadasmolestosas)
        filemenu.add_command(label="Rellamadas", command=self.openRellamadas)
        filemenu.add_command(label="Requerimientos Fiscales", command=self.openRequerimientosFiscales)
        filemenu.add_command(label="SMS Notifica", command=self.openSMSNotifica)
        filemenu.add_command(label="Tallycode", command=self.openTallycode)
        filemenu.add_command(label="Todos", command=self.openTodos)
        filemenu.add_command(label="TR4", command=self.openTR4)
        filemenu.add_command(label="wfo", command=self.openwfo)
        filemenu.add_command(label="wfo acr", command=self.openwfoacr)

        menubar.add_cascade(label="Tipo de ABM", menu=filemenu)

    def openAppInformativa(self):
        self.appi = tk.Toplevel(self.wind)
        self.addClass = NewAppi(self.wind, self.appi)

    def openCallbackSMS(self):
        self.appi = tk.Toplevel(self.wind)
        self.addClass = NewCSMS(self.wind, self.appi)

    def opencallbackhvc(self):
        self.appi = tk.Toplevel(self.wind)
        self.addClass = NewCHVC(self.wind, self.appi)

    def opencms17(self):
        self.appi = tk.Toplevel(self.wind)
        self.addClass = NewCMS17(self.wind, self.appi)

    def opencms19(self):
        self.appi = tk.Toplevel(self.wind)
        self.addClass = NewCMS19(self.wind, self.appi)

    def openIntegracionEBS(self):
        self.appi = tk.Toplevel(self.wind)
        self.addClass = NewIEBS(self.wind, self.appi)

    def openLlamadasmolestosas(self):
        self.appi = tk.Toplevel(self.wind)
        self.addClass = NewLM(self.wind, self.appi)

    def openRellamadas(self):
        self.appi = tk.Toplevel(self.wind)
        self.addClass = NewRL(self.wind, self.appi)

    def openRequerimientosFiscales(self):
        self.appi = tk.Toplevel(self.wind)
        self.addClass = NewRF(self.wind, self.appi)

    def openSMSNotifica(self):
        self.appi = tk.Toplevel(self.wind)
        self.addClass = NewSMSN(self.wind, self.appi)

    def openTallycode(self):
        self.appi = tk.Toplevel(self.wind)
        self.addClass = NewTC(self.wind, self.appi)

    def openTodos(self):
        self.appi = tk.Toplevel(self.wind)
        self.addClass = NewT(self.wind, self.appi)

    def openTR4(self):
        self.appi = tk.Toplevel(self.wind)
        self.addClass = NewTR4(self.wind, self.appi)

    def openwfo(self):
        self.appi = tk.Toplevel(self.wind)
        self.addClass = NewWFO(self.wind, self.appi)

    def openwfoacr(self):
        self.appi = tk.Toplevel(self.wind)
        self.addClass = NewWFOACR(self.wind, self.appi)


class NewAppi(tk.Frame):
    def __init__(self, wind, child, *args, **kwargs):
        tk.Frame.__init__(self, child)
        self.parent = wind
        self.child = child
        self.child.title("App Informativa")

class NewCSMS(tk.Frame):
    def __init__(self, wind, child, *args, **kwargs):
        tk.Frame.__init__(self, child)
        self.parent = wind
        self.child = child
        self.child.title("Callback SMS")

        self.child.focus_set()
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(0, weight=1)
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(1, weight=1)
        self.panelsup = Frame(self.child)
        self.panelsup.grid(column=0, row=0, sticky='nsew')
        self.panelsup.columnconfigure(0, weight=1)
        self.panelsup.rowconfigure(0, weight=1)
        self.panelsup.columnconfigure(1, weight=1)
        self.panelsup.rowconfigure(0, weight=1)

        self.subcuadro11 = LabelFrame(self.panelsup, background='white', text='Registrar Callback SMS Notificacion')

        self.subcuadro11.grid(column=0, row=0, sticky='nsew')

        Label(self.subcuadro11, text='usuario_id: ').grid(row=1, column=0)
        self.entrada1 = Entry(self.subcuadro11)
        self.entrada1.focus()
        self.entrada1.grid(row=1, column=1)

        Label(self.subcuadro11, text='rol_id: ').grid(row=2, column=0)
        self.entrada2 = Entry(self.subcuadro11)
        self.entrada2.focus()
        self.entrada2.grid(row=2, column=1)

        Label(self.subcuadro11, text='login: ').grid(row=3, column=0)
        self.entrada3 = Entry(self.subcuadro11)
        self.entrada3.focus()
        self.entrada3.grid(row=3, column=1)

        Label(self.subcuadro11, text='nombre: ').grid(row=4, column=0)
        self.entrada4 = Entry(self.subcuadro11)
        self.entrada4.focus()
        self.entrada4.grid(row=4, column=1)

        Label(self.subcuadro11, text='estado: ').grid(row=5, column=0)
        self.entrada5 = Entry(self.subcuadro11)
        self.entrada5.focus()
        self.entrada5.grid(row=5, column=1)

        Label(self.subcuadro11, text='abm alta: ').grid(row=6, column=0)
        self.entrada6 = Entry(self.subcuadro11)
        self.entrada6.focus()
        self.entrada6.grid(row=6, column=1)

        Label(self.subcuadro11, text='fecha alta: ').grid(row=7, column=0)
        self.entrada7 = Entry(self.subcuadro11)
        self.entrada7.focus()
        self.entrada7.grid(row=7, column=1)

        Label(self.subcuadro11, text='abm baja: ').grid(row=8, column=0)
        self.entrada8 = Entry(self.subcuadro11)
        self.entrada8.focus()
        self.entrada8.grid(row=8, column=1)

        Label(self.subcuadro11, text='fecha baja: ').grid(row=9, column=0)
        self.entrada9 = Entry(self.subcuadro11)
        self.entrada9.focus()
        self.entrada9.grid(row=9, column=1)

        Label(self.subcuadro11, text='abm quitar: ').grid(row=10, column=0)
        self.entrada10 = Entry(self.subcuadro11)
        self.entrada10.focus()
        self.entrada10.grid(row=10, column=1)

        Label(self.subcuadro11, text='fecha quitar: ').grid(row=11, column=0)
        self.entrada11 = Entry(self.subcuadro11)
        self.entrada11.focus()
        self.entrada11.grid(row=11, column=1)
        # Output Messages
        self.message = Label(self.subcuadro11, text='', fg='red')
        self.message.grid(row=12, column=0, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='Save', command=self.add).grid(row=13, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='DELETE', command=self.delete).grid(row=14, column=0, sticky=W + E)
        ttk.Button(self.subcuadro11, text='EDIT', command=self.edit).grid(row=14, column=1, sticky=W + E)

        self.subcuadro12 = LabelFrame(self.panelsup, background='white', text='Filtro')
        self.subcuadro12.grid(column=1, row=0, sticky='nsew')
        Label(self.subcuadro12, text='Estado: ').grid(row=0, column=0)

        self.search_var = StringVar()
        self.search_var.trace("w", self.update_list)
        self.entry = Entry(self.subcuadro12, textvariable=self.search_var, width=13)
        self.entry.grid(row=0, column=1)

        self.panelinf = Frame(self.child, background='blue')

        self.panelinf.grid(column=0, row=1, sticky='nsew', pady=2)
        self.panelinf.columnconfigure(0, weight=1)
        self.panelinf.rowconfigure(0, weight=1)

        self.tree = ttk.Treeview(self.panelinf)
        self.tree.grid(column=0, row=0, sticky='nsew')
        ladox = Scrollbar(self.panelinf, orient=HORIZONTAL, command=self.tree.xview)
        ladox.grid(column=0, row=1, sticky='ew')

        ladoy = Scrollbar(self.panelinf, orient=VERTICAL, command=self.tree.yview)
        ladoy.grid(column=1, row=0, sticky='ns')

        self.tree.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)

        # Buttons

        self.get_data()
        self.update_list()

    def run_query(self, query, parameters=()):
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()

        cursor.execute(query, parameters)
        column_names = [desc[0] for desc in cursor.description]
        result = cursor.fetchall()
        global dfdb
        dfdb = pd.DataFrame(result, columns=column_names)
        conn.commit()
        cursor.close()

        return dfdb

    def get_data(self):
        # cleaning Table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = 'SELECT * FROM public."callback sms notifica" '
        db_rows = self.run_query(query)
        db_rows['rol_id'] = db_rows['rol_id'].astype('Int64')
        db_rows['usuario_id'] = db_rows['usuario_id'].astype('Int64')

        # filling data
        self.tree['column'] = list(db_rows.columns)
        self.tree['show'] = "headings"
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        for row in db_rows.to_numpy().tolist():
            self.tree.insert('', 0, values=row)

    def add(self):
        if (len(self.entrada1.get()) == 0 or str(self.entrada1.get())=='None'  or str(self.entrada1.get())=='<NA>'):
            entra1 = None
        else:
            entra1 = self.entrada1.get()
        if (len(self.entrada2.get()) == 0 or str(self.entrada2.get())=='None'  or str(self.entrada2.get())=='<NA>'):
            entra2 = None
        else:
            entra2 = self.entrada2.get()
        if (len(self.entrada3.get()) == 0 or str(self.entrada3.get())=='None'  or str(self.entrada3.get())=='<NA>'):
            entra3 = None
        else:
            entra3 = self.entrada3.get()
        if (len(self.entrada4.get()) == 0 or str(self.entrada4.get())=='None'  or str(self.entrada4.get())=='<NA>'):
            entra4 = None
        else:
            entra4 = self.entrada4.get()
        if (len(self.entrada5.get()) == 0 or str(self.entrada5.get())=='None'  or str(self.entrada5.get())=='<NA>'):
            entra5 = None
        else:
            entra5 = self.entrada5.get()
        if (len(self.entrada6.get()) == 0 or str(self.entrada6.get())=='None'  or str(self.entrada6.get())=='<NA>'):
            entra6 = None
        else:
            entra6 = self.entrada6.get()
        if (len(self.entrada7.get()) == 0 or str(self.entrada7.get())=='None'  or str(self.entrada7.get())=='<NA>'):
            entra7 = None
        else:
            entra7 = self.entrada7.get()
        if (len(self.entrada8.get()) == 0 or str(self.entrada8.get())=='None'  or str(self.entrada8.get())=='<NA>'):
            entra8 = None
        else:
            entra8 = self.entrada8.get()
        if (len(self.entrada9.get()) == 0 or str(self.entrada9.get())=='None'  or str(self.entrada9.get())=='<NA>'):
            entra9 = None
        else:
            entra9 = self.entrada9.get()
        if (len(self.entrada10.get()) == 0 or str(self.entrada10.get())=='None'  or str(self.entrada10.get())=='<NA>'):
            entra10 = None
        else:
            entra10 = self.entrada10.get()
        if (len(self.entrada11.get()) == 0 or str(self.entrada11.get())=='None'  or str(self.entrada11.get())=='<NA>'):
            entra11 = None
        else:
            entra11 = self.entrada11.get()

        if( entra5==None or entra3==None):
            self.message['text'] = 'Login y Estado son necesarios'
        else:
            query = """INSERT INTO public."callback sms notifica"(usuario_id, rol_id, login, nombre, estado, "abm alta", "fecha alta", "abm baja", "fecha baja", "abm quitar", "fecha quitar") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            parameters = (entra1,
                      entra2,
                      entra3,
                      entra4,
                      entra5,
                      entra6,
                      entra7,
                      entra8,
                      entra9,
                      entra10,
                      entra11
                      )
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()

            cursor.execute(query, parameters)
            self.entrada1.delete(0, END)
            self.entrada2.delete(0, END)
            self.entrada3.delete(0, END)
            self.entrada4.delete(0, END)
            self.entrada5.delete(0, END)
            self.entrada6.delete(0, END)
            self.entrada7.delete(0, END)
            self.entrada8.delete(0, END)
            self.entrada9.delete(0, END)
            self.entrada10.delete(0, END)
            self.entrada11.delete(0, END)
            conn.commit()
            cursor.close()
            self.get_data()

    def edit(self):

        select = self.tree.item(self.tree.selection())['values']

        self.edit_wind = Toplevel(self.child)
        self.edit_wind.title = 'Edit'

        Label(self.edit_wind, text='usuario_id: ').grid(row=0, column=1)
        new_entrada1 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[0]))
        new_entrada1.grid(row=0, column=2)

        Label(self.edit_wind, text='rol_id: ').grid(row=1, column=1)
        new_entrada2 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[1]))
        new_entrada2.grid(row=1, column=2)

        Label(self.edit_wind, text='login: ').grid(row=2, column=1)
        new_entrada3 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[2]))
        new_entrada3.grid(row=2, column=2)

        Label(self.edit_wind, text='nombre: ').grid(row=3, column=1)
        new_entrada4 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[3]))
        new_entrada4.grid(row=3, column=2)

        Label(self.edit_wind, text='estado: ').grid(row=4, column=1)
        new_entrada5 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[4]))
        new_entrada5.grid(row=4, column=2)

        Label(self.edit_wind, text='abm alta: ').grid(row=5, column=1)
        new_entrada6 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[5]))
        new_entrada6.grid(row=5, column=2)

        Label(self.edit_wind, text='fecha alta: ').grid(row=6, column=1)
        new_entrada7 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[6]))
        new_entrada7.grid(row=6, column=2)

        Label(self.edit_wind, text='abm baja: ').grid(row=7, column=1)
        new_entrada8 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[7]))
        new_entrada8.grid(row=7, column=2)

        Label(self.edit_wind, text='fecha baja: ').grid(row=8, column=1)
        new_entrada9 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[8]))
        new_entrada9.grid(row=8, column=2)

        Label(self.edit_wind, text='abm quitar: ').grid(row=9, column=1)
        new_entrada10 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[9]))
        new_entrada10.grid(row=9, column=2)

        Label(self.edit_wind, text='fecha quitar: ').grid(row=10, column=1)
        new_entrada11 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[10]))
        new_entrada11.grid(row=10, column=2)

        self.messageedit = Label(self.edit_wind, text='', fg='red')
        self.messageedit.grid(row=12, column=0, columnspan=2, sticky=W + E)
        Button(self.edit_wind, text='Actualizar', command=lambda: self.edit_records(new_entrada1.get(),
                                                                                    new_entrada2.get(),
                                                                                    new_entrada3.get(),
                                                                                    new_entrada4.get(),
                                                                                    new_entrada5.get(),
                                                                                    new_entrada6.get(),
                                                                                    new_entrada7.get(),
                                                                                    new_entrada8.get(),
                                                                                    new_entrada9.get(),
                                                                                    new_entrada10.get(),
                                                                                    new_entrada11.get(),
                                                                                    select[0],
                                                                                    select[2]

                                                                                    )).grid(row=12, column=2, sticky=W)

        self.edit_wind.mainloop()

    def edit_records(self, idlogin, idrol, login, nombre, estado, aalta, falta, abaja, fbaja, aquitar, fquitar, idold,
                     loginold):
        if (len(idlogin) == 0 or str(idlogin) == 'None' or str(idlogin) == '<NA>'):
            entra1 = None
        else:
            entra1 = idlogin
        if (len(idrol) == 0 or str(idrol) == 'None' or str(idrol) == '<NA>'):
            entra2 = None
        else:
            entra2 = idrol
        if (len(login) == 0 or str(login) == 'None' or str(login) == '<NA>'):
            entra3 = None
        else:
            entra3 = login
        if (len(nombre) == 0 or str(nombre) == 'None' or str(nombre) == '<NA>'):
            entra4 = None
        else:
            entra4 = nombre
        if (len(estado) == 0 or str(estado) == 'None' or str(estado) == '<NA>'):
            entra5 = None
        else:
            entra5 = estado
        if (len(aalta) == 0 or str(aalta) == 'None' or str(aalta) == '<NA>'):
            entra6 = None
        else:
            entra6 = aalta
        if (len(falta) == 0 or str(falta) == 'None' or str(falta) == '<NA>'):
            entra7 = None
        else:
            entra7 = falta
        if (len(abaja) == 0 or str(abaja) == 'None' or str(abaja) == '<NA>'):
            entra8 = None
        else:
            entra8 = abaja
        if (len(fbaja) == 0 or str(fbaja) == 'None' or str(fbaja) == '<NA>'):
            entra9 = None
        else:
            entra9 = fbaja
        if (len(aquitar) == 0 or str(aquitar) == 'None' or str(
                aquitar) == '<NA>'):
            entra10 = None
        else:
            entra10 = aquitar
        if (len(fquitar) == 0 or str(fquitar) == 'None' or str(
                fquitar) == '<NA>'):
            entra11 = None
        else:
            entra11 = fquitar

        if (entra5 == None and entra3 == None):
            self.messageedit['text'] = 'Login y Estado son necesarios'
        else:
            query = 'UPDATE public."callback sms notifica" SET usuario_id = %s, rol_id= %s, login= %s, nombre = %s, estado= %s, "abm alta"= %s, "fecha alta"= %s, "abm baja"= %s, "fecha baja"= %s, "abm quitar"= %s, "fecha quitar" = %s WHERE usuario_id = %s AND login= %s'
            parameters = (
            entra1, entra2, entra3, entra4, entra5, entra6, entra7, entra8, entra9, entra10, entra11, idold, loginold)
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()
            cursor.execute(query, parameters)
            conn.commit()
            cursor.close()
            self.edit_wind.destroy()

            self.get_data()

    def update_list(self, *args):
        search_term = self.search_var.get()

        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        mask = dfdb['estado'].str.contains(search_term, case=False, na=False)

        self.tree['column'] = list(dfdb[mask].columns)
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        df_fila2 = dfdb[mask].to_numpy().tolist()
        for fila2 in df_fila2:
            self.tree.insert('', 'end', values=fila2)

    def delete(self):
        state = 'f'
        select = self.tree.item(self.tree.selection())['values']
        query = 'UPDATE public."callback sms notifica" SET  estado=%s  WHERE   login= %s'
        parameters = (state, select[2])
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        conn.commit()
        cursor.close()


        self.get_data()


class NewCHVC(tk.Frame):
    def __init__(self, wind, child, *args, **kwargs):
        tk.Frame.__init__(self, child)
        self.parent = wind
        self.child = child
        self.child.title("CallbackHVC")

        self.child.focus_set()
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(0, weight=1)
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(1, weight=1)
        self.panelsup = Frame(self.child)
        self.panelsup.grid(column=0, row=0, sticky='nsew')
        self.panelsup.columnconfigure(0, weight=1)
        self.panelsup.rowconfigure(0, weight=1)
        self.panelsup.columnconfigure(1, weight=1)
        self.panelsup.rowconfigure(0, weight=1)

        self.subcuadro11 = LabelFrame(self.panelsup, background='white', text='CallbackHVC')

        self.subcuadro11.grid(column=0, row=0, sticky='nsew')

        Label(self.subcuadro11, text='ci: ').grid(row=1, column=0)
        self.entrada1 = Entry(self.subcuadro11)
        self.entrada1.focus()
        self.entrada1.grid(row=1, column=1)

        Label(self.subcuadro11, text='carga_hora_id: ').grid(row=2, column=0)
        self.entrada2 = Entry(self.subcuadro11)
        self.entrada2.focus()
        self.entrada2.grid(row=2, column=1)

        Label(self.subcuadro11, text='operador_id: ').grid(row=3, column=0)
        self.entrada3 = Entry(self.subcuadro11)
        self.entrada3.focus()
        self.entrada3.grid(row=3, column=1)

        Label(self.subcuadro11, text='nombre: ').grid(row=4, column=0)
        self.entrada4 = Entry(self.subcuadro11)
        self.entrada4.focus()
        self.entrada4.grid(row=4, column=1)

        Label(self.subcuadro11, text='apellido_paterno: ').grid(row=5, column=0)
        self.entrada5 = Entry(self.subcuadro11)
        self.entrada5.focus()
        self.entrada5.grid(row=5, column=1)

        Label(self.subcuadro11, text='apellido_materno: ').grid(row=6, column=0)
        self.entrada6 = Entry(self.subcuadro11)
        self.entrada6.focus()
        self.entrada6.grid(row=6, column=1)

        Label(self.subcuadro11, text='correo_electronico: ').grid(row=7, column=0)
        self.entrada7 = Entry(self.subcuadro11)
        self.entrada7.focus()
        self.entrada7.grid(row=7, column=1)

        Label(self.subcuadro11, text='login: ').grid(row=8, column=0)
        self.entrada8 = Entry(self.subcuadro11)
        self.entrada8.focus()
        self.entrada8.grid(row=8, column=1)

        Label(self.subcuadro11, text='estado: ').grid(row=9, column=0)
        self.entrada9 = Entry(self.subcuadro11)
        self.entrada9.focus()
        self.entrada9.grid(row=9, column=1)

        Label(self.subcuadro11, text='abm alta: ').grid(row=10, column=0)
        self.entrada10 = Entry(self.subcuadro11)
        self.entrada10.focus()
        self.entrada10.grid(row=10, column=1)

      

        Label(self.subcuadro11, text='fecha alta: ').grid(row=11, column=0)
        self.entrada11 = Entry(self.subcuadro11)
        self.entrada11.focus()
        self.entrada11.grid(row=11, column=1)

        Label(self.subcuadro11, text='abm baja: ').grid(row=12, column=0)
        self.entrada12 = Entry(self.subcuadro11)
        self.entrada12.focus()
        self.entrada12.grid(row=12, column=1)

        Label(self.subcuadro11, text='fecha baja: ').grid(row=13, column=0)
        self.entrada13 = Entry(self.subcuadro11)
        self.entrada13.focus()
        self.entrada13.grid(row=13, column=1)

        Label(self.subcuadro11, text='abm quitar: ').grid(row=14, column=0)
        self.entrada14 = Entry(self.subcuadro11)
        self.entrada14.focus()
        self.entrada14.grid(row=14, column=1)

        Label(self.subcuadro11, text='fecha quitar: ').grid(row=15, column=0)
        self.entrada15 = Entry(self.subcuadro11)
        self.entrada15.focus()
        self.entrada15.grid(row=15, column=1)

        # Output Messages
        self.message = Label(self.subcuadro11, text='', fg='red')
        self.message.grid(row=17, column=0, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='Save', command=self.add).grid(row=18, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='DELETE', command=self.delete).grid(row=19, column=0, sticky=W + E)
        ttk.Button(self.subcuadro11, text='EDIT', command=self.edit).grid(row=19, column=1, sticky=W + E)

        self.subcuadro12 = LabelFrame(self.panelsup, background='white', text='Filtro')
        self.subcuadro12.grid(column=1, row=0, sticky='nsew')
        Label(self.subcuadro12, text='Estado: ').grid(row=0, column=0)

        self.search_var = StringVar()
        self.search_var.trace("w", self.update_list)
        self.entry = Entry(self.subcuadro12, textvariable=self.search_var, width=13)
        self.entry.grid(row=0, column=1)

        self.panelinf = Frame(self.child, background='blue')

        self.panelinf.grid(column=0, row=1, sticky='nsew', pady=2)
        self.panelinf.columnconfigure(0, weight=1)
        self.panelinf.rowconfigure(0, weight=1)

        self.tree = ttk.Treeview(self.panelinf)
        self.tree.grid(column=0, row=0, sticky='nsew')
        ladox = Scrollbar(self.panelinf, orient=HORIZONTAL, command=self.tree.xview)
        ladox.grid(column=0, row=1, sticky='ew')

        ladoy = Scrollbar(self.panelinf, orient=VERTICAL, command=self.tree.yview)
        ladoy.grid(column=1, row=0, sticky='ns')

        self.tree.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)

        # Buttons

        self.get_data()
        self.update_list()

    def run_query(self, query, parameters=()):
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()

        cursor.execute(query, parameters)
        column_names = [desc[0] for desc in cursor.description]
        result = cursor.fetchall()
        global dfdb
        dfdb = pd.DataFrame(result, columns=column_names)
        conn.commit()
        cursor.close()

        return dfdb

    def get_data(self):
        # cleaning Table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = 'SELECT * FROM public.callbackhvc '
        db_rows = self.run_query(query)
        db_rows['carga_hora_id'] = db_rows['carga_hora_id'].astype('Int64')
        db_rows['operador_id'] = db_rows['operador_id'].astype('Int64')

        # filling data
        self.tree['column'] = list(db_rows.columns)
        self.tree['show'] = "headings"
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        for row in db_rows.to_numpy().tolist():
            self.tree.insert('', 0, values=row)

    def add(self):
        if (len(self.entrada1.get()) == 0 or str(self.entrada1.get())=='None'  or str(self.entrada1.get())=='<NA>'):
            entra1 = None
        else:
            entra1 = self.entrada1.get()
        if (len(self.entrada2.get()) == 0 or str(self.entrada2.get())=='None'  or str(self.entrada2.get())=='<NA>'):
            entra2 = None
        else:
            entra2 = self.entrada2.get()
        if (len(self.entrada3.get()) == 0 or str(self.entrada3.get())=='None'  or str(self.entrada3.get())=='<NA>'):
            entra3 = None
        else:
            entra3 = self.entrada3.get()
        if (len(self.entrada4.get()) == 0 or str(self.entrada4.get())=='None'  or str(self.entrada4.get())=='<NA>'):
            entra4 = None
        else:
            entra4 = self.entrada4.get()
        if (len(self.entrada5.get()) == 0 or str(self.entrada5.get())=='None'  or str(self.entrada5.get())=='<NA>'):
            entra5 = None
        else:
            entra5 = self.entrada5.get()
        if (len(self.entrada6.get()) == 0 or str(self.entrada6.get())=='None'  or str(self.entrada6.get())=='<NA>'):
            entra6 = None
        else:
            entra6 = self.entrada6.get()
        if (len(self.entrada7.get()) == 0 or str(self.entrada7.get())=='None'  or str(self.entrada7.get())=='<NA>'):
            entra7 = None
        else:
            entra7 = self.entrada7.get()
        if (len(self.entrada8.get()) == 0 or str(self.entrada8.get())=='None'  or str(self.entrada8.get())=='<NA>'):
            entra8 = None
        else:
            entra8 = self.entrada8.get()
        if (len(self.entrada9.get()) == 0 or str(self.entrada9.get())=='None'  or str(self.entrada9.get())=='<NA>'):
            entra9 = None
        else:
            entra9 = self.entrada9.get()
            
        if (len(self.entrada10.get()) == 0 or str(self.entrada10.get())=='None'  or str(self.entrada10.get())=='<NA>'):
            entra10 = None
        else:
            entra10 = self.entrada10.get()
            
        if (len(self.entrada11.get()) == 0 or str(self.entrada11.get())=='None'  or str(self.entrada11.get())=='<NA>'):
            entra11 = None
        else:
            entra11 = self.entrada11.get()
            
        if (len(self.entrada13.get()) == 0 or str(self.entrada13.get())=='None'  or str(self.entrada13.get())=='<NA>'):
            entra13 = None
        else:
            entra13 = self.entrada13.get()
        if (len(self.entrada12.get()) == 0 or str(self.entrada12.get())=='None'  or str(self.entrada12.get())=='<NA>'):
            entra12 = None
        else:
            entra12 = self.entrada12.get()
        if (len(self.entrada14.get()) == 0 or str(self.entrada14.get())=='None'  or str(self.entrada14.get())=='<NA>'):
            entra14 = None
        else:
            entra14 = self.entrada14.get()
            
        if (len(self.entrada15.get()) == 0 or str(self.entrada15.get())=='None'  or str(self.entrada15.get())=='<NA>'):
            entra15 = None
        else:
            entra15 = self.entrada15.get()
        

        if( entra8==None and entra9==None):
            self.message['text'] = 'Login y Estado son necesarios'
        else:
            query = """INSERT INTO public.callbackhvc(ci, 
            carga_hora_id, 
            operador_id, 
            nombre, 
            apellido_paterno, 
            apellido_materno, 
            correo_electronico,
            login,
            estado,
            "abm alta",
            "fecha alta",
            "abm baja",
            "fecha baja",
            "abm quitar",
            "fecha quitar") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s);"""
            parameters = (entra1,
                      entra2,
                      entra3,
                      entra4,
                      entra5,
                      entra6,
                      entra7,
                      entra8,
                      entra9,
                      entra10,
                      entra11,
                      entra12,
                      entra13,
                      entra14,
                      entra15
                      )
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()

            cursor.execute(query, parameters)
            self.entrada1.delete(0, END)
            self.entrada2.delete(0, END)
            self.entrada3.delete(0, END)
            self.entrada4.delete(0, END)
            self.entrada5.delete(0, END)
            self.entrada6.delete(0, END)
            self.entrada7.delete(0, END)
            self.entrada8.delete(0, END)
            self.entrada9.delete(0, END)
            self.entrada10.delete(0, END)
            self.entrada11.delete(0, END)
            self.entrada12.delete(0, END)
            self.entrada13.delete(0, END)
            self.entrada14.delete(0, END)
            self.entrada15.delete(0, END)
           
            conn.commit()
            cursor.close()
            self.get_data()

    def edit(self):

        select = self.tree.item(self.tree.selection())['values']

        self.edit_wind = Toplevel(self.child)
        self.edit_wind.title = 'Edit'

        Label(self.edit_wind, text='ci: ').grid(row=0, column=1)
        new_entrada1 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[0]))
        new_entrada1.grid(row=0, column=2)

        Label(self.edit_wind, text='carga_hora_id: ').grid(row=1, column=1)
        new_entrada2 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[1]))
        new_entrada2.grid(row=1, column=2)

        Label(self.edit_wind, text='operador_id: ').grid(row=2, column=1)
        new_entrada3 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[2]))
        new_entrada3.grid(row=2, column=2)

        Label(self.edit_wind, text='nombre: ').grid(row=3, column=1)
        new_entrada4 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[3]))
        new_entrada4.grid(row=3, column=2)

        Label(self.edit_wind, text='apellido_paterno: ').grid(row=4, column=1)
        new_entrada5 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[4]))
        new_entrada5.grid(row=4, column=2)

        Label(self.edit_wind, text='apellido_materno: ').grid(row=5, column=1)
        new_entrada6 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[5]))
        new_entrada6.grid(row=5, column=2)

        Label(self.edit_wind, text='correo_electronico: ').grid(row=6, column=1)
        new_entrada7 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[6]))
        new_entrada7.grid(row=6, column=2)

        Label(self.edit_wind, text='login: ').grid(row=7, column=1)
        new_entrada8 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[7]))
        new_entrada8.grid(row=7, column=2)

        Label(self.edit_wind, text='estado: ').grid(row=8, column=1)
        new_entrada9 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[8]))
        new_entrada9.grid(row=8, column=2)

        Label(self.edit_wind, text='abm alta: ').grid(row=9, column=1)
        new_entrada10 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[9]))
        new_entrada10.grid(row=9, column=2)

        Label(self.edit_wind, text='fecha alta: ').grid(row=10, column=1)
        new_entrada11 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[10]))
        new_entrada11.grid(row=10, column=2)
        
        
        Label(self.edit_wind, text='abm baja: ').grid(row=11, column=1)
        new_entrada12 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[11]))
        new_entrada12.grid(row=11, column=2)
        
        Label(self.edit_wind, text='fecha baja: ').grid(row=12, column=1)
        new_entrada13 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[12]))
        new_entrada13.grid(row=12, column=2)
        
        Label(self.edit_wind, text='abm quitar: ').grid(row=13, column=1)
        new_entrada14 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[13]))
        new_entrada14.grid(row=13, column=2)
        
        Label(self.edit_wind, text='fecha quitar: ').grid(row=14, column=1)
        new_entrada15 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[14]))
        new_entrada15.grid(row=14, column=2)
        
    

        self.messageedit = Label(self.edit_wind, text='', fg='red')
        self.messageedit.grid(row=16, column=0, columnspan=2, sticky=W + E)
        Button(self.edit_wind, text='Actualizar', command=lambda: self.edit_records(new_entrada1.get(),
                                                                                    new_entrada2.get(),
                                                                                    new_entrada3.get(),
                                                                                    new_entrada4.get(),
                                                                                    new_entrada5.get(),
                                                                                    new_entrada6.get(),
                                                                                    new_entrada7.get(),
                                                                                    new_entrada8.get(),
                                                                                    new_entrada9.get(),
                                                                                    new_entrada10.get(),
                                                                                    new_entrada11.get(),
                                                                                    new_entrada12.get(),
                                                                                    new_entrada13.get(),
                                                                                    new_entrada14.get(),
                                                                                    new_entrada15.get(),
                                                                                    select[7],
                                                                                    select[8])).grid(row=17, column=2, sticky=W)

        self.edit_wind.mainloop()

    def edit_records(self, 
                     var1,
                     var2,
                     var3,
                     var4,
                     var5,
                     var6,
                     var7,
                     var8,
                     var9,
                     var10,
                     var11,
                     var12,
                     var13,
                     var14,
                     var15,
                     var16,
                     var17
                     ):
        if (len(var1) == 0 or str(var1) == 'None' or str(var1) == '<NA>'):
            entra1 = None
        else:
            entra1 = var1
        if (len(var2) == 0 or str(var2) == 'None' or str(var2) == '<NA>'):
            entra2 = None
        else:
            entra2 = var2
        if (len(var3) == 0 or str(var3) == 'None' or str(var3) == '<NA>'):
            entra3 = None
        else:
            entra3 = var3
        if (len(var4) == 0 or str(var4) == 'None' or str(var4) == '<NA>'):
            entra4 = None
        else:
            entra4 = var4
        if (len(var5) == 0 or str(var5) == 'None' or str(var5) == '<NA>'):
            entra5 = None
        else:
            entra5 = var5
        if (len(var6) == 0 or str(var6) == 'None' or str(var6) == '<NA>'):
            entra6 = None
        else:
            entra6 = var6
        if (len(var7) == 0 or str(var7) == 'None' or str(var7) == '<NA>'):
            entra7 = None
        else:
            entra7 = var7
        if (len(var8) == 0 or str(var8) == 'None' or str(var8) == '<NA>'):
            entra8 = None
        else:
            entra8 = var8
        if (len(var9) == 0 or str(var9) == 'None' or str(var9) == '<NA>'):
            entra9 = None
        else:
            entra9 = var9
        if (len(var10) == 0 or str(var10) == 'None' or str(
                var10) == '<NA>'):
            entra10 = None
        else:
            entra10 = var10
        if (len(var11) == 0 or str(var11) == 'None' or str(
                var11) == '<NA>'):
            entra11 = None
        else:
            entra11 = var11
        if (len(var12) == 0 or str(var12) == 'None' or str(
                var12) == '<NA>'):
            entra12 = None
        else:
            entra12 = var12
        if (len(var13) == 0 or str(var13) == 'None' or str(
                var13) == '<NA>'):
            entra13 = None
        else:
            entra13 = var13
        if (len(var14) == 0 or str(var14) == 'None' or str(
                var14) == '<NA>'):
            entra14 = None
        else:
            entra14 = var14
        if (len(var15) == 0 or str(var15) == 'None' or str(
                var15) == '<NA>'):
            entra15 = None
        else:
            entra15 = var15

        if (entra8 == None or entra9 == None):
            self.messageedit['text'] = 'Login y Estado son necesarios'
        else:
            query = 'UPDATE public.callbackhvc SET ci= %s, carga_hora_id= %s, operador_id= %s, nombre= %s, apellido_paterno= %s, apellido_materno= %s, correo_electronico= %s, login= %s, estado= %s, "abm alta" = %s,"fecha alta" = %s, "abm baja"= %s, "fecha baja"= %s, "abm quitar"= %s, "fecha quitar"= %s WHERE estado = %s AND login= %s'
            parameters = (
            entra1, entra2, entra3, entra4, entra5, entra6, entra7, entra8, entra9, entra10, entra11,
            entra12,
            entra13,
            entra14, 
            entra15,
            var17,var16)
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()
            cursor.execute(query, parameters)
            conn.commit()
            cursor.close()
            self.edit_wind.destroy()

            self.get_data()

    def update_list(self, *args):
        search_term = self.search_var.get()

        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        mask = dfdb['estado'].str.contains(search_term, case=False, na=False)

        self.tree['column'] = list(dfdb[mask].columns)
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        df_fila2 = dfdb[mask].to_numpy().tolist()
        for fila2 in df_fila2:
            self.tree.insert('', 'end', values=fila2)

    def delete(self):

        select = self.tree.item(self.tree.selection())['values']
        query = 'UPDATE public.callbackhvc SET  estado=%s  WHERE   login= %s'
        parameters = ('f',
            select[7])
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        conn.commit()
        cursor.close()


        self.get_data()

class NewCMS17(tk.Frame):
    def __init__(self, wind, child, *args, **kwargs):
        tk.Frame.__init__(self, child)
        self.parent = wind
        self.child = child
        self.child.title("App Informativa")

class NewCMS19(tk.Frame):
   

    def __init__(self, wind, child, *args, **kwargs):
        tk.Frame.__init__(self, child)
        self.parent = wind
        self.child = child
        self.child.title("CMS 19")

        self.child.focus_set()
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(0, weight=1)
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(1, weight=1)
        self.panelsup = Frame(self.child)
        self.panelsup.grid(column=0, row=0, sticky='nsew')
        self.panelsup.columnconfigure(0, weight=1)
        self.panelsup.rowconfigure(0, weight=1)
        self.panelsup.columnconfigure(1, weight=1)
        self.panelsup.rowconfigure(0, weight=1)

        self.subcuadro11 = LabelFrame(self.panelsup, background='white', text='Registrar CMS 19')

        self.subcuadro11.grid(column=0, row=0, sticky='nsew')

        Label(self.subcuadro11, text='campo 1: ').grid(row=1, column=0)
        self.entrada1 = Entry(self.subcuadro11)
        self.entrada1.focus()
        self.entrada1.grid(row=1, column=1)

        Label(self.subcuadro11, text='campo2: ').grid(row=2, column=0)
        self.entrada2 = Entry(self.subcuadro11)
        self.entrada2.focus()
        self.entrada2.grid(row=2, column=1)

        Label(self.subcuadro11, text='campo3: ').grid(row=3, column=0)
        self.entrada3 = Entry(self.subcuadro11)
        self.entrada3.focus()
        self.entrada3.grid(row=3, column=1)

        Label(self.subcuadro11, text='campo4: ').grid(row=4, column=0)
        self.entrada4 = Entry(self.subcuadro11)
        self.entrada4.focus()
        self.entrada4.grid(row=4, column=1)

        Label(self.subcuadro11, text='eh: ').grid(row=5, column=0)
        self.entrada5 = Entry(self.subcuadro11)
        self.entrada5.focus()
        self.entrada5.grid(row=5, column=1)

        Label(self.subcuadro11, text='nombre: ').grid(row=6, column=0)
        self.entrada6 = Entry(self.subcuadro11)
        self.entrada6.focus()
        self.entrada6.grid(row=6, column=1)

        Label(self.subcuadro11, text='campo5: ').grid(row=7, column=0)
        self.entrada7 = Entry(self.subcuadro11)
        self.entrada7.focus()
        self.entrada7.grid(row=7, column=1)

        Label(self.subcuadro11, text='cod avaya: ').grid(row=8, column=0)
        self.entrada8 = Entry(self.subcuadro11)
        self.entrada8.focus()
        self.entrada8.grid(row=8, column=1)

        Label(self.subcuadro11, text='campo6: ').grid(row=9, column=0)
        self.entrada9 = Entry(self.subcuadro11)
        self.entrada9.focus()
        self.entrada9.grid(row=9, column=1)

        Label(self.subcuadro11, text='estado: ').grid(row=10, column=0)
        self.entrada10 = Entry(self.subcuadro11)
        self.entrada10.focus()
        self.entrada10.grid(row=10, column=1)

        Label(self.subcuadro11, text='abm alta: ').grid(row=11, column=0)
        self.entrada11 = Entry(self.subcuadro11)
        self.entrada11.focus()
        self.entrada11.grid(row=11, column=1)

        Label(self.subcuadro11, text='fecha alta: ').grid(row=12, column=0)
        self.entrada12 = Entry(self.subcuadro11)
        self.entrada12.focus()
        self.entrada12.grid(row=12, column=1)

        Label(self.subcuadro11, text='abm baja: ').grid(row=13, column=0)
        self.entrada13 = Entry(self.subcuadro11)
        self.entrada13.focus()
        self.entrada13.grid(row=13, column=1)

        Label(self.subcuadro11, text='fecha baja: ').grid(row=14, column=0)
        self.entrada14 = Entry(self.subcuadro11)
        self.entrada14.focus()
        self.entrada14.grid(row=14, column=1)

        Label(self.subcuadro11, text='abm quitar: ').grid(row=15, column=0)
        self.entrada15 = Entry(self.subcuadro11)
        self.entrada15.focus()
        self.entrada15.grid(row=15, column=1)

        Label(self.subcuadro11, text='fecha quitar: ').grid(row=16, column=0)
        self.entrada16 = Entry(self.subcuadro11)
        self.entrada16.focus()
        self.entrada16.grid(row=16, column=1)
        # Output Messages
        self.message = Label(self.subcuadro11, text='', fg='red')
        self.message.grid(row=17, column=0, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='Save', command=self.add).grid(row=18, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='DELETE', command=self.delete).grid(row=19, column=0, sticky=W + E)
        ttk.Button(self.subcuadro11, text='EDIT', command=self.edit).grid(row=19, column=1, sticky=W + E)

        self.subcuadro12 = LabelFrame(self.panelsup, background='white', text='Filtro')
        self.subcuadro12.grid(column=1, row=0, sticky='nsew')
        Label(self.subcuadro12, text='Estado: ').grid(row=0, column=0)

        self.search_var = StringVar()
        self.search_var.trace("w", self.update_list)
        self.entry = Entry(self.subcuadro12, textvariable=self.search_var, width=13)
        self.entry.grid(row=0, column=1)

        self.panelinf = Frame(self.child, background='blue')

        self.panelinf.grid(column=0, row=1, sticky='nsew', pady=2)
        self.panelinf.columnconfigure(0, weight=1)
        self.panelinf.rowconfigure(0, weight=1)

        self.tree = ttk.Treeview(self.panelinf)
        self.tree.grid(column=0, row=0, sticky='nsew')
        ladox = Scrollbar(self.panelinf, orient=HORIZONTAL, command=self.tree.xview)
        ladox.grid(column=0, row=1, sticky='ew')

        ladoy = Scrollbar(self.panelinf, orient=VERTICAL, command=self.tree.yview)
        ladoy.grid(column=1, row=0, sticky='ns')

        self.tree.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)

        # Buttons

        self.get_data()
        self.update_list()

    def run_query(self, query, parameters=()):
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()

        cursor.execute(query, parameters)
        column_names = [desc[0] for desc in cursor.description]
        result = cursor.fetchall()
        global dfdb
        dfdb = pd.DataFrame(result, columns=column_names)
        conn.commit()
        cursor.close()

        return dfdb

    def get_data(self):
        # cleaning Table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = 'SELECT * FROM public."cms 19"  '
        db_rows = self.run_query(query)
        db_rows['campo 1'] = db_rows['campo 1'].astype('Int64')
        db_rows['cod avaya'] = db_rows['cod avaya'].astype('Int64')
        db_rows['eh'] = db_rows['eh'].astype('Int64')

        # filling data
        self.tree['column'] = list(db_rows.columns)
        self.tree['show'] = "headings"
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        for row in db_rows.to_numpy().tolist():
            self.tree.insert('', 0, values=row)

    def add(self):
        if (len(self.entrada1.get()) == 0 or str(self.entrada1.get())=='None'  or str(self.entrada1.get())=='<NA>'):
            entra1 = None
        else:
            entra1 = self.entrada1.get()
        if (len(self.entrada2.get()) == 0 or str(self.entrada2.get())=='None'  or str(self.entrada2.get())=='<NA>'):
            entra2 = None
        else:
            entra2 = self.entrada2.get()
        if (len(self.entrada3.get()) == 0 or str(self.entrada3.get())=='None'  or str(self.entrada3.get())=='<NA>'):
            entra3 = None
        else:
            entra3 = self.entrada3.get()
        if (len(self.entrada4.get()) == 0 or str(self.entrada4.get())=='None'  or str(self.entrada4.get())=='<NA>'):
            entra4 = None
        else:
            entra4 = self.entrada4.get()
        if (len(self.entrada5.get()) == 0 or str(self.entrada5.get())=='None'  or str(self.entrada5.get())=='<NA>'):
            entra5 = None
        else:
            entra5 = self.entrada5.get()
        if (len(self.entrada6.get()) == 0 or str(self.entrada6.get())=='None'  or str(self.entrada6.get())=='<NA>'):
            entra6 = None
        else:
            entra6 = self.entrada6.get()
        if (len(self.entrada7.get()) == 0 or str(self.entrada7.get())=='None'  or str(self.entrada7.get())=='<NA>'):
            entra7 = None
        else:
            entra7 = self.entrada7.get()
        if (len(self.entrada8.get()) == 0 or str(self.entrada8.get())=='None'  or str(self.entrada8.get())=='<NA>'):
            entra8 = None
        else:
            entra8 = self.entrada8.get()
        if (len(self.entrada9.get()) == 0 or str(self.entrada9.get())=='None'  or str(self.entrada9.get())=='<NA>'):
            entra9 = None
        else:
            entra9 = self.entrada9.get()
        if (len(self.entrada10.get()) == 0 or str(self.entrada10.get())=='None'  or str(self.entrada10.get())=='<NA>'):
            entra10 = None
        else:
            entra10 = self.entrada10.get()
        if (len(self.entrada11.get()) == 0 or str(self.entrada11.get())=='None'  or str(self.entrada11.get())=='<NA>'):
            entra11 = None
        else:
            entra11 = self.entrada11.get()
        if (len(self.entrada12.get()) == 0 or str(self.entrada12.get())=='None'  or str(self.entrada12.get())=='<NA>'):
            entra12 = None
        else:
            entra12 = self.entrada12.get()
        if (len(self.entrada13.get()) == 0 or str(self.entrada13.get())=='None'  or str(self.entrada13.get())=='<NA>'):
            entra13 = None
        else:
            entra13 = self.entrada13.get()
        if (len(self.entrada14.get()) == 0 or str(self.entrada14.get())=='None'  or str(self.entrada14.get())=='<NA>'):
            entra14 = None
        else:
            entra14 = self.entrada14.get()
        if (len(self.entrada15.get()) == 0 or str(self.entrada15.get())=='None'  or str(self.entrada15.get())=='<NA>'):
            entra15 = None
        else:
            entra15 = self.entrada15.get()
        if (len(self.entrada16.get()) == 0 or str(self.entrada16.get())=='None'  or str(self.entrada16.get())=='<NA>'):
            entra16 = None
        else:
            entra16 = self.entrada16.get()

        if( entra5==None and entra10==None):
            self.message['text'] = 'EH y Estado son necesarios'
        else:
            query = """INSERT INTO public."cms 19"(
	                "campo 1", campo2, campo3, campo4, eh, nombre, campo5, "cod avaya", campo6, estado, "abm alta", "fecha alta", "abm baja", "fecha baja", "abm quitar", "fecha quitar")
	                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            parameters = (entra1,
                      entra2,
                      entra3,
                      entra4,
                      entra5,
                      entra6,
                      entra7,
                      entra8,
                      entra9,
                      entra10,
                      entra11,
                      entra12,
                      entra13,
                      entra14,
                      entra15,
                      entra16
                      )
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()

            cursor.execute(query, parameters)
            self.entrada1.delete(0, END)
            self.entrada2.delete(0, END)
            self.entrada3.delete(0, END)
            self.entrada4.delete(0, END)
            self.entrada5.delete(0, END)
            self.entrada6.delete(0, END)
            self.entrada7.delete(0, END)
            self.entrada8.delete(0, END)
            self.entrada9.delete(0, END)
            self.entrada10.delete(0, END)
            self.entrada11.delete(0, END)
            self.entrada12.delete(0, END)
            self.entrada13.delete(0, END)
            self.entrada14.delete(0, END)
            self.entrada15.delete(0, END)
            self.entrada16.delete(0, END)
            conn.commit()
            cursor.close()
            self.get_data()

    def edit(self):

        select = self.tree.item(self.tree.selection())['values']

        self.edit_wind = Toplevel(self.child)
        self.edit_wind.title = 'Edit'

        Label(self.edit_wind, text='campo 1: ').grid(row=0, column=1)
        new_entrada1 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[0]))
        new_entrada1.grid(row=0, column=2)

        Label(self.edit_wind, text='campo2: ').grid(row=1, column=1)
        new_entrada2 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[1]))
        new_entrada2.grid(row=1, column=2)

        Label(self.edit_wind, text='campo3: ').grid(row=2, column=1)
        new_entrada3 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[2]))
        new_entrada3.grid(row=2, column=2)

        Label(self.edit_wind, text='campo4: ').grid(row=3, column=1)
        new_entrada4 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[3]))
        new_entrada4.grid(row=3, column=2)

        Label(self.edit_wind, text='eh: ').grid(row=4, column=1)
        new_entrada5 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[4]))
        new_entrada5.grid(row=4, column=2)

        Label(self.edit_wind, text='nombre: ').grid(row=5, column=1)
        new_entrada6 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[5]))
        new_entrada6.grid(row=5, column=2)

        Label(self.edit_wind, text='campo5: ').grid(row=6, column=1)
        new_entrada7 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[6]))
        new_entrada7.grid(row=6, column=2)

        Label(self.edit_wind, text='cod avaya: ').grid(row=7, column=1)
        new_entrada8 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[7]))
        new_entrada8.grid(row=7, column=2)

        Label(self.edit_wind, text='campo6: ').grid(row=8, column=1)
        new_entrada9 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[8]))
        new_entrada9.grid(row=8, column=2)

        Label(self.edit_wind, text='estado: ').grid(row=9, column=1)
        new_entrada10 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[9]))
        new_entrada10.grid(row=9, column=2)

        Label(self.edit_wind, text='abm alta: ').grid(row=10, column=1)
        new_entrada11 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[10]))
        new_entrada11.grid(row=10, column=2)
        
        Label(self.edit_wind, text='fecha alta: ').grid(row=11, column=1)
        new_entrada12 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[11]))
        new_entrada12.grid(row=11, column=2)
        
        Label(self.edit_wind, text='abm baja: ').grid(row=12, column=1)
        new_entrada13 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[12]))
        new_entrada13.grid(row=12, column=2)
        
        Label(self.edit_wind, text='fecha baja: ').grid(row=13, column=1)
        new_entrada14 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[13]))
        new_entrada14.grid(row=13, column=2)
        
        Label(self.edit_wind, text='abm quitar: ').grid(row=14, column=1)
        new_entrada15 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[14]))
        new_entrada15.grid(row=14, column=2)
        
        Label(self.edit_wind, text='fecha quitar: ').grid(row=15, column=1)
        new_entrada16 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[15]))
        new_entrada16.grid(row=15, column=2)

        self.messageedit = Label(self.edit_wind, text='', fg='red')
        self.messageedit.grid(row=16, column=0, columnspan=2, sticky=W + E)
        Button(self.edit_wind, text='Actualizar', command=lambda: self.edit_records(new_entrada1.get(),
                                                                                    new_entrada2.get(),
                                                                                    new_entrada3.get(),
                                                                                    new_entrada4.get(),
                                                                                    new_entrada5.get(),
                                                                                    new_entrada6.get(),
                                                                                    new_entrada7.get(),
                                                                                    new_entrada8.get(),
                                                                                    new_entrada9.get(),
                                                                                    new_entrada10.get(),
                                                                                    new_entrada11.get(),
                                                                                    new_entrada12.get(),
                                                                                    new_entrada13.get(),
                                                                                    new_entrada14.get(),
                                                                                    new_entrada15.get(),
                                                                                    new_entrada16.get(),
                                                                                    select[4],
                                                                                    select[9]

                                                                                    )).grid(row=17, column=2, sticky=W)

        self.edit_wind.mainloop()

    def edit_records(self, 
                     var1,
                     var2,
                     var3,
                     var4,
                     var5,
                     var6,
                     var7,
                     var8,
                     var9,
                     var10,
                     var11,
                     var12,
                     var13,
                     var14,
                     var15,
                     var16,
                     var17,
                     var18
                     ):
        if (len(var1) == 0 or str(var1) == 'None' or str(var1) == '<NA>'):
            entra1 = None
        else:
            entra1 = var1
        if (len(var2) == 0 or str(var2) == 'None' or str(var2) == '<NA>'):
            entra2 = None
        else:
            entra2 = var2
        if (len(var3) == 0 or str(var3) == 'None' or str(var3) == '<NA>'):
            entra3 = None
        else:
            entra3 = var3
        if (len(var4) == 0 or str(var4) == 'None' or str(var4) == '<NA>'):
            entra4 = None
        else:
            entra4 = var4
        if (len(var5) == 0 or str(var5) == 'None' or str(var5) == '<NA>'):
            entra5 = None
        else:
            entra5 = var5
        if (len(var6) == 0 or str(var6) == 'None' or str(var6) == '<NA>'):
            entra6 = None
        else:
            entra6 = var6
        if (len(var7) == 0 or str(var7) == 'None' or str(var7) == '<NA>'):
            entra7 = None
        else:
            entra7 = var7
        if (len(var8) == 0 or str(var8) == 'None' or str(var8) == '<NA>'):
            entra8 = None
        else:
            entra8 = var8
        if (len(var9) == 0 or str(var9) == 'None' or str(var9) == '<NA>'):
            entra9 = None
        else:
            entra9 = var9
        if (len(var10) == 0 or str(var10) == 'None' or str(
                var10) == '<NA>'):
            entra10 = None
        else:
            entra10 = var10
        if (len(var11) == 0 or str(var11) == 'None' or str(
                var11) == '<NA>'):
            entra11 = None
        else:
            entra11 = var11
        if (len(var12) == 0 or str(var12) == 'None' or str(
                var12) == '<NA>'):
            entra12 = None
        else:
            entra12 = var12
        if (len(var13) == 0 or str(var13) == 'None' or str(
                var13) == '<NA>'):
            entra13 = None
        else:
            entra13 = var13
        if (len(var14) == 0 or str(var14) == 'None' or str(
                var14) == '<NA>'):
            entra14 = None
        else:
            entra14 = var14
        if (len(var15) == 0 or str(var15) == 'None' or str(
                var15) == '<NA>'):
            entra15 = None
        else:
            entra15 = var15
        if (len(var16) == 0 or str(var16) == 'None' or str(
                var16) == '<NA>'):
            entra16 = None
        else:
            entra16 = var16

        if (entra5 == None or entra10 == None):
            self.messageedit['text'] = 'EH y Estado son necesarios'
        else:
            query = 'UPDATE public."cms 19" SET "campo 1"=%s, campo2=%s, campo3=%s, campo4=%s, eh=%s, nombre=%s, campo5=%s, "cod avaya"=%s, campo6=%s, estado=%s, "abm alta"=%s, "fecha alta"=%s, "abm baja"=%s, "fecha baja"=%s, "abm quitar"=%s, "fecha quitar"=%s WHERE estado = %s AND eh= %s'
            parameters = (
            entra1, entra2, entra3, entra4, entra5, entra6, entra7, entra8, entra9, entra10, entra11,
            entra12,
            entra13,
            entra14, 
            entra15,
            entra16,
            var18,var17)
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()
            cursor.execute(query, parameters)
            conn.commit()
            cursor.close()
            self.edit_wind.destroy()

            self.get_data()

    def update_list(self, *args):
        search_term = self.search_var.get()

        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        mask = dfdb['estado'].str.contains(search_term, case=False, na=False)

        self.tree['column'] = list(dfdb[mask].columns)
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        df_fila2 = dfdb[mask].to_numpy().tolist()
        for fila2 in df_fila2:
            self.tree.insert('', 'end', values=fila2)

    def delete(self):

        select = self.tree.item(self.tree.selection())['values']
        query = 'UPDATE public."cms 19" SET  estado=%s  WHERE   eh= %s'
        parameters = ('f',
            select[4])
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        conn.commit()
        cursor.close()


        self.get_data()

class NewIEBS(tk.Frame):
   

    def __init__(self, wind, child, *args, **kwargs):
        tk.Frame.__init__(self, child)
        self.parent = wind
        self.child = child
        self.child.title("Integracion EBS")

        self.child.focus_set()
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(0, weight=1)
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(1, weight=1)
        self.panelsup = Frame(self.child)
        self.panelsup.grid(column=0, row=0, sticky='nsew')
        self.panelsup.columnconfigure(0, weight=1)
        self.panelsup.rowconfigure(0, weight=1)
        self.panelsup.columnconfigure(1, weight=1)
        self.panelsup.rowconfigure(0, weight=1)

        self.subcuadro11 = LabelFrame(self.panelsup, background='white', text='Registrar Integracion EBS')

        self.subcuadro11.grid(column=0, row=0, sticky='nsew')

        Label(self.subcuadro11, text='USUARIO: ').grid(row=1, column=0)
        self.entrada1 = Entry(self.subcuadro11)
        self.entrada1.focus()
        self.entrada1.grid(row=1, column=1)

        Label(self.subcuadro11, text='NOMBRE: ').grid(row=2, column=0)
        self.entrada2 = Entry(self.subcuadro11)
        self.entrada2.focus()
        self.entrada2.grid(row=2, column=1)

        Label(self.subcuadro11, text='ROL: ').grid(row=3, column=0)
        self.entrada3 = Entry(self.subcuadro11)
        self.entrada3.focus()
        self.entrada3.grid(row=3, column=1)

        Label(self.subcuadro11, text='ESTADO: ').grid(row=4, column=0)
        self.entrada4 = Entry(self.subcuadro11)
        self.entrada4.focus()
        self.entrada4.grid(row=4, column=1)

        Label(self.subcuadro11, text='abm alta: ').grid(row=5, column=0)
        self.entrada5 = Entry(self.subcuadro11)
        self.entrada5.focus()
        self.entrada5.grid(row=5, column=1)

        Label(self.subcuadro11, text='fecha alta: ').grid(row=6, column=0)
        self.entrada6 = Entry(self.subcuadro11)
        self.entrada6.focus()
        self.entrada6.grid(row=6, column=1)

        Label(self.subcuadro11, text='abm baja: ').grid(row=7, column=0)
        self.entrada7 = Entry(self.subcuadro11)
        self.entrada7.focus()
        self.entrada7.grid(row=7, column=1)

        Label(self.subcuadro11, text='fecha baja: ').grid(row=8, column=0)
        self.entrada8 = Entry(self.subcuadro11)
        self.entrada8.focus()
        self.entrada8.grid(row=8, column=1)

        Label(self.subcuadro11, text='abm quitar: ').grid(row=9, column=0)
        self.entrada9 = Entry(self.subcuadro11)
        self.entrada9.focus()
        self.entrada9.grid(row=9, column=1)

        Label(self.subcuadro11, text='fecha quitar: ').grid(row=10, column=0)
        self.entrada10 = Entry(self.subcuadro11)
        self.entrada10.focus()
        self.entrada10.grid(row=10, column=1)


        # Output Messages
        self.message = Label(self.subcuadro11, text='', fg='red')
        self.message.grid(row=17, column=0, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='Save', command=self.add).grid(row=18, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='DELETE', command=self.delete).grid(row=19, column=0, sticky=W + E)
        ttk.Button(self.subcuadro11, text='EDIT', command=self.edit).grid(row=19, column=1, sticky=W + E)

        self.subcuadro12 = LabelFrame(self.panelsup, background='white', text='Filtro')
        self.subcuadro12.grid(column=1, row=0, sticky='nsew')
        Label(self.subcuadro12, text='Estado: ').grid(row=0, column=0)

        self.search_var = StringVar()
        self.search_var.trace("w", self.update_list)
        self.entry = Entry(self.subcuadro12, textvariable=self.search_var, width=13)
        self.entry.grid(row=0, column=1)

        self.panelinf = Frame(self.child, background='blue')

        self.panelinf.grid(column=0, row=1, sticky='nsew', pady=2)
        self.panelinf.columnconfigure(0, weight=1)
        self.panelinf.rowconfigure(0, weight=1)

        self.tree = ttk.Treeview(self.panelinf)
        self.tree.grid(column=0, row=0, sticky='nsew')
        ladox = Scrollbar(self.panelinf, orient=HORIZONTAL, command=self.tree.xview)
        ladox.grid(column=0, row=1, sticky='ew')

        ladoy = Scrollbar(self.panelinf, orient=VERTICAL, command=self.tree.yview)
        ladoy.grid(column=1, row=0, sticky='ns')

        self.tree.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)

        # Buttons

        self.get_data()
        self.update_list()

    def run_query(self, query, parameters=()):
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()

        cursor.execute(query, parameters)
        column_names = [desc[0] for desc in cursor.description]
        result = cursor.fetchall()
        global dfdb
        dfdb = pd.DataFrame(result, columns=column_names)
        conn.commit()
        cursor.close()

        return dfdb

    def get_data(self):
        # cleaning Table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = 'SELECT * FROM public."integracion ebs"  '
        db_rows = self.run_query(query)
        
        

        # filling data
        self.tree['column'] = list(db_rows.columns)
        self.tree['show'] = "headings"
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        for row in db_rows.to_numpy().tolist():
            self.tree.insert('', 0, values=row)

    def add(self):
        if (len(self.entrada1.get()) == 0 or str(self.entrada1.get())=='None'  or str(self.entrada1.get())=='<NA>'):
            entra1 = None
        else:
            entra1 = self.entrada1.get()
        if (len(self.entrada2.get()) == 0 or str(self.entrada2.get())=='None'  or str(self.entrada2.get())=='<NA>'):
            entra2 = None
        else:
            entra2 = self.entrada2.get()
        if (len(self.entrada3.get()) == 0 or str(self.entrada3.get())=='None'  or str(self.entrada3.get())=='<NA>'):
            entra3 = None
        else:
            entra3 = self.entrada3.get()
        if (len(self.entrada4.get()) == 0 or str(self.entrada4.get())=='None'  or str(self.entrada4.get())=='<NA>'):
            entra4 = None
        else:
            entra4 = self.entrada4.get()
        if (len(self.entrada5.get()) == 0 or str(self.entrada5.get())=='None'  or str(self.entrada5.get())=='<NA>'):
            entra5 = None
        else:
            entra5 = self.entrada5.get()
        if (len(self.entrada6.get()) == 0 or str(self.entrada6.get())=='None'  or str(self.entrada6.get())=='<NA>'):
            entra6 = None
        else:
            entra6 = self.entrada6.get()
        if (len(self.entrada7.get()) == 0 or str(self.entrada7.get())=='None'  or str(self.entrada7.get())=='<NA>'):
            entra7 = None
        else:
            entra7 = self.entrada7.get()
        if (len(self.entrada8.get()) == 0 or str(self.entrada8.get())=='None'  or str(self.entrada8.get())=='<NA>'):
            entra8 = None
        else:
            entra8 = self.entrada8.get()
        if (len(self.entrada9.get()) == 0 or str(self.entrada9.get())=='None'  or str(self.entrada9.get())=='<NA>'):
            entra9 = None
        else:
            entra9 = self.entrada9.get()
        if (len(self.entrada10.get()) == 0 or str(self.entrada10.get())=='None'  or str(self.entrada9.get())=='<NA>'):
            entra10 = None
        else:
            entra10 = self.entrada10.get()
      

        if( entra1==None or entra4==None):
            self.message['text'] = 'USUARIO y ESTADO son necesarios'
        else:
            query = """INSERT INTO public."integracion ebs"(
	                "USUARIO", "NOMBRE", "ROL", "ESTADO", "abm alta", "fecha alta", "abm baja", "fecha baja", "abm quitar", "fecha quitar")
	                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            parameters = (entra1,
                      entra2,
                      entra3,
                      entra4,
                      entra5,
                      entra6,
                      entra7,
                      entra8,
                      entra9,
                      entra10
                      )
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()

            cursor.execute(query, parameters)
            self.entrada1.delete(0, END)
            self.entrada2.delete(0, END)
            self.entrada3.delete(0, END)
            self.entrada4.delete(0, END)
            self.entrada5.delete(0, END)
            self.entrada6.delete(0, END)
            self.entrada7.delete(0, END)
            self.entrada8.delete(0, END)
            self.entrada9.delete(0, END)
            self.entrada10.delete(0, END)
            
            conn.commit()
            cursor.close()
            self.get_data()

    def edit(self):

        select = self.tree.item(self.tree.selection())['values']

        self.edit_wind = Toplevel(self.child)
        self.edit_wind.title = 'Edit'

        Label(self.edit_wind, text='USUARIO: ').grid(row=0, column=1)
        new_entrada1 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[0]))
        new_entrada1.grid(row=0, column=2)

        Label(self.edit_wind, text='NOMBRE: ').grid(row=1, column=1)
        new_entrada2 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[1]))
        new_entrada2.grid(row=1, column=2)

        Label(self.edit_wind, text='ROL: ').grid(row=2, column=1)
        new_entrada3 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[2]))
        new_entrada3.grid(row=2, column=2)

        Label(self.edit_wind, text='ESTADO: ').grid(row=3, column=1)
        new_entrada4 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[3]))
        new_entrada4.grid(row=3, column=2)

        Label(self.edit_wind, text='abm alta: ').grid(row=4, column=1)
        new_entrada5 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[4]))
        new_entrada5.grid(row=4, column=2)

        Label(self.edit_wind, text='fecha alta: ').grid(row=5, column=1)
        new_entrada6 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[5]))
        new_entrada6.grid(row=5, column=2)

        Label(self.edit_wind, text='abm baja: ').grid(row=6, column=1)
        new_entrada7 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[6]))
        new_entrada7.grid(row=6, column=2)

        Label(self.edit_wind, text='fecha baja: ').grid(row=7, column=1)
        new_entrada8 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[7]))
        new_entrada8.grid(row=7, column=2)

        Label(self.edit_wind, text='abm quitar: ').grid(row=8, column=1)
        new_entrada9 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[8]))
        new_entrada9.grid(row=8, column=2)

        Label(self.edit_wind, text='fecha quitar: ').grid(row=9, column=1)
        new_entrada10 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[9]))
        new_entrada10.grid(row=9, column=2)

        self.messageedit = Label(self.edit_wind, text='', fg='red')
        self.messageedit.grid(row=16, column=0, columnspan=2, sticky=W + E)
        Button(self.edit_wind, text='Actualizar', command=lambda: self.edit_records(new_entrada1.get(),
                                              )).grid(row=17, column=2, sticky=W)

        self.edit_wind.mainloop()

    def edit_records(self, 
                     var1,
                     var2,
                     var3,
                     var4,
                     var5,
                     var6,
                     var7,
                     var8,
                     var9,
                     var10,
                     var11,
                     var12
                     ):
        if (len(var1) == 0 or str(var1) == 'None' or str(var1) == '<NA>'):
            entra1 = None
        else:
            entra1 = var1
        if (len(var2) == 0 or str(var2) == 'None' or str(var2) == '<NA>'):
            entra2 = None
        else:
            entra2 = var2
        if (len(var3) == 0 or str(var3) == 'None' or str(var3) == '<NA>'):
            entra3 = None
        else:
            entra3 = var3
        if (len(var4) == 0 or str(var4) == 'None' or str(var4) == '<NA>'):
            entra4 = None
        else:
            entra4 = var4
        if (len(var5) == 0 or str(var5) == 'None' or str(var5) == '<NA>'):
            entra5 = None
        else:
            entra5 = var5
        if (len(var6) == 0 or str(var6) == 'None' or str(var6) == '<NA>'):
            entra6 = None
        else:
            entra6 = var6
        if (len(var7) == 0 or str(var7) == 'None' or str(var7) == '<NA>'):
            entra7 = None
        else:
            entra7 = var7
        if (len(var8) == 0 or str(var8) == 'None' or str(var8) == '<NA>'):
            entra8 = None
        else:
            entra8 = var8
        if (len(var9) == 0 or str(var9) == 'None' or str(var9) == '<NA>'):
            entra9 = None
        else:
            entra9 = var9
        if (len(var10) == 0 or str(var10) == 'None' or str(
                var10) == '<NA>'):
            entra10 = None
        else:
            entra10 = var10
        if (len(var11) == 0 or str(var11) == 'None' or str(
                var11) == '<NA>'):
            entra11 = None
        else:
            entra11 = var11
        if (len(var12) == 0 or str(var12) == 'None' or str(
                var12) == '<NA>'):
            entra12 = None
        else:
            entra12 = var12
        

        if (entra1 == None or entra4 == None):
            self.messageedit['text'] = 'USUARIO y Estado son necesarios'
        else:
            query = 'UPDATE public."integracion ebs" SET "USUARIO"=%s, "NOMBRE"=%s, "ROL"=%s, "ESTADO"=%s, "abm alta"=%s, "fecha alta"=%s, "abm baja"=%s, "fecha baja"=%s, "abm quitar"=%s, "fecha quitar"=%s WHERE estado = %s AND eh= %s'
            parameters = (
            entra1, entra2, entra3, entra4, entra5, entra6, entra7, entra8, entra9, entra10, entra11,
            entra12)
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()
            cursor.execute(query, parameters)
            conn.commit()
            cursor.close()
            self.edit_wind.destroy()

            self.get_data()

    def update_list(self, *args):
        search_term = self.search_var.get()

        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        mask = dfdb['ESTADO'].str.contains(search_term, case=False, na=False)

        self.tree['column'] = list(dfdb[mask].columns)
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        df_fila2 = dfdb[mask].to_numpy().tolist()
        for fila2 in df_fila2:
            self.tree.insert('', 'end', values=fila2)

    def delete(self):

        select = self.tree.item(self.tree.selection())['values']
        query = 'UPDATE public."integracion ebs" SET  ESTADO=%s  WHERE USUARIO= %s'
        parameters = ('f',
            select[0])
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        conn.commit()
        cursor.close()


        self.get_data()


class NewLM(tk.Frame):
    def __init__(self, wind, child, *args, **kwargs):
        tk.Frame.__init__(self, child)
        self.parent = wind
        self.child = child
        self.child.title("Callback SMS")

        self.child.focus_set()
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(0, weight=1)
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(1, weight=1)
        self.panelsup = Frame(self.child)
        self.panelsup.grid(column=0, row=0, sticky='nsew')
        self.panelsup.columnconfigure(0, weight=1)
        self.panelsup.rowconfigure(0, weight=1)
        self.panelsup.columnconfigure(1, weight=1)
        self.panelsup.rowconfigure(0, weight=1)

        self.subcuadro11 = LabelFrame(self.panelsup, background='white', text='Registrar Callback Llamadas molestosas')

        self.subcuadro11.grid(column=0, row=0, sticky='nsew')

        Label(self.subcuadro11, text='codigo: ').grid(row=1, column=0)
        self.entrada1 = Entry(self.subcuadro11)
        self.entrada1.focus()
        self.entrada1.grid(row=1, column=1)

        Label(self.subcuadro11, text='codigoperfil: ').grid(row=2, column=0)
        self.entrada2 = Entry(self.subcuadro11)
        self.entrada2.focus()
        self.entrada2.grid(row=2, column=1)

        Label(self.subcuadro11, text='nombrecompleto: ').grid(row=3, column=0)
        self.entrada3 = Entry(self.subcuadro11)
        self.entrada3.focus()
        self.entrada3.grid(row=3, column=1)

        Label(self.subcuadro11, text='estado: ').grid(row=4, column=0)
        self.entrada4 = Entry(self.subcuadro11)
        self.entrada4.focus()
        self.entrada4.grid(row=4, column=1)

        Label(self.subcuadro11, text='fechaalta: ').grid(row=5, column=0)
        self.entrada5 = Entry(self.subcuadro11)
        self.entrada5.focus()
        self.entrada5.grid(row=5, column=1)

        Label(self.subcuadro11, text='abm alta: ').grid(row=6, column=0)
        self.entrada6 = Entry(self.subcuadro11)
        self.entrada6.focus()
        self.entrada6.grid(row=6, column=1)

        Label(self.subcuadro11, text='fecha alta: ').grid(row=7, column=0)
        self.entrada7 = Entry(self.subcuadro11)
        self.entrada7.focus()
        self.entrada7.grid(row=7, column=1)

        Label(self.subcuadro11, text='abm baja: ').grid(row=8, column=0)
        self.entrada8 = Entry(self.subcuadro11)
        self.entrada8.focus()
        self.entrada8.grid(row=8, column=1)

        Label(self.subcuadro11, text='fecha baja: ').grid(row=9, column=0)
        self.entrada9 = Entry(self.subcuadro11)
        self.entrada9.focus()
        self.entrada9.grid(row=9, column=1)

        Label(self.subcuadro11, text='abm quitar: ').grid(row=10, column=0)
        self.entrada10 = Entry(self.subcuadro11)
        self.entrada10.focus()
        self.entrada10.grid(row=10, column=1)

        Label(self.subcuadro11, text='fecha quitar: ').grid(row=11, column=0)
        self.entrada11 = Entry(self.subcuadro11)
        self.entrada11.focus()
        self.entrada11.grid(row=11, column=1)
        # Output Messages
        self.message = Label(self.subcuadro11, text='', fg='red')
        self.message.grid(row=12, column=0, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='Save', command=self.add).grid(row=13, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='DELETE', command=self.delete).grid(row=14, column=0, sticky=W + E)
        ttk.Button(self.subcuadro11, text='EDIT', command=self.edit).grid(row=14, column=1, sticky=W + E)

        self.subcuadro12 = LabelFrame(self.panelsup, background='white', text='Filtro')
        self.subcuadro12.grid(column=1, row=0, sticky='nsew')
        Label(self.subcuadro12, text='Estado: ').grid(row=0, column=0)

        self.search_var = StringVar()
        self.search_var.trace("w", self.update_list)
        self.entry = Entry(self.subcuadro12, textvariable=self.search_var, width=13)
        self.entry.grid(row=0, column=1)

        self.panelinf = Frame(self.child, background='blue')

        self.panelinf.grid(column=0, row=1, sticky='nsew', pady=2)
        self.panelinf.columnconfigure(0, weight=1)
        self.panelinf.rowconfigure(0, weight=1)

        self.tree = ttk.Treeview(self.panelinf)
        self.tree.grid(column=0, row=0, sticky='nsew')
        ladox = Scrollbar(self.panelinf, orient=HORIZONTAL, command=self.tree.xview)
        ladox.grid(column=0, row=1, sticky='ew')

        ladoy = Scrollbar(self.panelinf, orient=VERTICAL, command=self.tree.yview)
        ladoy.grid(column=1, row=0, sticky='ns')

        self.tree.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)

        # Buttons

        self.get_data()
        self.update_list()

    def run_query(self, query, parameters=()):
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()

        cursor.execute(query, parameters)
        column_names = [desc[0] for desc in cursor.description]
        result = cursor.fetchall()
        global dfdb
        dfdb = pd.DataFrame(result, columns=column_names)
        conn.commit()
        cursor.close()

        return dfdb

    def get_data(self):
        # cleaning Table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = 'SELECT * FROM public."llamadas molestosas" '
        db_rows = self.run_query(query)
        db_rows['codigoperfil'] = db_rows['codigoperfil'].astype('Int64')
        

        # filling data
        self.tree['column'] = list(db_rows.columns)
        self.tree['show'] = "headings"
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        for row in db_rows.to_numpy().tolist():
            self.tree.insert('', 0, values=row)

    def add(self):
        if (len(self.entrada1.get()) == 0 or str(self.entrada1.get())=='None'  or str(self.entrada1.get())=='<NA>'):
            entra1 = None
        else:
            entra1 = self.entrada1.get()
        if (len(self.entrada2.get()) == 0 or str(self.entrada2.get())=='None'  or str(self.entrada2.get())=='<NA>'):
            entra2 = None
        else:
            entra2 = self.entrada2.get()
        if (len(self.entrada3.get()) == 0 or str(self.entrada3.get())=='None'  or str(self.entrada3.get())=='<NA>'):
            entra3 = None
        else:
            entra3 = self.entrada3.get()
        if (len(self.entrada4.get()) == 0 or str(self.entrada4.get())=='None'  or str(self.entrada4.get())=='<NA>'):
            entra4 = None
        else:
            entra4 = self.entrada4.get()
        if (len(self.entrada5.get()) == 0 or str(self.entrada5.get())=='None'  or str(self.entrada5.get())=='<NA>'):
            entra5 = None
        else:
            entra5 = self.entrada5.get()
        if (len(self.entrada6.get()) == 0 or str(self.entrada6.get())=='None'  or str(self.entrada6.get())=='<NA>'):
            entra6 = None
        else:
            entra6 = self.entrada6.get()
        if (len(self.entrada7.get()) == 0 or str(self.entrada7.get())=='None'  or str(self.entrada7.get())=='<NA>'):
            entra7 = None
        else:
            entra7 = self.entrada7.get()
        if (len(self.entrada8.get()) == 0 or str(self.entrada8.get())=='None'  or str(self.entrada8.get())=='<NA>'):
            entra8 = None
        else:
            entra8 = self.entrada8.get()
        if (len(self.entrada9.get()) == 0 or str(self.entrada9.get())=='None'  or str(self.entrada9.get())=='<NA>'):
            entra9 = None
        else:
            entra9 = self.entrada9.get()
        if (len(self.entrada10.get()) == 0 or str(self.entrada10.get())=='None'  or str(self.entrada10.get())=='<NA>'):
            entra10 = None
        else:
            entra10 = self.entrada10.get()
        if (len(self.entrada11.get()) == 0 or str(self.entrada11.get())=='None'  or str(self.entrada11.get())=='<NA>'):
            entra11 = None
        else:
            entra11 = self.entrada11.get()

        if( entra5==None and entra3==None):
            self.message['text'] = 'Login y Estado son necesarios'
        else:
            query = """INTO public."llamadas molestosas"(
	        codigo, codigoperfil, nombrecompleto, estado, fechaalta, "abm alta", "fecha alta", "abm baja", "fecha baja", "abm quitar", "fecha quitar")
	        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            parameters = (entra1,
                      entra2,
                      entra3,
                      entra4,
                      entra5,
                      entra6,
                      entra7,
                      entra8,
                      entra9,
                      entra10,
                      entra11
                      )
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()

            cursor.execute(query, parameters)
            self.entrada1.delete(0, END)
            self.entrada2.delete(0, END)
            self.entrada3.delete(0, END)
            self.entrada4.delete(0, END)
            self.entrada5.delete(0, END)
            self.entrada6.delete(0, END)
            self.entrada7.delete(0, END)
            self.entrada8.delete(0, END)
            self.entrada9.delete(0, END)
            self.entrada10.delete(0, END)
            self.entrada11.delete(0, END)
            conn.commit()
            cursor.close()
            self.get_data()

    def edit(self):

        select = self.tree.item(self.tree.selection())['values']

        self.edit_wind = Toplevel(self.child)
        self.edit_wind.title = 'Edit'

        Label(self.edit_wind, text='codigo: ').grid(row=0, column=1)
        new_entrada1 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[0]))
        new_entrada1.grid(row=0, column=2)

        Label(self.edit_wind, text='codigoperfil: ').grid(row=1, column=1)
        new_entrada2 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[1]))
        new_entrada2.grid(row=1, column=2)

        Label(self.edit_wind, text='nombrecompleto: ').grid(row=2, column=1)
        new_entrada3 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[2]))
        new_entrada3.grid(row=2, column=2)

        Label(self.edit_wind, text='fechaalta: ').grid(row=3, column=1)
        new_entrada4 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[3]))
        new_entrada4.grid(row=3, column=2)

        Label(self.edit_wind, text='estado: ').grid(row=4, column=1)
        new_entrada5 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[4]))
        new_entrada5.grid(row=4, column=2)

        Label(self.edit_wind, text='abm alta: ').grid(row=5, column=1)
        new_entrada6 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[5]))
        new_entrada6.grid(row=5, column=2)

        Label(self.edit_wind, text='fecha alta: ').grid(row=6, column=1)
        new_entrada7 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[6]))
        new_entrada7.grid(row=6, column=2)

        Label(self.edit_wind, text='abm baja: ').grid(row=7, column=1)
        new_entrada8 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[7]))
        new_entrada8.grid(row=7, column=2)

        Label(self.edit_wind, text='fecha baja: ').grid(row=8, column=1)
        new_entrada9 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[8]))
        new_entrada9.grid(row=8, column=2)

        Label(self.edit_wind, text='abm quitar: ').grid(row=9, column=1)
        new_entrada10 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[9]))
        new_entrada10.grid(row=9, column=2)

        Label(self.edit_wind, text='fecha quitar: ').grid(row=10, column=1)
        new_entrada11 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[10]))
        new_entrada11.grid(row=10, column=2)

        self.messageedit = Label(self.edit_wind, text='', fg='red')
        self.messageedit.grid(row=12, column=0, columnspan=2, sticky=W + E)
        Button(self.edit_wind, text='Actualizar', command=lambda: self.edit_records(new_entrada1.get(),
                                                                                    new_entrada2.get(),
                                                                                    new_entrada3.get(),
                                                                                    new_entrada4.get(),
                                                                                    new_entrada5.get(),
                                                                                    new_entrada6.get(),
                                                                                    new_entrada7.get(),
                                                                                    new_entrada8.get(),
                                                                                    new_entrada9.get(),
                                                                                    new_entrada10.get(),
                                                                                    new_entrada11.get(),
                                                                                    select[1],
                                                                                    select[3]

                                                                                    )).grid(row=12, column=2, sticky=W)

        self.edit_wind.mainloop()

    def edit_records(self, idlogin, idrol, login, nombre, estado, aalta, falta, abaja, fbaja, aquitar, fquitar, idold,
                     loginold):
        if (len(idlogin) == 0 or str(idlogin) == 'None' or str(idlogin) == '<NA>'):
            entra1 = None
        else:
            entra1 = idlogin
        if (len(idrol) == 0 or str(idrol) == 'None' or str(idrol) == '<NA>'):
            entra2 = None
        else:
            entra2 = idrol
        if (len(login) == 0 or str(login) == 'None' or str(login) == '<NA>'):
            entra3 = None
        else:
            entra3 = login
        if (len(nombre) == 0 or str(nombre) == 'None' or str(nombre) == '<NA>'):
            entra4 = None
        else:
            entra4 = nombre
        if (len(estado) == 0 or str(estado) == 'None' or str(estado) == '<NA>'):
            entra5 = None
        else:
            entra5 = estado
        if (len(aalta) == 0 or str(aalta) == 'None' or str(aalta) == '<NA>'):
            entra6 = None
        else:
            entra6 = aalta
        if (len(falta) == 0 or str(falta) == 'None' or str(falta) == '<NA>'):
            entra7 = None
        else:
            entra7 = falta
        if (len(abaja) == 0 or str(abaja) == 'None' or str(abaja) == '<NA>'):
            entra8 = None
        else:
            entra8 = abaja
        if (len(fbaja) == 0 or str(fbaja) == 'None' or str(fbaja) == '<NA>'):
            entra9 = None
        else:
            entra9 = fbaja
        if (len(aquitar) == 0 or str(aquitar) == 'None' or str(
                aquitar) == '<NA>'):
            entra10 = None
        else:
            entra10 = aquitar
        if (len(fquitar) == 0 or str(fquitar) == 'None' or str(
                fquitar) == '<NA>'):
            entra11 = None
        else:
            entra11 = fquitar

        if (entra5 == None and entra3 == None):
            self.messageedit['text'] = 'Login y Estado son necesarios'
        else:
            query = 'UPDATE public."callback sms notifica" SET usuario_id = %s, rol_id= %s, login= %s, nombre = %s, estado= %s, "abm alta"= %s, "fecha alta"= %s, "abm baja"= %s, "fecha baja"= %s, "abm quitar"= %s, "fecha quitar" = %s WHERE usuario_id = %s AND login= %s'
            parameters = (
            entra1, entra2, entra3, entra4, entra5, entra6, entra7, entra8, entra9, entra10, entra11, idold, loginold)
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()
            cursor.execute(query, parameters)
            conn.commit()
            cursor.close()
            self.edit_wind.destroy()

            self.get_data()

    def update_list(self, *args):
        search_term = self.search_var.get()

        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        mask = dfdb['estado'].str.contains(search_term, case=False, na=False)

        self.tree['column'] = list(dfdb[mask].columns)
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        df_fila2 = dfdb[mask].to_numpy().tolist()
        for fila2 in df_fila2:
            self.tree.insert('', 'end', values=fila2)

    def delete(self):

        select = self.tree.item(self.tree.selection())['values']
        query = 'UPDATE public."callback sms notifica" SET  estado='f'  WHERE   login= %s'
        parameters = (
            select[2])
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        conn.commit()
        cursor.close()


        self.get_data()

class NewRL(tk.Frame):
    def __init__(self, wind, child, *args, **kwargs):
        tk.Frame.__init__(self, child)
        self.parent = wind
        self.child = child
        self.child.title("Callback SMS")

        self.child.focus_set()
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(0, weight=1)
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(1, weight=1)
        self.panelsup = Frame(self.child)
        self.panelsup.grid(column=0, row=0, sticky='nsew')
        self.panelsup.columnconfigure(0, weight=1)
        self.panelsup.rowconfigure(0, weight=1)
        self.panelsup.columnconfigure(1, weight=1)
        self.panelsup.rowconfigure(0, weight=1)

        self.subcuadro11 = LabelFrame(self.panelsup, background='white', text='Registrar Callback SMS Notificacion')

        self.subcuadro11.grid(column=0, row=0, sticky='nsew')

        Label(self.subcuadro11, text='usuario_id: ').grid(row=1, column=0)
        self.entrada1 = Entry(self.subcuadro11)
        self.entrada1.focus()
        self.entrada1.grid(row=1, column=1)

        Label(self.subcuadro11, text='rol_id: ').grid(row=2, column=0)
        self.entrada2 = Entry(self.subcuadro11)
        self.entrada2.focus()
        self.entrada2.grid(row=2, column=1)

        Label(self.subcuadro11, text='login: ').grid(row=3, column=0)
        self.entrada3 = Entry(self.subcuadro11)
        self.entrada3.focus()
        self.entrada3.grid(row=3, column=1)

        Label(self.subcuadro11, text='nombre: ').grid(row=4, column=0)
        self.entrada4 = Entry(self.subcuadro11)
        self.entrada4.focus()
        self.entrada4.grid(row=4, column=1)

        Label(self.subcuadro11, text='estado: ').grid(row=5, column=0)
        self.entrada5 = Entry(self.subcuadro11)
        self.entrada5.focus()
        self.entrada5.grid(row=5, column=1)

        Label(self.subcuadro11, text='abm alta: ').grid(row=6, column=0)
        self.entrada6 = Entry(self.subcuadro11)
        self.entrada6.focus()
        self.entrada6.grid(row=6, column=1)

        Label(self.subcuadro11, text='fecha alta: ').grid(row=7, column=0)
        self.entrada7 = Entry(self.subcuadro11)
        self.entrada7.focus()
        self.entrada7.grid(row=7, column=1)

        Label(self.subcuadro11, text='abm baja: ').grid(row=8, column=0)
        self.entrada8 = Entry(self.subcuadro11)
        self.entrada8.focus()
        self.entrada8.grid(row=8, column=1)

        Label(self.subcuadro11, text='fecha baja: ').grid(row=9, column=0)
        self.entrada9 = Entry(self.subcuadro11)
        self.entrada9.focus()
        self.entrada9.grid(row=9, column=1)

        Label(self.subcuadro11, text='abm quitar: ').grid(row=10, column=0)
        self.entrada10 = Entry(self.subcuadro11)
        self.entrada10.focus()
        self.entrada10.grid(row=10, column=1)

        Label(self.subcuadro11, text='fecha quitar: ').grid(row=11, column=0)
        self.entrada11 = Entry(self.subcuadro11)
        self.entrada11.focus()
        self.entrada11.grid(row=11, column=1)
        # Output Messages
        self.message = Label(self.subcuadro11, text='', fg='red')
        self.message.grid(row=12, column=0, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='Save', command=self.add).grid(row=13, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='DELETE').grid(row=14, column=0, sticky=W + E)
        ttk.Button(self.subcuadro11, text='EDIT', command=self.edit).grid(row=14, column=1, sticky=W + E)

        self.subcuadro12 = LabelFrame(self.panelsup, background='white', text='Filtro')
        self.subcuadro12.grid(column=1, row=0, sticky='nsew')
        Label(self.subcuadro12, text='Estado: ').grid(row=0, column=0)

        self.search_var = StringVar()
        self.search_var.trace("w", self.update_list)
        self.entry = Entry(self.subcuadro12, textvariable=self.search_var, width=13)
        self.entry.grid(row=0, column=1)

        self.panelinf = Frame(self.child, background='blue')

        self.panelinf.grid(column=0, row=1, sticky='nsew', pady=2)
        self.panelinf.columnconfigure(0, weight=1)
        self.panelinf.rowconfigure(0, weight=1)

        self.tree = ttk.Treeview(self.panelinf)
        self.tree.grid(column=0, row=0, sticky='nsew')
        ladox = Scrollbar(self.panelinf, orient=HORIZONTAL, command=self.tree.xview)
        ladox.grid(column=0, row=1, sticky='ew')

        ladoy = Scrollbar(self.panelinf, orient=VERTICAL, command=self.tree.yview)
        ladoy.grid(column=1, row=0, sticky='ns')

        self.tree.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)

        # Buttons

        self.get_data()
        self.update_list()

    def run_query(self, query, parameters=()):
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()

        cursor.execute(query, parameters)
        column_names = [desc[0] for desc in cursor.description]
        result = cursor.fetchall()
        global dfdb
        dfdb = pd.DataFrame(result, columns=column_names)
        conn.commit()
        cursor.close()

        return dfdb

    def get_data(self):
        # cleaning Table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = 'SELECT * FROM public."callback sms notifica" '
        db_rows = self.run_query(query)
        db_rows['rol_id'] = db_rows['rol_id'].astype('Int64')
        db_rows['usuario_id'] = db_rows['usuario_id'].astype('Int64')

        # filling data
        self.tree['column'] = list(db_rows.columns)
        self.tree['show'] = "headings"
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        for row in db_rows.to_numpy().tolist():
            self.tree.insert('', 0, values=row)

    def add(self):
        if (len(self.entrada1.get()) == 0 or str(self.entrada1.get())=='None'  or str(self.entrada1.get())=='<NA>'):
            entra1 = None
        else:
            entra1 = self.entrada1.get()
        if (len(self.entrada2.get()) == 0 or str(self.entrada2.get())=='None'  or str(self.entrada2.get())=='<NA>'):
            entra2 = None
        else:
            entra2 = self.entrada2.get()
        if (len(self.entrada3.get()) == 0 or str(self.entrada3.get())=='None'  or str(self.entrada3.get())=='<NA>'):
            entra3 = None
        else:
            entra3 = self.entrada3.get()
        if (len(self.entrada4.get()) == 0 or str(self.entrada4.get())=='None'  or str(self.entrada4.get())=='<NA>'):
            entra4 = None
        else:
            entra4 = self.entrada4.get()
        if (len(self.entrada5.get()) == 0 or str(self.entrada5.get())=='None'  or str(self.entrada5.get())=='<NA>'):
            entra5 = None
        else:
            entra5 = self.entrada5.get()
        if (len(self.entrada6.get()) == 0 or str(self.entrada6.get())=='None'  or str(self.entrada6.get())=='<NA>'):
            entra6 = None
        else:
            entra6 = self.entrada6.get()
        if (len(self.entrada7.get()) == 0 or str(self.entrada7.get())=='None'  or str(self.entrada7.get())=='<NA>'):
            entra7 = None
        else:
            entra7 = self.entrada7.get()
        if (len(self.entrada8.get()) == 0 or str(self.entrada8.get())=='None'  or str(self.entrada8.get())=='<NA>'):
            entra8 = None
        else:
            entra8 = self.entrada8.get()
        if (len(self.entrada9.get()) == 0 or str(self.entrada9.get())=='None'  or str(self.entrada9.get())=='<NA>'):
            entra9 = None
        else:
            entra9 = self.entrada9.get()
        if (len(self.entrada10.get()) == 0 or str(self.entrada10.get())=='None'  or str(self.entrada10.get())=='<NA>'):
            entra10 = None
        else:
            entra10 = self.entrada10.get()
        if (len(self.entrada11.get()) == 0 or str(self.entrada11.get())=='None'  or str(self.entrada11.get())=='<NA>'):
            entra11 = None
        else:
            entra11 = self.entrada11.get()

        if( entra5==None and entra3==None):
            self.message['text'] = 'Login y Estado son necesarios'
        else:
            query = """INSERT INTO public."callback sms notifica"(usuario_id, rol_id, login, nombre, estado, "abm alta", "fecha alta", "abm baja", "fecha baja", "abm quitar", "fecha quitar") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            parameters = (entra1,
                      entra2,
                      entra3,
                      entra4,
                      entra5,
                      entra6,
                      entra7,
                      entra8,
                      entra9,
                      entra10,
                      entra11
                      )
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()

            cursor.execute(query, parameters)
            self.entrada1.delete(0, END)
            self.entrada2.delete(0, END)
            self.entrada3.delete(0, END)
            self.entrada4.delete(0, END)
            self.entrada5.delete(0, END)
            self.entrada6.delete(0, END)
            self.entrada7.delete(0, END)
            self.entrada8.delete(0, END)
            self.entrada9.delete(0, END)
            self.entrada10.delete(0, END)
            self.entrada11.delete(0, END)
            conn.commit()
            cursor.close()
            self.get_data()

    def edit(self):

        select = self.tree.item(self.tree.selection())['values']

        self.edit_wind = Toplevel(self.child)
        self.edit_wind.title = 'Edit'

        Label(self.edit_wind, text='usuario_id: ').grid(row=0, column=1)
        new_entrada1 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[0]))
        new_entrada1.grid(row=0, column=2)

        Label(self.edit_wind, text='rol_id: ').grid(row=1, column=1)
        new_entrada2 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[1]))
        new_entrada2.grid(row=1, column=2)

        Label(self.edit_wind, text='login: ').grid(row=2, column=1)
        new_entrada3 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[2]))
        new_entrada3.grid(row=2, column=2)

        Label(self.edit_wind, text='nombre: ').grid(row=3, column=1)
        new_entrada4 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[3]))
        new_entrada4.grid(row=3, column=2)

        Label(self.edit_wind, text='estado: ').grid(row=4, column=1)
        new_entrada5 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[4]))
        new_entrada5.grid(row=4, column=2)

        Label(self.edit_wind, text='abm alta: ').grid(row=5, column=1)
        new_entrada6 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[5]))
        new_entrada6.grid(row=5, column=2)

        Label(self.edit_wind, text='fecha alta: ').grid(row=6, column=1)
        new_entrada7 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[6]))
        new_entrada7.grid(row=6, column=2)

        Label(self.edit_wind, text='abm baja: ').grid(row=7, column=1)
        new_entrada8 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[7]))
        new_entrada8.grid(row=7, column=2)

        Label(self.edit_wind, text='fecha baja: ').grid(row=8, column=1)
        new_entrada9 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[8]))
        new_entrada9.grid(row=8, column=2)

        Label(self.edit_wind, text='abm quitar: ').grid(row=9, column=1)
        new_entrada10 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[9]))
        new_entrada10.grid(row=9, column=2)

        Label(self.edit_wind, text='fecha quitar: ').grid(row=10, column=1)
        new_entrada11 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[10]))
        new_entrada11.grid(row=10, column=2)

        self.messageedit = Label(self.edit_wind, text='', fg='red')
        self.messageedit.grid(row=12, column=0, columnspan=2, sticky=W + E)
        Button(self.edit_wind, text='Actualizar', command=lambda: self.edit_records(new_entrada1.get(),
                                                                                    new_entrada2.get(),
                                                                                    new_entrada3.get(),
                                                                                    new_entrada4.get(),
                                                                                    new_entrada5.get(),
                                                                                    new_entrada6.get(),
                                                                                    new_entrada7.get(),
                                                                                    new_entrada8.get(),
                                                                                    new_entrada9.get(),
                                                                                    new_entrada10.get(),
                                                                                    new_entrada11.get(),
                                                                                    select[0],
                                                                                    select[2]

                                                                                    )).grid(row=12, column=2, sticky=W)

        self.edit_wind.mainloop()

    def edit_records(self, idlogin, idrol, login, nombre, estado, aalta, falta, abaja, fbaja, aquitar, fquitar, idold,
                     loginold):
        if (len(idlogin) == 0 or str(idlogin) == 'None' or str(idlogin) == '<NA>'):
            entra1 = None
        else:
            entra1 = idlogin
        if (len(idrol) == 0 or str(idrol) == 'None' or str(idrol) == '<NA>'):
            entra2 = None
        else:
            entra2 = idrol
        if (len(login) == 0 or str(login) == 'None' or str(login) == '<NA>'):
            entra3 = None
        else:
            entra3 = login
        if (len(nombre) == 0 or str(nombre) == 'None' or str(nombre) == '<NA>'):
            entra4 = None
        else:
            entra4 = nombre
        if (len(estado) == 0 or str(estado) == 'None' or str(estado) == '<NA>'):
            entra5 = None
        else:
            entra5 = estado
        if (len(aalta) == 0 or str(aalta) == 'None' or str(aalta) == '<NA>'):
            entra6 = None
        else:
            entra6 = aalta
        if (len(falta) == 0 or str(falta) == 'None' or str(falta) == '<NA>'):
            entra7 = None
        else:
            entra7 = falta
        if (len(abaja) == 0 or str(abaja) == 'None' or str(abaja) == '<NA>'):
            entra8 = None
        else:
            entra8 = abaja
        if (len(fbaja) == 0 or str(fbaja) == 'None' or str(fbaja) == '<NA>'):
            entra9 = None
        else:
            entra9 = fbaja
        if (len(aquitar) == 0 or str(aquitar) == 'None' or str(
                aquitar) == '<NA>'):
            entra10 = None
        else:
            entra10 = aquitar
        if (len(fquitar) == 0 or str(fquitar) == 'None' or str(
                fquitar) == '<NA>'):
            entra11 = None
        else:
            entra11 = fquitar

        if (entra5 == None and entra3 == None):
            self.messageedit['text'] = 'Login y Estado son necesarios'
        else:
            query = 'UPDATE public."callback sms notifica" SET usuario_id = %s, rol_id= %s, login= %s, nombre = %s, estado= %s, "abm alta"= %s, "fecha alta"= %s, "abm baja"= %s, "fecha baja"= %s, "abm quitar"= %s, "fecha quitar" = %s WHERE usuario_id = %s AND login= %s'
            parameters = (
            entra1, entra2, entra3, entra4, entra5, entra6, entra7, entra8, entra9, entra10, entra11, idold, loginold)
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()
            cursor.execute(query, parameters)
            conn.commit()
            cursor.close()
            self.edit_wind.destroy()

            self.get_data()

    def update_list(self, *args):
        search_term = self.search_var.get()

        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        mask = dfdb['estado'].str.contains(search_term, case=False, na=False)

        self.tree['column'] = list(dfdb[mask].columns)
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        df_fila2 = dfdb[mask].to_numpy().tolist()
        for fila2 in df_fila2:
            self.tree.insert('', 'end', values=fila2)

    def delete(self):

        select = self.tree.item(self.tree.selection())['values']
        query = 'UPDATE public."callback sms notifica" SET  estado='f'  WHERE   login= %s'
        parameters = (
            select[2])
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        conn.commit()
        cursor.close()


        self.get_data()

class NewRF(tk.Frame):
    def __init__(self, wind, child, *args, **kwargs):
        tk.Frame.__init__(self, child)
        self.parent = wind
        self.child = child
        self.child.title("Callback SMS")

        self.child.focus_set()
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(0, weight=1)
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(1, weight=1)
        self.panelsup = Frame(self.child)
        self.panelsup.grid(column=0, row=0, sticky='nsew')
        self.panelsup.columnconfigure(0, weight=1)
        self.panelsup.rowconfigure(0, weight=1)
        self.panelsup.columnconfigure(1, weight=1)
        self.panelsup.rowconfigure(0, weight=1)

        self.subcuadro11 = LabelFrame(self.panelsup, background='white', text='Registrar Callback SMS Notificacion')

        self.subcuadro11.grid(column=0, row=0, sticky='nsew')

        Label(self.subcuadro11, text='usuario_id: ').grid(row=1, column=0)
        self.entrada1 = Entry(self.subcuadro11)
        self.entrada1.focus()
        self.entrada1.grid(row=1, column=1)

        Label(self.subcuadro11, text='rol_id: ').grid(row=2, column=0)
        self.entrada2 = Entry(self.subcuadro11)
        self.entrada2.focus()
        self.entrada2.grid(row=2, column=1)

        Label(self.subcuadro11, text='login: ').grid(row=3, column=0)
        self.entrada3 = Entry(self.subcuadro11)
        self.entrada3.focus()
        self.entrada3.grid(row=3, column=1)

        Label(self.subcuadro11, text='nombre: ').grid(row=4, column=0)
        self.entrada4 = Entry(self.subcuadro11)
        self.entrada4.focus()
        self.entrada4.grid(row=4, column=1)

        Label(self.subcuadro11, text='estado: ').grid(row=5, column=0)
        self.entrada5 = Entry(self.subcuadro11)
        self.entrada5.focus()
        self.entrada5.grid(row=5, column=1)

        Label(self.subcuadro11, text='abm alta: ').grid(row=6, column=0)
        self.entrada6 = Entry(self.subcuadro11)
        self.entrada6.focus()
        self.entrada6.grid(row=6, column=1)

        Label(self.subcuadro11, text='fecha alta: ').grid(row=7, column=0)
        self.entrada7 = Entry(self.subcuadro11)
        self.entrada7.focus()
        self.entrada7.grid(row=7, column=1)

        Label(self.subcuadro11, text='abm baja: ').grid(row=8, column=0)
        self.entrada8 = Entry(self.subcuadro11)
        self.entrada8.focus()
        self.entrada8.grid(row=8, column=1)

        Label(self.subcuadro11, text='fecha baja: ').grid(row=9, column=0)
        self.entrada9 = Entry(self.subcuadro11)
        self.entrada9.focus()
        self.entrada9.grid(row=9, column=1)

        Label(self.subcuadro11, text='abm quitar: ').grid(row=10, column=0)
        self.entrada10 = Entry(self.subcuadro11)
        self.entrada10.focus()
        self.entrada10.grid(row=10, column=1)

        Label(self.subcuadro11, text='fecha quitar: ').grid(row=11, column=0)
        self.entrada11 = Entry(self.subcuadro11)
        self.entrada11.focus()
        self.entrada11.grid(row=11, column=1)
        # Output Messages
        self.message = Label(self.subcuadro11, text='', fg='red')
        self.message.grid(row=12, column=0, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='Save', command=self.add).grid(row=13, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='DELETE').grid(row=14, column=0, sticky=W + E)
        ttk.Button(self.subcuadro11, text='EDIT', command=self.edit).grid(row=14, column=1, sticky=W + E)

        self.subcuadro12 = LabelFrame(self.panelsup, background='white', text='Filtro')
        self.subcuadro12.grid(column=1, row=0, sticky='nsew')
        Label(self.subcuadro12, text='Estado: ').grid(row=0, column=0)

        self.search_var = StringVar()
        self.search_var.trace("w", self.update_list)
        self.entry = Entry(self.subcuadro12, textvariable=self.search_var, width=13)
        self.entry.grid(row=0, column=1)

        self.panelinf = Frame(self.child, background='blue')

        self.panelinf.grid(column=0, row=1, sticky='nsew', pady=2)
        self.panelinf.columnconfigure(0, weight=1)
        self.panelinf.rowconfigure(0, weight=1)

        self.tree = ttk.Treeview(self.panelinf)
        self.tree.grid(column=0, row=0, sticky='nsew')
        ladox = Scrollbar(self.panelinf, orient=HORIZONTAL, command=self.tree.xview)
        ladox.grid(column=0, row=1, sticky='ew')

        ladoy = Scrollbar(self.panelinf, orient=VERTICAL, command=self.tree.yview)
        ladoy.grid(column=1, row=0, sticky='ns')

        self.tree.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)

        # Buttons

        self.get_data()
        self.update_list()

    def run_query(self, query, parameters=()):
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()

        cursor.execute(query, parameters)
        column_names = [desc[0] for desc in cursor.description]
        result = cursor.fetchall()
        global dfdb
        dfdb = pd.DataFrame(result, columns=column_names)
        conn.commit()
        cursor.close()

        return dfdb

    def get_data(self):
        # cleaning Table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = 'SELECT * FROM public."callback sms notifica" '
        db_rows = self.run_query(query)
        db_rows['rol_id'] = db_rows['rol_id'].astype('Int64')
        db_rows['usuario_id'] = db_rows['usuario_id'].astype('Int64')

        # filling data
        self.tree['column'] = list(db_rows.columns)
        self.tree['show'] = "headings"
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        for row in db_rows.to_numpy().tolist():
            self.tree.insert('', 0, values=row)

    def add(self):
        if (len(self.entrada1.get()) == 0 or str(self.entrada1.get())=='None'  or str(self.entrada1.get())=='<NA>'):
            entra1 = None
        else:
            entra1 = self.entrada1.get()
        if (len(self.entrada2.get()) == 0 or str(self.entrada2.get())=='None'  or str(self.entrada2.get())=='<NA>'):
            entra2 = None
        else:
            entra2 = self.entrada2.get()
        if (len(self.entrada3.get()) == 0 or str(self.entrada3.get())=='None'  or str(self.entrada3.get())=='<NA>'):
            entra3 = None
        else:
            entra3 = self.entrada3.get()
        if (len(self.entrada4.get()) == 0 or str(self.entrada4.get())=='None'  or str(self.entrada4.get())=='<NA>'):
            entra4 = None
        else:
            entra4 = self.entrada4.get()
        if (len(self.entrada5.get()) == 0 or str(self.entrada5.get())=='None'  or str(self.entrada5.get())=='<NA>'):
            entra5 = None
        else:
            entra5 = self.entrada5.get()
        if (len(self.entrada6.get()) == 0 or str(self.entrada6.get())=='None'  or str(self.entrada6.get())=='<NA>'):
            entra6 = None
        else:
            entra6 = self.entrada6.get()
        if (len(self.entrada7.get()) == 0 or str(self.entrada7.get())=='None'  or str(self.entrada7.get())=='<NA>'):
            entra7 = None
        else:
            entra7 = self.entrada7.get()
        if (len(self.entrada8.get()) == 0 or str(self.entrada8.get())=='None'  or str(self.entrada8.get())=='<NA>'):
            entra8 = None
        else:
            entra8 = self.entrada8.get()
        if (len(self.entrada9.get()) == 0 or str(self.entrada9.get())=='None'  or str(self.entrada9.get())=='<NA>'):
            entra9 = None
        else:
            entra9 = self.entrada9.get()
        if (len(self.entrada10.get()) == 0 or str(self.entrada10.get())=='None'  or str(self.entrada10.get())=='<NA>'):
            entra10 = None
        else:
            entra10 = self.entrada10.get()
        if (len(self.entrada11.get()) == 0 or str(self.entrada11.get())=='None'  or str(self.entrada11.get())=='<NA>'):
            entra11 = None
        else:
            entra11 = self.entrada11.get()

        if( entra5==None and entra3==None):
            self.message['text'] = 'Login y Estado son necesarios'
        else:
            query = """INSERT INTO public."callback sms notifica"(usuario_id, rol_id, login, nombre, estado, "abm alta", "fecha alta", "abm baja", "fecha baja", "abm quitar", "fecha quitar") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            parameters = (entra1,
                      entra2,
                      entra3,
                      entra4,
                      entra5,
                      entra6,
                      entra7,
                      entra8,
                      entra9,
                      entra10,
                      entra11
                      )
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()

            cursor.execute(query, parameters)
            self.entrada1.delete(0, END)
            self.entrada2.delete(0, END)
            self.entrada3.delete(0, END)
            self.entrada4.delete(0, END)
            self.entrada5.delete(0, END)
            self.entrada6.delete(0, END)
            self.entrada7.delete(0, END)
            self.entrada8.delete(0, END)
            self.entrada9.delete(0, END)
            self.entrada10.delete(0, END)
            self.entrada11.delete(0, END)
            conn.commit()
            cursor.close()
            self.get_data()

    def edit(self):

        select = self.tree.item(self.tree.selection())['values']

        self.edit_wind = Toplevel(self.child)
        self.edit_wind.title = 'Edit'

        Label(self.edit_wind, text='usuario_id: ').grid(row=0, column=1)
        new_entrada1 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[0]))
        new_entrada1.grid(row=0, column=2)

        Label(self.edit_wind, text='rol_id: ').grid(row=1, column=1)
        new_entrada2 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[1]))
        new_entrada2.grid(row=1, column=2)

        Label(self.edit_wind, text='login: ').grid(row=2, column=1)
        new_entrada3 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[2]))
        new_entrada3.grid(row=2, column=2)

        Label(self.edit_wind, text='nombre: ').grid(row=3, column=1)
        new_entrada4 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[3]))
        new_entrada4.grid(row=3, column=2)

        Label(self.edit_wind, text='estado: ').grid(row=4, column=1)
        new_entrada5 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[4]))
        new_entrada5.grid(row=4, column=2)

        Label(self.edit_wind, text='abm alta: ').grid(row=5, column=1)
        new_entrada6 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[5]))
        new_entrada6.grid(row=5, column=2)

        Label(self.edit_wind, text='fecha alta: ').grid(row=6, column=1)
        new_entrada7 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[6]))
        new_entrada7.grid(row=6, column=2)

        Label(self.edit_wind, text='abm baja: ').grid(row=7, column=1)
        new_entrada8 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[7]))
        new_entrada8.grid(row=7, column=2)

        Label(self.edit_wind, text='fecha baja: ').grid(row=8, column=1)
        new_entrada9 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[8]))
        new_entrada9.grid(row=8, column=2)

        Label(self.edit_wind, text='abm quitar: ').grid(row=9, column=1)
        new_entrada10 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[9]))
        new_entrada10.grid(row=9, column=2)

        Label(self.edit_wind, text='fecha quitar: ').grid(row=10, column=1)
        new_entrada11 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[10]))
        new_entrada11.grid(row=10, column=2)

        self.messageedit = Label(self.edit_wind, text='', fg='red')
        self.messageedit.grid(row=12, column=0, columnspan=2, sticky=W + E)
        Button(self.edit_wind, text='Actualizar', command=lambda: self.edit_records(new_entrada1.get(),
                                                                                    new_entrada2.get(),
                                                                                    new_entrada3.get(),
                                                                                    new_entrada4.get(),
                                                                                    new_entrada5.get(),
                                                                                    new_entrada6.get(),
                                                                                    new_entrada7.get(),
                                                                                    new_entrada8.get(),
                                                                                    new_entrada9.get(),
                                                                                    new_entrada10.get(),
                                                                                    new_entrada11.get(),
                                                                                    select[0],
                                                                                    select[2]

                                                                                    )).grid(row=12, column=2, sticky=W)

        self.edit_wind.mainloop()

    def edit_records(self, idlogin, idrol, login, nombre, estado, aalta, falta, abaja, fbaja, aquitar, fquitar, idold,
                     loginold):
        if (len(idlogin) == 0 or str(idlogin) == 'None' or str(idlogin) == '<NA>'):
            entra1 = None
        else:
            entra1 = idlogin
        if (len(idrol) == 0 or str(idrol) == 'None' or str(idrol) == '<NA>'):
            entra2 = None
        else:
            entra2 = idrol
        if (len(login) == 0 or str(login) == 'None' or str(login) == '<NA>'):
            entra3 = None
        else:
            entra3 = login
        if (len(nombre) == 0 or str(nombre) == 'None' or str(nombre) == '<NA>'):
            entra4 = None
        else:
            entra4 = nombre
        if (len(estado) == 0 or str(estado) == 'None' or str(estado) == '<NA>'):
            entra5 = None
        else:
            entra5 = estado
        if (len(aalta) == 0 or str(aalta) == 'None' or str(aalta) == '<NA>'):
            entra6 = None
        else:
            entra6 = aalta
        if (len(falta) == 0 or str(falta) == 'None' or str(falta) == '<NA>'):
            entra7 = None
        else:
            entra7 = falta
        if (len(abaja) == 0 or str(abaja) == 'None' or str(abaja) == '<NA>'):
            entra8 = None
        else:
            entra8 = abaja
        if (len(fbaja) == 0 or str(fbaja) == 'None' or str(fbaja) == '<NA>'):
            entra9 = None
        else:
            entra9 = fbaja
        if (len(aquitar) == 0 or str(aquitar) == 'None' or str(
                aquitar) == '<NA>'):
            entra10 = None
        else:
            entra10 = aquitar
        if (len(fquitar) == 0 or str(fquitar) == 'None' or str(
                fquitar) == '<NA>'):
            entra11 = None
        else:
            entra11 = fquitar

        if (entra5 == None and entra3 == None):
            self.messageedit['text'] = 'Login y Estado son necesarios'
        else:
            query = 'UPDATE public."callback sms notifica" SET usuario_id = %s, rol_id= %s, login= %s, nombre = %s, estado= %s, "abm alta"= %s, "fecha alta"= %s, "abm baja"= %s, "fecha baja"= %s, "abm quitar"= %s, "fecha quitar" = %s WHERE usuario_id = %s AND login= %s'
            parameters = (
            entra1, entra2, entra3, entra4, entra5, entra6, entra7, entra8, entra9, entra10, entra11, idold, loginold)
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()
            cursor.execute(query, parameters)
            conn.commit()
            cursor.close()
            self.edit_wind.destroy()

            self.get_data()

    def update_list(self, *args):
        search_term = self.search_var.get()

        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        mask = dfdb['estado'].str.contains(search_term, case=False, na=False)

        self.tree['column'] = list(dfdb[mask].columns)
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        df_fila2 = dfdb[mask].to_numpy().tolist()
        for fila2 in df_fila2:
            self.tree.insert('', 'end', values=fila2)

    def delete(self):

        select = self.tree.item(self.tree.selection())['values']
        query = 'UPDATE public."callback sms notifica" SET  estado='f'  WHERE   login= %s'
        parameters = (
            select[2])
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        conn.commit()
        cursor.close()


        self.get_data()

class NewSMSN(tk.Frame):
    def __init__(self, wind, child, *args, **kwargs):
        tk.Frame.__init__(self, child)
        self.parent = wind
        self.child = child
        self.child.title("Callback SMS")

        self.child.focus_set()
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(0, weight=1)
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(1, weight=1)
        self.panelsup = Frame(self.child)
        self.panelsup.grid(column=0, row=0, sticky='nsew')
        self.panelsup.columnconfigure(0, weight=1)
        self.panelsup.rowconfigure(0, weight=1)
        self.panelsup.columnconfigure(1, weight=1)
        self.panelsup.rowconfigure(0, weight=1)

        self.subcuadro11 = LabelFrame(self.panelsup, background='white', text='Registrar Callback SMS Notificacion')

        self.subcuadro11.grid(column=0, row=0, sticky='nsew')

        Label(self.subcuadro11, text='usuario_id: ').grid(row=1, column=0)
        self.entrada1 = Entry(self.subcuadro11)
        self.entrada1.focus()
        self.entrada1.grid(row=1, column=1)

        Label(self.subcuadro11, text='rol_id: ').grid(row=2, column=0)
        self.entrada2 = Entry(self.subcuadro11)
        self.entrada2.focus()
        self.entrada2.grid(row=2, column=1)

        Label(self.subcuadro11, text='login: ').grid(row=3, column=0)
        self.entrada3 = Entry(self.subcuadro11)
        self.entrada3.focus()
        self.entrada3.grid(row=3, column=1)

        Label(self.subcuadro11, text='nombre: ').grid(row=4, column=0)
        self.entrada4 = Entry(self.subcuadro11)
        self.entrada4.focus()
        self.entrada4.grid(row=4, column=1)

        Label(self.subcuadro11, text='estado: ').grid(row=5, column=0)
        self.entrada5 = Entry(self.subcuadro11)
        self.entrada5.focus()
        self.entrada5.grid(row=5, column=1)

        Label(self.subcuadro11, text='abm alta: ').grid(row=6, column=0)
        self.entrada6 = Entry(self.subcuadro11)
        self.entrada6.focus()
        self.entrada6.grid(row=6, column=1)

        Label(self.subcuadro11, text='fecha alta: ').grid(row=7, column=0)
        self.entrada7 = Entry(self.subcuadro11)
        self.entrada7.focus()
        self.entrada7.grid(row=7, column=1)

        Label(self.subcuadro11, text='abm baja: ').grid(row=8, column=0)
        self.entrada8 = Entry(self.subcuadro11)
        self.entrada8.focus()
        self.entrada8.grid(row=8, column=1)

        Label(self.subcuadro11, text='fecha baja: ').grid(row=9, column=0)
        self.entrada9 = Entry(self.subcuadro11)
        self.entrada9.focus()
        self.entrada9.grid(row=9, column=1)

        Label(self.subcuadro11, text='abm quitar: ').grid(row=10, column=0)
        self.entrada10 = Entry(self.subcuadro11)
        self.entrada10.focus()
        self.entrada10.grid(row=10, column=1)

        Label(self.subcuadro11, text='fecha quitar: ').grid(row=11, column=0)
        self.entrada11 = Entry(self.subcuadro11)
        self.entrada11.focus()
        self.entrada11.grid(row=11, column=1)
        # Output Messages
        self.message = Label(self.subcuadro11, text='', fg='red')
        self.message.grid(row=12, column=0, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='Save', command=self.add).grid(row=13, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='DELETE').grid(row=14, column=0, sticky=W + E)
        ttk.Button(self.subcuadro11, text='EDIT', command=self.edit).grid(row=14, column=1, sticky=W + E)

        self.subcuadro12 = LabelFrame(self.panelsup, background='white', text='Filtro')
        self.subcuadro12.grid(column=1, row=0, sticky='nsew')
        Label(self.subcuadro12, text='Estado: ').grid(row=0, column=0)

        self.search_var = StringVar()
        self.search_var.trace("w", self.update_list)
        self.entry = Entry(self.subcuadro12, textvariable=self.search_var, width=13)
        self.entry.grid(row=0, column=1)

        self.panelinf = Frame(self.child, background='blue')

        self.panelinf.grid(column=0, row=1, sticky='nsew', pady=2)
        self.panelinf.columnconfigure(0, weight=1)
        self.panelinf.rowconfigure(0, weight=1)

        self.tree = ttk.Treeview(self.panelinf)
        self.tree.grid(column=0, row=0, sticky='nsew')
        ladox = Scrollbar(self.panelinf, orient=HORIZONTAL, command=self.tree.xview)
        ladox.grid(column=0, row=1, sticky='ew')

        ladoy = Scrollbar(self.panelinf, orient=VERTICAL, command=self.tree.yview)
        ladoy.grid(column=1, row=0, sticky='ns')

        self.tree.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)

        # Buttons

        self.get_data()
        self.update_list()

    def run_query(self, query, parameters=()):
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()

        cursor.execute(query, parameters)
        column_names = [desc[0] for desc in cursor.description]
        result = cursor.fetchall()
        global dfdb
        dfdb = pd.DataFrame(result, columns=column_names)
        conn.commit()
        cursor.close()

        return dfdb

    def get_data(self):
        # cleaning Table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = 'SELECT * FROM public."callback sms notifica" '
        db_rows = self.run_query(query)
        db_rows['rol_id'] = db_rows['rol_id'].astype('Int64')
        db_rows['usuario_id'] = db_rows['usuario_id'].astype('Int64')

        # filling data
        self.tree['column'] = list(db_rows.columns)
        self.tree['show'] = "headings"
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        for row in db_rows.to_numpy().tolist():
            self.tree.insert('', 0, values=row)

    def add(self):
        if (len(self.entrada1.get()) == 0 or str(self.entrada1.get())=='None'  or str(self.entrada1.get())=='<NA>'):
            entra1 = None
        else:
            entra1 = self.entrada1.get()
        if (len(self.entrada2.get()) == 0 or str(self.entrada2.get())=='None'  or str(self.entrada2.get())=='<NA>'):
            entra2 = None
        else:
            entra2 = self.entrada2.get()
        if (len(self.entrada3.get()) == 0 or str(self.entrada3.get())=='None'  or str(self.entrada3.get())=='<NA>'):
            entra3 = None
        else:
            entra3 = self.entrada3.get()
        if (len(self.entrada4.get()) == 0 or str(self.entrada4.get())=='None'  or str(self.entrada4.get())=='<NA>'):
            entra4 = None
        else:
            entra4 = self.entrada4.get()
        if (len(self.entrada5.get()) == 0 or str(self.entrada5.get())=='None'  or str(self.entrada5.get())=='<NA>'):
            entra5 = None
        else:
            entra5 = self.entrada5.get()
        if (len(self.entrada6.get()) == 0 or str(self.entrada6.get())=='None'  or str(self.entrada6.get())=='<NA>'):
            entra6 = None
        else:
            entra6 = self.entrada6.get()
        if (len(self.entrada7.get()) == 0 or str(self.entrada7.get())=='None'  or str(self.entrada7.get())=='<NA>'):
            entra7 = None
        else:
            entra7 = self.entrada7.get()
        if (len(self.entrada8.get()) == 0 or str(self.entrada8.get())=='None'  or str(self.entrada8.get())=='<NA>'):
            entra8 = None
        else:
            entra8 = self.entrada8.get()
        if (len(self.entrada9.get()) == 0 or str(self.entrada9.get())=='None'  or str(self.entrada9.get())=='<NA>'):
            entra9 = None
        else:
            entra9 = self.entrada9.get()
        if (len(self.entrada10.get()) == 0 or str(self.entrada10.get())=='None'  or str(self.entrada10.get())=='<NA>'):
            entra10 = None
        else:
            entra10 = self.entrada10.get()
        if (len(self.entrada11.get()) == 0 or str(self.entrada11.get())=='None'  or str(self.entrada11.get())=='<NA>'):
            entra11 = None
        else:
            entra11 = self.entrada11.get()

        if( entra5==None and entra3==None):
            self.message['text'] = 'Login y Estado son necesarios'
        else:
            query = """INSERT INTO public."callback sms notifica"(usuario_id, rol_id, login, nombre, estado, "abm alta", "fecha alta", "abm baja", "fecha baja", "abm quitar", "fecha quitar") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            parameters = (entra1,
                      entra2,
                      entra3,
                      entra4,
                      entra5,
                      entra6,
                      entra7,
                      entra8,
                      entra9,
                      entra10,
                      entra11
                      )
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()

            cursor.execute(query, parameters)
            self.entrada1.delete(0, END)
            self.entrada2.delete(0, END)
            self.entrada3.delete(0, END)
            self.entrada4.delete(0, END)
            self.entrada5.delete(0, END)
            self.entrada6.delete(0, END)
            self.entrada7.delete(0, END)
            self.entrada8.delete(0, END)
            self.entrada9.delete(0, END)
            self.entrada10.delete(0, END)
            self.entrada11.delete(0, END)
            conn.commit()
            cursor.close()
            self.get_data()

    def edit(self):

        select = self.tree.item(self.tree.selection())['values']

        self.edit_wind = Toplevel(self.child)
        self.edit_wind.title = 'Edit'

        Label(self.edit_wind, text='usuario_id: ').grid(row=0, column=1)
        new_entrada1 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[0]))
        new_entrada1.grid(row=0, column=2)

        Label(self.edit_wind, text='rol_id: ').grid(row=1, column=1)
        new_entrada2 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[1]))
        new_entrada2.grid(row=1, column=2)

        Label(self.edit_wind, text='login: ').grid(row=2, column=1)
        new_entrada3 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[2]))
        new_entrada3.grid(row=2, column=2)

        Label(self.edit_wind, text='nombre: ').grid(row=3, column=1)
        new_entrada4 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[3]))
        new_entrada4.grid(row=3, column=2)

        Label(self.edit_wind, text='estado: ').grid(row=4, column=1)
        new_entrada5 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[4]))
        new_entrada5.grid(row=4, column=2)

        Label(self.edit_wind, text='abm alta: ').grid(row=5, column=1)
        new_entrada6 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[5]))
        new_entrada6.grid(row=5, column=2)

        Label(self.edit_wind, text='fecha alta: ').grid(row=6, column=1)
        new_entrada7 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[6]))
        new_entrada7.grid(row=6, column=2)

        Label(self.edit_wind, text='abm baja: ').grid(row=7, column=1)
        new_entrada8 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[7]))
        new_entrada8.grid(row=7, column=2)

        Label(self.edit_wind, text='fecha baja: ').grid(row=8, column=1)
        new_entrada9 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[8]))
        new_entrada9.grid(row=8, column=2)

        Label(self.edit_wind, text='abm quitar: ').grid(row=9, column=1)
        new_entrada10 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[9]))
        new_entrada10.grid(row=9, column=2)

        Label(self.edit_wind, text='fecha quitar: ').grid(row=10, column=1)
        new_entrada11 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[10]))
        new_entrada11.grid(row=10, column=2)

        self.messageedit = Label(self.edit_wind, text='', fg='red')
        self.messageedit.grid(row=12, column=0, columnspan=2, sticky=W + E)
        Button(self.edit_wind, text='Actualizar', command=lambda: self.edit_records(new_entrada1.get(),
                                                                                    new_entrada2.get(),
                                                                                    new_entrada3.get(),
                                                                                    new_entrada4.get(),
                                                                                    new_entrada5.get(),
                                                                                    new_entrada6.get(),
                                                                                    new_entrada7.get(),
                                                                                    new_entrada8.get(),
                                                                                    new_entrada9.get(),
                                                                                    new_entrada10.get(),
                                                                                    new_entrada11.get(),
                                                                                    select[0],
                                                                                    select[2]

                                                                                    )).grid(row=12, column=2, sticky=W)

        self.edit_wind.mainloop()

    def edit_records(self, idlogin, idrol, login, nombre, estado, aalta, falta, abaja, fbaja, aquitar, fquitar, idold,
                     loginold):
        if (len(idlogin) == 0 or str(idlogin) == 'None' or str(idlogin) == '<NA>'):
            entra1 = None
        else:
            entra1 = idlogin
        if (len(idrol) == 0 or str(idrol) == 'None' or str(idrol) == '<NA>'):
            entra2 = None
        else:
            entra2 = idrol
        if (len(login) == 0 or str(login) == 'None' or str(login) == '<NA>'):
            entra3 = None
        else:
            entra3 = login
        if (len(nombre) == 0 or str(nombre) == 'None' or str(nombre) == '<NA>'):
            entra4 = None
        else:
            entra4 = nombre
        if (len(estado) == 0 or str(estado) == 'None' or str(estado) == '<NA>'):
            entra5 = None
        else:
            entra5 = estado
        if (len(aalta) == 0 or str(aalta) == 'None' or str(aalta) == '<NA>'):
            entra6 = None
        else:
            entra6 = aalta
        if (len(falta) == 0 or str(falta) == 'None' or str(falta) == '<NA>'):
            entra7 = None
        else:
            entra7 = falta
        if (len(abaja) == 0 or str(abaja) == 'None' or str(abaja) == '<NA>'):
            entra8 = None
        else:
            entra8 = abaja
        if (len(fbaja) == 0 or str(fbaja) == 'None' or str(fbaja) == '<NA>'):
            entra9 = None
        else:
            entra9 = fbaja
        if (len(aquitar) == 0 or str(aquitar) == 'None' or str(
                aquitar) == '<NA>'):
            entra10 = None
        else:
            entra10 = aquitar
        if (len(fquitar) == 0 or str(fquitar) == 'None' or str(
                fquitar) == '<NA>'):
            entra11 = None
        else:
            entra11 = fquitar

        if (entra5 == None and entra3 == None):
            self.messageedit['text'] = 'Login y Estado son necesarios'
        else:
            query = 'UPDATE public."callback sms notifica" SET usuario_id = %s, rol_id= %s, login= %s, nombre = %s, estado= %s, "abm alta"= %s, "fecha alta"= %s, "abm baja"= %s, "fecha baja"= %s, "abm quitar"= %s, "fecha quitar" = %s WHERE usuario_id = %s AND login= %s'
            parameters = (
            entra1, entra2, entra3, entra4, entra5, entra6, entra7, entra8, entra9, entra10, entra11, idold, loginold)
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()
            cursor.execute(query, parameters)
            conn.commit()
            cursor.close()
            self.edit_wind.destroy()

            self.get_data()

    def update_list(self, *args):
        search_term = self.search_var.get()

        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        mask = dfdb['estado'].str.contains(search_term, case=False, na=False)

        self.tree['column'] = list(dfdb[mask].columns)
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        df_fila2 = dfdb[mask].to_numpy().tolist()
        for fila2 in df_fila2:
            self.tree.insert('', 'end', values=fila2)

    def delete(self):

        select = self.tree.item(self.tree.selection())['values']
        query = 'UPDATE public."callback sms notifica" SET  estado='f'  WHERE   login= %s'
        parameters = (
            select[2])
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        conn.commit()
        cursor.close()


        self.get_data()

class NewTC(tk.Frame):
    def __init__(self, wind, child, *args, **kwargs):
        tk.Frame.__init__(self, child)
        self.parent = wind
        self.child = child
        self.child.title("Callback SMS")

        self.child.focus_set()
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(0, weight=1)
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(1, weight=1)
        self.panelsup = Frame(self.child)
        self.panelsup.grid(column=0, row=0, sticky='nsew')
        self.panelsup.columnconfigure(0, weight=1)
        self.panelsup.rowconfigure(0, weight=1)
        self.panelsup.columnconfigure(1, weight=1)
        self.panelsup.rowconfigure(0, weight=1)

        self.subcuadro11 = LabelFrame(self.panelsup, background='white', text='Registrar Callback SMS Notificacion')

        self.subcuadro11.grid(column=0, row=0, sticky='nsew')

        Label(self.subcuadro11, text='usuario_id: ').grid(row=1, column=0)
        self.entrada1 = Entry(self.subcuadro11)
        self.entrada1.focus()
        self.entrada1.grid(row=1, column=1)

        Label(self.subcuadro11, text='rol_id: ').grid(row=2, column=0)
        self.entrada2 = Entry(self.subcuadro11)
        self.entrada2.focus()
        self.entrada2.grid(row=2, column=1)

        Label(self.subcuadro11, text='login: ').grid(row=3, column=0)
        self.entrada3 = Entry(self.subcuadro11)
        self.entrada3.focus()
        self.entrada3.grid(row=3, column=1)

        Label(self.subcuadro11, text='nombre: ').grid(row=4, column=0)
        self.entrada4 = Entry(self.subcuadro11)
        self.entrada4.focus()
        self.entrada4.grid(row=4, column=1)

        Label(self.subcuadro11, text='estado: ').grid(row=5, column=0)
        self.entrada5 = Entry(self.subcuadro11)
        self.entrada5.focus()
        self.entrada5.grid(row=5, column=1)

        Label(self.subcuadro11, text='abm alta: ').grid(row=6, column=0)
        self.entrada6 = Entry(self.subcuadro11)
        self.entrada6.focus()
        self.entrada6.grid(row=6, column=1)

        Label(self.subcuadro11, text='fecha alta: ').grid(row=7, column=0)
        self.entrada7 = Entry(self.subcuadro11)
        self.entrada7.focus()
        self.entrada7.grid(row=7, column=1)

        Label(self.subcuadro11, text='abm baja: ').grid(row=8, column=0)
        self.entrada8 = Entry(self.subcuadro11)
        self.entrada8.focus()
        self.entrada8.grid(row=8, column=1)

        Label(self.subcuadro11, text='fecha baja: ').grid(row=9, column=0)
        self.entrada9 = Entry(self.subcuadro11)
        self.entrada9.focus()
        self.entrada9.grid(row=9, column=1)

        Label(self.subcuadro11, text='abm quitar: ').grid(row=10, column=0)
        self.entrada10 = Entry(self.subcuadro11)
        self.entrada10.focus()
        self.entrada10.grid(row=10, column=1)

        Label(self.subcuadro11, text='fecha quitar: ').grid(row=11, column=0)
        self.entrada11 = Entry(self.subcuadro11)
        self.entrada11.focus()
        self.entrada11.grid(row=11, column=1)
        # Output Messages
        self.message = Label(self.subcuadro11, text='', fg='red')
        self.message.grid(row=12, column=0, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='Save', command=self.add).grid(row=13, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='DELETE').grid(row=14, column=0, sticky=W + E)
        ttk.Button(self.subcuadro11, text='EDIT', command=self.edit).grid(row=14, column=1, sticky=W + E)

        self.subcuadro12 = LabelFrame(self.panelsup, background='white', text='Filtro')
        self.subcuadro12.grid(column=1, row=0, sticky='nsew')
        Label(self.subcuadro12, text='Estado: ').grid(row=0, column=0)

        self.search_var = StringVar()
        self.search_var.trace("w", self.update_list)
        self.entry = Entry(self.subcuadro12, textvariable=self.search_var, width=13)
        self.entry.grid(row=0, column=1)

        self.panelinf = Frame(self.child, background='blue')

        self.panelinf.grid(column=0, row=1, sticky='nsew', pady=2)
        self.panelinf.columnconfigure(0, weight=1)
        self.panelinf.rowconfigure(0, weight=1)

        self.tree = ttk.Treeview(self.panelinf)
        self.tree.grid(column=0, row=0, sticky='nsew')
        ladox = Scrollbar(self.panelinf, orient=HORIZONTAL, command=self.tree.xview)
        ladox.grid(column=0, row=1, sticky='ew')

        ladoy = Scrollbar(self.panelinf, orient=VERTICAL, command=self.tree.yview)
        ladoy.grid(column=1, row=0, sticky='ns')

        self.tree.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)

        # Buttons

        self.get_data()
        self.update_list()

    def run_query(self, query, parameters=()):
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()

        cursor.execute(query, parameters)
        column_names = [desc[0] for desc in cursor.description]
        result = cursor.fetchall()
        global dfdb
        dfdb = pd.DataFrame(result, columns=column_names)
        conn.commit()
        cursor.close()

        return dfdb

    def get_data(self):
        # cleaning Table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = 'SELECT * FROM public."callback sms notifica" '
        db_rows = self.run_query(query)
        db_rows['rol_id'] = db_rows['rol_id'].astype('Int64')
        db_rows['usuario_id'] = db_rows['usuario_id'].astype('Int64')

        # filling data
        self.tree['column'] = list(db_rows.columns)
        self.tree['show'] = "headings"
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        for row in db_rows.to_numpy().tolist():
            self.tree.insert('', 0, values=row)

    def add(self):
        if (len(self.entrada1.get()) == 0 or str(self.entrada1.get())=='None'  or str(self.entrada1.get())=='<NA>'):
            entra1 = None
        else:
            entra1 = self.entrada1.get()
        if (len(self.entrada2.get()) == 0 or str(self.entrada2.get())=='None'  or str(self.entrada2.get())=='<NA>'):
            entra2 = None
        else:
            entra2 = self.entrada2.get()
        if (len(self.entrada3.get()) == 0 or str(self.entrada3.get())=='None'  or str(self.entrada3.get())=='<NA>'):
            entra3 = None
        else:
            entra3 = self.entrada3.get()
        if (len(self.entrada4.get()) == 0 or str(self.entrada4.get())=='None'  or str(self.entrada4.get())=='<NA>'):
            entra4 = None
        else:
            entra4 = self.entrada4.get()
        if (len(self.entrada5.get()) == 0 or str(self.entrada5.get())=='None'  or str(self.entrada5.get())=='<NA>'):
            entra5 = None
        else:
            entra5 = self.entrada5.get()
        if (len(self.entrada6.get()) == 0 or str(self.entrada6.get())=='None'  or str(self.entrada6.get())=='<NA>'):
            entra6 = None
        else:
            entra6 = self.entrada6.get()
        if (len(self.entrada7.get()) == 0 or str(self.entrada7.get())=='None'  or str(self.entrada7.get())=='<NA>'):
            entra7 = None
        else:
            entra7 = self.entrada7.get()
        if (len(self.entrada8.get()) == 0 or str(self.entrada8.get())=='None'  or str(self.entrada8.get())=='<NA>'):
            entra8 = None
        else:
            entra8 = self.entrada8.get()
        if (len(self.entrada9.get()) == 0 or str(self.entrada9.get())=='None'  or str(self.entrada9.get())=='<NA>'):
            entra9 = None
        else:
            entra9 = self.entrada9.get()
        if (len(self.entrada10.get()) == 0 or str(self.entrada10.get())=='None'  or str(self.entrada10.get())=='<NA>'):
            entra10 = None
        else:
            entra10 = self.entrada10.get()
        if (len(self.entrada11.get()) == 0 or str(self.entrada11.get())=='None'  or str(self.entrada11.get())=='<NA>'):
            entra11 = None
        else:
            entra11 = self.entrada11.get()

        if( entra5==None and entra3==None):
            self.message['text'] = 'Login y Estado son necesarios'
        else:
            query = """INSERT INTO public."callback sms notifica"(usuario_id, rol_id, login, nombre, estado, "abm alta", "fecha alta", "abm baja", "fecha baja", "abm quitar", "fecha quitar") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            parameters = (entra1,
                      entra2,
                      entra3,
                      entra4,
                      entra5,
                      entra6,
                      entra7,
                      entra8,
                      entra9,
                      entra10,
                      entra11
                      )
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()

            cursor.execute(query, parameters)
            self.entrada1.delete(0, END)
            self.entrada2.delete(0, END)
            self.entrada3.delete(0, END)
            self.entrada4.delete(0, END)
            self.entrada5.delete(0, END)
            self.entrada6.delete(0, END)
            self.entrada7.delete(0, END)
            self.entrada8.delete(0, END)
            self.entrada9.delete(0, END)
            self.entrada10.delete(0, END)
            self.entrada11.delete(0, END)
            conn.commit()
            cursor.close()
            self.get_data()

    def edit(self):

        select = self.tree.item(self.tree.selection())['values']

        self.edit_wind = Toplevel(self.child)
        self.edit_wind.title = 'Edit'

        Label(self.edit_wind, text='usuario_id: ').grid(row=0, column=1)
        new_entrada1 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[0]))
        new_entrada1.grid(row=0, column=2)

        Label(self.edit_wind, text='rol_id: ').grid(row=1, column=1)
        new_entrada2 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[1]))
        new_entrada2.grid(row=1, column=2)

        Label(self.edit_wind, text='login: ').grid(row=2, column=1)
        new_entrada3 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[2]))
        new_entrada3.grid(row=2, column=2)

        Label(self.edit_wind, text='nombre: ').grid(row=3, column=1)
        new_entrada4 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[3]))
        new_entrada4.grid(row=3, column=2)

        Label(self.edit_wind, text='estado: ').grid(row=4, column=1)
        new_entrada5 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[4]))
        new_entrada5.grid(row=4, column=2)

        Label(self.edit_wind, text='abm alta: ').grid(row=5, column=1)
        new_entrada6 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[5]))
        new_entrada6.grid(row=5, column=2)

        Label(self.edit_wind, text='fecha alta: ').grid(row=6, column=1)
        new_entrada7 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[6]))
        new_entrada7.grid(row=6, column=2)

        Label(self.edit_wind, text='abm baja: ').grid(row=7, column=1)
        new_entrada8 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[7]))
        new_entrada8.grid(row=7, column=2)

        Label(self.edit_wind, text='fecha baja: ').grid(row=8, column=1)
        new_entrada9 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[8]))
        new_entrada9.grid(row=8, column=2)

        Label(self.edit_wind, text='abm quitar: ').grid(row=9, column=1)
        new_entrada10 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[9]))
        new_entrada10.grid(row=9, column=2)

        Label(self.edit_wind, text='fecha quitar: ').grid(row=10, column=1)
        new_entrada11 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[10]))
        new_entrada11.grid(row=10, column=2)

        self.messageedit = Label(self.edit_wind, text='', fg='red')
        self.messageedit.grid(row=12, column=0, columnspan=2, sticky=W + E)
        Button(self.edit_wind, text='Actualizar', command=lambda: self.edit_records(new_entrada1.get(),
                                                                                    new_entrada2.get(),
                                                                                    new_entrada3.get(),
                                                                                    new_entrada4.get(),
                                                                                    new_entrada5.get(),
                                                                                    new_entrada6.get(),
                                                                                    new_entrada7.get(),
                                                                                    new_entrada8.get(),
                                                                                    new_entrada9.get(),
                                                                                    new_entrada10.get(),
                                                                                    new_entrada11.get(),
                                                                                    select[0],
                                                                                    select[2]

                                                                                    )).grid(row=12, column=2, sticky=W)

        self.edit_wind.mainloop()

    def edit_records(self, idlogin, idrol, login, nombre, estado, aalta, falta, abaja, fbaja, aquitar, fquitar, idold,
                     loginold):
        if (len(idlogin) == 0 or str(idlogin) == 'None' or str(idlogin) == '<NA>'):
            entra1 = None
        else:
            entra1 = idlogin
        if (len(idrol) == 0 or str(idrol) == 'None' or str(idrol) == '<NA>'):
            entra2 = None
        else:
            entra2 = idrol
        if (len(login) == 0 or str(login) == 'None' or str(login) == '<NA>'):
            entra3 = None
        else:
            entra3 = login
        if (len(nombre) == 0 or str(nombre) == 'None' or str(nombre) == '<NA>'):
            entra4 = None
        else:
            entra4 = nombre
        if (len(estado) == 0 or str(estado) == 'None' or str(estado) == '<NA>'):
            entra5 = None
        else:
            entra5 = estado
        if (len(aalta) == 0 or str(aalta) == 'None' or str(aalta) == '<NA>'):
            entra6 = None
        else:
            entra6 = aalta
        if (len(falta) == 0 or str(falta) == 'None' or str(falta) == '<NA>'):
            entra7 = None
        else:
            entra7 = falta
        if (len(abaja) == 0 or str(abaja) == 'None' or str(abaja) == '<NA>'):
            entra8 = None
        else:
            entra8 = abaja
        if (len(fbaja) == 0 or str(fbaja) == 'None' or str(fbaja) == '<NA>'):
            entra9 = None
        else:
            entra9 = fbaja
        if (len(aquitar) == 0 or str(aquitar) == 'None' or str(
                aquitar) == '<NA>'):
            entra10 = None
        else:
            entra10 = aquitar
        if (len(fquitar) == 0 or str(fquitar) == 'None' or str(
                fquitar) == '<NA>'):
            entra11 = None
        else:
            entra11 = fquitar

        if (entra5 == None and entra3 == None):
            self.messageedit['text'] = 'Login y Estado son necesarios'
        else:
            query = 'UPDATE public."callback sms notifica" SET usuario_id = %s, rol_id= %s, login= %s, nombre = %s, estado= %s, "abm alta"= %s, "fecha alta"= %s, "abm baja"= %s, "fecha baja"= %s, "abm quitar"= %s, "fecha quitar" = %s WHERE usuario_id = %s AND login= %s'
            parameters = (
            entra1, entra2, entra3, entra4, entra5, entra6, entra7, entra8, entra9, entra10, entra11, idold, loginold)
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()
            cursor.execute(query, parameters)
            conn.commit()
            cursor.close()
            self.edit_wind.destroy()

            self.get_data()

    def update_list(self, *args):
        search_term = self.search_var.get()

        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        mask = dfdb['estado'].str.contains(search_term, case=False, na=False)

        self.tree['column'] = list(dfdb[mask].columns)
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        df_fila2 = dfdb[mask].to_numpy().tolist()
        for fila2 in df_fila2:
            self.tree.insert('', 'end', values=fila2)

    def delete(self):

        select = self.tree.item(self.tree.selection())['values']
        query = 'UPDATE public."callback sms notifica" SET  estado='f'  WHERE   login= %s'
        parameters = (
            select[2])
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        conn.commit()
        cursor.close()


        self.get_data()

class NewT(tk.Frame):
    def __init__(self, wind, child, *args, **kwargs):
        tk.Frame.__init__(self, child)
        self.parent = wind
        self.child = child
        self.child.title("Callback SMS")

        self.child.focus_set()
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(0, weight=1)
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(1, weight=1)
        self.panelsup = Frame(self.child)
        self.panelsup.grid(column=0, row=0, sticky='nsew')
        self.panelsup.columnconfigure(0, weight=1)
        self.panelsup.rowconfigure(0, weight=1)
        self.panelsup.columnconfigure(1, weight=1)
        self.panelsup.rowconfigure(0, weight=1)

        self.subcuadro11 = LabelFrame(self.panelsup, background='white', text='Registrar Callback SMS Notificacion')

        self.subcuadro11.grid(column=0, row=0, sticky='nsew')

        Label(self.subcuadro11, text='usuario_id: ').grid(row=1, column=0)
        self.entrada1 = Entry(self.subcuadro11)
        self.entrada1.focus()
        self.entrada1.grid(row=1, column=1)

        Label(self.subcuadro11, text='rol_id: ').grid(row=2, column=0)
        self.entrada2 = Entry(self.subcuadro11)
        self.entrada2.focus()
        self.entrada2.grid(row=2, column=1)

        Label(self.subcuadro11, text='login: ').grid(row=3, column=0)
        self.entrada3 = Entry(self.subcuadro11)
        self.entrada3.focus()
        self.entrada3.grid(row=3, column=1)

        Label(self.subcuadro11, text='nombre: ').grid(row=4, column=0)
        self.entrada4 = Entry(self.subcuadro11)
        self.entrada4.focus()
        self.entrada4.grid(row=4, column=1)

        Label(self.subcuadro11, text='estado: ').grid(row=5, column=0)
        self.entrada5 = Entry(self.subcuadro11)
        self.entrada5.focus()
        self.entrada5.grid(row=5, column=1)

        Label(self.subcuadro11, text='abm alta: ').grid(row=6, column=0)
        self.entrada6 = Entry(self.subcuadro11)
        self.entrada6.focus()
        self.entrada6.grid(row=6, column=1)

        Label(self.subcuadro11, text='fecha alta: ').grid(row=7, column=0)
        self.entrada7 = Entry(self.subcuadro11)
        self.entrada7.focus()
        self.entrada7.grid(row=7, column=1)

        Label(self.subcuadro11, text='abm baja: ').grid(row=8, column=0)
        self.entrada8 = Entry(self.subcuadro11)
        self.entrada8.focus()
        self.entrada8.grid(row=8, column=1)

        Label(self.subcuadro11, text='fecha baja: ').grid(row=9, column=0)
        self.entrada9 = Entry(self.subcuadro11)
        self.entrada9.focus()
        self.entrada9.grid(row=9, column=1)

        Label(self.subcuadro11, text='abm quitar: ').grid(row=10, column=0)
        self.entrada10 = Entry(self.subcuadro11)
        self.entrada10.focus()
        self.entrada10.grid(row=10, column=1)

        Label(self.subcuadro11, text='fecha quitar: ').grid(row=11, column=0)
        self.entrada11 = Entry(self.subcuadro11)
        self.entrada11.focus()
        self.entrada11.grid(row=11, column=1)
        # Output Messages
        self.message = Label(self.subcuadro11, text='', fg='red')
        self.message.grid(row=12, column=0, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='Save', command=self.add).grid(row=13, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='DELETE').grid(row=14, column=0, sticky=W + E)
        ttk.Button(self.subcuadro11, text='EDIT', command=self.edit).grid(row=14, column=1, sticky=W + E)

        self.subcuadro12 = LabelFrame(self.panelsup, background='white', text='Filtro')
        self.subcuadro12.grid(column=1, row=0, sticky='nsew')
        Label(self.subcuadro12, text='Estado: ').grid(row=0, column=0)

        self.search_var = StringVar()
        self.search_var.trace("w", self.update_list)
        self.entry = Entry(self.subcuadro12, textvariable=self.search_var, width=13)
        self.entry.grid(row=0, column=1)

        self.panelinf = Frame(self.child, background='blue')

        self.panelinf.grid(column=0, row=1, sticky='nsew', pady=2)
        self.panelinf.columnconfigure(0, weight=1)
        self.panelinf.rowconfigure(0, weight=1)

        self.tree = ttk.Treeview(self.panelinf)
        self.tree.grid(column=0, row=0, sticky='nsew')
        ladox = Scrollbar(self.panelinf, orient=HORIZONTAL, command=self.tree.xview)
        ladox.grid(column=0, row=1, sticky='ew')

        ladoy = Scrollbar(self.panelinf, orient=VERTICAL, command=self.tree.yview)
        ladoy.grid(column=1, row=0, sticky='ns')

        self.tree.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)

        # Buttons

        self.get_data()
        self.update_list()

    def run_query(self, query, parameters=()):
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()

        cursor.execute(query, parameters)
        column_names = [desc[0] for desc in cursor.description]
        result = cursor.fetchall()
        global dfdb
        dfdb = pd.DataFrame(result, columns=column_names)
        conn.commit()
        cursor.close()

        return dfdb

    def get_data(self):
        # cleaning Table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = 'SELECT * FROM public."callback sms notifica" '
        db_rows = self.run_query(query)
        db_rows['rol_id'] = db_rows['rol_id'].astype('Int64')
        db_rows['usuario_id'] = db_rows['usuario_id'].astype('Int64')

        # filling data
        self.tree['column'] = list(db_rows.columns)
        self.tree['show'] = "headings"
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        for row in db_rows.to_numpy().tolist():
            self.tree.insert('', 0, values=row)

    def add(self):
        if (len(self.entrada1.get()) == 0 or str(self.entrada1.get())=='None'  or str(self.entrada1.get())=='<NA>'):
            entra1 = None
        else:
            entra1 = self.entrada1.get()
        if (len(self.entrada2.get()) == 0 or str(self.entrada2.get())=='None'  or str(self.entrada2.get())=='<NA>'):
            entra2 = None
        else:
            entra2 = self.entrada2.get()
        if (len(self.entrada3.get()) == 0 or str(self.entrada3.get())=='None'  or str(self.entrada3.get())=='<NA>'):
            entra3 = None
        else:
            entra3 = self.entrada3.get()
        if (len(self.entrada4.get()) == 0 or str(self.entrada4.get())=='None'  or str(self.entrada4.get())=='<NA>'):
            entra4 = None
        else:
            entra4 = self.entrada4.get()
        if (len(self.entrada5.get()) == 0 or str(self.entrada5.get())=='None'  or str(self.entrada5.get())=='<NA>'):
            entra5 = None
        else:
            entra5 = self.entrada5.get()
        if (len(self.entrada6.get()) == 0 or str(self.entrada6.get())=='None'  or str(self.entrada6.get())=='<NA>'):
            entra6 = None
        else:
            entra6 = self.entrada6.get()
        if (len(self.entrada7.get()) == 0 or str(self.entrada7.get())=='None'  or str(self.entrada7.get())=='<NA>'):
            entra7 = None
        else:
            entra7 = self.entrada7.get()
        if (len(self.entrada8.get()) == 0 or str(self.entrada8.get())=='None'  or str(self.entrada8.get())=='<NA>'):
            entra8 = None
        else:
            entra8 = self.entrada8.get()
        if (len(self.entrada9.get()) == 0 or str(self.entrada9.get())=='None'  or str(self.entrada9.get())=='<NA>'):
            entra9 = None
        else:
            entra9 = self.entrada9.get()
        if (len(self.entrada10.get()) == 0 or str(self.entrada10.get())=='None'  or str(self.entrada10.get())=='<NA>'):
            entra10 = None
        else:
            entra10 = self.entrada10.get()
        if (len(self.entrada11.get()) == 0 or str(self.entrada11.get())=='None'  or str(self.entrada11.get())=='<NA>'):
            entra11 = None
        else:
            entra11 = self.entrada11.get()

        if( entra5==None and entra3==None):
            self.message['text'] = 'Login y Estado son necesarios'
        else:
            query = """INSERT INTO public."callback sms notifica"(usuario_id, rol_id, login, nombre, estado, "abm alta", "fecha alta", "abm baja", "fecha baja", "abm quitar", "fecha quitar") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            parameters = (entra1,
                      entra2,
                      entra3,
                      entra4,
                      entra5,
                      entra6,
                      entra7,
                      entra8,
                      entra9,
                      entra10,
                      entra11
                      )
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()

            cursor.execute(query, parameters)
            self.entrada1.delete(0, END)
            self.entrada2.delete(0, END)
            self.entrada3.delete(0, END)
            self.entrada4.delete(0, END)
            self.entrada5.delete(0, END)
            self.entrada6.delete(0, END)
            self.entrada7.delete(0, END)
            self.entrada8.delete(0, END)
            self.entrada9.delete(0, END)
            self.entrada10.delete(0, END)
            self.entrada11.delete(0, END)
            conn.commit()
            cursor.close()
            self.get_data()

    def edit(self):

        select = self.tree.item(self.tree.selection())['values']

        self.edit_wind = Toplevel(self.child)
        self.edit_wind.title = 'Edit'

        Label(self.edit_wind, text='usuario_id: ').grid(row=0, column=1)
        new_entrada1 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[0]))
        new_entrada1.grid(row=0, column=2)

        Label(self.edit_wind, text='rol_id: ').grid(row=1, column=1)
        new_entrada2 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[1]))
        new_entrada2.grid(row=1, column=2)

        Label(self.edit_wind, text='login: ').grid(row=2, column=1)
        new_entrada3 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[2]))
        new_entrada3.grid(row=2, column=2)

        Label(self.edit_wind, text='nombre: ').grid(row=3, column=1)
        new_entrada4 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[3]))
        new_entrada4.grid(row=3, column=2)

        Label(self.edit_wind, text='estado: ').grid(row=4, column=1)
        new_entrada5 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[4]))
        new_entrada5.grid(row=4, column=2)

        Label(self.edit_wind, text='abm alta: ').grid(row=5, column=1)
        new_entrada6 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[5]))
        new_entrada6.grid(row=5, column=2)

        Label(self.edit_wind, text='fecha alta: ').grid(row=6, column=1)
        new_entrada7 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[6]))
        new_entrada7.grid(row=6, column=2)

        Label(self.edit_wind, text='abm baja: ').grid(row=7, column=1)
        new_entrada8 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[7]))
        new_entrada8.grid(row=7, column=2)

        Label(self.edit_wind, text='fecha baja: ').grid(row=8, column=1)
        new_entrada9 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[8]))
        new_entrada9.grid(row=8, column=2)

        Label(self.edit_wind, text='abm quitar: ').grid(row=9, column=1)
        new_entrada10 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[9]))
        new_entrada10.grid(row=9, column=2)

        Label(self.edit_wind, text='fecha quitar: ').grid(row=10, column=1)
        new_entrada11 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[10]))
        new_entrada11.grid(row=10, column=2)

        self.messageedit = Label(self.edit_wind, text='', fg='red')
        self.messageedit.grid(row=12, column=0, columnspan=2, sticky=W + E)
        Button(self.edit_wind, text='Actualizar', command=lambda: self.edit_records(new_entrada1.get(),
                                                                                    new_entrada2.get(),
                                                                                    new_entrada3.get(),
                                                                                    new_entrada4.get(),
                                                                                    new_entrada5.get(),
                                                                                    new_entrada6.get(),
                                                                                    new_entrada7.get(),
                                                                                    new_entrada8.get(),
                                                                                    new_entrada9.get(),
                                                                                    new_entrada10.get(),
                                                                                    new_entrada11.get(),
                                                                                    select[0],
                                                                                    select[2]

                                                                                    )).grid(row=12, column=2, sticky=W)

        self.edit_wind.mainloop()

    def edit_records(self, idlogin, idrol, login, nombre, estado, aalta, falta, abaja, fbaja, aquitar, fquitar, idold,
                     loginold):
        if (len(idlogin) == 0 or str(idlogin) == 'None' or str(idlogin) == '<NA>'):
            entra1 = None
        else:
            entra1 = idlogin
        if (len(idrol) == 0 or str(idrol) == 'None' or str(idrol) == '<NA>'):
            entra2 = None
        else:
            entra2 = idrol
        if (len(login) == 0 or str(login) == 'None' or str(login) == '<NA>'):
            entra3 = None
        else:
            entra3 = login
        if (len(nombre) == 0 or str(nombre) == 'None' or str(nombre) == '<NA>'):
            entra4 = None
        else:
            entra4 = nombre
        if (len(estado) == 0 or str(estado) == 'None' or str(estado) == '<NA>'):
            entra5 = None
        else:
            entra5 = estado
        if (len(aalta) == 0 or str(aalta) == 'None' or str(aalta) == '<NA>'):
            entra6 = None
        else:
            entra6 = aalta
        if (len(falta) == 0 or str(falta) == 'None' or str(falta) == '<NA>'):
            entra7 = None
        else:
            entra7 = falta
        if (len(abaja) == 0 or str(abaja) == 'None' or str(abaja) == '<NA>'):
            entra8 = None
        else:
            entra8 = abaja
        if (len(fbaja) == 0 or str(fbaja) == 'None' or str(fbaja) == '<NA>'):
            entra9 = None
        else:
            entra9 = fbaja
        if (len(aquitar) == 0 or str(aquitar) == 'None' or str(
                aquitar) == '<NA>'):
            entra10 = None
        else:
            entra10 = aquitar
        if (len(fquitar) == 0 or str(fquitar) == 'None' or str(
                fquitar) == '<NA>'):
            entra11 = None
        else:
            entra11 = fquitar

        if (entra5 == None and entra3 == None):
            self.messageedit['text'] = 'Login y Estado son necesarios'
        else:
            query = 'UPDATE public."callback sms notifica" SET usuario_id = %s, rol_id= %s, login= %s, nombre = %s, estado= %s, "abm alta"= %s, "fecha alta"= %s, "abm baja"= %s, "fecha baja"= %s, "abm quitar"= %s, "fecha quitar" = %s WHERE usuario_id = %s AND login= %s'
            parameters = (
            entra1, entra2, entra3, entra4, entra5, entra6, entra7, entra8, entra9, entra10, entra11, idold, loginold)
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()
            cursor.execute(query, parameters)
            conn.commit()
            cursor.close()
            self.edit_wind.destroy()

            self.get_data()

    def update_list(self, *args):
        search_term = self.search_var.get()

        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        mask = dfdb['estado'].str.contains(search_term, case=False, na=False)

        self.tree['column'] = list(dfdb[mask].columns)
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        df_fila2 = dfdb[mask].to_numpy().tolist()
        for fila2 in df_fila2:
            self.tree.insert('', 'end', values=fila2)

    def delete(self):

        select = self.tree.item(self.tree.selection())['values']
        query = 'UPDATE public."callback sms notifica" SET  estado='f'  WHERE   login= %s'
        parameters = (
            select[2])
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        conn.commit()
        cursor.close()


        self.get_data()

class NewTR4(tk.Frame):
    def __init__(self, wind, child, *args, **kwargs):
        tk.Frame.__init__(self, child)
        self.parent = wind
        self.child = child
        self.child.title("Callback SMS")

        self.child.focus_set()
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(0, weight=1)
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(1, weight=1)
        self.panelsup = Frame(self.child)
        self.panelsup.grid(column=0, row=0, sticky='nsew')
        self.panelsup.columnconfigure(0, weight=1)
        self.panelsup.rowconfigure(0, weight=1)
        self.panelsup.columnconfigure(1, weight=1)
        self.panelsup.rowconfigure(0, weight=1)

        self.subcuadro11 = LabelFrame(self.panelsup, background='white', text='Registrar Callback SMS Notificacion')

        self.subcuadro11.grid(column=0, row=0, sticky='nsew')

        Label(self.subcuadro11, text='usuario_id: ').grid(row=1, column=0)
        self.entrada1 = Entry(self.subcuadro11)
        self.entrada1.focus()
        self.entrada1.grid(row=1, column=1)

        Label(self.subcuadro11, text='rol_id: ').grid(row=2, column=0)
        self.entrada2 = Entry(self.subcuadro11)
        self.entrada2.focus()
        self.entrada2.grid(row=2, column=1)

        Label(self.subcuadro11, text='login: ').grid(row=3, column=0)
        self.entrada3 = Entry(self.subcuadro11)
        self.entrada3.focus()
        self.entrada3.grid(row=3, column=1)

        Label(self.subcuadro11, text='nombre: ').grid(row=4, column=0)
        self.entrada4 = Entry(self.subcuadro11)
        self.entrada4.focus()
        self.entrada4.grid(row=4, column=1)

        Label(self.subcuadro11, text='estado: ').grid(row=5, column=0)
        self.entrada5 = Entry(self.subcuadro11)
        self.entrada5.focus()
        self.entrada5.grid(row=5, column=1)

        Label(self.subcuadro11, text='abm alta: ').grid(row=6, column=0)
        self.entrada6 = Entry(self.subcuadro11)
        self.entrada6.focus()
        self.entrada6.grid(row=6, column=1)

        Label(self.subcuadro11, text='fecha alta: ').grid(row=7, column=0)
        self.entrada7 = Entry(self.subcuadro11)
        self.entrada7.focus()
        self.entrada7.grid(row=7, column=1)

        Label(self.subcuadro11, text='abm baja: ').grid(row=8, column=0)
        self.entrada8 = Entry(self.subcuadro11)
        self.entrada8.focus()
        self.entrada8.grid(row=8, column=1)

        Label(self.subcuadro11, text='fecha baja: ').grid(row=9, column=0)
        self.entrada9 = Entry(self.subcuadro11)
        self.entrada9.focus()
        self.entrada9.grid(row=9, column=1)

        Label(self.subcuadro11, text='abm quitar: ').grid(row=10, column=0)
        self.entrada10 = Entry(self.subcuadro11)
        self.entrada10.focus()
        self.entrada10.grid(row=10, column=1)

        Label(self.subcuadro11, text='fecha quitar: ').grid(row=11, column=0)
        self.entrada11 = Entry(self.subcuadro11)
        self.entrada11.focus()
        self.entrada11.grid(row=11, column=1)
        # Output Messages
        self.message = Label(self.subcuadro11, text='', fg='red')
        self.message.grid(row=12, column=0, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='Save', command=self.add).grid(row=13, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='DELETE').grid(row=14, column=0, sticky=W + E)
        ttk.Button(self.subcuadro11, text='EDIT', command=self.edit).grid(row=14, column=1, sticky=W + E)

        self.subcuadro12 = LabelFrame(self.panelsup, background='white', text='Filtro')
        self.subcuadro12.grid(column=1, row=0, sticky='nsew')
        Label(self.subcuadro12, text='Estado: ').grid(row=0, column=0)

        self.search_var = StringVar()
        self.search_var.trace("w", self.update_list)
        self.entry = Entry(self.subcuadro12, textvariable=self.search_var, width=13)
        self.entry.grid(row=0, column=1)

        self.panelinf = Frame(self.child, background='blue')

        self.panelinf.grid(column=0, row=1, sticky='nsew', pady=2)
        self.panelinf.columnconfigure(0, weight=1)
        self.panelinf.rowconfigure(0, weight=1)

        self.tree = ttk.Treeview(self.panelinf)
        self.tree.grid(column=0, row=0, sticky='nsew')
        ladox = Scrollbar(self.panelinf, orient=HORIZONTAL, command=self.tree.xview)
        ladox.grid(column=0, row=1, sticky='ew')

        ladoy = Scrollbar(self.panelinf, orient=VERTICAL, command=self.tree.yview)
        ladoy.grid(column=1, row=0, sticky='ns')

        self.tree.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)

        # Buttons

        self.get_data()
        self.update_list()

    def run_query(self, query, parameters=()):
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()

        cursor.execute(query, parameters)
        column_names = [desc[0] for desc in cursor.description]
        result = cursor.fetchall()
        global dfdb
        dfdb = pd.DataFrame(result, columns=column_names)
        conn.commit()
        cursor.close()

        return dfdb

    def get_data(self):
        # cleaning Table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = 'SELECT * FROM public."callback sms notifica" '
        db_rows = self.run_query(query)
        db_rows['rol_id'] = db_rows['rol_id'].astype('Int64')
        db_rows['usuario_id'] = db_rows['usuario_id'].astype('Int64')

        # filling data
        self.tree['column'] = list(db_rows.columns)
        self.tree['show'] = "headings"
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        for row in db_rows.to_numpy().tolist():
            self.tree.insert('', 0, values=row)

    def add(self):
        if (len(self.entrada1.get()) == 0 or str(self.entrada1.get())=='None'  or str(self.entrada1.get())=='<NA>'):
            entra1 = None
        else:
            entra1 = self.entrada1.get()
        if (len(self.entrada2.get()) == 0 or str(self.entrada2.get())=='None'  or str(self.entrada2.get())=='<NA>'):
            entra2 = None
        else:
            entra2 = self.entrada2.get()
        if (len(self.entrada3.get()) == 0 or str(self.entrada3.get())=='None'  or str(self.entrada3.get())=='<NA>'):
            entra3 = None
        else:
            entra3 = self.entrada3.get()
        if (len(self.entrada4.get()) == 0 or str(self.entrada4.get())=='None'  or str(self.entrada4.get())=='<NA>'):
            entra4 = None
        else:
            entra4 = self.entrada4.get()
        if (len(self.entrada5.get()) == 0 or str(self.entrada5.get())=='None'  or str(self.entrada5.get())=='<NA>'):
            entra5 = None
        else:
            entra5 = self.entrada5.get()
        if (len(self.entrada6.get()) == 0 or str(self.entrada6.get())=='None'  or str(self.entrada6.get())=='<NA>'):
            entra6 = None
        else:
            entra6 = self.entrada6.get()
        if (len(self.entrada7.get()) == 0 or str(self.entrada7.get())=='None'  or str(self.entrada7.get())=='<NA>'):
            entra7 = None
        else:
            entra7 = self.entrada7.get()
        if (len(self.entrada8.get()) == 0 or str(self.entrada8.get())=='None'  or str(self.entrada8.get())=='<NA>'):
            entra8 = None
        else:
            entra8 = self.entrada8.get()
        if (len(self.entrada9.get()) == 0 or str(self.entrada9.get())=='None'  or str(self.entrada9.get())=='<NA>'):
            entra9 = None
        else:
            entra9 = self.entrada9.get()
        if (len(self.entrada10.get()) == 0 or str(self.entrada10.get())=='None'  or str(self.entrada10.get())=='<NA>'):
            entra10 = None
        else:
            entra10 = self.entrada10.get()
        if (len(self.entrada11.get()) == 0 or str(self.entrada11.get())=='None'  or str(self.entrada11.get())=='<NA>'):
            entra11 = None
        else:
            entra11 = self.entrada11.get()

        if( entra5==None and entra3==None):
            self.message['text'] = 'Login y Estado son necesarios'
        else:
            query = """INSERT INTO public."callback sms notifica"(usuario_id, rol_id, login, nombre, estado, "abm alta", "fecha alta", "abm baja", "fecha baja", "abm quitar", "fecha quitar") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            parameters = (entra1,
                      entra2,
                      entra3,
                      entra4,
                      entra5,
                      entra6,
                      entra7,
                      entra8,
                      entra9,
                      entra10,
                      entra11
                      )
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()

            cursor.execute(query, parameters)
            self.entrada1.delete(0, END)
            self.entrada2.delete(0, END)
            self.entrada3.delete(0, END)
            self.entrada4.delete(0, END)
            self.entrada5.delete(0, END)
            self.entrada6.delete(0, END)
            self.entrada7.delete(0, END)
            self.entrada8.delete(0, END)
            self.entrada9.delete(0, END)
            self.entrada10.delete(0, END)
            self.entrada11.delete(0, END)
            conn.commit()
            cursor.close()
            self.get_data()

    def edit(self):

        select = self.tree.item(self.tree.selection())['values']

        self.edit_wind = Toplevel(self.child)
        self.edit_wind.title = 'Edit'

        Label(self.edit_wind, text='usuario_id: ').grid(row=0, column=1)
        new_entrada1 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[0]))
        new_entrada1.grid(row=0, column=2)

        Label(self.edit_wind, text='rol_id: ').grid(row=1, column=1)
        new_entrada2 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[1]))
        new_entrada2.grid(row=1, column=2)

        Label(self.edit_wind, text='login: ').grid(row=2, column=1)
        new_entrada3 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[2]))
        new_entrada3.grid(row=2, column=2)

        Label(self.edit_wind, text='nombre: ').grid(row=3, column=1)
        new_entrada4 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[3]))
        new_entrada4.grid(row=3, column=2)

        Label(self.edit_wind, text='estado: ').grid(row=4, column=1)
        new_entrada5 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[4]))
        new_entrada5.grid(row=4, column=2)

        Label(self.edit_wind, text='abm alta: ').grid(row=5, column=1)
        new_entrada6 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[5]))
        new_entrada6.grid(row=5, column=2)

        Label(self.edit_wind, text='fecha alta: ').grid(row=6, column=1)
        new_entrada7 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[6]))
        new_entrada7.grid(row=6, column=2)

        Label(self.edit_wind, text='abm baja: ').grid(row=7, column=1)
        new_entrada8 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[7]))
        new_entrada8.grid(row=7, column=2)

        Label(self.edit_wind, text='fecha baja: ').grid(row=8, column=1)
        new_entrada9 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[8]))
        new_entrada9.grid(row=8, column=2)

        Label(self.edit_wind, text='abm quitar: ').grid(row=9, column=1)
        new_entrada10 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[9]))
        new_entrada10.grid(row=9, column=2)

        Label(self.edit_wind, text='fecha quitar: ').grid(row=10, column=1)
        new_entrada11 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[10]))
        new_entrada11.grid(row=10, column=2)

        self.messageedit = Label(self.edit_wind, text='', fg='red')
        self.messageedit.grid(row=12, column=0, columnspan=2, sticky=W + E)
        Button(self.edit_wind, text='Actualizar', command=lambda: self.edit_records(new_entrada1.get(),
                                                                                    new_entrada2.get(),
                                                                                    new_entrada3.get(),
                                                                                    new_entrada4.get(),
                                                                                    new_entrada5.get(),
                                                                                    new_entrada6.get(),
                                                                                    new_entrada7.get(),
                                                                                    new_entrada8.get(),
                                                                                    new_entrada9.get(),
                                                                                    new_entrada10.get(),
                                                                                    new_entrada11.get(),
                                                                                    select[0],
                                                                                    select[2]

                                                                                    )).grid(row=12, column=2, sticky=W)

        self.edit_wind.mainloop()

    def edit_records(self, idlogin, idrol, login, nombre, estado, aalta, falta, abaja, fbaja, aquitar, fquitar, idold,
                     loginold):
        if (len(idlogin) == 0 or str(idlogin) == 'None' or str(idlogin) == '<NA>'):
            entra1 = None
        else:
            entra1 = idlogin
        if (len(idrol) == 0 or str(idrol) == 'None' or str(idrol) == '<NA>'):
            entra2 = None
        else:
            entra2 = idrol
        if (len(login) == 0 or str(login) == 'None' or str(login) == '<NA>'):
            entra3 = None
        else:
            entra3 = login
        if (len(nombre) == 0 or str(nombre) == 'None' or str(nombre) == '<NA>'):
            entra4 = None
        else:
            entra4 = nombre
        if (len(estado) == 0 or str(estado) == 'None' or str(estado) == '<NA>'):
            entra5 = None
        else:
            entra5 = estado
        if (len(aalta) == 0 or str(aalta) == 'None' or str(aalta) == '<NA>'):
            entra6 = None
        else:
            entra6 = aalta
        if (len(falta) == 0 or str(falta) == 'None' or str(falta) == '<NA>'):
            entra7 = None
        else:
            entra7 = falta
        if (len(abaja) == 0 or str(abaja) == 'None' or str(abaja) == '<NA>'):
            entra8 = None
        else:
            entra8 = abaja
        if (len(fbaja) == 0 or str(fbaja) == 'None' or str(fbaja) == '<NA>'):
            entra9 = None
        else:
            entra9 = fbaja
        if (len(aquitar) == 0 or str(aquitar) == 'None' or str(
                aquitar) == '<NA>'):
            entra10 = None
        else:
            entra10 = aquitar
        if (len(fquitar) == 0 or str(fquitar) == 'None' or str(
                fquitar) == '<NA>'):
            entra11 = None
        else:
            entra11 = fquitar

        if (entra5 == None and entra3 == None):
            self.messageedit['text'] = 'Login y Estado son necesarios'
        else:
            query = 'UPDATE public."callback sms notifica" SET usuario_id = %s, rol_id= %s, login= %s, nombre = %s, estado= %s, "abm alta"= %s, "fecha alta"= %s, "abm baja"= %s, "fecha baja"= %s, "abm quitar"= %s, "fecha quitar" = %s WHERE usuario_id = %s AND login= %s'
            parameters = (
            entra1, entra2, entra3, entra4, entra5, entra6, entra7, entra8, entra9, entra10, entra11, idold, loginold)
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()
            cursor.execute(query, parameters)
            conn.commit()
            cursor.close()
            self.edit_wind.destroy()

            self.get_data()

    def update_list(self, *args):
        search_term = self.search_var.get()

        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        mask = dfdb['estado'].str.contains(search_term, case=False, na=False)

        self.tree['column'] = list(dfdb[mask].columns)
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        df_fila2 = dfdb[mask].to_numpy().tolist()
        for fila2 in df_fila2:
            self.tree.insert('', 'end', values=fila2)

    def delete(self):

        select = self.tree.item(self.tree.selection())['values']
        query = 'UPDATE public."callback sms notifica" SET  estado='f'  WHERE   login= %s'
        parameters = (
            select[2])
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        conn.commit()
        cursor.close()


        self.get_data()

class NewWFO(tk.Frame):
    def __init__(self, wind, child, *args, **kwargs):
        tk.Frame.__init__(self, child)
        self.parent = wind
        self.child = child
        self.child.title("Callback SMS")

        self.child.focus_set()
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(0, weight=1)
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(1, weight=1)
        self.panelsup = Frame(self.child)
        self.panelsup.grid(column=0, row=0, sticky='nsew')
        self.panelsup.columnconfigure(0, weight=1)
        self.panelsup.rowconfigure(0, weight=1)
        self.panelsup.columnconfigure(1, weight=1)
        self.panelsup.rowconfigure(0, weight=1)

        self.subcuadro11 = LabelFrame(self.panelsup, background='white', text='Registrar Callback SMS Notificacion')

        self.subcuadro11.grid(column=0, row=0, sticky='nsew')

        Label(self.subcuadro11, text='usuario_id: ').grid(row=1, column=0)
        self.entrada1 = Entry(self.subcuadro11)
        self.entrada1.focus()
        self.entrada1.grid(row=1, column=1)

        Label(self.subcuadro11, text='rol_id: ').grid(row=2, column=0)
        self.entrada2 = Entry(self.subcuadro11)
        self.entrada2.focus()
        self.entrada2.grid(row=2, column=1)

        Label(self.subcuadro11, text='login: ').grid(row=3, column=0)
        self.entrada3 = Entry(self.subcuadro11)
        self.entrada3.focus()
        self.entrada3.grid(row=3, column=1)

        Label(self.subcuadro11, text='nombre: ').grid(row=4, column=0)
        self.entrada4 = Entry(self.subcuadro11)
        self.entrada4.focus()
        self.entrada4.grid(row=4, column=1)

        Label(self.subcuadro11, text='estado: ').grid(row=5, column=0)
        self.entrada5 = Entry(self.subcuadro11)
        self.entrada5.focus()
        self.entrada5.grid(row=5, column=1)

        Label(self.subcuadro11, text='abm alta: ').grid(row=6, column=0)
        self.entrada6 = Entry(self.subcuadro11)
        self.entrada6.focus()
        self.entrada6.grid(row=6, column=1)

        Label(self.subcuadro11, text='fecha alta: ').grid(row=7, column=0)
        self.entrada7 = Entry(self.subcuadro11)
        self.entrada7.focus()
        self.entrada7.grid(row=7, column=1)

        Label(self.subcuadro11, text='abm baja: ').grid(row=8, column=0)
        self.entrada8 = Entry(self.subcuadro11)
        self.entrada8.focus()
        self.entrada8.grid(row=8, column=1)

        Label(self.subcuadro11, text='fecha baja: ').grid(row=9, column=0)
        self.entrada9 = Entry(self.subcuadro11)
        self.entrada9.focus()
        self.entrada9.grid(row=9, column=1)

        Label(self.subcuadro11, text='abm quitar: ').grid(row=10, column=0)
        self.entrada10 = Entry(self.subcuadro11)
        self.entrada10.focus()
        self.entrada10.grid(row=10, column=1)

        Label(self.subcuadro11, text='fecha quitar: ').grid(row=11, column=0)
        self.entrada11 = Entry(self.subcuadro11)
        self.entrada11.focus()
        self.entrada11.grid(row=11, column=1)
        # Output Messages
        self.message = Label(self.subcuadro11, text='', fg='red')
        self.message.grid(row=12, column=0, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='Save', command=self.add).grid(row=13, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='DELETE').grid(row=14, column=0, sticky=W + E)
        ttk.Button(self.subcuadro11, text='EDIT', command=self.edit).grid(row=14, column=1, sticky=W + E)

        self.subcuadro12 = LabelFrame(self.panelsup, background='white', text='Filtro')
        self.subcuadro12.grid(column=1, row=0, sticky='nsew')
        Label(self.subcuadro12, text='Estado: ').grid(row=0, column=0)

        self.search_var = StringVar()
        self.search_var.trace("w", self.update_list)
        self.entry = Entry(self.subcuadro12, textvariable=self.search_var, width=13)
        self.entry.grid(row=0, column=1)

        self.panelinf = Frame(self.child, background='blue')

        self.panelinf.grid(column=0, row=1, sticky='nsew', pady=2)
        self.panelinf.columnconfigure(0, weight=1)
        self.panelinf.rowconfigure(0, weight=1)

        self.tree = ttk.Treeview(self.panelinf)
        self.tree.grid(column=0, row=0, sticky='nsew')
        ladox = Scrollbar(self.panelinf, orient=HORIZONTAL, command=self.tree.xview)
        ladox.grid(column=0, row=1, sticky='ew')

        ladoy = Scrollbar(self.panelinf, orient=VERTICAL, command=self.tree.yview)
        ladoy.grid(column=1, row=0, sticky='ns')

        self.tree.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)

        # Buttons

        self.get_data()
        self.update_list()

    def run_query(self, query, parameters=()):
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()

        cursor.execute(query, parameters)
        column_names = [desc[0] for desc in cursor.description]
        result = cursor.fetchall()
        global dfdb
        dfdb = pd.DataFrame(result, columns=column_names)
        conn.commit()
        cursor.close()

        return dfdb

    def get_data(self):
        # cleaning Table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = 'SELECT * FROM public."callback sms notifica" '
        db_rows = self.run_query(query)
        db_rows['rol_id'] = db_rows['rol_id'].astype('Int64')
        db_rows['usuario_id'] = db_rows['usuario_id'].astype('Int64')

        # filling data
        self.tree['column'] = list(db_rows.columns)
        self.tree['show'] = "headings"
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        for row in db_rows.to_numpy().tolist():
            self.tree.insert('', 0, values=row)

    def add(self):
        if (len(self.entrada1.get()) == 0 or str(self.entrada1.get())=='None'  or str(self.entrada1.get())=='<NA>'):
            entra1 = None
        else:
            entra1 = self.entrada1.get()
        if (len(self.entrada2.get()) == 0 or str(self.entrada2.get())=='None'  or str(self.entrada2.get())=='<NA>'):
            entra2 = None
        else:
            entra2 = self.entrada2.get()
        if (len(self.entrada3.get()) == 0 or str(self.entrada3.get())=='None'  or str(self.entrada3.get())=='<NA>'):
            entra3 = None
        else:
            entra3 = self.entrada3.get()
        if (len(self.entrada4.get()) == 0 or str(self.entrada4.get())=='None'  or str(self.entrada4.get())=='<NA>'):
            entra4 = None
        else:
            entra4 = self.entrada4.get()
        if (len(self.entrada5.get()) == 0 or str(self.entrada5.get())=='None'  or str(self.entrada5.get())=='<NA>'):
            entra5 = None
        else:
            entra5 = self.entrada5.get()
        if (len(self.entrada6.get()) == 0 or str(self.entrada6.get())=='None'  or str(self.entrada6.get())=='<NA>'):
            entra6 = None
        else:
            entra6 = self.entrada6.get()
        if (len(self.entrada7.get()) == 0 or str(self.entrada7.get())=='None'  or str(self.entrada7.get())=='<NA>'):
            entra7 = None
        else:
            entra7 = self.entrada7.get()
        if (len(self.entrada8.get()) == 0 or str(self.entrada8.get())=='None'  or str(self.entrada8.get())=='<NA>'):
            entra8 = None
        else:
            entra8 = self.entrada8.get()
        if (len(self.entrada9.get()) == 0 or str(self.entrada9.get())=='None'  or str(self.entrada9.get())=='<NA>'):
            entra9 = None
        else:
            entra9 = self.entrada9.get()
        if (len(self.entrada10.get()) == 0 or str(self.entrada10.get())=='None'  or str(self.entrada10.get())=='<NA>'):
            entra10 = None
        else:
            entra10 = self.entrada10.get()
        if (len(self.entrada11.get()) == 0 or str(self.entrada11.get())=='None'  or str(self.entrada11.get())=='<NA>'):
            entra11 = None
        else:
            entra11 = self.entrada11.get()

        if( entra5==None and entra3==None):
            self.message['text'] = 'Login y Estado son necesarios'
        else:
            query = """INSERT INTO public."callback sms notifica"(usuario_id, rol_id, login, nombre, estado, "abm alta", "fecha alta", "abm baja", "fecha baja", "abm quitar", "fecha quitar") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            parameters = (entra1,
                      entra2,
                      entra3,
                      entra4,
                      entra5,
                      entra6,
                      entra7,
                      entra8,
                      entra9,
                      entra10,
                      entra11
                      )
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()

            cursor.execute(query, parameters)
            self.entrada1.delete(0, END)
            self.entrada2.delete(0, END)
            self.entrada3.delete(0, END)
            self.entrada4.delete(0, END)
            self.entrada5.delete(0, END)
            self.entrada6.delete(0, END)
            self.entrada7.delete(0, END)
            self.entrada8.delete(0, END)
            self.entrada9.delete(0, END)
            self.entrada10.delete(0, END)
            self.entrada11.delete(0, END)
            conn.commit()
            cursor.close()
            self.get_data()

    def edit(self):

        select = self.tree.item(self.tree.selection())['values']

        self.edit_wind = Toplevel(self.child)
        self.edit_wind.title = 'Edit'

        Label(self.edit_wind, text='usuario_id: ').grid(row=0, column=1)
        new_entrada1 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[0]))
        new_entrada1.grid(row=0, column=2)

        Label(self.edit_wind, text='rol_id: ').grid(row=1, column=1)
        new_entrada2 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[1]))
        new_entrada2.grid(row=1, column=2)

        Label(self.edit_wind, text='login: ').grid(row=2, column=1)
        new_entrada3 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[2]))
        new_entrada3.grid(row=2, column=2)

        Label(self.edit_wind, text='nombre: ').grid(row=3, column=1)
        new_entrada4 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[3]))
        new_entrada4.grid(row=3, column=2)

        Label(self.edit_wind, text='estado: ').grid(row=4, column=1)
        new_entrada5 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[4]))
        new_entrada5.grid(row=4, column=2)

        Label(self.edit_wind, text='abm alta: ').grid(row=5, column=1)
        new_entrada6 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[5]))
        new_entrada6.grid(row=5, column=2)

        Label(self.edit_wind, text='fecha alta: ').grid(row=6, column=1)
        new_entrada7 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[6]))
        new_entrada7.grid(row=6, column=2)

        Label(self.edit_wind, text='abm baja: ').grid(row=7, column=1)
        new_entrada8 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[7]))
        new_entrada8.grid(row=7, column=2)

        Label(self.edit_wind, text='fecha baja: ').grid(row=8, column=1)
        new_entrada9 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[8]))
        new_entrada9.grid(row=8, column=2)

        Label(self.edit_wind, text='abm quitar: ').grid(row=9, column=1)
        new_entrada10 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[9]))
        new_entrada10.grid(row=9, column=2)

        Label(self.edit_wind, text='fecha quitar: ').grid(row=10, column=1)
        new_entrada11 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[10]))
        new_entrada11.grid(row=10, column=2)

        self.messageedit = Label(self.edit_wind, text='', fg='red')
        self.messageedit.grid(row=12, column=0, columnspan=2, sticky=W + E)
        Button(self.edit_wind, text='Actualizar', command=lambda: self.edit_records(new_entrada1.get(),
                                                                                    new_entrada2.get(),
                                                                                    new_entrada3.get(),
                                                                                    new_entrada4.get(),
                                                                                    new_entrada5.get(),
                                                                                    new_entrada6.get(),
                                                                                    new_entrada7.get(),
                                                                                    new_entrada8.get(),
                                                                                    new_entrada9.get(),
                                                                                    new_entrada10.get(),
                                                                                    new_entrada11.get(),
                                                                                    select[0],
                                                                                    select[2]

                                                                                    )).grid(row=12, column=2, sticky=W)

        self.edit_wind.mainloop()

    def edit_records(self, idlogin, idrol, login, nombre, estado, aalta, falta, abaja, fbaja, aquitar, fquitar, idold,
                     loginold):
        if (len(idlogin) == 0 or str(idlogin) == 'None' or str(idlogin) == '<NA>'):
            entra1 = None
        else:
            entra1 = idlogin
        if (len(idrol) == 0 or str(idrol) == 'None' or str(idrol) == '<NA>'):
            entra2 = None
        else:
            entra2 = idrol
        if (len(login) == 0 or str(login) == 'None' or str(login) == '<NA>'):
            entra3 = None
        else:
            entra3 = login
        if (len(nombre) == 0 or str(nombre) == 'None' or str(nombre) == '<NA>'):
            entra4 = None
        else:
            entra4 = nombre
        if (len(estado) == 0 or str(estado) == 'None' or str(estado) == '<NA>'):
            entra5 = None
        else:
            entra5 = estado
        if (len(aalta) == 0 or str(aalta) == 'None' or str(aalta) == '<NA>'):
            entra6 = None
        else:
            entra6 = aalta
        if (len(falta) == 0 or str(falta) == 'None' or str(falta) == '<NA>'):
            entra7 = None
        else:
            entra7 = falta
        if (len(abaja) == 0 or str(abaja) == 'None' or str(abaja) == '<NA>'):
            entra8 = None
        else:
            entra8 = abaja
        if (len(fbaja) == 0 or str(fbaja) == 'None' or str(fbaja) == '<NA>'):
            entra9 = None
        else:
            entra9 = fbaja
        if (len(aquitar) == 0 or str(aquitar) == 'None' or str(
                aquitar) == '<NA>'):
            entra10 = None
        else:
            entra10 = aquitar
        if (len(fquitar) == 0 or str(fquitar) == 'None' or str(
                fquitar) == '<NA>'):
            entra11 = None
        else:
            entra11 = fquitar

        if (entra5 == None and entra3 == None):
            self.messageedit['text'] = 'Login y Estado son necesarios'
        else:
            query = 'UPDATE public."callback sms notifica" SET usuario_id = %s, rol_id= %s, login= %s, nombre = %s, estado= %s, "abm alta"= %s, "fecha alta"= %s, "abm baja"= %s, "fecha baja"= %s, "abm quitar"= %s, "fecha quitar" = %s WHERE usuario_id = %s AND login= %s'
            parameters = (
            entra1, entra2, entra3, entra4, entra5, entra6, entra7, entra8, entra9, entra10, entra11, idold, loginold)
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()
            cursor.execute(query, parameters)
            conn.commit()
            cursor.close()
            self.edit_wind.destroy()

            self.get_data()

    def update_list(self, *args):
        search_term = self.search_var.get()

        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        mask = dfdb['estado'].str.contains(search_term, case=False, na=False)

        self.tree['column'] = list(dfdb[mask].columns)
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        df_fila2 = dfdb[mask].to_numpy().tolist()
        for fila2 in df_fila2:
            self.tree.insert('', 'end', values=fila2)

    def delete(self):

        select = self.tree.item(self.tree.selection())['values']
        query = 'UPDATE public."callback sms notifica" SET  estado='f'  WHERE   login= %s'
        parameters = (
            select[2])
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        conn.commit()
        cursor.close()


        self.get_data()

class NewWFOACR(tk.Frame):
    def __init__(self, wind, child, *args, **kwargs):
        tk.Frame.__init__(self, child)
        self.parent = wind
        self.child = child
        self.child.title("Callback SMS")

        self.child.focus_set()
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(0, weight=1)
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(1, weight=1)
        self.panelsup = Frame(self.child)
        self.panelsup.grid(column=0, row=0, sticky='nsew')
        self.panelsup.columnconfigure(0, weight=1)
        self.panelsup.rowconfigure(0, weight=1)
        self.panelsup.columnconfigure(1, weight=1)
        self.panelsup.rowconfigure(0, weight=1)

        self.subcuadro11 = LabelFrame(self.panelsup, background='white', text='Registrar Callback SMS Notificacion')

        self.subcuadro11.grid(column=0, row=0, sticky='nsew')

        Label(self.subcuadro11, text='usuario_id: ').grid(row=1, column=0)
        self.entrada1 = Entry(self.subcuadro11)
        self.entrada1.focus()
        self.entrada1.grid(row=1, column=1)

        Label(self.subcuadro11, text='rol_id: ').grid(row=2, column=0)
        self.entrada2 = Entry(self.subcuadro11)
        self.entrada2.focus()
        self.entrada2.grid(row=2, column=1)

        Label(self.subcuadro11, text='login: ').grid(row=3, column=0)
        self.entrada3 = Entry(self.subcuadro11)
        self.entrada3.focus()
        self.entrada3.grid(row=3, column=1)

        Label(self.subcuadro11, text='nombre: ').grid(row=4, column=0)
        self.entrada4 = Entry(self.subcuadro11)
        self.entrada4.focus()
        self.entrada4.grid(row=4, column=1)

        Label(self.subcuadro11, text='estado: ').grid(row=5, column=0)
        self.entrada5 = Entry(self.subcuadro11)
        self.entrada5.focus()
        self.entrada5.grid(row=5, column=1)

        Label(self.subcuadro11, text='abm alta: ').grid(row=6, column=0)
        self.entrada6 = Entry(self.subcuadro11)
        self.entrada6.focus()
        self.entrada6.grid(row=6, column=1)

        Label(self.subcuadro11, text='fecha alta: ').grid(row=7, column=0)
        self.entrada7 = Entry(self.subcuadro11)
        self.entrada7.focus()
        self.entrada7.grid(row=7, column=1)

        Label(self.subcuadro11, text='abm baja: ').grid(row=8, column=0)
        self.entrada8 = Entry(self.subcuadro11)
        self.entrada8.focus()
        self.entrada8.grid(row=8, column=1)

        Label(self.subcuadro11, text='fecha baja: ').grid(row=9, column=0)
        self.entrada9 = Entry(self.subcuadro11)
        self.entrada9.focus()
        self.entrada9.grid(row=9, column=1)

        Label(self.subcuadro11, text='abm quitar: ').grid(row=10, column=0)
        self.entrada10 = Entry(self.subcuadro11)
        self.entrada10.focus()
        self.entrada10.grid(row=10, column=1)

        Label(self.subcuadro11, text='fecha quitar: ').grid(row=11, column=0)
        self.entrada11 = Entry(self.subcuadro11)
        self.entrada11.focus()
        self.entrada11.grid(row=11, column=1)
        # Output Messages
        self.message = Label(self.subcuadro11, text='', fg='red')
        self.message.grid(row=12, column=0, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='Save', command=self.add).grid(row=13, columnspan=2, sticky=W + E)
        ttk.Button(self.subcuadro11, text='DELETE').grid(row=14, column=0, sticky=W + E)
        ttk.Button(self.subcuadro11, text='EDIT', command=self.edit).grid(row=14, column=1, sticky=W + E)

        self.subcuadro12 = LabelFrame(self.panelsup, background='white', text='Filtro')
        self.subcuadro12.grid(column=1, row=0, sticky='nsew')
        Label(self.subcuadro12, text='Estado: ').grid(row=0, column=0)

        self.search_var = StringVar()
        self.search_var.trace("w", self.update_list)
        self.entry = Entry(self.subcuadro12, textvariable=self.search_var, width=13)
        self.entry.grid(row=0, column=1)

        self.panelinf = Frame(self.child, background='blue')

        self.panelinf.grid(column=0, row=1, sticky='nsew', pady=2)
        self.panelinf.columnconfigure(0, weight=1)
        self.panelinf.rowconfigure(0, weight=1)

        self.tree = ttk.Treeview(self.panelinf)
        self.tree.grid(column=0, row=0, sticky='nsew')
        ladox = Scrollbar(self.panelinf, orient=HORIZONTAL, command=self.tree.xview)
        ladox.grid(column=0, row=1, sticky='ew')

        ladoy = Scrollbar(self.panelinf, orient=VERTICAL, command=self.tree.yview)
        ladoy.grid(column=1, row=0, sticky='ns')

        self.tree.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)

        # Buttons

        self.get_data()
        self.update_list()

    def run_query(self, query, parameters=()):
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()

        cursor.execute(query, parameters)
        column_names = [desc[0] for desc in cursor.description]
        result = cursor.fetchall()
        global dfdb
        dfdb = pd.DataFrame(result, columns=column_names)
        conn.commit()
        cursor.close()

        return dfdb

    def get_data(self):
        # cleaning Table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = 'SELECT * FROM public."callback sms notifica" '
        db_rows = self.run_query(query)
        db_rows['rol_id'] = db_rows['rol_id'].astype('Int64')
        db_rows['usuario_id'] = db_rows['usuario_id'].astype('Int64')

        # filling data
        self.tree['column'] = list(db_rows.columns)
        self.tree['show'] = "headings"
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        for row in db_rows.to_numpy().tolist():
            self.tree.insert('', 0, values=row)

    def add(self):
        if (len(self.entrada1.get()) == 0 or str(self.entrada1.get())=='None'  or str(self.entrada1.get())=='<NA>'):
            entra1 = None
        else:
            entra1 = self.entrada1.get()
        if (len(self.entrada2.get()) == 0 or str(self.entrada2.get())=='None'  or str(self.entrada2.get())=='<NA>'):
            entra2 = None
        else:
            entra2 = self.entrada2.get()
        if (len(self.entrada3.get()) == 0 or str(self.entrada3.get())=='None'  or str(self.entrada3.get())=='<NA>'):
            entra3 = None
        else:
            entra3 = self.entrada3.get()
        if (len(self.entrada4.get()) == 0 or str(self.entrada4.get())=='None'  or str(self.entrada4.get())=='<NA>'):
            entra4 = None
        else:
            entra4 = self.entrada4.get()
        if (len(self.entrada5.get()) == 0 or str(self.entrada5.get())=='None'  or str(self.entrada5.get())=='<NA>'):
            entra5 = None
        else:
            entra5 = self.entrada5.get()
        if (len(self.entrada6.get()) == 0 or str(self.entrada6.get())=='None'  or str(self.entrada6.get())=='<NA>'):
            entra6 = None
        else:
            entra6 = self.entrada6.get()
        if (len(self.entrada7.get()) == 0 or str(self.entrada7.get())=='None'  or str(self.entrada7.get())=='<NA>'):
            entra7 = None
        else:
            entra7 = self.entrada7.get()
        if (len(self.entrada8.get()) == 0 or str(self.entrada8.get())=='None'  or str(self.entrada8.get())=='<NA>'):
            entra8 = None
        else:
            entra8 = self.entrada8.get()
        if (len(self.entrada9.get()) == 0 or str(self.entrada9.get())=='None'  or str(self.entrada9.get())=='<NA>'):
            entra9 = None
        else:
            entra9 = self.entrada9.get()
        if (len(self.entrada10.get()) == 0 or str(self.entrada10.get())=='None'  or str(self.entrada10.get())=='<NA>'):
            entra10 = None
        else:
            entra10 = self.entrada10.get()
        if (len(self.entrada11.get()) == 0 or str(self.entrada11.get())=='None'  or str(self.entrada11.get())=='<NA>'):
            entra11 = None
        else:
            entra11 = self.entrada11.get()

        if( entra5==None and entra3==None):
            self.message['text'] = 'Login y Estado son necesarios'
        else:
            query = """INSERT INTO public."callback sms notifica"(usuario_id, rol_id, login, nombre, estado, "abm alta", "fecha alta", "abm baja", "fecha baja", "abm quitar", "fecha quitar") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            parameters = (entra1,
                      entra2,
                      entra3,
                      entra4,
                      entra5,
                      entra6,
                      entra7,
                      entra8,
                      entra9,
                      entra10,
                      entra11
                      )
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()

            cursor.execute(query, parameters)
            self.entrada1.delete(0, END)
            self.entrada2.delete(0, END)
            self.entrada3.delete(0, END)
            self.entrada4.delete(0, END)
            self.entrada5.delete(0, END)
            self.entrada6.delete(0, END)
            self.entrada7.delete(0, END)
            self.entrada8.delete(0, END)
            self.entrada9.delete(0, END)
            self.entrada10.delete(0, END)
            self.entrada11.delete(0, END)
            conn.commit()
            cursor.close()
            self.get_data()

    def edit(self):

        select = self.tree.item(self.tree.selection())['values']

        self.edit_wind = Toplevel(self.child)
        self.edit_wind.title = 'Edit'

        Label(self.edit_wind, text='usuario_id: ').grid(row=0, column=1)
        new_entrada1 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[0]))
        new_entrada1.grid(row=0, column=2)

        Label(self.edit_wind, text='rol_id: ').grid(row=1, column=1)
        new_entrada2 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[1]))
        new_entrada2.grid(row=1, column=2)

        Label(self.edit_wind, text='login: ').grid(row=2, column=1)
        new_entrada3 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[2]))
        new_entrada3.grid(row=2, column=2)

        Label(self.edit_wind, text='nombre: ').grid(row=3, column=1)
        new_entrada4 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[3]))
        new_entrada4.grid(row=3, column=2)

        Label(self.edit_wind, text='estado: ').grid(row=4, column=1)
        new_entrada5 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[4]))
        new_entrada5.grid(row=4, column=2)

        Label(self.edit_wind, text='abm alta: ').grid(row=5, column=1)
        new_entrada6 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[5]))
        new_entrada6.grid(row=5, column=2)

        Label(self.edit_wind, text='fecha alta: ').grid(row=6, column=1)
        new_entrada7 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[6]))
        new_entrada7.grid(row=6, column=2)

        Label(self.edit_wind, text='abm baja: ').grid(row=7, column=1)
        new_entrada8 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[7]))
        new_entrada8.grid(row=7, column=2)

        Label(self.edit_wind, text='fecha baja: ').grid(row=8, column=1)
        new_entrada9 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[8]))
        new_entrada9.grid(row=8, column=2)

        Label(self.edit_wind, text='abm quitar: ').grid(row=9, column=1)
        new_entrada10 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[9]))
        new_entrada10.grid(row=9, column=2)

        Label(self.edit_wind, text='fecha quitar: ').grid(row=10, column=1)
        new_entrada11 = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=select[10]))
        new_entrada11.grid(row=10, column=2)

        self.messageedit = Label(self.edit_wind, text='', fg='red')
        self.messageedit.grid(row=12, column=0, columnspan=2, sticky=W + E)
        Button(self.edit_wind, text='Actualizar', command=lambda: self.edit_records(new_entrada1.get(),
                                                                                    new_entrada2.get(),
                                                                                    new_entrada3.get(),
                                                                                    new_entrada4.get(),
                                                                                    new_entrada5.get(),
                                                                                    new_entrada6.get(),
                                                                                    new_entrada7.get(),
                                                                                    new_entrada8.get(),
                                                                                    new_entrada9.get(),
                                                                                    new_entrada10.get(),
                                                                                    new_entrada11.get(),
                                                                                    select[0],
                                                                                    select[2]

                                                                                    )).grid(row=12, column=2, sticky=W)

        self.edit_wind.mainloop()

    def edit_records(self, idlogin, idrol, login, nombre, estado, aalta, falta, abaja, fbaja, aquitar, fquitar, idold,
                     loginold):
        if (len(idlogin) == 0 or str(idlogin) == 'None' or str(idlogin) == '<NA>'):
            entra1 = None
        else:
            entra1 = idlogin
        if (len(idrol) == 0 or str(idrol) == 'None' or str(idrol) == '<NA>'):
            entra2 = None
        else:
            entra2 = idrol
        if (len(login) == 0 or str(login) == 'None' or str(login) == '<NA>'):
            entra3 = None
        else:
            entra3 = login
        if (len(nombre) == 0 or str(nombre) == 'None' or str(nombre) == '<NA>'):
            entra4 = None
        else:
            entra4 = nombre
        if (len(estado) == 0 or str(estado) == 'None' or str(estado) == '<NA>'):
            entra5 = None
        else:
            entra5 = estado
        if (len(aalta) == 0 or str(aalta) == 'None' or str(aalta) == '<NA>'):
            entra6 = None
        else:
            entra6 = aalta
        if (len(falta) == 0 or str(falta) == 'None' or str(falta) == '<NA>'):
            entra7 = None
        else:
            entra7 = falta
        if (len(abaja) == 0 or str(abaja) == 'None' or str(abaja) == '<NA>'):
            entra8 = None
        else:
            entra8 = abaja
        if (len(fbaja) == 0 or str(fbaja) == 'None' or str(fbaja) == '<NA>'):
            entra9 = None
        else:
            entra9 = fbaja
        if (len(aquitar) == 0 or str(aquitar) == 'None' or str(
                aquitar) == '<NA>'):
            entra10 = None
        else:
            entra10 = aquitar
        if (len(fquitar) == 0 or str(fquitar) == 'None' or str(
                fquitar) == '<NA>'):
            entra11 = None
        else:
            entra11 = fquitar

        if (entra5 == None and entra3 == None):
            self.messageedit['text'] = 'Login y Estado son necesarios'
        else:
            query = 'UPDATE public."callback sms notifica" SET usuario_id = %s, rol_id= %s, login= %s, nombre = %s, estado= %s, "abm alta"= %s, "fecha alta"= %s, "abm baja"= %s, "fecha baja"= %s, "abm quitar"= %s, "fecha quitar" = %s WHERE usuario_id = %s AND login= %s'
            parameters = (
            entra1, entra2, entra3, entra4, entra5, entra6, entra7, entra8, entra9, entra10, entra11, idold, loginold)
            host = '127.0.0.1'
            user = 'postgres'
            password = 'postgres'
            database = 'testabm'

            conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
            cursor = conn.cursor()
            cursor.execute(query, parameters)
            conn.commit()
            cursor.close()
            self.edit_wind.destroy()

            self.get_data()

    def update_list(self, *args):
        search_term = self.search_var.get()

        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        mask = dfdb['estado'].str.contains(search_term, case=False, na=False)

        self.tree['column'] = list(dfdb[mask].columns)
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        df_fila2 = dfdb[mask].to_numpy().tolist()
        for fila2 in df_fila2:
            self.tree.insert('', 'end', values=fila2)

    def delete(self):

        select = self.tree.item(self.tree.selection())['values']
        query = 'UPDATE public."callback sms notifica" SET  estado='f'  WHERE   login= %s'
        parameters = (
            select[2])
        host = '127.0.0.1'
        user = 'postgres'
        password = 'postgres'
        database = 'testabm'

        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=database)
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        conn.commit()
        cursor.close()


        self.get_data()


if __name__ == '__main__':
    window = Tk()
    aplication = Register(window)
    s = ttk.Style()
    s.theme_use('alt')

    s.configure(".", font=('Arial', 14), foreground='red2')

    s.configure("Treeview", font=('Helvetica', 12), foreground='black', background='white')
    s.map('Treeview', background=[('selected', 'green2')], foreground=[('selected', 'black')])

    window.mainloop()
