class Estoque:
    estoque = {
        1 : ['Arroz', 20, 7.35, 5.0],
        2 : ['Feijão', 20, 8.2, 6.25],
        3 : ['Carne', 10, 29.9, 22.4],
        4 : ['Ovos', 15, 9.9, 7.5],
        5 : ['Leite', 10, 5.5, 4.0],
    }

    @classmethod
    def consulta_estoque(cls, chave: int) -> list:
        return cls.estoque.get(chave)

    @classmethod
    def atualizar_estoque(cls, produto: int, quantidade: int) -> bool:
        if quantidade <= cls.estoque.get(produto)[1]:
            cls.estoque.update({produto : [cls.estoque.get(produto)[0], cls.estoque.get(produto)[1] - quantidade, cls.estoque.get(produto)[2], cls.estoque.get(produto)[3]]})
            return True        
        else:
            print(f'Estoque insuficiente, temos apenas {cls.estoque.get(produto)[1]} unidades\nVamos tentar novamente')
            return False