# import os
# hostname = "google.com" #example
# response = os.system("ping " + hostname)

# #and then check the response...
# if response == 0:
#   print (f"{hostname} is up!")
# else:
#   print (f"{hostname} is down!")

from tkinter import *
from  tkinter import ttk

class AppPing(Frame):
    def __init__(self,master=None) -> None:
        Frame.__init__(self,master)
        self.master['bg'] = '#AC99F2'
        self.pack(expand=True,fill=BOTH)

        """
        tabla = ttk.Frame(self)
        
        tabla.grid_columnconfigure(1, weight=1)

        data = [
            # Nr. Name  Active
            ["1",   "ST", "True"],
            ["2",   "SO", "Falseasdasdads"],
            ["3",   "SX", "True"],
            ]

        #define our column
        cx,cy=0,0
        for y in data:
            label_y = LabelFrame(tabla)
            
            for x in y:
                label_x = Label(label_y,text=x,width=len(x))
                label_x.grid(row=0,column=cx)
                cx+=1
            label_y.grid(row=cy,column=0)
            cy+=1
        tabla.pack()
        """
        
        menu = LabelFrame(self,text="Opciones")
        menu.grid(column=2,row=0,sticky=S+N+E+W)

        texto_label = Label(menu,text="Check Rate")
        texto_label.pack(side=TOP)
        texto = Entry(menu)
        texto.pack(side=TOP,padx = 10, pady = 5)



        tabla_scrolly = Scrollbar(self)
        # tabla_scrolly.pack(side=RIGHT, fill=Y)
        tabla_scrolly.grid(column=1,row=0,sticky=N+S)

        tabla_scrollx = Scrollbar(self,orient='horizontal')
        # tabla_scrollx.pack(side= BOTTOM,fill=X)
        tabla_scrollx.grid(column=0,row=1,sticky=W+E)

        agarre = ttk.Sizegrip(self)
        # tabla_scrollx.pack(side= BOTTOM,fill=X)
        agarre.grid(column=2,row=1,sticky=S+E)
        
        def select(a):
            curItem = self.tabla.focus()
            textItem = self.tabla.item(curItem)["values"]
            print (textItem)
            
            newWindow = Toplevel(master)
            newWindow.title("New Window")
            Label(newWindow, text =textItem).pack()

        self.tabla = ttk.Treeview(self,yscrollcommand=tabla_scrolly.set, xscrollcommand =tabla_scrollx.set)
        self.tabla.bind('<Double-Button-1>', select)


        # self.table.pack(expand=True,fill=BOTH)
        self.tabla.grid(column=0,row=0,sticky=S+N+E+W)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)

        tabla_scrolly.config(command=self.tabla.yview)
        tabla_scrollx.config(command=self.tabla.xview)

        #define our column

        self.tabla['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city')

        # format our column
        self.tabla.column("#0", width=0,  stretch=NO)
        self.tabla.heading("#0",text="",anchor=W)
        self.insertar_columna("player_id")
        self.insertar_columna("player_name")
        self.insertar_columna("player_Rank")
        self.insertar_columna("player_states")
        self.insertar_columna("player_city")


        #add data 
        self.insertar_fila(('1','Ninja','101','Oklahoma', 'Moore'))
        self.insertar_fila(('2','Ranger','102','Wisconsin', 'Green Bay'))
        self.insertar_fila(('3','Deamon','103', 'California', 'Placentia'))
        self.insertar_fila(('4','Dragon','104','New York' , 'White Plains'))
        self.insertar_fila(('5','CrissCross','105','California', 'San Diego'))

    def insertar_fila(self, valores):
        self.tabla.insert(parent='',index='end',text='',
        values=valores)

    def insertar_columna(self, texto):
        self.tabla.column(texto,anchor=W,width=80)
        self.tabla.heading(texto,text=texto,anchor=W)

if __name__ == "__main__":
    app = AppPing()
    app.master.title('PythonGuides')
    app.master.geometry('500x300')
    app.mainloop()
    app.quit()

