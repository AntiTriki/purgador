from tkinter import Tk, Entry, Label, Button, Frame, messagebox, filedialog, ttk, Scrollbar, VERTICAL, HORIZONTAL
import pandas as pd
import tkinter as tk
import sqlalchemy
import psycopg2 
from sqlalchemy import create_engine
import datetime
from tkinter import *

from test import NewMember

class Register(tk.Frame):
    def __init__(self, window, *args,**kwargs):
        tk.Frame.__init__(self,window)
        self.wind = window
        self.wind.title('ABM')
        menubar = Menu(self.wind)
        self.wind.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="App Informativa",command=self.openAppInformativa)
        filemenu.add_command(label="Callback SMS Notifica", command=self.openCallbackSMS)
        filemenu.add_command(label="callbackhvc", command=self.opencallbackhvc)
        filemenu.add_command(label="cms17", command=self.opencms17 )
        filemenu.add_command(label="cms 19", command=self.opencms19 )
        filemenu.add_command(label="Integración EBS", command=self.openIntegracionEBS )
        filemenu.add_command(label="Llamadas molestosas", command=self.openLlamadasmolestosas )
        filemenu.add_command(label="Rellamadas", command=self.openRellamadas )
        filemenu.add_command(label="Requerimientos Fiscales", command=self.openRequerimientosFiscales )
        filemenu.add_command(label="SMS Notifica", command=self.openSMSNotifica)
        filemenu.add_command(label="Tallycode", command=self.openTallycode)
        filemenu.add_command(label="Todos", command=self.openTodos)
        filemenu.add_command(label="TR4", command=self.openTR4)
        filemenu.add_command(label="wfo", command=self.openwfo)
        filemenu.add_command(label="wfo acr", command=self.openwfoacr)
        
        
        menubar.add_cascade(label="Tipo de ABM", menu=filemenu)
        
    def openAppInformativa(self):    
        self.appi= tk.Toplevel(self.wind)
        self.addClass = NewAppi(self.wind, self.appi)
    def openCallbackSMS(self):    
        self.appi= tk.Toplevel(self.wind)
        self.addClass = NewCSMS(self.wind, self.appi)
    def opencallbackhvc(self):    
        self.appi= tk.Toplevel(self.wind)
        self.addClass = NewCHVC(self.wind, self.appi)
    def opencms17(self):    
        self.appi= tk.Toplevel(self.wind)
        self.addClass = NewAppi(self.wind, self.appi)
    def opencms19(self):    
        self.appi= tk.Toplevel(self.wind)
        self.addClass = NewAppi(self.wind, self.appi)
    def openIntegracionEBS(self):    
        self.appi= tk.Toplevel(self.wind)
        self.addClass = NewAppi(self.wind, self.appi)
    def openLlamadasmolestosas(self):    
        self.appi= tk.Toplevel(self.wind)
        self.addClass = NewAppi(self.wind, self.appi)
    def openRellamadas(self):    
        self.appi= tk.Toplevel(self.wind)
        self.addClass = NewAppi(self.wind, self.appi)
    def openRequerimientosFiscales(self):    
        self.appi= tk.Toplevel(self.wind)
        self.addClass = NewAppi(self.wind, self.appi)
    def openSMSNotifica(self):    
        self.appi= tk.Toplevel(self.wind)
        self.addClass = NewAppi(self.wind, self.appi)
    def openTallycode(self):    
        self.appi= tk.Toplevel(self.wind)
        self.addClass = NewAppi(self.wind, self.appi)
    def openTodos(self):    
        self.appi= tk.Toplevel(self.wind)
        self.addClass = NewAppi(self.wind, self.appi)
    def openTR4(self):    
        self.appi= tk.Toplevel(self.wind)
        self.addClass = NewAppi(self.wind, self.appi)
    def openwfo(self):    
        self.appi= tk.Toplevel(self.wind)
        self.addClass = NewAppi(self.wind, self.appi)
    def openwfoacr(self):    
        self.appi= tk.Toplevel(self.wind)
        self.addClass = NewAppi(self.wind, self.appi)

