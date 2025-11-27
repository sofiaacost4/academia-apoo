class Pagamento:
    def __init__(self, id, status, valor, id_inscricao):
        self.set_id(id)
        self.set_status(status)
        self.set_valor(valor)

    def __str__(self):
        return f'{self.__id} - {self.__status} - {self.__valor}'

    def get_id(self): return self.__id
    def get_status(self): return self.__status
    def get_valor(self): return self.__valor

    def set_id(self, id): self.__id = id 
    def set_status(self, status): self.__status = status
    def set_valor(self, valor): self.__valor = valor

    def to_json(self):
        dic = {"id": self.__id, "status": self.__status, "valor": self.__valor}
        return dic
    
    @staticmethod
    def from_json(dic):
       return Pagamento(dic["id"], dic["status"], dic["valor"])
    
     import json
    from models.dao import DAO

    class PagamentoDAO(DAO):
         @classmethod
         def abrir(cls):
              cls._objetos = []
              try:
                   with open("pagamentos.json", mode="r") as arquivo:
                        list_dic = json.load(arquivo)
                        for dic in list_dic:
                             obj = Pagamento.from_json(dic)
                             cls.objetos.append(obj)
              except FileNotFoundError:
                   pass
    