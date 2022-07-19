from tkinter import Tk, Label, Button, Frame, messagebox, filedialog, ttk, Scrollbar, VERTICAL, HORIZONTAL
import pandas as pd


ventana = Tk()
ventana.config(bg='black')
ventana.geometry('600x400')
ventana.minsize(width=600, height=400)
ventana.title('Leer datos excel')



ventana.columnconfigure(0, weight=25)
ventana.rowconfigure(0, weight=25)
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)

frame1 = Frame(ventana, bg='blue')
frame1.grid(column=0, row=0, sticky='nsew')
frame2 = Frame(ventana, bg='gray26')
frame2.grid(column=0, row=1, sticky='nsew')

frame1.columnconfigure(0, weight=1)
frame1.rowconfigure(0, weight=1)

frame2.columnconfigure(0, weight=1)
frame2.rowconfigure(0, weight=1)
frame2.columnconfigure(1, weight=1)
frame2.rowconfigure(0, weight=1)

frame2.columnconfigure(2, weight=1)
frame2.rowconfigure(0, weight=1)

frame2.columnconfigure(3, weight=2)
frame2.rowconfigure(0, weight=1)


def abrir_archivo():
    archivo = filedialog.askopenfilename(initialdir='/', title='Seleccione archivo', filetype=(('xlsx files', '*.xlsx*'), ('All files', '*.*')))
    indica['text'] = archivo


def datos_excel():

    datos_obtenidos = indica['text']
    try:
        archivoexcel = r'{}'.format(datos_obtenidos)
        df = pd.read_excel(archivoexcel)
        xl = pd.ExcelFile(archivoexcel)
        print(xl.sheet_names)

    except ValueError:
        messagebox.showerror('Informacion', 'Formato incorrecto')
        return None

    except FileNotFoundError:
        messagebox.showerror('Informacion', 'El archivo está \n corrupto')
        return None

    Limpiar()

    tabla['column'] = list(df.columns)
    tabla['show'] = "headings"


    for columna in tabla['column']:
        tabla.heading(columna, text= columna)

    df_fila = df.to_numpy().tolist()
    for fila in df_fila:
        tabla.insert('', 'end', values =fila)


def Limpiar():
    tabla.delete(*tabla.get_children())


tabla = ttk.Treeview(frame1, height=10)
tabla.grid(column=0, row=0, sticky='nsew')

ladox = Scrollbar(frame1, orient=HORIZONTAL, command=tabla.xview)
ladox.grid(column=0, row=1, sticky='ew')

ladoy = Scrollbar(frame1, orient=VERTICAL, command=tabla.yview)
ladoy.grid(column=1, row=0, sticky='ns')

tabla.configure(xscrollcommand = ladoy.set, yscrollcommand=ladoy.set)

estilo = ttk.Style(frame1)
estilo.theme_use('clam') # ('clam', 'alt', 'default', 'classic')
estilo.configure(".", font=('Arial', 14), foreground='red2')
estilo.configure("Treeview", font= ('Helvetica', 12), foreground='black', background='white')
estilo.map('Treeview', background=[('selected', 'green2')], foreground=[('selected', 'black')])


boton1 = Button(frame2, text='Abrir', bg='green2', command=abrir_archivo)
boton1.grid(column=0, row=0, sticky='nsew', padx=10, pady=10)

boton2 = Button(frame2, text='Mostrar', bg='red', command=datos_excel)
boton2.grid(column=1, row=0, sticky='nsew', padx=10, pady=10)

boton1 = Button(frame2, text='Limpiar', bg='magenta', command=Limpiar)
boton1.grid(column=2, row=0, sticky='nsew', padx=10, pady=10)

indica = Label(frame2, fg='white', bg='gray26', text='Ubicacion del archivo', font=('Arial',10,'bold'))
indica.grid(column=3, row=0)

ventana.mainloop()


