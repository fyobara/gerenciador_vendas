'''
A classe Compra possui 4 métodos

1.adicionar_venda   - Recebe um objeto, verifica se pertence a classe Venda e adiciona ao dict compra
2.finalizar_compra  - Armazena o dict compra, redefine o dicionario e invoca adicionar_compra com preço e custo totais
3.consultar_compra  - Recebe um inteiro, utiliza-o como chave de busca, percorre e exibe a compra buscada
4.consultar_extrato - Percorre todas as compras e as exibe

'''

class Compra:

    registro_compras = {}       #Dicionario que armazena dicionarios compra
    indice_registro = 1         #Chave que empilha compras
    compra = {}                 #Dicionario que armazena objetos da Classe Venda
    indice_compra = 1           #Chave que empilha vendas


    @classmethod
    def adicionar_venda(cls, venda: object) -> None: 
        from vendas import Venda
        if isinstance(venda, Venda):
            cls.compra.update({cls.indice_compra : venda})
            cls.indice_compra += 1
        else:
            print('Erro, Objeto Não Pertence a Classe Vendas')


    @classmethod
    def finalizar_compra(cls) -> None:
        cls.registro_compras.update({cls.indice_registro: cls.compra.copy()})   #Armazena cópia do dicionário
        cls.indice_registro += 1                                                #Atualiza o indice do registro
        cls.indice_compra = 1                                                   #Redefini o indice do dicionário compra
        cls.compra.clear()                                                      #Limpa o dicionário compra
        total_compra, custo_total  = cls.consultar_extrato()

        from vendas import Relatorio
        Relatorio.adicionar_compra(total_compra, custo_total)                   #Invoca adicionar_compra com preço e custo

        from vendas import menu_pagamentos
        menu_pagamentos(total_compra)                                           #Invoca adicionar_compra com total_compra


        
    @classmethod
    def consultar_compra(cls, chave: int) -> None:
        if chave in cls.registro_compras:
            compra = cls.registro_compras[chave]
            print(f'Compra {chave}:')
            for venda_id, venda in compra.items():
                print(f'  Venda {venda_id}: {venda}')
        else:
            print(f'Compra {chave} não pode ser encontrada.')


    @classmethod
    def consultar_extrato(cls) -> float:
        for compra_id, compra in cls.registro_compras.items():      #Percorre Dicionário de Compras
            print(f'\nCompra {compra_id}:')
            total_compra = 0
            custo_total = 0

            for venda_id, venda in compra.items():                  #Percorre Dicionário de Vendas
                print(f'{venda_id} {venda}')
                total_compra += venda.valor * venda.quantidade      #Atualiza total_compra
                custo_total += venda.custo * venda.quantidade       #Atualiza custo_total

            print(f'\nTotal:  R${total_compra:.2f}')

        return total_compra, custo_total