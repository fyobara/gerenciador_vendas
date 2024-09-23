def pagamento_dinheiro(total):
    
    if float(valor := input('Insira o valor em espécie')) > total:
        print(f'Troco: R${valor - total}')
        return True
    else:
        print('Valor insuficiente')
        return False
    
def pagamento_debito():
    print('Gateway de Pagamento')
    return True


def pagamento_credito():
    print('Gateway de Pagamento')
    return True


def pagamento_pix():
    print('Gateway de Pagamento')
    return True