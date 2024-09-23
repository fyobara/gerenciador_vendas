from vendas import menu_vendas

def main():

    while True:
        print('''\n\t(1) Iniciar Venda\n\t(2) Extrato\n\t(3) Consulta\n\t(4) Sair\n''')
        opcao = int(input('Insira sua Resposta: '))

        match opcao:
            case 1:
                menu_vendas()
            case 2:
                from vendas import Relatorio
                Relatorio.emitir_relatorio()
            case 3:
                chave3 = int(input('Insira o Índice para Busca'))
                from vendas import Compra
                Compra.consultar_compra(chave3)
            case 4:
                break
            case _:
                print('Por favor, escolha uma opção válida')


if __name__ == "__main__":
    main()