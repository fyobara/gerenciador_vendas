class Relatorio:
    
    relatorio_vendas = []
    relatorio_custos = []

    @classmethod
    def adicionar_compra(cls, compra: float, custo: float) -> None:
        cls.relatorio_vendas.append(compra)
        cls.relatorio_custos.append(custo)
        
    
    @classmethod
    def emitir_relatorio(cls) -> None:

        print(f'Total de Compras: {len(cls.relatorio_vendas)}')
        print(f'Menor Compra: R${min(cls.relatorio_vendas):.2f}')
        print(f'Maior Compra: R${max(cls.relatorio_vendas):.2f}')
        print(f'Tiket Médio: R${(sum(cls.relatorio_vendas) / len(cls.relatorio_vendas)):.2f}')
        print(f'Faturamento Bruto: R${sum(cls.relatorio_vendas):.2f}')
        print(f'Faturamento Líquido: R${(sum(cls.relatorio_vendas) - sum(cls.relatorio_custos)):.2f}')
        print(f'Margem de Lucro: {((sum(cls.relatorio_vendas) - sum(cls.relatorio_custos)) / sum(cls.relatorio_vendas) * 100):.2f}%')