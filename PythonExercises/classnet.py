
class Netclass:
    def __init__(self,id,name,client_type,product_type,total):
        self.id = id
        self.name = name
        self.client_type = client_type
        self.product_type = product_type
        self.total = total

    def __str__(self):
        r = (f"Identificacion: {self.id:<10} | Titular:{self.name:<30} | Tipo de cliente: {self.client_type} " 
             f"|Tipo de producto: {self.product_type} | Monto mensual: {self.total:<10}")
        return r