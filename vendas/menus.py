def menu_vendas():

    from vendas import Estoque
    from vendas import Venda
    from vendas import Compra

    '''
    O produto e sua quantidade são adicionados pelo usuário, o valor e custo unitários são consultados.
    A disponibilidade do produto é verificada e somente assim a venda pode ser instanciada e adicionada a compra
    Opção de encerrar a compra é ofericida ao usuário ao fim, a compra é finalizada e o programa retorna a main
    
    '''
    
    while True:

        try:
            produto = int(input("Digite o ID do produto: "))
            quantidade = int(input("Digite a quantidade: "))
        except ValueError:
            print('A identificação e quantidade dos produtos devem ser numéricos inteiros\nVamos tentar novamente')
            continue


        try:
            valor = float(Estoque.consulta_estoque(produto)[2])
            custo = float(Estoque.consulta_estoque(produto)[3])
        except Exception:
            print('Produto informado não pode ser identificado\nVamos tentar novamente')
            continue
        

        if Estoque.atualizar_estoque(produto, quantidade) == False:     #Confere disponibilidade do produto 
            continue
        else:                                                                             
            venda = Venda(produto, quantidade, valor, custo)            #Criação de uma instância da classe Venda
            Compra.adicionar_venda(venda)                               

        
        print('''\n(1) Finalizar Compra''')
        if input('Insira sua Resposta: ').strip() == '1':
            Compra.finalizar_compra()
            break 


def menu_pagamentos(total: float):
    
    from vendas import pagamento_dinheiro, pagamento_debito, pagamento_credito, pagamento_pix 
    
    '''
    É invocando após finalizar uma compra e invoca as resepctivas funções de processamento de pagamento
    
    '''
    
    while True:

        print(f'Valor pendente: R${total}')
        print('''\n\t(1) Dinheiro\n\t(2) Débito\n\t(3) Crédito\n\t(4) Pix''')
        opcao = int(input('Insira sua Resposta: '))

        match opcao:
            case 1:
                if pagamento_dinheiro(total):
                    print('Pagamento Realizado')
                    break
                else:
                    print('Falha ao processar pagamento\nTente Novamente')
                    continue
            case 2:
                if pagamento_debito(total):
                    print('Pagamento Realizado')
                    break
                else:
                    print('Falha ao processar pagamento\nTente Novamente')
                    continue
            case 3:
                if pagamento_credito(total):
                    print('Pagamento Realizado')
                    break
                else:
                    print('Falha ao processar pagamento\nTente Novamente')
                    continue
            case 4:
                if pagamento_pix(total):
                    print('Pagamento Realizado')
                    break
                else:
                    print('Falha ao processar pagamento\nTente Novamente')
                    continue
            case _:
                print('Por favor, escolha uma opção válida')