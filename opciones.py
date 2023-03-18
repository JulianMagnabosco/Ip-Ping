import pickle

class Opciones():
    

    def __init__(self):
        self.intervalo=100
        self.tamanio_p=60
        self.cantidad_p=4
        self.tiempo_espera=2000
        self.metodo_chequeo=0
        self.ips = list()

    def cargar(self):
        data = Opciones()
        with open("data",mode="+ab") as archivo:
            try:
                archivo.seek(0)
                data = pickle.load(archivo)
            except:
                print("sin datos")
        return data
    
    def guardar(self):
        with open("data",mode="wb") as archivo:
            try:
                pickle.dump(self,archivo)
            except:
                print("error datos")
