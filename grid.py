from tkinter import Tk, Entry, Label, Button, Frame, messagebox, filedialog, ttk, Scrollbar, VERTICAL, HORIZONTAL
import pandas as pd
import tkinter as tk
import sqlalchemy
import psycopg2 
from sqlalchemy import create_engine
import datetime

def sqlcol(dfparam):   #Creacion de columnas con su tipo correspondiente de acuerdo al tipo de dato entregado por el DataFrame 
    
    dtypedict = {}
    for i,j in zip(dfparam.columns, dfparam.dtypes):
        if "object" in str(j):
            dtypedict.update({i: sqlalchemy.types.VARCHAR(length=255)})
                                 
        if "datetime" in str(j):
            dtypedict.update({i: sqlalchemy.types.DateTime()})

        if "float" in str(j):
            dtypedict.update({i: sqlalchemy.types.Float(precision=3, asdecimal=True)})

        if "int" in str(j):
            dtypedict.update({i: sqlalchemy.types.INT()})

    return dtypedict


def seleccion_hoja(event=None):
    global seleccion_sheet
    seleccion_sheet = hoja.get()
    
def seleccion_excel(event=None):
    global seleccion_xcolumna
    seleccion_xcolumna = hojax.get()
    
def seleccion_db(event=None): #Opcion DE COLUMNA escogida por el comboDB
    global seleccion_db
    seleccion_db = columna_combo.get()

def procesar():
    engine =create_engine(f'postgresql+psycopg2://{user}:{password}@{host}/{database}',pool_recycle=3600);
    cnx= engine.connect();
    table_engine=table+datetime.datetime.now().isoformat(timespec='minutes')
    try: 
        format = sqlcol(df3)
        frame =df3.to_sql(table_engine,cnx, if_exists='append',index=False,dtype=format);
    except Exception as ex:
        print(ex)
    else:
        print('Datos ingresados')
    finally:
        cnx.close()


def abrir_archivo():
    archivo = filedialog.askopenfilename(initialdir='/home/pintog/Documents/proyecto/virtual1/v2/purgador',
                                         title='Seleccione archivo',
                                         filetypes=(('xlsx files', '*.xlsx*'), ('All files', '*.*')))
    indica['text'] = archivo
   
    global archivoexcel
    archivoexcel = r'{}'.format(archivo)

    global xl
    xl = pd.ExcelFile(archivoexcel)
    
    list_sheet =xl.sheet_names
    combo_sheet['values'] =list_sheet
    

def datos_filtro():
    if(combo_db.get()!="" and combo_excel.get()!=""):
        global df3
        df3= dfdb[dfdb.eval(combo_db.get()).isin(df.eval(combo_excel.get()))]
        
        
        tabla3['column'] = list(df3.columns)
        
        tabla3['show'] = "headings"  # encabezado

        for columna3 in tabla3['column']:
            tabla3.heading(columna3, text=columna3)

            df_fila3 = df3.to_numpy().tolist()
        for fila3 in df_fila3:
            tabla3.insert('', 'end', values=fila3)
    else:
        print("no")
    
def datos_db():
    global host
    global user
    global password
    global database
    global table
    host=str(entrada21.get())
    user=str(entrada22.get())
    password=str(entrada23.get())
    database=str(entrada24.get())
    table=str(entrada25.get())
    try: 
        connection =psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor= connection.cursor()
        
        cursor.execute(f'SELECT * FROM {table}')
       
        global column_names
        column_names = [desc[0] for desc in cursor.description]
        Limpiar2()
        tupples = cursor.fetchall()
        cursor.close()
            
    except Exception as ex:
        print(ex)
    
    
    
    # We just need to turn it into a pandas dataframe
    global dfdb
    dfdb = pd.DataFrame(tupples, columns=column_names)
    print(sqlcol(dfdb))
    
    tabla2['column'] = list(dfdb.columns)
    combo_db['values']=list(dfdb.columns)
    tabla2['show'] = "headings"  # encabezado

    for columna2 in tabla2['column']:
        tabla2.heading(columna2, text=columna2)

    df_fila2 = dfdb.to_numpy().tolist()
    for fila2 in df_fila2:
        tabla2.insert('', 'end', values=fila2)


def datos_excel():
    
    try:
        global df
        df = pd.read_excel(archivoexcel,seleccion_sheet)
        

    except ValueError:
        messagebox.showerror('Informacion', 'Formato incorrecto')
        return None

    except FileNotFoundError:
        messagebox.showerror('Informacion', 'El archivo esta \n malogrado')
        return None

    Limpiar()

    tabla['column'] = list(df.columns)
    combo_excel['values'] = list(df.columns)
    tabla['show'] = "headings"  # encabezado

    for columna in tabla['column']:
        tabla.heading(columna, text=columna)

    df_fila = df.to_numpy().tolist()
    for fila in df_fila:
        tabla.insert('', 'end', values=fila)


