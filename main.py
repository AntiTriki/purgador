from tkinter import Tk, Entry, Label, Button, Frame, messagebox, filedialog, ttk, Scrollbar, VERTICAL, HORIZONTAL
import pandas as pd
import tkinter as tk
import sqlalchemy
import psycopg2
from sqlalchemy import create_engine
import datetime

user = 'postgres'
password ='12345678'
host='127.0.0.1'
database='testabm'
ventana = tk.Tk()
ventana.config(bg='yellow')

ventana.title('CARGA')
ventana.configure(background='black')
ventana.focus_set()

engine =create_engine("postgresql+psycopg2://postgres:12345678@localhost:5432/testabm")

def sheets(datos,archivo):
    if(datos == 'todos'):
        df = pd.read_excel(archivo,datos)
        df.to_sql(name='todos',con=engine, if_exists='append',index=False)
    elif(datos == 'llamadas molestosas'):
        df = pd.read_excel(archivo,datos)
        df.to_sql(name='llamadas molestosas',con=engine, if_exists='append',index=False)
    elif (datos == 'TR4'):
        df = pd.read_excel(archivo, datos)
        df.to_sql(name='tr4', con=engine, if_exists='append', index=False)
    elif (datos == 'Tallycode'):
        df = pd.read_excel(archivo, datos)
        df.to_sql(name='tallycode', con=engine, if_exists='append', index=False)
    elif (datos == 'Callbackhvc'):
        df = pd.read_excel(archivo, datos)
        df.to_sql(name='callbackhvc', con=engine, if_exists='append', index=False)
    elif (datos == 'rellamadas'):
        df = pd.read_excel(archivo, datos)
        df.to_sql(name='rellamadas', con=engine, if_exists='append', index=False)
    elif (datos == 'callback sms notifica'):
        df = pd.read_excel(archivo, datos)
        df.to_sql(name='callback sms notifica', con=engine, if_exists='append', index=False)
    elif (datos == 'integracion ebs'):
        df = pd.read_excel(archivo, datos)
        df.to_sql(name='integracion ebs', con=engine, if_exists='append', index=False)
    elif (datos == 'Requerimientos Fiscales'):
        df = pd.read_excel(archivo, datos)
        df.to_sql(name='requerimientos fiscales', con=engine, if_exists='append', index=False)
    elif (datos == 'SMS Notifica'):
        df = pd.read_excel(archivo, datos)
        df.to_sql(name='sms notifica', con=engine, if_exists='append', index=False)
    elif (datos == 'App Informativa'):
        df = pd.read_excel(archivo, datos)
        df.to_sql(name='app informativa', con=engine, if_exists='append', index=False)
    elif (datos == 'CMS 19'):
        df = pd.read_excel(archivo, datos)
        df.to_sql(name='cms 19', con=engine, if_exists='append', index=False)
    elif (datos == 'CMS17'):
        df = pd.read_excel(archivo, datos)
        df.to_sql(name='cms17', con=engine, if_exists='append', index=False)
    elif (datos == 'WFO'):
        df = pd.read_excel(archivo, datos)
        df.to_sql(name='wfo', con=engine, if_exists='append', index=False)
    elif (datos == 'WFO ACR'):
        df = pd.read_excel(archivo, datos)
        df.to_sql(name='wfo acr', con=engine, if_exists='append', index=False)

def sqlcol(dfparam):  # Creacion de columnas con su tipo correspondiente de acuerdo al tipo de dato entregado por el DataFrame

    dtypedict = {}
    for i, j in zip(dfparam.columns, dfparam.dtypes):
        if ("fecha" in str(i)):
            dtypedict.update({i: sqlalchemy.types.VARCHAR(length=255)})

        else:
            if "object" in str(j):
                dtypedict.update({i: sqlalchemy.types.VARCHAR(length=255)})

            if "datetime" in str(j):
                dtypedict.update({i: sqlalchemy.types.VARCHAR(length=255)})

            if "float" in str(j):
                dtypedict.update({i: sqlalchemy.types.VARCHAR(length=255)})

            if "int" in str(j):
                dtypedict.update({i: sqlalchemy.types.VARCHAR(length=255)})

            if "real" in str(j):
                dtypedict.update({i: sqlalchemy.types.VARCHAR(length=255)})

    return dtypedict

def procesar(table,xl):
    df = pd.read_excel(xl, table)
    engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}/{database}', pool_recycle=3600);
    cnx = engine.connect();
    table_engine = table
    try:
        format = sqlcol(df)
        frame = df.to_sql(table_engine, cnx, if_exists='append', index=False, dtype=format);
    except Exception as ex:
        print(ex)
    else:
        print('Datos ingresados')
    finally:
        cnx.close()





def datos_db():
    archivo = filedialog.askopenfilename(initialdir='/',
                                         title='Seleccione archivo',
                                         filetypes=(('xlsx files', '*.xlsx*'), ('All files', '*.*')))
    etiqueta['text'] = archivo

    global archivoexcel
    archivoexcel = r'{}'.format(archivo)
    print(archivoexcel)

    global xl
    xl = pd.ExcelFile(archivoexcel)

    list_sheet = xl.sheet_names
    print(list_sheet)
def process():
    for sheet in xl.sheet_names:
        procesar(sheet,xl)



Button(ventana, text='Cargar', bg='magenta', command=datos_db).grid(column=0, row=0, sticky='nsew', padx=5, pady=5)
etiqueta = Label(ventana)
etiqueta.grid(row=0, column=1)
Button(ventana, text='Procesar', bg='magenta', command=process).grid(column=0, row=1, sticky='nsew', padx=5, pady=5)



ventana.mainloop()
