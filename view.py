from Controller import *

if __name__ == '__main__':
    print('SOFTWARE GERENCIAMENTO MERCEARIA V2')
    while True:
        print('BEM VINDO AO MENU!!!')
        print('OPÇÕES:\n 1-AREA CATEGORIAS\n 2-AREA FUNCIONARIOS\n 3-AREA ESTOQUE\n 4-AREA FORNECEDORES\n 5-AREA VENDAS\n 6-AREA CLIENTES\n 7-SAIR')
        escolha = input('Digite uma das opções: ')
        if escolha == '7':
            print('SAINDOOOO')
            break
        elif escolha == '1':
            print('BEM VINDO A AREA CATEGORIA AQUI VOCE TEM AS SEGUINTES FUNCIONALIDADE:')
            print(' 1-CADASTRO DE CATEGORIAS\n 2-REMOÇÃO DE CATEGORIAS\n 3-ALTERARAÇÃO DE CATEGORIAS\n 4-LISTAR CATEGORIAS')
            escolha = input('digite uma das opções: ')
            if escolha == '1':
                print('CERTO VAMOS CADASTAR UMA NOVA CATEGORIA PARA SEUS PRODUTOS')
                x = ControllerCategoria()
                try:
                    x.cadastra_categoria(nova_categoria=input('DIGITE O NOME DA CATEGORIA: '))
                    print(f'CATEGORIA CADASTRADA COM SUCESSO!!')
                    break
                except Exception as e:
                    erro = e
                    print('OPS ocorreu um erro')
            elif escolha == '2':
                print('CERTO VAMOS REMOVER A CATEGORIA')
                try:
                    c = ControllerCategoria()
                    categoria_del=input('Digite o nome da categoria que deseja remover: ')
                    c.remove_categoria(categoria_del)
                    if c.remove_categoria == False:
                        print('categoria nao existe')
                    else:
                        print('categoria removida com sucesso')
                        break
                except Exception as e:
                    erro = e
                    print('OPS ocorreu um erro')
                    print(erro)
            elif escolha == '3':
                print('CERTO VAMOS ALTERAR UMA CATEGORIA')
                c = ControllerCategoria()
                alterar_cat = input('digite o nome da categoria que deseja alterar: ')
                alterada_cat =input('digite o novo nome: ')
                try:
                    c.altera_categoria(alterar_cat=alterar_cat, alterada_cat=alterada_cat)
                    print('CATEGORIA ALTERADA COM SUCESSO!!!')
                    break
                except Exception:
                    print('ERRO')
            elif escolha == '4':
                print('CERTO LISTANDO CATEGORIAS:')
                c = ControllerCategoria()
                try:
                    c.mostra_categoria()
                    break
                except Exception:
                    print('ERRO')                            
        elif escolha == '2':
            f = ControllerFuncionarios()
            print('BEM VINDO A AREA FUNCIONARIOS')
            print('TEMOS AS SEGUINTES FUNCIONALIDADES:')
            print('1-CADASTRO DE FUNCIONARIOS\n2-REMOÇÃO DE FUNCIONARIOS\n3-ALTERAÇÃO DE FUNCIONARIOS\n4-LISTAGEM DE FUNCIONARIOS')
            escolha = input('digite uma das opçoes: ')
            if escolha == '1':
                print('CERTO VAMOS CADASTRAR UM NOVO FUNCIONARIO')
                nome = input('digite o nome do funcionario: ')
                cpf = input('digite o cpf do funcionario: ')
                tel = input('digite o telefone do funcionario: ')
                endereco = input('digite o endereco do funcionario: ')
                email = input('digite o email do funcionario: ')
                clt = input('digite o numero da clt do funcionario: ')
                try:
                    f.cadastrar_funcionario(nome, cpf, tel, endereco, email, clt)
                    print('FUNCIONARIO CADASTRADO COM SUCESSO')       
                    break
                except Exception:            
                    print('OCORREU UM ERRO')
                    break
            elif escolha == '2':
                print('CERTO VAMOS REMOVER UM FUNCIONARIO')
                try:
                    f.remover_funcionario(clt=input('digite o numero da clt do funcionario que deseja remover: '))
                    print('Funcionario removido com sucesso')
                    break
                except Exception:
                    print('ERRO')
                    break
            elif escolha == '3':
                print('CERTO VAMOS ALTERAR UM FUNCIONARIO')
                try:
                    clt_alterar = input('Digite o numero da clt do funcionario que deseja alterar: ')
                    novo_tel = input('Digite o novo tel do funcionario: ')
                    novo_endereco = input('Digite o novo endereco do funcionario: ')
                    novo_email= input('Digite o novo email do funcionario: ')
                    f.alterar_funcionario(clt_alterar, novo_tel, novo_endereco, novo_email)
                    print('FUNCIONARIO ALTERADO COM SUCESSO')
                    break
                except Exception:
                    print('ERRO')
            elif escolha == '4':
                print('CERTO VAMOS LISTAR  OS FUNCIONARIOS')
                try:
                    f.mostrar_funcionario()
                    break
                except Exception:
                    print('ERRO')
        elif escolha == '3':
            e = ControllerEstoque()
            print('BEM VINDO A AREA ESTOQUE')
            print('TEMOS AS SEGUINTES FUNCIONALIDADES:')
            print('1-CADASTRO DE PRODUTOS\n2-REMOÇÃO DE PRODUTOS\n3-ALTERAÇÃO DE PRODUTOS\n4-LISTAGEM DE PRODUTOS EM ESTOQUE')
            escolha = input('digite uma das opçoes: ')
            if escolha == '1':
                print('CERTO VAMOS CADASTAR UM NOVO PRODUTO')
                nome = input('digite o nome do produto: ')
                preco = input('digite o preco do produto: ')
                id_categoria = int(input('digite o id da categoria desse produto: '))
                quantidade = input('digite a quantidade que tera em estoque: ')
                try:
                    e.cadastra_produto(nome, preco, id_categoria, quantidade)
                    print('PRODUTO CADASTRADO COM SUCESSO')
                    break
                except Exception:
                    print('ERRO')
                    break
            elif escolha == '2':
                print('CERTO VAMOS REMOVER UM PRODUTO')
                try:
                    e.remove_produto(nome=input('Digite o nome do produto que deseja remover: '))
                    print('produto removido com sucesso')
                    break
                except Exception:
                    print('ERRO')
                    break
            elif escolha == '3':
                print('CERTO VAMOS ALTERAR PRODUTO')
                produto_alterar = input('digite o nome do produto que deseja alterar: ')
                novo_nome = input('digite o novo nome do produto: ')
                id_nova_categoria = input('digite o id da nova categoria: ')
                novo_preco = input('digite o novo preco desse produto: ')
                quantidade = input('digite a quantidade em estoque do novo produto: ')
                try:
                    e.altera_produto(produto_alterar, novo_nome, novo_preco, int(id_nova_categoria), quantidade)
                    print('PRODUTO ALTERADO COM SUCESSO')
                    break
                except Exception:
                    print('ERRO')
                    break
            elif escolha == '4':
                print('CERTO VAMOS LISTAR OS PRODUTO')
                try:
                    e.mostrar_estoque()
                    break
                except Exception as e:
                    print(f'ERRO {e}')
                    break
        elif escolha == '4':
            f = ControllerFornecedores()
            print('BEM VINDO A AREA FORNECEDORES')
            print('TEMOS AS SEGUINTES FUNCIONALIDADES:')
            print('1-CADASTRO DE FORNECEDORES\n2-REMOÇÃO DE FORNECEDORES\n3-ALTERAÇÃO DE FORNECEDORES\n4-LISTAGEM DE FORNECEDORES')
            escolha = input('digite uma das opçoes: ')
            if escolha == '1':
                print('CERTO VAMOS CADASTRAR UM NOVO FORNECEDOR')
                nome = input('digite o nome do novo fornecedor: ')
                cnpj = input('digite o cnpj do fornecedor: ')
                tel = input('digite o telefone do fornecedor: ')
                endereco = input('digite o endereco do fornecedor: ')
                email = input('digite o email do fornecedor: ')
                id_cat = input(f'digite o id da categoria fornecedida pelo {nome}: ')
                try:
                    f.cadastra_fornecedor(nome, cnpj, tel, endereco, email, int(id_cat))
                    print('FORNECEDOR CADASTRADO COM SUCESSO')
                    break
                except Exception:
                    print('ERRO')
            elif escolha == '2':
                print('CERTO VAMOS REMOVER UM FORNECEDOR')
                try:
                    f.remove_fornecedor(cnpj=input('digite o cnpj do fornecedor que deseja remover: '))
                    print('FORNECEDOR REMOVIDO COM SUCESSO')
                    break
                except Exception:
                    print('ERRO')
                    break
            elif escolha == '3':
                print('CERTO VAMOS ALTERAR UM FORNECEDOR')
                cnpj_alterar = input('digite o cnpj do fornecedor que deseja alterar: ')
                novo_tel = input('digite o novo telefone: ')
                novo_endereco = input('digite o novo endereco: ')
                novo_email = input('digite o novo email: ')
                try:
                    f.altera_fornecedor(cnpj_alterar, novo_tel, novo_endereco, novo_email)
                    print('FORNECEDOR ALTERADO COM SUCESSO')
                    break
                except Exception as e:
                    print(f'ERRO {e}')
                    break
            elif escolha == '4':
                print('CERTO VAMOS LISATR OS FORNECEDORES')
                try:
                    f.mostrar_fornecedor()
                    break
                except Exception as e:
                    print(f'ERRO {e}')
        elif escolha == '5':
            v = ControllerVenda()
            print('BEM VINDO A AREA VENDAS')
            print('TEMOS AS SEGUINTES FUNCIONALIDADES:')
            print('1-FAZER VENDAS\n2-RELATORIA DE TODAS AS VENDAS\n3-VENDAS POR DATA')
            escolha = input('digite uma das opçoes: ')
            if escolha == '1':
                print('CERTO VAMOS EFETUAR UMA VENDA')
                nome_produto = input('digite o nome do produto vendido: ')
                comprador = input('digite o nome do comprador: ')
                vendedor= input('digite o nome do vendedor: ')
                qtd_vendida = input('digite a quantidade vendida: ')
                try:
                    v.cadastra_venda(nome_produto, comprador, vendedor, int(qtd_vendida))
                    print('VENDA REALIZADA COM SUCESSO')  
                    break               
                except Exception as e:
                    print(f'ERRO {e}')
                    break
            elif escolha == '2':
                print('CERTO VAMOS AOS RELATORIOS DETALHE AS VENDAS ESTAO ORDENADAS POR PRODUTOS MAIS VENDIDOS')
                try:
                    v.relatorio_vendas()
                    break
                except Exception as e:
                    print(f'ERRO {e}')
                    break
            elif escolha == '3':
                print('CERTO SEGUE VENDAS ENTRE UMA DATA E OUTRA')
                data_inicio = input('digite a data de inicio ex: 25/09/2022\ninicio: ')
                data_termino = input('digite a data de termino detalhe deve ser maior que data de inicio ex: 29/09/2022\ntermino: ')
                try:
                    v.mostrar_vendas(data_inicio, data_termino)
                    break
                except Exception as e:
                    print(f'ERRO {e}')      
        elif escolha == '6':
            c = ControllerCliente()
            print('BEM VINDO A AREA CLIENTES')
            print('TEMOS AS SEGUINTES FUNCIONALIDADES:')
            print('1-CADASTRO DE CLIENTES\n2-REMOÇÃO DE CLIENTES\n3-ALTERAÇÃO DE CLIENTES\n4-LISTAGEM DE CLIENTES')
            escolha = input('digite uma das opçoes: ')
            if escolha == '1':
                print('CERTO VAMOS CADASTRAR UM CLINTES')
                nome = input('digite o nome do cliente: ')
                cpf = input('digite o cpf do cliente: ')
                telefone = input('digite o telefone do cliente: ')
                endereco = input('digite o endereco do cliente: ')
                email = input('digite o email do cliente: ')
                try:
                    c.cadastrar_cliente(nome,cpf,telefone,endereco,email)
                    print('CLIENTE CADASTRADO COM SUCESSO')
                    break
                except Exception as e:
                    print(f'ERRO {e}')
            elif escolha == '2':
                print('CERTO VAMOS REMOVER UM CLINTE')
                try:
                    c.remover_cliente(cpf=input('digite o cpf do cliente que deseja remover: '))
                    print('CLIENTE REMOVIDO COM SUCESSO')
                    break
                except Exception as e:
                    print(f'ERRO {e}')
                    break
            elif escolha == '3':
                print('CERTO VAMOS ALTERAR UM CLIENTE')
                cpf = input('digite o cpf do cliente que deseja alterar: ')
                telefone = input('digite o novo telefone: ')
                endereco = input('digite o novo endereco: ')
                email = input('digite o novo email: ')
                try:
                    c.alterar_cliente(cpf_alterar=cpf , novo_tel=telefone , novo_endereco=endereco , novo_email=email)
                    print('CLIENTE ALTERADO COM SUCESSO')
                    break
                except Exception as e:
                    print(f'ERRO {e}')
                    break
            elif escolha == '4':
                print('CERTO EXIBINDO CLIENTES')
                try:
                    c.mostrar_cliente()
                    break
                except Exception as e:
                    print(f'ERRO {e}')
                    break



            