def Limpiar():
    tabla.delete(*tabla.get_children())

def Limpiar2():
    tabla2.delete(*tabla2.get_children())

def Limpiar3():
    tabla3.delete(*tabla3.get_children())
# creando ventana principal
ventana = tk.Tk()
ventana.config(bg='yellow')
ventana.geometry('800x600')
ventana.minsize(width=800, height=600)
ventana.title('Purgador')
ventana.configure(background='black')
ventana.focus_set()

# Estructurando la ventana principal, 2 secciones
ventana.columnconfigure(0, weight=25)
ventana.rowconfigure(0, weight=25)
ventana.columnconfigure(0, weight=4)
ventana.rowconfigure(1, weight=4)

# seccion para el cuadro de tabs
cuadro1 = Frame(ventana)
cuadro1.config(bg='green')
cuadro1.grid(column=0, row=0, sticky='nsew')

# seccion para el cuadro fijo al final de la ventana principal
cuadro2 = Frame(ventana)
cuadro2.config(bg='pink')
cuadro2.grid(column=0, row=1, sticky='nsew')

cuadro2.columnconfigure(0, weight=1)
cuadro2.rowconfigure(0, weight=1)
cuadro2.columnconfigure(1, weight=1)
cuadro2.rowconfigure(0, weight=1)

botonfinal = Button(cuadro2, text='Procesar', bg='green2', command=procesar)
botonfinal.grid(column=1, row=0, sticky='nse', padx=5, pady=5)



# En el cuadro 1, declarar el notebook para despues asignarle los tabs
note = ttk.Notebook(cuadro1)

# Creando primer tab
tab1= ttk.Notebook(note)

# Estructura de secciones del primer tab, 2 secciones
tab1.columnconfigure(0, weight=6)
tab1.rowconfigure(0, weight=6)
tab1.columnconfigure(0, weight=25)
tab1.rowconfigure(1, weight=25)

# Creando Cuadro para los botones y entrada de datos del Tab1
subcuadro11 = Frame(tab1, bg='green')
subcuadro11.grid(column=0, row=0, sticky='nsew')


# Secciones del cuadro de botones de forma horizontal del Tab1
subcuadro11.columnconfigure(0, weight=1)
subcuadro11.rowconfigure(0, weight=1)
subcuadro11.columnconfigure(1, weight=3)
subcuadro11.rowconfigure(0, weight=3)
subcuadro11.columnconfigure(2, weight=1)
subcuadro11.rowconfigure(0, weight=1)
subcuadro11.columnconfigure(0, weight=1)
subcuadro11.rowconfigure(1, weight=1)
subcuadro11.columnconfigure(1, weight=3)
subcuadro11.rowconfigure(1, weight=3)
subcuadro11.columnconfigure(2, weight=1)
subcuadro11.rowconfigure(1, weight=1)
subcuadro11.columnconfigure(0, weight=1)
subcuadro11.rowconfigure(2, weight=1)
subcuadro11.columnconfigure(1, weight=3)
subcuadro11.rowconfigure(2, weight=3)
subcuadro11.columnconfigure(2, weight=1)
subcuadro11.rowconfigure(2, weight=1)




boton1 = Button(subcuadro11, text='Abrir', bg='green2', command=abrir_archivo)
boton1.grid(column=0, row=0, sticky='nse', padx=5, pady=5)

boton2 = Button(subcuadro11, text='Mostrar', bg='magenta', command=datos_excel)
boton2.grid(column=2, row=2, sticky='nsew', padx=5, pady=5)

boton3 = Button(subcuadro11, text='Limpiar', bg='red', command=Limpiar)
boton3.grid(column=0, row=2, sticky='nsw', padx=5, pady=5)

indica = Label(subcuadro11, text='Ubicación del archivo', font=('Arial', 10, 'bold'))
indica.grid(column=1, row=0, sticky='nsew', padx=5, pady=5)

indica2 = Label(subcuadro11, text='Elegir Hoja', font=('Arial', 10, 'bold'))
indica2.grid(column=0, row=1, sticky='nse', padx=5, pady=5)

hoja = tk.StringVar()
combo_sheet = ttk.Combobox(subcuadro11, textvariable=hoja, font=('Arial', 10, 'bold'))

combo_sheet.grid(column=1, row=1, sticky='nsew', padx=5, pady=5)

