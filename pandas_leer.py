import tkinter as tk 
import pandas as pd
from tkinter import Tk, Entry, Label, Button, Frame, messagebox, filedialog, ttk, Scrollbar, VERTICAL, HORIZONTAL


def procesar():
    try:
        
        hojaxl = df2.keys()
        asign1 = []
        if(str(entrada.get()) == ""):
            datos = dfsheet.eval(seleccion_column)
            
            for z in datos:            
                for x in hojaxl:
                    temp1=df2[x].to_numpy().tolist()
                    for y in temp1:   
                        if z in y:
                            asign1.append([z,x])
                        
            df = pd.DataFrame(asign1, columns=["Dato", "Se encuentra en Hoja"])
        else:
            dato = str(entrada.get())
            for x in hojaxl:
                    temp1=df2[x].to_numpy().tolist()
                    for y in temp1:   
                        if dato in y:
                            asign1.append([dato,x])
            df = pd.DataFrame(asign1, columns=["Dato", "Se encuentra en Hoja"])
        
        
                        
                    
            


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
    
    

    
    

def abrir_archivo_base():
    archivo2 = filedialog.askopenfilename(initialdir='/home/pintog/Documents/proyecto/virtual1/v2/purgador',
                                         title='Seleccione archivo',
                                         filetypes=(('xlsx files', '*.xlsx*'), ('All files', '*.*')))
    indica22['text'] = archivo2
    archivoexcel2 = r'{}'.format(archivo2)
    
    global df2
    df2 = pd.read_excel(archivoexcel2, sheet_name=None)
    
    
        
    
    
    
def abrir_archivo_buscar():
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
    
    
   
def seleccion_hoja(event=None):
    global seleccion_sheet
    seleccion_sheet = hoja.get()
    
    global dfsheet
    dfsheet = pd.read_excel(archivoexcel, seleccion_sheet)
    combo_columna['values'] = list(dfsheet.columns)

def seleccion_columna(event=None):
    global seleccion_column
    seleccion_column =columna.get()
    
    
    

def Limpiar():
    tabla.delete(*tabla.get_children())
    entrada.delete(0, 'end')
    indica.config(text="")
    combo_sheet.set('')
    combo_columna.set('')

    

ventana = tk.Tk()
ventana.config(bg='yellow')
ventana.geometry('1000x600')
ventana.minsize(width=800, height=600)
ventana.title('Buscador')
ventana.configure(background='white')
ventana.focus_set()

ventana.columnconfigure(0, weight=4)
ventana.rowconfigure(0, weight=4)
ventana.columnconfigure(0, weight=25)
ventana.rowconfigure(1, weight=25)
ventana.columnconfigure(0, weight=4)
ventana.rowconfigure(2, weight=4)

cuadro1 = Frame(ventana)

cuadro1.grid(column=0, row=0, sticky='nsew')

cuadro1.columnconfigure(0, weight=1)
cuadro1.rowconfigure(0, weight=1)
cuadro1.columnconfigure(1, weight=1)
cuadro1.rowconfigure(0, weight=1)

cuadro2 = Frame(ventana)

cuadro2.grid(column=0, row=1, sticky='nsew')
cuadro2.columnconfigure(0, weight=1)
cuadro2.rowconfigure(0, weight=1)


subcuadro11 = Frame(cuadro1, bg='green')
subcuadro11.grid(column=0, row=0, sticky='nsew')

subcuadro11.columnconfigure(0, weight=4)
subcuadro11.rowconfigure(0, weight=4)
subcuadro11.columnconfigure(1, weight=4)
subcuadro11.rowconfigure(0, weight=4)
subcuadro11.columnconfigure(0, weight=1)
subcuadro11.rowconfigure(1, weight=1)
subcuadro11.columnconfigure(1, weight=3)
subcuadro11.rowconfigure(1, weight=3)

subcuadro11.columnconfigure(0, weight=1)
subcuadro11.rowconfigure(2, weight=1)
subcuadro11.columnconfigure(1, weight=3)
subcuadro11.rowconfigure(2, weight=3)


subcuadro11.columnconfigure(0, weight=1)
subcuadro11.rowconfigure(3, weight=1)
subcuadro11.columnconfigure(1, weight=3)
subcuadro11.rowconfigure(3, weight=3)
subcuadro11.columnconfigure(2, weight=1)
subcuadro11.rowconfigure(3, weight=1)

subcuadro11.columnconfigure(0, weight=1)
subcuadro11.rowconfigure(2, weight=1)
subcuadro11.columnconfigure(1, weight=3)
subcuadro11.rowconfigure(2, weight=3)

subcuadro11.columnconfigure(0, weight=1)
subcuadro11.rowconfigure(3, weight=1)
subcuadro11.columnconfigure(1, weight=3)
subcuadro11.rowconfigure(3, weight=3)

subcuadro11.columnconfigure(0, weight=1)
subcuadro11.rowconfigure(4, weight=1)
subcuadro11.columnconfigure(1, weight=3)
subcuadro11.rowconfigure(4, weight=3)

subcuadro11.columnconfigure(0, weight=1)
subcuadro11.rowconfigure(5, weight=1)
subcuadro11.columnconfigure(1, weight=3)
subcuadro11.rowconfigure(5, weight=3)

