import os
import pickle
import threading
from tkinter import *
from  tkinter import ttk

class RepeatingThread(threading.Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function( *self.args,**self.kwargs)

class AppPing(Frame):
    def __init__(self,master=None) -> None:
        Frame.__init__(self,master)
        self.master['bg'] = '#AC99F2'
        self.pack(expand=True,fill=BOTH)
        self.ventana_edicion = None

        #menu pop up

        self.popup_m = Menu(self, tearoff = 0)
        self.popup_m.add_command(label ="Editar",command=)
        self.popup_m.add_command(label ="Eliminar")

        #menu de agregado

        menu = LabelFrame(self,text="Opciones")
        menu.grid(column=0,row=0,sticky=S+N+E+W)

        label_nombre = Label(menu,text="Nombre")
        label_nombre.pack(side=LEFT)
        self.entry_nombre = Entry(menu)
        self.entry_nombre.pack(side=LEFT,padx = 10, pady = 5)

        label_ip = Label(menu,text="IP")
        label_ip.pack(side=LEFT)
        self.entry_ip = Entry(menu)
        self.entry_ip.pack(side=LEFT,padx = 10, pady = 5)

        button_agregar = Button(menu,text="Agregar",command=lambda: self.insertar_fila((self.entry_nombre.get(),self.entry_ip.get(),"Desconectado")))
        button_agregar.pack(side=LEFT)

        self.label_error = Label(menu,text="",fg="red")
        self.label_error.pack(side=LEFT)

        #desplegable

        tabla_scrolly = Scrollbar(self)
        tabla_scrolly.grid(column=1,row=1,sticky=N+S)

        tabla_scrollx = Scrollbar(self,orient='horizontal')
        tabla_scrollx.grid(column=0,row=2,sticky=W+E)

        agarre = ttk.Sizegrip(self)
        agarre.grid(column=1,row=2,sticky=S+E)
        
        #configurar tabla

        self.tabla = ttk.Treeview(self,yscrollcommand=tabla_scrolly.set, xscrollcommand =tabla_scrollx.set)
        self.tabla.bind('<Double-Button-1>', self.seleccionar)
        self.tabla.bind('<Button-2>', self.popup_menu)

        self.tabla.grid(column=0,row=1,sticky=S+N+E+W)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)

        tabla_scrolly.config(command=self.tabla.yview)
        tabla_scrollx.config(command=self.tabla.xview)

        #crear columnas

        self.crear_columnas(["nombre","ip","estado"])

        with open("data",mode="+ab") as archivo:
            archivo.seek(0)
            datos = pickle.load(archivo)
            for dato in datos:
                self.tabla.insert(parent='',index='end',text='',values=dato)

        #Chequeos

        self.timer = RepeatingThread(100, self.check)
        self.check()
        self.timer.start()

    def popup_menu(self,event):
        try:
            self.popup_m.tk_popup(event.x_root, event.y_root)
        finally:
            self.popup_m.grab_release()

    def seleccionar(self,event):
        item = self.tabla.focus()
        valores_item = self.tabla.item(item)["values"]
        
        if self.ventana_edicion:
            self.ventana_edicion.destroy()
        self.ventana_edicion = Toplevel(self.master)
        self.ventana_edicion.title("Editar")
        self.ventana_edicion.geometry(f"100x100+{event.x}+{event.y}")
        self.ventana_edicion.focus_force()
        self.ventana_edicion.wm_attributes("-topmost", True)
        
        Label(self.ventana_edicion, text ="Nombre").pack()
        nuevo_nombre = Entry(self.ventana_edicion)
        nuevo_nombre.insert(0,valores_item[0])
        nuevo_nombre.pack()
        Label(self.ventana_edicion, text ="textItem").pack()
        nuevo_ip = Entry(self.ventana_edicion)
        nuevo_ip.insert(0,valores_item[1])
        nuevo_ip.pack()
        Button(self.ventana_edicion, text ="Guardar", command=lambda: self.editar(item,(nuevo_nombre.get(),nuevo_ip.get(),valores_item[2]))).pack()
        Button(self.ventana_edicion, text ="Borrar", command=lambda: self.editar(item,(nuevo_nombre.get(),nuevo_ip.get(),valores_item[2]))).pack()
        
    def editar(self, fila, datos):
        self.tabla.item(fila,text="",values=datos)
        self.guardar()

    def insertar_fila(self, valores):
        texto = StringVar()
        for child in self.tabla.get_children():
            if self.tabla.item(child)["values"][0] == valores[0] or self.tabla.item(child)["values"][1] == valores[1]:
                texto.set("Error: no repetir nombres/ips")
                self.label_error.config(textvariable=texto)
                return
        self.tabla.insert(parent='',index='end',text='',values=valores)
        self.entry_nombre.delete(first=0,last=END)
        self.entry_ip.delete(first=0,last=END)

        texto.set("")
        self.label_error.config(textvariable=texto)
        self.check()
        self.guardar()

    def crear_columnas(self, columnas):
        self.tabla['columns'] = tuple(columnas)

        # format our column
        self.tabla.column("#0", width=0,  stretch=NO)
        self.tabla.heading("#0",text="",anchor=W)
        for c in columnas:
            self.tabla.column(c,anchor=W,width=80)
            self.tabla.heading(c,text=str(c).upper(),anchor=W)
    

    def quit(self):
        self.timer.cancel()
        Frame.quit(self)

    def guardar(self):
        with open("data",mode="wb") as archivo:
            datos = list()
            for child in self.tabla.get_children():
                datos.append(self.tabla.item(child)["values"])
            pickle.dump(datos,archivo)
    
    def check(self):
        for child in self.tabla.get_children():
            host = self.tabla.item(child)["values"][1] #example
            # respuesta = os.system("ping " + str(host))
            # if respuesta == 0: estado="Conectado"
            # else : estado="Desconectado"
            # try:
            #     self.tabla.item(child,text="",values=(self.tabla.item(child)["values"][0],
            #                                     host,
            #                                     estado))
            # except:
            #     break

if __name__ == "__main__":
    app = AppPing()
    app.master.title('PythonGuides')
    app.master.geometry("800x500")
    app.mainloop()
    app.quit()

