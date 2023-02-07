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

        #scrollbar
        tabla_scrolly = Scrollbar(self)
        tabla_scrolly.pack(side=RIGHT, fill=Y)

        tabla_scrollx = Scrollbar(self,orient='horizontal')
        tabla_scrollx.pack(side= BOTTOM,fill=X)

        tabla = ttk.Treeview(self,yscrollcommand=tabla_scrolly.set, xscrollcommand =tabla_scrollx.set)


        tabla.pack(fill=BOTH)

        tabla_scrolly.config(command=tabla.yview)
        tabla_scrollx.config(command=tabla.xview)

        #define our column

        tabla['columns'] = ('dispositivo_id', 'dir_mac', 'dir_ip', 'estado', 'acciones')

        # format our column
        tabla.column("#0", width=0,  stretch=NO)
        tabla.column("dispositivo_id",anchor=CENTER, width=80)
        tabla.column("dir_mac",anchor=CENTER,width=80)
        tabla.column("dir_ip",anchor=CENTER,width=80)
        tabla.column("estado",anchor=CENTER,width=80)
        tabla.column("acciones",anchor=CENTER,width=80)

        #Create Headings 
        tabla.heading("#0",text="",anchor=CENTER)
        tabla.heading("dispositivo_id",text="Id",anchor=CENTER)
        tabla.heading("dir_mac",text="Name",anchor=CENTER)
        tabla.heading("dir_ip",text="Rank",anchor=CENTER)
        tabla.heading("estado",text="dir_ips",anchor=CENTER)
        tabla.heading("acciones",text="dir_ips",anchor=CENTER)

        #add data 
        tabla.insert(parent='',index='end',iid=0,text='',
        values=('1','Ninja','101','Oklahoma', 'Moore'))
        tabla.insert(parent='',index='end',iid=1,text='',
        values=('2','Ranger','102','Wisconsin', 'Green Bay'))
        tabla.insert(parent='',index='end',iid=2,text='',
        values=('3','Deamon','103', 'California', 'Placentia'))
        tabla.insert(parent='',index='end',iid=3,text='',
        values=('4','Dragon','104','New York' , 'White Plains'))
        tabla.insert(parent='',index='end',iid=4,text='',
        values=('5','CrissCross','105','California', 'San Diego'))

        
        tabla.insert(parent='',index='end',
        values=('5','asdasd','105','asdasd', 'San ad'))
        tabla.insert(parent='',index='end',
        values=('5','asdasd','105','asdasd', 'San ad'))
        tabla.insert(parent='',index='end',
        values=('5','asdasd','105','asdasd', 'San ad'))
        tabla.insert(parent='',index='end',
        values=('5','asdasd','105','asdasd', 'San ad'))
        tabla.insert(parent='',index='end',
        values=('5','asdasd','105','asdasd', 'San ad'))
        tabla.insert(parent='',index='end',
        values=('5','asdasd','105','asdasd', 'San ad'))
        tabla.insert(parent='',index='end',
        values=('5','asdasd','105','asdasd', 'San ad'))
        tabla.insert(parent='',index='end',
        values=('5','asdasd','105','asdasd', 'San ad'))
        tabla.insert(parent='',index='end',
        values=('5','asdasd','105','asdasd', 'San ad'))

if __name__ == "__main__":
    app = AppPing()
    app.master.title('PythonGuides')
    app.master.geometry('500x300')
    app.mainloop()
    app.quit()

