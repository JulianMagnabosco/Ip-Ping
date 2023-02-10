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
        self.pack()

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
        

        tabla_scrolly = Scrollbar(self)
        tabla_scrolly.pack(side=RIGHT, fill=Y)

        tabla_scrollx = Scrollbar(self,orient='horizontal')
        tabla_scrollx.pack(side= BOTTOM,fill=X)

        
        def select(a):
            curItem = self.table.focus()
            print (self.table.item(curItem)["values"])
            curRow = self.table.set(a)
            print(curRow)

        self.table = ttk.Treeview(self,yscrollcommand=tabla_scrolly.set, xscrollcommand =tabla_scrollx.set)
        self.table.bind('<Double-Button-1>', select)


        self.table.pack()

        tabla_scrolly.config(command=self.table.yview)
        tabla_scrollx.config(command=self.table.xview)

        #define our column

        self.table['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city')

        # format our column
        self.table.column("#0", width=0,  stretch=NO)
        self.table.column("player_id",anchor=CENTER, width=80)
        self.table.column("player_name",anchor=CENTER,width=80)
        self.table.column("player_Rank",anchor=CENTER,width=80)
        self.table.column("player_states",anchor=CENTER,width=80)
        self.table.column("player_city",anchor=CENTER,width=80)

        #Create Headings 
        self.table.heading("#0",text="",anchor=CENTER)
        self.table.heading("player_id",text="Id",anchor=CENTER)
        self.table.heading("player_name",text="Name",anchor=CENTER)
        self.table.heading("player_Rank",text="Rank",anchor=CENTER)
        self.table.heading("player_states",text="States",anchor=CENTER)
        self.table.heading("player_city",text="States",anchor=CENTER)

        #add data 
        self.table.insert(parent='',index='end',iid=0,text='',
        values=('1','Ninja','101','Oklahoma', 'Moore'))
        self.table.insert(parent='',index='end',iid=1,text='',
        values=('2','Ranger','102','Wisconsin', 'Green Bay'))
        self.table.insert(parent='',index='end',iid=2,text='',
        values=('3','Deamon','103', 'California', 'Placentia'))
        self.table.insert(parent='',index='end',iid=3,text='',
        values=('4','Dragon','104','New York' , 'White Plains'))
        self.table.insert(parent='',index='end',iid=4,text='',
        values=('5','CrissCross','105','California', 'San Diego'))

        
        self.table.insert(parent='',index='end',
        values=('5','asdasd','105','asdasd', 'San ad'))
        self.table.insert(parent='',index='end',
        values=('5','asdasd','105','asdasd', 'San ad'))
        self.table.insert(parent='',index='end',
        values=('5','asdasd','105','asdasd', 'San ad'))
        self.table.insert(parent='',index='end',
        values=('5','asdasd','105','asdasd', 'San ad'))
        self.table.insert(parent='',index='end',
        values=('5','asdasd','105','asdasd', 'San ad'))
        self.table.insert(parent='',index='end',
        values=('5','asdasd','105','asdasd', 'San ad'))
        self.table.insert(parent='',index='end',
        values=('5','asdasd','105','asdasd', 'San ad'))
        self.table.insert(parent='',index='end',
        values=('5','asdasd','105','asdasd', 'San ad'))
        self.table.insert(parent='',index='end',
        values=('5','asdasd','105','asdasd', 'San ad'))




if __name__ == "__main__":
    app = AppPing()
    app.master.title('PythonGuides')
    app.master.geometry('500x300')
    app.mainloop()
    app.quit()

