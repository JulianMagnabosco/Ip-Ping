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

        texto_label = Label(menu,text="Tasa de verificación")
        texto_label.pack(side=TOP)
        texto = Entry(menu)
        texto.pack(side=TOP,padx = 10, pady = 5)



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

        self.tabla['columns'] = ('nombre', 'ip', 'estado')

        # format our column
        self.tabla.column("#0", width=0,  stretch=NO)
        self.tabla.heading("#0",text="",anchor=W)
        self.insertar_columna("nombre")
        self.insertar_columna("ip")
        self.insertar_columna("estado")

        #add data 
        self.check()

    def select(self,*args):
        curItem = self.tabla.focus()
        textItem = self.tabla.item(curItem)["values"]
        print (textItem)
        
        newWindow = Toplevel(self.master)
        newWindow.title("New Window")
        Label(newWindow, text =textItem).pack()

    def insertar_fila(self, valores):
        self.tabla.insert(parent='',index='end',text='',
        values=valores)

    def insertar_columna(self, texto):
        self.tabla.column(texto,anchor=W,width=80)
        self.tabla.heading(texto,text=texto,anchor=W)
    
    def check(self):
        self.insertar_fila()

    def quit(self):
        Frame.quit(self)


if __name__ == "__main__":
    app = AppPing()
    app.master.title('PythonGuides')
    app.master.geometry("800x500")
    app.mainloop()
    app.quit()

