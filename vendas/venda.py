from datetime import datetime
from vendas import Estoque

class Venda:

    '''
    A classe destina-se a definir o objeto do tipo venda e garantir sua ideal exibição

    '''

    def __init__(self, produto, quantidade, valor, custo):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor
        self.custo = custo
        self.hora = datetime.now().strftime("%H:%M:%S    %d/%m/%Y")


    def __str__(self) -> str:
        return (f"|| {self.quantidade}x    {Estoque.consulta_estoque(self.produto)[0]}    R${self.quantidade * self.valor:.2f} ||  {self.hora} ||")