combo_sheet.bind('<<ComboboxSelected>>', seleccion_hoja)
# Creando cuadro para la cuadricula del Tab1
subcuadro12 = Frame(tab1, bg='yellow')
subcuadro12.grid(column=0, row=1, sticky='nsew')
subcuadro12.columnconfigure(0, weight=1)
subcuadro12.rowconfigure(0, weight=1)

tabla = ttk.Treeview(subcuadro12, height=10)
tabla.grid(column=0, row=0, sticky='nsew')
ladox = Scrollbar(subcuadro12, orient=HORIZONTAL, command=tabla.xview)
ladox.grid(column=0, row=1, sticky='ew')

ladoy = Scrollbar(subcuadro12, orient=VERTICAL, command=tabla.yview)
ladoy.grid(column=1, row=0, sticky='ns')

tabla.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)



# Creando Segundo tab y configuracion
tab2= ttk.Notebook(note)
tab2.columnconfigure(0, weight=6)
tab2.rowconfigure(0, weight=6)
tab2.columnconfigure(0, weight=25)
tab2.rowconfigure(1, weight=25)

# Creando Cuadro para los botones y entrada de datos del Tab2
subcuadro21 = Frame(tab2, bg='yellow')
subcuadro21.grid(column=0, row=0, sticky='nsew')  

subcuadro21.rowconfigure(0, weight=1)
subcuadro21.columnconfigure(0, weight=1)
subcuadro21.columnconfigure(1, weight=1)
subcuadro21.rowconfigure(0, weight=1)
subcuadro21.columnconfigure(2, weight=1)
subcuadro21.rowconfigure(0, weight=1)
subcuadro21.columnconfigure(3, weight=1)
subcuadro21.rowconfigure(0, weight=1)
subcuadro21.columnconfigure(4, weight=1)
subcuadro21.rowconfigure(0, weight=1)
subcuadro21.columnconfigure(5, weight=1)
subcuadro21.rowconfigure(0, weight=1)

subcuadro21.columnconfigure(0, weight=1)
subcuadro21.rowconfigure(1, weight=1)
subcuadro21.columnconfigure(1, weight=1)
subcuadro21.rowconfigure(1, weight=1)
subcuadro21.columnconfigure(2, weight=1)
subcuadro21.rowconfigure(1, weight=1)
subcuadro21.columnconfigure(0, weight=1)
subcuadro21.rowconfigure(2, weight=1)
subcuadro21.columnconfigure(1, weight=1)
subcuadro21.rowconfigure(2, weight=1)
subcuadro21.columnconfigure(2, weight=1)
subcuadro21.rowconfigure(2, weight=1)

label21 = Label(subcuadro21 ,text = "Host").grid(row = 0,column = 0)
entrada21 = tk.Entry(subcuadro21)
entrada21.insert(0, "localhost")
entrada21.grid(column=1, row=0, sticky='nse', padx=5, pady=5)
label22 = Label(subcuadro21 ,text = "Usuario").grid(row = 0,column = 2)
entrada22 = tk.Entry(subcuadro21)
entrada22.insert(0, "postgres")
entrada22.grid(column=3, row=0, sticky='nse', padx=5, pady=5)
label23 = Label(subcuadro21 ,text = "Contraseña").grid(row = 0,column = 4)
entrada23 = tk.Entry(subcuadro21)
entrada23.insert(0, "postgres")
entrada23.grid(column=5, row=0, sticky='nse', padx=5, pady=5)
label24 = Label(subcuadro21 ,text = "Base de datos").grid(row = 1,column = 0)
entrada24 = tk.Entry(subcuadro21)
entrada24.insert(0, "test1")
entrada24.grid(column=1, row=1, sticky='nse', padx=5, pady=5)
label24 = Label(subcuadro21 ,text = "Tabla").grid(row = 1,column = 2)
entrada25 = tk.Entry(subcuadro21)
entrada25.insert(0, "users")
entrada25.grid(column=3, row=1, sticky='nse', padx=5, pady=5)



boton22 = Button(subcuadro21, text='Mostrar', bg='magenta', command=datos_db)
boton22.grid(column=5, row=2, sticky='nsew', padx=5, pady=5)

boton23 = Button(subcuadro21, text='Limpiar', bg='red', command=Limpiar2)
boton23.grid(column=0, row=2, sticky='nsw', padx=5, pady=5)

#Cuadro de display de datos dataframe
subcuadro22 = Frame(tab2, bg='yellow')
subcuadro22.grid(column=0, row=1, sticky='nsew')
subcuadro22.columnconfigure(0, weight=1)
subcuadro22.rowconfigure(0, weight=1)