class NewAppi(tk.Frame):
    def __init__(self, wind, child, *args, **kwargs):
        tk.Frame.__init__(self,child)
        self.parent = wind
        self.child = child
        self.child.title("App Informativa")
class NewCSMS(tk.Frame):
    def __init__(self, wind, child, *args, **kwargs):
        tk.Frame.__init__(self,child)
        self.parent = wind
        self.child = child
        self.child.title("Callback SMS")
        
        self.child.focus_set()
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(0, weight=1)
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(1, weight=1)
        self.panelsup= Frame(self.child)
        self.panelsup.grid(column=0, row=0, sticky = 'nsew')
        self.panelsup.columnconfigure(0, weight=1)
        self.panelsup.rowconfigure(0, weight=1)
        self.panelsup.columnconfigure(1, weight=1)
        self.panelsup.rowconfigure(0, weight=1)


        self.subcuadro11 = LabelFrame(self.panelsup, background='white', text = 'Registrar Callback SMS Notificacion')
        
        self.subcuadro11.grid(column=0, row=0, sticky='nsew')
        

       
        Label(self.subcuadro11, text = 'usuario_id: ').grid(row = 1, column = 0)
        self.entrada1 = Entry(self.subcuadro11)
        self.entrada1.focus()
        self.entrada1.grid(row = 1, column = 1)

        Label(self.subcuadro11, text = 'rol_id: ').grid(row = 2, column = 0)
        self.entrada2 = Entry(self.subcuadro11)
        self.entrada2.focus()
        self.entrada2.grid(row = 2, column = 1)

        Label(self.subcuadro11, text = 'login: ').grid(row = 3, column = 0)
        self.entrada3 = Entry(self.subcuadro11)
        self.entrada3.focus()
        self.entrada3.grid(row = 3, column = 1)


        Label(self.subcuadro11, text = 'nombre: ').grid(row = 4, column = 0)
        self.entrada4 = Entry(self.subcuadro11)
        self.entrada4.focus()
        self.entrada4.grid(row = 4, column = 1)

        Label(self.subcuadro11, text = 'estado: ').grid(row = 5, column = 0)
        self.entrada5 = Entry(self.subcuadro11)
        self.entrada5.focus()
        self.entrada5.grid(row = 5, column = 1)

        Label(self.subcuadro11, text = 'abm alta: ').grid(row = 6, column = 0)
        self.entrada6 = Entry(self.subcuadro11)
        self.entrada6.focus()
        self.entrada6.grid(row = 6, column = 1)

        Label(self.subcuadro11, text = 'fecha alta: ').grid(row = 7, column = 0)
        self.entrada7 = Entry(self.subcuadro11)
        self.entrada7.focus()
        self.entrada7.grid(row = 7, column = 1)


        Label(self.subcuadro11, text = 'abm baja: ').grid(row = 8, column = 0)
        self.entrada8 = Entry(self.subcuadro11)
        self.entrada8.focus()
        self.entrada8.grid(row = 8, column = 1)



        Label(self.subcuadro11, text = 'fecha baja: ').grid(row = 9, column = 0)
        self.entrada9 = Entry(self.subcuadro11)
        self.entrada9.focus()
        self.entrada9.grid(row = 9, column = 1)

        Label(self.subcuadro11, text = 'abm quitar: ').grid(row = 10, column = 0)
        self.entrada10 = Entry(self.subcuadro11)
        self.entrada10.focus()
        self.entrada10.grid(row = 10, column = 1)

        Label(self.subcuadro11, text = 'fecha quitar: ').grid(row = 11, column = 0)
        self.entrada11 = Entry(self.subcuadro11)
        self.entrada11.focus()
        self.entrada11.grid(row = 11, column = 1)
        ttk.Button(self.subcuadro11, text = 'Save', command=self.add).grid(row = 12, columnspan = 2, sticky = W + E)
        ttk.Button(self.subcuadro11, text = 'DELETE').grid(row = 13, column = 0, sticky = W + E)
        ttk.Button(self.subcuadro11, text = 'EDIT', command=self.edit).grid(row = 13, column = 1, sticky = W + E)
        
        self.subcuadro12 = LabelFrame(self.panelsup, background='white', text='Filtro')
        self.subcuadro12.grid(column=1, row=0, sticky='nsew')
        Label(self.subcuadro12, text = 'Estado: ').grid(row = 0, column = 0)
        
        self.search_var = StringVar()
        self.search_var.trace("w", self.update_list)
        self.entry = Entry(self.subcuadro12, textvariable=self.search_var, width=13)
        self.entry.grid(row = 0, column = 1)  



        self.panelinf = Frame(self.child, background='blue')
        
        self.panelinf.grid(column=0, row=1, sticky='nsew',  pady = 2)
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
    def run_query(self, query, parameters= ()):
        host='127.0.0.1'
        user='postgres'
        password='postgres'
        database='testabm'
        
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
        
         # filling data
        self.tree['column']=list(db_rows.columns)
        self.tree['show'] = "headings"
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)
        
        
        
        
            
        for row in db_rows.to_numpy().tolist():
            
            self.tree.insert('', 0, values = row)
    
    def add(self):
        if (len(self.entrada1.get())==0):
            entra1= None
        else:
            entra1 = self.entrada1.get()
        if (len(self.entrada2.get())==0):
            entra2= None
        else:
            entra2 = self.entrada2.get()
        if (len(self.entrada3.get())==0):
            entra3= None
        else:
            entra3 = self.entrada3.get()
        if (len(self.entrada4.get())==0):
            entra4= None
        else:
            entra4 = self.entrada4.get()
        if (len(self.entrada5.get())==0):
            entra5= None
        else:
            entra5 = self.entrada5.get()
        if (len(self.entrada6.get())==0):
            entra6= None
        else:
            entra6 = self.entrada6.get()
        if (len(self.entrada7.get())==0):
            entra7 = None
        else:
            entra7 = self.entrada7.get()
        if (len(self.entrada8.get())==0):
            entra8= None
        else:
            entra8 = self.entrada8.get()
        if (len(self.entrada9.get())==0):
            entra9= None
        else:
            entra9 = self.entrada9.get()
        if (len(self.entrada10.get())==0):
            entra10= None
        else:
            entra10 = self.entrada10.get()
        if (len(self.entrada11.get())==0):
            entra11= None
        else:
            entra11 = self.entrada11.get()
            
        
        query = """INSERT INTO public."callback sms notifica"(usuario_id, rol_id, login, nombre, estado, "abm alta", "fecha alta", "abm baja", "fecha baja", "abm quitar", "fecha quitar") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        parameters =  (entra1,
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
        host='127.0.0.1'
        user='postgres'
        password='postgres'
        database='testabm'
        
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
        
        
        
        select=self.tree.item(self.tree.selection())['values']
        
        self.edit_wind = Toplevel(self.child)
        self.edit_wind.title = 'Edit'
        
     
        Label(self.edit_wind, text = 'usuario_id: ').grid(row = 0, column = 1)
        new_entrada1 = Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = select[0]))
        new_entrada1.grid(row = 0, column = 2)
        
        Label(self.edit_wind, text = 'rol_id: ').grid(row = 1, column = 1)
        new_entrada2 = Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = select[1]))
        new_entrada2.grid(row = 1, column = 2)
        
        Label(self.edit_wind, text = 'login: ').grid(row = 2, column = 1)
        new_entrada3 = Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = select[2]))
        new_entrada3.grid(row = 2, column = 2)
        
        Label(self.edit_wind, text = 'nombre: ').grid(row = 3, column = 1)
        new_entrada4 = Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = select[3]))
        new_entrada4.grid(row = 3, column = 2)
        
        Label(self.edit_wind, text = 'estado: ').grid(row = 4, column = 1)
        new_entrada5 = Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = select[4]))
        new_entrada5.grid(row = 4, column = 2)
        
        Label(self.edit_wind, text = 'abm alta: ').grid(row = 5, column = 1)
        new_entrada6 = Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = select[5]))
        new_entrada6.grid(row = 5, column = 2)
        
        Label(self.edit_wind, text = 'fecha alta: ').grid(row = 6, column = 1)
        new_entrada7 = Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = select[6]))
        new_entrada7.grid(row = 6, column = 2)
        
        Label(self.edit_wind, text = 'abm baja: ').grid(row = 7, column = 1)
        new_entrada8 = Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = select[7]))
        new_entrada8.grid(row = 7, column = 2)
        
        Label(self.edit_wind, text = 'fecha baja: ').grid(row = 8, column = 1)
        new_entrada9 = Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = select[8]))
        new_entrada9.grid(row = 8, column = 2)
        
        Label(self.edit_wind, text = 'abm quitar: ').grid(row = 9, column = 1)
        new_entrada10 = Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = select[9]))
        new_entrada10.grid(row = 9, column = 2)
        
        Label(self.edit_wind, text = 'fecha quitar: ').grid(row = 10, column = 1)
        new_entrada11 = Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = select[10]))
        new_entrada11.grid(row = 10, column = 2)
        Button(self.edit_wind, text = 'Actualizar', command = lambda: self.edit_records(new_entrada1.get(),
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
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                        )).grid(row = 12, column = 2, sticky = W)
        
        
        self.edit_wind.mainloop()

    def edit_records(self, idlogin, idrol,login,nombre, estado, aalta,falta,abaja,fbaja,aquitar,fquitar,idold,loginold):
        query = 'UPDATE public."callback sms notifica" SET usuario_id = %s, rol_id= %s, login= %s, nombre = %s, estado= %s, "abm alta"= %s, "fecha alta"= %s, "abm baja"= %s, "fecha baja"= %s, "abm quitar"= %s, "fecha quitar" = %s WHERE usuario_id = %s AND login= %s'
        parameters = (idlogin, idrol,login,nombre, estado, aalta,falta,abaja,fbaja,aquitar,fquitar,idold,loginold)
        host='127.0.0.1'
        user='postgres'
        password='postgres'
        database='testabm'
        
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
        mask = dfdb['estado'].str.contains(search_term, case= False, na=False)
        
        self.tree['column']=list(dfdb[mask].columns)
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        df_fila2 = dfdb[mask].to_numpy().tolist()
        for fila2 in df_fila2:
            self.tree.insert('', 'end', values=fila2)

                
    
    

        
class NewCHVC(tk.Frame):
    def __init__(self, wind, child, *args, **kwargs):
        tk.Frame.__init__(self,child)
        self.parent = wind
        self.child = child
        self.child.title("Callbackhvc")
        
        self.child.focus_set()
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(0, weight=1)
        self.child.columnconfigure(0, weight=1)
        self.child.rowconfigure(1, weight=1)
        self.panelsup= Frame(self.child)
        self.panelsup.grid(column=0, row=0, sticky = 'nsew')
        self.panelsup.columnconfigure(0, weight=1)
        self.panelsup.rowconfigure(0, weight=1)
        self.panelsup.columnconfigure(1, weight=1)
        self.panelsup.rowconfigure(0, weight=1)


        self.subcuadro11 = LabelFrame(self.panelsup, background='white', text = 'Registrar Callback SMS Notificacion')
        
        self.subcuadro11.grid(column=0, row=0, sticky='nsew')
        

       
        Label(self.subcuadro11, text = 'CI: ').grid(row = 1, column = 0)
        self.entrada1 = Entry(self.subcuadro11)
        self.entrada1.focus()
        self.entrada1.grid(row = 1, column = 1)

        Label(self.subcuadro11, text = 'carga_hora_id: ').grid(row = 2, column = 0)
        self.entrada2 = Entry(self.subcuadro11)
        self.entrada2.focus()
        self.entrada2.grid(row = 2, column = 1)

        Label(self.subcuadro11, text = 'operador: ').grid(row = 3, column = 0)
        self.entrada3 = Entry(self.subcuadro11)
        self.entrada3.focus()
        self.entrada3.grid(row = 3, column = 1)


        Label(self.subcuadro11, text = 'nombre: ').grid(row = 4, column = 0)
        self.entrada4 = Entry(self.subcuadro11)
        self.entrada4.focus()
        self.entrada4.grid(row = 4, column = 1)

        Label(self.subcuadro11, text = 'apellido: ').grid(row = 5, column = 0)
        self.entrada5 = Entry(self.subcuadro11)
        self.entrada5.focus()
        self.entrada5.grid(row = 5, column = 1)

        Label(self.subcuadro11, text = 'correo: ').grid(row = 6, column = 0)
        self.entrada6 = Entry(self.subcuadro11)
        self.entrada6.focus()
        self.entrada6.grid(row = 6, column = 1)

        Label(self.subcuadro11, text = 'login: ').grid(row = 7, column = 0)
        self.entrada7 = Entry(self.subcuadro11)
        self.entrada7.focus()
        self.entrada7.grid(row = 7, column = 1)


        Label(self.subcuadro11, text = 'estado: ').grid(row = 8, column = 0)
        self.entrada8 = Entry(self.subcuadro11)
        self.entrada8.focus()
        self.entrada8.grid(row = 8, column = 1)



        Label(self.subcuadro11, text = 'abm alta: ').grid(row = 9, column = 0)
        self.entrada9 = Entry(self.subcuadro11)
        self.entrada9.focus()
        self.entrada9.grid(row = 9, column = 1)

        Label(self.subcuadro11, text = 'fecha alta: ').grid(row = 10, column = 0)
        self.entrada10 = Entry(self.subcuadro11)
        self.entrada10.focus()
        self.entrada10.grid(row = 10, column = 1)

        Label(self.subcuadro11, text = 'abm baja: ').grid(row = 11, column = 0)
        self.entrada11 = Entry(self.subcuadro11)
        self.entrada11.focus()
        self.entrada11.grid(row = 11, column = 1)
        ttk.Button(self.subcuadro11, text = 'Save', command=self.add).grid(row = 12, columnspan = 2, sticky = W + E)
        ttk.Button(self.subcuadro11, text = 'DELETE').grid(row = 13, column = 0, sticky = W + E)
        ttk.Button(self.subcuadro11, text = 'EDIT', command=self.edit).grid(row = 13, column = 1, sticky = W + E)
        
        self.subcuadro12 = LabelFrame(self.panelsup, background='white', text='Filtro')
        self.subcuadro12.grid(column=1, row=0, sticky='nsew')
        Label(self.subcuadro12, text = 'Estado: ').grid(row = 0, column = 0)
        
        self.search_var = StringVar()
        self.search_var.trace("w", self.update_list)
        self.entry = Entry(self.subcuadro12, textvariable=self.search_var, width=13)
        self.entry.grid(row = 0, column = 1)  



        self.panelinf = Frame(self.child, background='blue')
        
        self.panelinf.grid(column=0, row=1, sticky='nsew',  pady = 2)
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
    def run_query(self, query, parameters= ()):
        host='127.0.0.1'
        user='postgres'
        password='postgres'
        database='testabm'
        
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
        
         # filling data
        self.tree['column']=list(db_rows.columns)
        self.tree['show'] = "headings"
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)
        
        
        
        
            
        for row in db_rows.to_numpy().tolist():
            
            self.tree.insert('', 0, values = row)
    
    def add(self):
        
        
        
        query = """INSERT INTO public."callback sms notifica"(usuario_id, rol_id, login, nombre, estado, "abm alta", "fecha alta", "abm baja", "fecha baja", "abm quitar", "fecha quitar") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        parameters =  (self.entrada1.get(), 
                       self.entrada2.get(),
                       self.entrada3.get(),
                       self.entrada4.get(),
                       self.entrada5.get(),
                       self.entrada6.get(),
                       self.entrada7.get(),
                       self.entrada8.get(),
                       self.entrada9.get(),
                       self.entrada10.get(),
                       self.entrada11.get())
        host='127.0.0.1'
        user='postgres'
        password='postgres'
        database='testabm'
        
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
        
        self.get_data()
        
    
    
    def edit(self):
        
        
        
        select=self.tree.item(self.tree.selection())['values']
        
        self.edit_wind = Toplevel(self.child)
        self.edit_wind.title = 'Edit'
        
     
        Label(self.edit_wind, text = 'usuario_id: ').grid(row = 0, column = 1)
        new_entrada1 = Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = select[0]))
        new_entrada1.grid(row = 0, column = 2)
        
        Label(self.edit_wind, text = 'rol_id: ').grid(row = 1, column = 1)
        new_entrada2 = Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = select[1]))
        new_entrada2.grid(row = 1, column = 2)
        
        Label(self.edit_wind, text = 'login: ').grid(row = 2, column = 1)
        new_entrada3 = Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = select[2]))
        new_entrada3.grid(row = 2, column = 2)
        
        Label(self.edit_wind, text = 'nombre: ').grid(row = 3, column = 1)
        new_entrada4 = Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = select[3]))
        new_entrada4.grid(row = 3, column = 2)
        
        Label(self.edit_wind, text = 'estado: ').grid(row = 4, column = 1)
        new_entrada5 = Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = select[4]))
        new_entrada5.grid(row = 4, column = 2)
        
        Label(self.edit_wind, text = 'abm alta: ').grid(row = 5, column = 1)
        new_entrada6 = Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = select[5]))
        new_entrada6.grid(row = 5, column = 2)
        
        Label(self.edit_wind, text = 'fecha alta: ').grid(row = 6, column = 1)
        new_entrada7 = Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = select[6]))
        new_entrada7.grid(row = 6, column = 2)
        
        Label(self.edit_wind, text = 'abm baja: ').grid(row = 7, column = 1)
        new_entrada8 = Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = select[7]))
        new_entrada8.grid(row = 7, column = 2)
        
        Label(self.edit_wind, text = 'fecha baja: ').grid(row = 8, column = 1)
        new_entrada9 = Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = select[8]))
        new_entrada9.grid(row = 8, column = 2)
        
        Label(self.edit_wind, text = 'abm quitar: ').grid(row = 9, column = 1)
        new_entrada10 = Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = select[9]))
        new_entrada10.grid(row = 9, column = 2)
        
        Label(self.edit_wind, text = 'fecha quitar: ').grid(row = 10, column = 1)
        new_entrada11 = Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = select[10]))
        new_entrada11.grid(row = 10, column = 2)
        Button(self.edit_wind, text = 'Actualizar', command = lambda: self.edit_records(new_entrada1.get(),
                                                             )).grid(row = 12, column = 2, sticky = W)
        
        
        self.edit_wind.mainloop()

    def edit_records(self, idlogin, idrol,login,nombre, estado, aalta,falta,abaja,fbaja,aquitar,fquitar,idold,loginold):
        query = 'UPDATE public."callback sms notifica" SET usuario_id = %s, rol_id= %s, login= %s, nombre = %s, estado= %s, "abm alta"= %s, "fecha alta"= %s, "abm baja"= %s, "fecha baja"= %s, "abm quitar"= %s, "fecha quitar" = %s WHERE usuario_id = %s AND login= %s'
        parameters = (idlogin, idrol,login,nombre, estado, aalta,falta,abaja,fbaja,aquitar,fquitar,idold,loginold)
        host='127.0.0.1'
        user='postgres'
        password='postgres'
        database='testabm'
        
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

        # Just a generic list to populate the listbox
        
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        mask = dfdb['estado'].str.contains(search_term, case= False, na=False)
        
        self.tree['column']=list(dfdb[mask].columns)
        for columna2 in self.tree['column']:
            self.tree.heading(columna2, text=columna2)

        df_fila2 = dfdb[mask].to_numpy().tolist()
        for fila2 in df_fila2:
            self.tree.insert('', 'end', values=fila2)

        



if __name__=='__main__':
    window= Tk()
    aplication = Register(window)
    s = ttk.Style()
    s.theme_use('alt')

    s.configure(".", font=('Arial', 14), foreground='red2')
    
    s.configure("Treeview", font=('Helvetica', 12), foreground='black', background='white')
    s.map('Treeview', background=[('selected', 'green2')], foreground=[('selected', 'black')])

    window.mainloop()
