import pickle
import threading
from pythonping import ping
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Opciones():
    
    intervalo=100
    tamanio_p=60
    ping_menor=15
    ping_medio=50
    ips = list()

    def __getitem__(self, item):
        return getattr(self,item)
    
    def get(self):
        ignorar = ["set","get","ips"]
        valores = dict()
        for n in dir(self):
            if n.find("_",0,1) == 0 or n in ignorar:
                continue
            valores[n] = getattr(self,n)
        return valores
    
    def set(self, valores):
        for v in valores:
            setattr(self,v,valores[v])


class RepeatingThread(threading.Timer):
    
    def run(self):
        while not self.finished.wait(self.interval):
            self.function( *self.args,**self.kwargs)


class AppPing(Frame):
    Disp_Conectado = "Conectado"
    Disp_Desconectado = "Desconectado"
    Disp_Indefinido = "Indefinido"

    def __init__(self,master=None) -> None:

        Frame.__init__(self,master)
        self.pack(expand=True,fill=BOTH)
        self.ventana_edicion = None
        self.menu_opciones = None
        self.mouse_pos = (0,0)
        self.opciones = Opciones()
        #menu pop up

        self.popup_m = Menu(self, tearoff = 0)
        self.popup_m.add_command(label ="Editar", command=self.abrir_edicion)
        self.popup_m.add_command(label ="Eliminar", command=self.eliminar)

        #menu superior

        menu = LabelFrame(self,text="Menu")
        menu.grid(column=0,row=0,sticky=S+N+E+W)

        self.button_chequear= Button(menu,text="Chequear",command=self.check)
        self.button_chequear.pack(side=LEFT, padx=10, ipadx=30)

        label_nombre = Label(menu,text="Nombre")
        label_nombre.pack(side=LEFT)
        self.entry_nombre = Entry(menu)
        self.entry_nombre.pack(side=LEFT,padx = 10, pady = 5)

        label_ip = Label(menu,text="IP")
        label_ip.pack(side=LEFT)
        self.entry_ip = Entry(menu)
        self.entry_ip.pack(side=LEFT,padx = 10, pady = 5)

        self.button_agregar = Button(menu,text="Agregar",command=self.insertar_fila)
        self.button_agregar.pack(side=LEFT)

        self.label_error = Label(menu,text="",fg="red")
        self.label_error.pack(side=LEFT)
        
        #barra inferior

        b_inferior = Frame(self)
        b_inferior.grid(column=0,row=3,sticky=S+N+E+W)

        self.button_opciones= Button(b_inferior,text="Opciones",command=self.abrir_opciones)
        self.button_opciones.pack(side=LEFT, padx=10, ipadx=30)

        self.pb = ttk.Progressbar(b_inferior, orient='horizontal', mode='indeterminate', length=150)
        self.pb.pack(side=LEFT,expand=True,fill=X, padx=5, pady=5)

        self.label_actualizado= Label(b_inferior,text="",fg="green")
        self.label_actualizado.pack(side=LEFT)

        #scrollbars y grip

        tabla_scrolly = Scrollbar(self)
        tabla_scrolly.grid(column=1,row=1,sticky=N+S)

        tabla_scrollx = Scrollbar(self,orient='horizontal')
        tabla_scrollx.grid(column=0,row=2,sticky=W+E)

        agarre = ttk.Sizegrip(self)
        agarre.grid(column=1,row=3,sticky=S+E)
        
        #configurar tabla

        self.tabla = ttk.Treeview(self,yscrollcommand=tabla_scrolly.set, xscrollcommand =tabla_scrollx.set)
        self.tabla.tag_configure(self.Disp_Conectado    ,background="#7FA0FE")
        self.tabla.tag_configure(self.Disp_Desconectado ,background="#FE7F7F")
        self.tabla.tag_configure(self.Disp_Indefinido   ,background="#DDEDB4")
        self.enable(True)

        self.tabla.grid(column=0,row=1,sticky=S+N+E+W)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)

        tabla_scrolly.config(command=self.tabla.yview)
        tabla_scrollx.config(command=self.tabla.xview)

        #crear columnas

        self.crear_columnas(["nombre","ip","estado"])

        with open("data",mode="+ab") as archivo:
            try:
                archivo.seek(0)
                self.opciones = pickle.load(archivo)

                for fila in self.opciones.ips:
                    tag = self.Disp_Indefinido
                    if str(fila[2]).find(self.Disp_Desconectado) == 0:
                        tag = self.Disp_Desconectado
                    elif str(fila[2]).find(self.Disp_Conectado) == 0:
                        tag = self.Disp_Conectado
                    
                    self.tabla.insert(parent='',index='end',text='',
                                      values=fila,
                                      tags=tag)
            except:
                pass

        #Chequeos

        self.timer = RepeatingThread(int(self.opciones.intervalo), self.check)
        self.check()
        self.timer.start()

    def quit(self):
        self.timer.cancel()
        self.guardar()
        Frame.quit(self)

    def mouse(self,event):
        self.mouse_pos = (event.x_root,event.y_root)    

    def enable(self,bool):
        if bool:
            self.button_agregar.configure(state="normal")
            self.button_chequear.configure(state="normal")
            self.button_opciones.configure(state="normal")
            self.tabla.bind('<Double-Button-1>', self.abrir_edicion)
            self.tabla.bind('<Button-3>', self.popup_menu)
            self.tabla.bind("<Motion>",self.mouse)
        else:
            self.button_agregar.configure(state="disabled")
            self.button_chequear.configure(state="disabled")
            self.button_opciones.configure(state="disabled")
            self.tabla.unbind_all('<Double-Button-1>')
            self.tabla.unbind_all('<Button-3>')
            self.tabla.unbind_all("<Motion>")

    def popup_menu(self,event):
        try:
            if self.tabla.focus():
                self.popup_m.tk_popup(event.x_root, event.y_root)
        finally:
            self.popup_m.grab_release()


    def crear_columnas(self, columnas):
        self.tabla['columns'] = tuple(columnas)

        # format our column
        self.tabla.column("#0", width=0,  stretch=NO)
        self.tabla.heading("#0",text="",anchor=W)
        for c in columnas:
            self.tabla.column(c,anchor=W,width=80)
            self.tabla.heading(c,text=str(c).upper(),anchor=W)
    
    def mostrar_ips(self):
        datos = dict()
        for child in self.tabla.get_children():
            datos[child] = {"nombre":self.tabla.item(child)["values"][0],"ip":self.tabla.item(child)["values"][1]}
        return datos
    
    def validar_ip(self, fila ,nombre,ip):
        if len(ip.split(".")) != 4:
            return 1
        for f, valor in self.mostrar_ips().items():
            if fila != f and (valor["nombre"] == nombre or valor["ip"]  == ip):
                return 2
        return 0

    def insertar_fila(self):
        valores = (self.entry_nombre.get(),self.entry_ip.get(),self.Disp_Indefinido)
        texto = ""
        resultado = self.validar_ip(-1,valores[0],valores[1]) 

        if resultado == 0:
            self.tabla.insert(parent='',index='end',text='',values=valores)
            self.entry_nombre.delete(first=0,last=END)
            self.entry_ip.delete(first=0,last=END)
            self.check()
        elif resultado == 1:
            texto = "Error: ip incorrecta"
        elif resultado == 2:
            texto = "Error: no repetir nombres/ips"
        self.label_error.config(text=texto)

        
    def abrir_edicion(self,*args):
        item = self.tabla.focus()
        if not item:
            return
        valores_item = self.tabla.item(item)["values"]
        self.enable(False)

        if self.ventana_edicion:
            self.ventana_edicion.destroy()
        self.ventana_edicion = Toplevel(self.master)
        self.ventana_edicion.resizable(0,0)
        self.ventana_edicion.title("Editar")
        self.ventana_edicion.transient(self)
        self.ventana_edicion.protocol("WM_DELETE_WINDOW", self.cerrar_edicion)
        
        v_nuevo_nombre = StringVar(valores_item[0])
        Label(self.ventana_edicion, text ="Nombre").pack()
        Entry(self.ventana_edicion, textvariable=v_nuevo_nombre).pack(padx=5,pady=5)

        v_nuevo_ip = StringVar(valores_item[1])
        Label(self.ventana_edicion, text ="Ip").pack()
        Entry(self.ventana_edicion, textvariable=v_nuevo_ip).pack(padx=5,pady=5)

        Button(self.ventana_edicion, text ="Guardar", 
               command=lambda: self.editar(item,(v_nuevo_nombre.get(),v_nuevo_ip.get(),valores_item[2]))
               ).pack(padx=5,pady=5)
        
    def editar(self, fila, datos):
        resultado = self.validar_ip(fila,datos[0],datos[1]) 
        if resultado > 0:
            messagebox.showerror("Error","Ip incorrecta")
            return
        self.tabla.item(fila,text="",values=datos)
        self.ventana_edicion.destroy()
        datos = list()
        for valor in self.mostrar_ips().values():
            datos.append(valor.values())
        self.opciones.ips = datos
        self.enable(True)

    def eliminar(self):
        item = self.tabla.focus()
        self.tabla.delete(item)
        datos = list()
        for valor in self.mostrar_ips().values():
            datos.append(valor.values())
        self.opciones.ips = datos
    
    def cerrar_edicion(self):
        self.enable(True)
        self.ventana_edicion.destroy()

    def abrir_opciones(self):
        if self.menu_opciones:
            self.menu_opciones.destroy()
        self.menu_opciones = Toplevel()
        self.menu_opciones.title("Opciones")
        self.menu_opciones.resizable(0,0)
        
        self.menu_opciones.protocol("WM_DELETE_WINDOW", self.cerrar_opciones)
        self.enable(False)
        px=15
        py=8

        datos = self.opciones.get()
        self.variables = dict()
        for it, opc in enumerate(datos):
            self.variables[opc] = StringVar(value=datos[opc])
            Label(self.menu_opciones,text=opc).grid(row=it,padx=px,pady=py,sticky=E)
            Entry(self.menu_opciones,textvariable=self.variables[opc]).grid(column=1,row=it,padx=px,pady=py)

        Button(self.menu_opciones,text="Aceptar",command=self.guardar_opciones_cerrar).grid(row=4,padx=px,pady=py,column=0)
        Button(self.menu_opciones,text="Guardar",command=self.guardar_opciones).grid(row=4,padx=px,pady=py,column=1)
        self.label_error2 = Label(self.menu_opciones,text="",fg="red")
        self.label_error2.grid(row=5,padx=px,pady=py,columnspan=2)
    
    def guardar_opciones(self):
        self.opciones.set({x: int(self.variables[x].get()) for x in self.variables})
        self.timer.interval = self.opciones.intervalo
        return True
    
    def guardar_opciones_cerrar(self):
        if self.guardar_opciones():
            self.cerrar_opciones()
    
    def cerrar_opciones(self):
        self.enable(True)
        self.menu_opciones.destroy()


    def guardar(self):
        with open("data",mode="wb") as archivo:
            pickle.dump(self.opciones,archivo)

    def check(self):
        self.pb.start(5)
        self.enable(False)
        self.label_actualizado.configure(text="")

        t = threading.Thread(target=self.hacer_ping)
        t.start()    

    def hacer_ping(self):
        for child in self.tabla.get_children():
            host = self.tabla.item(child)["values"][1] #example
            respuesta = ping(str(host), verbose=False, count=4, size=self.opciones.tamanio_p)
            print(respuesta)
            if respuesta == 0: estado=self.Disp_Conectado
            else : estado=self.Disp_Desconectado
            
            latencia = "normal"
            if respuesta.rtt_avg_ms >= self.opciones.ping_menor :
                latencia = "lento"
            if respuesta.rtt_avg_ms >= self.opciones.ping_medio :
                latencia = "muy lento"

            try:
                self.tabla.item(child,text="",
                                values=(self.tabla.item(child)["values"][0], host, f"{estado} ({latencia})"),
                                tags=(estado))
            except:
                break
        
        
        self.pb.stop()
        self.enable(True)
        self.label_actualizado.configure(text="Actualizado!")

        datos = list()
        for child in self.tabla.get_children():
            datos.append(self.tabla.item(child)["values"])
        self.opciones.ips = datos
        self.guardar()


if __name__ == "__main__":
    app = AppPing()
    app.master.title('PythonGuides')
    app.master.geometry("800x500")
    app.mainloop()
    app.quit()