subtitulo1 = Label(subcuadro11, text='A buscar', font=('Arial', 15, 'bold'), bg='green')
subtitulo1.grid(column=1, row=0, sticky='nsew', padx=5, pady=5)

boton1 = Button(subcuadro11, text='Abrir', bg='green2', command=abrir_archivo_buscar)
boton1.grid(column=0, row=3, sticky='nse', padx=5, pady=5)

entrada = tk.Entry(subcuadro11)

entrada.grid(column=1, row=1, sticky='nsew', padx=5, pady=5)

escribe = Label(subcuadro11, text='Escribir Datos', font=('Arial', 10, 'bold'))
escribe.grid(column=0, row=1, sticky='nsew', padx=5, pady=5)

opcion = Label(subcuadro11, text='Ó desde Archivo', font=('Arial', 10, 'bold'), bg='green')
opcion.grid(column=1, row=2, sticky='nsew', padx=5, pady=5)

indica = Label(subcuadro11, text='Ubicación del archivo', font=('Arial', 10, 'bold'))
indica.grid(column=1, row=3, sticky='nsew', padx=5, pady=5)

indica2 = Label(subcuadro11, text='Elegir Hoja', font=('Arial', 10, 'bold'))
indica2.grid(column=0, row=4, sticky='nse', padx=5, pady=5)

indica3 = Label(subcuadro11, text='Elegir Columna', font=('Arial', 10, 'bold'))
indica3.grid(column=0, row=5, sticky='nse', padx=5, pady=5)

hoja = tk.StringVar()
combo_sheet = ttk.Combobox(subcuadro11, textvariable=hoja, font=('Arial', 10, 'bold'))

combo_sheet.grid(column=1, row=4, sticky='nsew', padx=5, pady=5)

combo_sheet.bind('<<ComboboxSelected>>', seleccion_hoja)

columna = tk.StringVar()
combo_columna = ttk.Combobox(subcuadro11, textvariable=columna, font=('Arial', 10, 'bold'))

combo_columna.grid(column=1, row=5, sticky='nsew', padx=5, pady=5)

combo_columna.bind('<<ComboboxSelected>>', seleccion_columna)

subcuadro22 = Frame(cuadro1, bg='gray')
subcuadro22.grid(column=1, row=0, sticky='nsew')

subcuadro22.columnconfigure(1, weight=1)
subcuadro22.rowconfigure(0, weight=4)
subcuadro22.columnconfigure(0, weight=1)
subcuadro22.rowconfigure(1, weight=1)
subcuadro22.columnconfigure(1, weight=3)
subcuadro22.rowconfigure(1, weight=3)

subcuadro22.columnconfigure(0, weight=1)
subcuadro22.rowconfigure(1, weight=1)
subcuadro22.columnconfigure(1, weight=3)
subcuadro22.rowconfigure(1, weight=3)

subcuadro22.columnconfigure(0, weight=1)
subcuadro22.rowconfigure(2, weight=1)
subcuadro22.columnconfigure(1, weight=3)
subcuadro22.rowconfigure(2, weight=3)
subcuadro22.columnconfigure(2, weight=1)
subcuadro22.rowconfigure(2, weight=1)

subtitulo2 = Label(subcuadro22, text='Base de Datos', font=('Arial', 15, 'bold'), bg='gray')
subtitulo2.grid(column=1, row=0, sticky='nsew', padx=5, pady=5)


boton21 = Button(subcuadro22, text='Abrir', bg='green2' , command=abrir_archivo_base)
boton21.grid(column=0, row=1, sticky='nse', padx=5, pady=5)

indica22 = Label(subcuadro22, text='Ubicación del archivo', font=('Arial', 10, 'bold'))
indica22.grid(column=1, row=1, sticky='nsew', padx=5, pady=5)

cuadro3 = Frame(ventana)
cuadro3.config(bg='blue')
cuadro3.grid(column=0, row=2, sticky='nsew')

cuadro3.columnconfigure(0, weight=1)
cuadro3.rowconfigure(0, weight=1)
cuadro3.columnconfigure(1, weight=1)
cuadro3.rowconfigure(0, weight=1)

boton31 = Button(cuadro3, text='Mostrar', bg='magenta', command=procesar)
boton31.grid(column=1, row=3, sticky='nse', padx=5, pady=5)

boton32 = Button(cuadro3, text='Limpiar', bg='red', command=Limpiar )
boton32.grid(column=0, row=3, sticky='nsw', padx=5, pady=5)

tabla = ttk.Treeview(cuadro2)
tabla.grid(column=0, row=0, sticky='nsew')
ladox = Scrollbar(cuadro2, orient=HORIZONTAL, command=tabla.xview)
ladox.grid(column=0, row=1, sticky='ew')

ladoy = Scrollbar(cuadro2, orient=VERTICAL, command=tabla.yview)
ladoy.grid(column=1, row=0, sticky='ns')

tabla.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)


s = ttk.Style()
s.theme_use('alt')
s.configure("Treeview", font=('Helvetica', 12), foreground='black', background='white')
s.map('Treeview', background=[('selected', 'green2')], foreground=[('selected', 'black')])


ventana.mainloop()
    
    