tabla2 = ttk.Treeview(subcuadro22, height=10)
tabla2.grid(column=0, row=0, sticky='nsew')
ladox2 = Scrollbar(subcuadro22, orient=HORIZONTAL, command=tabla2.xview)
ladox2.grid(column=0, row=1, sticky='ew')

ladoy2 = Scrollbar(subcuadro22, orient=VERTICAL, command=tabla2.yview)
ladoy2.grid(column=1, row=0, sticky='ns')

tabla2.configure(xscrollcommand=ladox2.set, yscrollcommand=ladoy2.set)

# Creando Tercer tab y configuracion
tab3= ttk.Notebook(note)
tab3.columnconfigure(0, weight=1)
tab3.rowconfigure(0, weight=1)
tab3.columnconfigure(0, weight=25)
tab3.rowconfigure(1, weight=25)

# Creando Cuadro para los botones y entrada de datos del Tab3
subcuadro31 = Frame(tab3, bg='blue')
subcuadro31.grid(column=0, row=0, sticky='nsew') 

subcuadro31.columnconfigure(0, weight=1)
subcuadro31.rowconfigure(0, weight=1)
subcuadro31.columnconfigure(1, weight=1)
subcuadro31.rowconfigure(0, weight=1)
subcuadro31.columnconfigure(0, weight=1)
subcuadro31.rowconfigure(1, weight=1)
subcuadro31.columnconfigure(1, weight=1)
subcuadro31.rowconfigure(1, weight=1)
subcuadro31.columnconfigure(0, weight=1)
subcuadro31.rowconfigure(2, weight=1)
subcuadro31.columnconfigure(1, weight=1)
subcuadro31.rowconfigure(2, weight=1)
subcuadro31.columnconfigure(0, weight=1)
subcuadro31.rowconfigure(3, weight=1)
subcuadro31.columnconfigure(1, weight=1)
subcuadro31.rowconfigure(3, weight=1)

label31 = Label(subcuadro31 ,text = "Cubo").grid(row = 0,column = 0)
hojax = tk.StringVar()
combo_excel = ttk.Combobox(subcuadro31, textvariable=hojax, font=('Arial', 10, 'bold'))
combo_excel.grid(column=0, row=1, sticky='nsew', padx=5, pady=5)
combo_excel.bind('<<ComboboxSelected>>', seleccion_excel)
label32 = Label(subcuadro31 ,text = "BD a procesar").grid(row = 0,column = 1)
columna_combo = tk.StringVar()
combo_db = ttk.Combobox(subcuadro31, textvariable=columna_combo, font=('Arial', 10, 'bold'))
combo_db.grid(column=1, row=1, sticky='nsew', padx=5, pady=5)
combo_db.bind('<<ComboboxSelected>>', seleccion_db)
label33 = Label(subcuadro31 ,text = "Consulta").grid(row = 2,column = 0)

boton31 = Button(subcuadro31, text='Mostrar', bg='magenta', command=datos_filtro)
boton31.grid(column=1, row=3, sticky='nse', padx=5, pady=5)

boton32 = Button(subcuadro31, text='Limpiar', bg='red', command=Limpiar3 )
boton32.grid(column=0, row=3, sticky='nsw', padx=5, pady=5)


# Creando Cuadro para display del Tab3
subcuadro32 = Frame(tab3)
subcuadro32.grid(column=0, row=1, sticky='nsew') 
subcuadro32.columnconfigure(0, weight=1)
subcuadro32.rowconfigure(0, weight=1)

tabla3 = ttk.Treeview(subcuadro32, height=10)
tabla3.grid(column=0, row=0, sticky='nsew')
ladox3 = Scrollbar(subcuadro32, orient=HORIZONTAL, command=tabla3.xview)
ladox3.grid(column=0, row=1, sticky='ew')

ladoy3 = Scrollbar(subcuadro32, orient=VERTICAL, command=tabla3.yview)
ladoy3.grid(column=1, row=0, sticky='ns')

tabla3.configure(xscrollcommand=ladox3.set, yscrollcommand=ladoy3.set)


# estilo de Tabs
s = ttk.Style()
s.theme_use('alt')

s.configure(".", font=('Arial', 14), foreground='red2')
s.configure('TNotebook.Tab', font=('URW Gothic L','11','bold'), padding= [100, 10])
s.configure("Treeview", font=('Helvetica', 12), foreground='black', background='white')
s.map('Treeview', background=[('selected', 'green2')], foreground=[('selected', 'black')])




#Agregar los tabs creados al cuadro de control de tabs
note.add(tab1,text='Cubo')
note.add(tab2,text='A filtrar')
note.add(tab3,text='Purgar')

note.pack(expand=1, fill='both')

ventana.mainloop()
