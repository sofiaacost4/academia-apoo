from datetime import datetime
class Aula:
    def __init__(self, id, data, dt_inicio, dt_fim, id_instrutor ):
        self.set_id(id)
        self.set_data(data)
        self.set_dt_inicio(dt_inicio)
        self.set_dt_fim(dt_fim)
        self.set_id_instrutor(id_instrutor)
    
    def  __str__(self): 
        return f'{self.__id} - {self.__data.strftime('%d/%m/%y %H:%M')} - {self.__dt_inicio.strftime('%d/%m/%Y %H:%M')} - {self.__dt_fim.strftime('%d/%m/%Y %H:%M')} - {self.__id_instrutor}'
    
    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_dt_inicio(self): return self.__dt_inicio
    def get_dt_fim(self): return self.__dt_fim
    def get_id_instrutor(self): return self.__id_instrutor

    def set_id(self, id): self.__id = id
    def set_data(self, data):
        if data.year < 2025: raise ValueError("Datas passadas são inválidas.")
        self.__data = data
    def set_dt_inicio(self, dt_inicio): self.__dt_inicio
    def set_
