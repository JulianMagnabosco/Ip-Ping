# import os
# hostname = "google.com" #example
# response = os.system("ping " + hostname)

# #and then check the response...
# if response == 0:
#   print (f"{hostname} is up!")
# else:
#   print (f"{hostname} is down!")

import pickle
from tkinter import *
from  tkinter import ttk

class AppPing(Frame):
    def __init__(self,master=None) -> None:
        Frame.__init__(self,master)
        self.master['bg'] = '#AC99F2'
        self.pack(expand=True,fill=BOTH)


        menu = LabelFrame(self,text="Opciones")
        menu.grid(column=2,row=0,sticky=S+N+E+W)

        label_nombre = Label(menu,text="Nombre")
        label_nombre.pack(side=TOP)
        self.entry_nombre = Entry(menu)
        self.entry_nombre.pack(side=TOP,padx = 10, pady = 5)

        label_ip = Label(menu,text="IP")
        label_ip.pack(side=TOP)
        self.entry_ip = Entry(menu)
        self.entry_ip.pack(side=TOP,padx = 10, pady = 5)

        button_agregar = Button(menu,text="Agregar",command=lambda: self.insertar_fila((self.entry_nombre.get(),self.entry_ip.get(),"Desconectado")))
        button_agregar.pack(side=TOP)

        self.label_error = Label(menu,text="",fg="red")
        self.label_error.pack(side=TOP)


        tabla_scrolly = Scrollbar(self)
        tabla_scrolly.grid(column=1,row=0,sticky=N+S)

        tabla_scrollx = Scrollbar(self,orient='horizontal')
        tabla_scrollx.grid(column=0,row=1,sticky=W+E)

        agarre = ttk.Sizegrip(self)
        agarre.grid(column=2,row=1,sticky=S+E)
        


        self.tabla = ttk.Treeview(self,yscrollcommand=tabla_scrolly.set, xscrollcommand =tabla_scrollx.set)
        self.tabla.bind('<Double-Button-1>', self.select)


        self.tabla.grid(column=0,row=0,sticky=S+N+E+W)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)

        tabla_scrolly.config(command=self.tabla.yview)
        tabla_scrollx.config(command=self.tabla.xview)

        #define our column

        self.crear_columnas(["nombre","ip","estado"])

    def select(self,*args):
        curItem = self.tabla.focus()
        textItem = self.tabla.item(curItem)["values"]
        print (textItem)
        
        newWindow = Toplevel(self.master)
        newWindow.title("New Window")
        Label(newWindow, text =textItem).pack()

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

    def crear_columnas(self, columnas):
        self.tabla['columns'] = tuple(columnas)

        # format our column
        self.tabla.column("#0", width=0,  stretch=NO)
        self.tabla.heading("#0",text="",anchor=W)
        for c in columnas:
            self.tabla.column(c,anchor=W,width=80)
            self.tabla.heading(c,text=str(c).upper(),anchor=W)
    

    def quit(self):
        Frame.quit(self)


if __name__ == "__main__":
    app = AppPing()
    app.master.title('PythonGuides')
    app.master.geometry("800x500")
    app.mainloop()
    app.quit()

