from tkinter import Tk, Entry, Label, Button, Frame, messagebox, filedialog, ttk, Scrollbar, VERTICAL, HORIZONTAL
import pandas as pd

list_sheet =[1,2,3]
# creando ventana principal
ventana = Tk()
ventana.config(bg='yellow')
ventana.geometry('800x600')
ventana.minsize(width=800, height=600)
ventana.title('Purgador')
ventana.configure(background='black')

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
subcuadro11.columnconfigure(1, weight=1)
subcuadro11.rowconfigure(0, weight=1)
subcuadro11.columnconfigure(0, weight=1)
subcuadro11.rowconfigure(1, weight=1)
subcuadro11.columnconfigure(1, weight=1)
subcuadro11.rowconfigure(1, weight=1)
subcuadro11.columnconfigure(0, weight=1)
subcuadro11.rowconfigure(2, weight=1)
subcuadro11.columnconfigure(1, weight=1)
subcuadro11.rowconfigure(2, weight=1)

def abrir_archivo():
    archivo = filedialog.askopenfilename(initialdir='/',
                                         title='Selecione archivo',
                                         filetypes=(('xlsx files', '*.xlsx*'), ('All files', '*.*')))
    indica['text'] = archivo

# def listadeHoja(list_sheet):


def datos_excel():
    datos_obtenidos = indica['text']
    global list_sheet
    try:
        archivoexcel = r'{}'.format(datos_obtenidos)

        df = pd.read_excel(archivoexcel)
        xl = pd.ExcelFile(archivoexcel)
        list_sheet =xl.sheet_names

    except ValueError:
        messagebox.showerror('Informacion', 'Formato incorrecto')
        return None

    except FileNotFoundError:
        messagebox.showerror('Informacion', 'El archivo esta \n malogrado')
        return None

    Limpiar()

    tabla['column'] = list(df.columns)
    tabla['show'] = "headings"  # encabezado

    for columna in tabla['column']:
        tabla.heading(columna, text=columna)

    df_fila = df.to_numpy().tolist()
    for fila in df_fila:
        tabla.insert('', 'end', values=fila)


def Limpiar():
    tabla.delete(*tabla.get_children())


boton1 = Button(subcuadro11, text='Abrir', bg='green2', command=abrir_archivo)
boton1.grid(column=0, row=0, sticky='nsew', padx=5, pady=5)

boton2 = Button(subcuadro11, text='Mostrar', bg='magenta', command=datos_excel)
boton2.grid(column=0, row=2, sticky='nsew', padx=5, pady=5)

boton3 = Button(subcuadro11, text='Limpiar', bg='red', command=Limpiar)
boton3.grid(column=1, row=2, sticky='nsew', padx=5, pady=5)

indica = Label(subcuadro11, text='Ubicación del archivo', font=('Arial', 10, 'bold'))
indica.grid(column=1, row=0, sticky='nsew', padx=5, pady=5)

indica2 = Label(subcuadro11, text='Elegir Hoja', font=('Arial', 10, 'bold'))
indica2.grid(column=0, row=1, sticky='nsew', padx=5, pady=5)


combo_sheet = ttk.Combobox(subcuadro11, value=list_sheet, font=('Arial', 10, 'bold'))
combo_sheet.grid(column=1, row=1, sticky='nsew', padx=5, pady=5)

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
subcuadro21 = Frame(tab2, bg='red')
subcuadro21.grid(column=0, row=0, sticky='nsew')

# Creando Tercer tab y configuracion
tab3= ttk.Notebook(note)
tab3.columnconfigure(0, weight=1)
tab3.rowconfigure(0, weight=1)

# estilo de Tabs
s = ttk.Style()
s.theme_use('alt')  # ('clam', 'alt', 'default', 'classic')

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
