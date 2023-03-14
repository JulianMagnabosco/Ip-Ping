import pickle

class Opciones():
    
    intervalo=100
    tamanio_p=60
    tiempo_espera=2000
    ips = list()

    # def __setattr__(self, __name: str, __value) -> None:
    #     if __name != "ips":
    #         valor = max(__value,getattr(Opciones(),__name))
    #         self.__dict__[__name] =valor
    #     else:
    #         self.__dict__[__name] =__value

    def cargar(self):
        with open("data",mode="+ab") as archivo:
            try:
                archivo.seek(0)
                self = pickle.load(archivo)
            except:
                print("sin datos")
    
    def guardar(self):
        with open("data",mode="wb") as archivo:
            pickle.dump(self,archivo)
