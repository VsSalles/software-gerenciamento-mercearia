from Models import *
from DAO import *
from datetime import datetime

class ControllerCategoria:
    def cadastra_categoria(self, nova_categoria):
        dados = DaoCategoria.ler()
        cats = list(filter(lambda y:y.nome == nova_categoria, dados))

        if len(cats) > 0 :
            return False
        else:
            DaoCategoria.salvar(nova_categoria)
            return True

    def remove_categoria(self, categoria_del):
        x = DaoCategoria.ler()
        cat = list(filter(lambda y:y.nome == categoria_del, x))
        if len(cat) > 0:
            session.delete(cat[0])
            session.commit()
            return True
        else:
            return False
                                
    def altera_categoria(self, alterar_cat, alterada_cat):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x:x.nome == alterar_cat, x))
        if len(cat) > 0:   #se esse if for true, existe a categoria que quero alterar
            cat1 = list(filter(lambda x:x.nome == alterada_cat, x))
            if len(cat1) == 0: #se esse if for true, posso alterar a categoria
                cat[0].nome = alterada_cat
                session.commit()
                return True
            else:
                return 'ja existe'
        else:
            return 'nao existe'

    def mostra_categoria(self):
        x = DaoCategoria.ler()
        if len(x) > 0:
            for i in x:
                print(f'ID:{i.id}, CATEGORIA:{i.nome}')
        else:
            print('NAO EXISTE NENHUMA CATEGORIA CADASTRADA')

class ControllerEstoque:
    def cadastra_produto(self, nome, preco, id_categoria, quantidade):
        dados_p = DaoProduto.ler()
        dados_c = DaoCategoria.ler()
        prod = list(filter(lambda x:x.nome == nome, dados_p))
        cat = list(filter(lambda x:x.id == id_categoria, dados_c))
        if len(prod) == 0:
            if len(cat) > 0:
                DaoProduto.salvar(nome, preco, id_categoria)
                ler_denovo = DaoProduto.ler()
                prodd = list(filter(lambda x:x.nome == nome, ler_denovo))
                DaoEstoque.salvar(prodd[0].id, quantidade)
                return True
            else:
                return 'nao existe'
        else:
            return 'existe'

    def remove_produto(self,nome):
        dados_p = DaoProduto.ler()
        dados_e = DaoEstoque.ler()
        prod = [x for x in dados_p if x.nome == nome]
        est = [x for x in dados_e if x.id_produto == prod[0].id]
        if len(prod) > 0:
            session.delete(prod[0])
            session.delete(est[0])
            session.commit()
            return True
        else:
            return False
    
    def altera_produto(self, produto_alterar, novo_nome, novo_preco, id_nova_categoria, quantidade):
        dados_p = DaoProduto.ler()
        dados_c = DaoCategoria.ler()
        dados_e = DaoEstoque.ler()
        prod = [x for x in dados_p if x.nome == produto_alterar]
        if len(prod) > 0:
            x = [y for y in dados_p if y.nome == novo_nome]
            if len(x) == 0:
                cat = [x for x in dados_c if x.id == id_nova_categoria]
                if len(cat) > 0:
                    prod[0].nome = novo_nome, 
                    prod[0].preco = novo_preco
                    prod[0].id_categoria = id_nova_categoria
                    est = [x for x in dados_e if x.id_produto == prod[0].id]
                    est[0].quantidade = quantidade
                    session.commit()
                    return True
                else:
                    return 'nao existe essa categoria'                    
            else:
                return 'ja existe um prod com esse nome'
        else:
            return 'produto que deseja alterar nao existe'        
    def mostrar_estoque(self):
        x = DaoProduto.ler()
        y = DaoEstoque.ler()
        e = [x for x in y]
        intera = 0
        for p in x:
            print(f'ID:{p.id} NOME:{p.nome} PREÇO:{p.preco} ID_CATEGORIA:{p.id_categoria} QUANTIDADE:{e[intera].quantidade}')
            intera += 1
            if intera == len(e):
                break
        
        return True

class ControllerVenda:
    def cadastra_venda(self,nome_produto, comprador, vendedor, qtd_vendida):
        dados_p = DaoProduto.ler()
        dados_e = DaoEstoque.ler()
        dados_c = DaoPessoa.ler()
        dados_v = DaoFuncionario.ler()
        prod = [x for x in dados_p if x.nome == nome_produto]
        est = [x for x in dados_e if x.quantidade >= qtd_vendida]
        com = [x for x in dados_c if x.nome == comprador]
        ven = [x for x in dados_v if x.nome == vendedor]
        if len(prod) > 0:
            if len(est) > 0:
                if len(com) > 0:
                    if len(ven) > 0:
                        total_v = prod[0].preco * qtd_vendida
                        DaoVenda.salvar(Venda(id_produto_vendido=prod[0].id ,id_comprador=com[0].id ,id_vendedor=ven[0].id, qtd_vendida=qtd_vendida, total_venda=total_v))
                        est[0].quantidade -= qtd_vendida
                        session.commit()
                        return True
                    else:
                        return 'vendedor nao existe'
                else:
                    return 'comprador nao existe'
            else:
                return 'qtd insuficiente'
        else:
            return 'nao existe p'

    def relatorio_vendas(self):
        dados_v = DaoVenda.ler()
        dados_P = DaoProduto.ler()
        produtos = []
        for y in dados_P:
            for x in dados_v:
                if y.id == x.id_produto_vendido:
                    nome = y.nome
                    quantidade = x.qtd_vendida
                    tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
                    if len(tamanho) > 0:
                        produtos = list(map(lambda x: {'produto': nome, 'quantidade': x['quantidade'] + quantidade} if (x['produto'] == nome) else (x), produtos))
                    else:
                        produtos.append({'produto': nome, 'quantidade': quantidade})
        ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse=True)
        for i in ordenado:
            print(f"PRODUTO:{i['produto']} QUANTIDADE VENDIDA:{i['quantidade']}")
        return True

    def mostrar_vendas(self, data_inicio, data_termino):
        dados_vend = DaoVenda.ler()
        dados_p = DaoProduto.ler()
        dados_c = DaoPessoa.ler()
        dados_v = DaoFuncionario.ler()
        data_inicio1 = datetime.strptime(data_inicio, '%d/%m/%Y')
        data_termino2 = datetime.strptime(data_termino, '%d/%m/%Y')
        vend = [x for x in dados_vend if x.data >= data_inicio1 and x.data <= data_termino2] 
        for x in vend:
            prod = [y for y in dados_p if y.id ==x.id_produto_vendido]
            com = [c for c in dados_c if c.id == x.id_comprador]
            v = [v for v in dados_v if v.id == x.id_vendedor]
            print(f'PRODUTO:{prod[0].nome} CLIENTE:{com[0].nome} VENDEDOR:{v[0].nome} QTD VENDIDA:{x.qtd_vendida} TOTAL:R$:{x.total_venda} DATA:{x.data}')

class ControllerCliente:
    def cadastrar_cliente(self, nome, cpf, telefone, endereco, email):
        dados_c = DaoPessoa.ler()
        cli = [x for x in dados_c if x.cpf == str(cpf)]
        clit = [x for x in dados_c if x.tel == str(telefone)]
        clie = [x for x in dados_c if x.endereco == endereco]
        clim = [x for x in dados_c if x.email == email]
        if len(cli) == 0:
            if len(clit) == 0:
                if len(clie) == 0:
                    if len(clim) == 0:
                        DaoPessoa.salvar(Pessoa(nome=nome, cpf=str(cpf), tel=str(telefone), endereco=endereco, email=email))
                        return True               
                    else:
                        return 'email'                  
                else:
                    return 'end'
            else:
                return 'tel'           
        else:
            return 'cpf'
            
    def remover_cliente(self, cpf):
        dados_c = DaoPessoa.ler()
        cli = [x for x in dados_c if x.cpf == str(cpf)]
        if len(cli) > 0:
            session.delete(cli[0])
            session.commit()
            return True
        else:
            return 'cpf'
    
    def alterar_cliente(self, cpf_alterar, novo_tel, novo_endereco, novo_email):
        dados_c = DaoPessoa.ler()
        cli = [x for x in dados_c if x.cpf == str(cpf_alterar)]
        if len(cli) > 0:
            for x in dados_c:
                if str(x.tel) == str(novo_tel):
                    return 'tel'
                elif x.endereco == novo_endereco:
                    return 'end'
                elif x.email == novo_email:
                    return 'email'
            cli[0].tel = novo_tel
            cli[0].endereco = novo_endereco
            cli[0].email = novo_email
            session.commit()
            return True
        
    def mostrar_cliente(self):
        dados_c = DaoPessoa.ler()
        for x in dados_c:
            print(f'NOME:{x.nome} CPF:{x.cpf} TELEFONE:{x.tel} ENDERECO:{x.endereco} EMAIL:{x.email}')
        return True

class ControllerFuncionarios:
    def cadastrar_funcionario(self,nome,cpf, tel,endereco,email,clt):
        dados_f = DaoFuncionario.ler()
        func = [x for x in dados_f if x.cpf == cpf or x.tel == tel or x.endereco == endereco or x.email == email or x.clt == clt]
        if len(func) == 0:
            try:
                DaoFuncionario.salvar(Funcionario(nome=nome, cpf=cpf, tel=tel, endereco=endereco, email=email, clt=clt))
                return True
            except Exception as erro:
                print(f'error: {erro}')
        else:
            return False

    def remover_funcionario(self, clt):
        dados_f = DaoFuncionario.ler()
        func = [x for x in dados_f if x.clt == clt]
        if len(func) > 0:
            session.delete(func[0])
            session.commit()
        else:
            return False
    
    def alterar_funcionario(self, clt_alterar, novo_tel, novo_endereco, novo_email):
        dados_f = DaoFuncionario.ler()
        func = [x for x in dados_f if x.clt == clt_alterar]
        if len(func) > 0:
            verifica = [x for x in dados_f if x.tel == novo_tel or x.endereco == novo_endereco or x.email == novo_email]
            if len(verifica) == 0:
                func[0].tel = novo_tel
                func[0].endereco = novo_endereco
                func[0].email = novo_email
                session.commit()
                return True
            else:
                return False
        return 'nao existe'

    def mostrar_funcionario(self):
        dados_f = DaoFuncionario.ler()
        for x in dados_f:
            print(f'NOME:{x.nome} CPF:{x.cpf} TEL:{x.tel} ENDERECO:{x.endereco} EMAIL:{x.email} nºCLT:{x.clt}')
        return True
        
class ControllerFornecedores:
    def cadastra_fornecedor(self, nome, cnpj, tel, endereco, email, id_cat):
        dados_for = DaoFornecedor.ler()
        dados_c = DaoCategoria.ler()
        forn = [x for x in dados_for if x.cnpj == cnpj or x.tel == tel or x.endereco == endereco or x.email == email]
        if len(forn) == 0:
            cat = [x for x in dados_c if x.id == id_cat]
            if len(cat) > 0:
                DaoFornecedor.salvar(Fornecedor(nome=nome, cnpj=cnpj, tel=tel, endereco=endereco, email=email, id_categoria=id_cat))
                session.commit()
                return True
            else:
                return 'cat nao existe'
        else:
            return False

    def remove_fornecedor(self, cnpj):
        dados_forn = DaoFornecedor.ler()
        forn = [x for x in dados_forn if x.cnpj == cnpj]
        if len(forn) > 0:
            session.delete(forn[0])
            session.commit()
        else:
            return 'nao existe'

    def altera_fornecedor(self, cnpj_alterar, novo_tel, novo_endereco, novo_email):
        dados_f = DaoFornecedor.ler()
        forn = [x for x in dados_f if x.cnpj == cnpj_alterar]
        if len(forn) > 0:
            verifica = [x for x in dados_f if x.tel == novo_tel or x.endereco == novo_endereco or x.email == novo_email]
            if len(verifica) == 0:
                forn[0].tel = novo_tel
                forn[0].endereco = novo_endereco
                forn[0].email = novo_email
                session.commit()
                return True
            else:
                return False
        else:
            return 'nao existe cnpj'
    
    def mostrar_fornecedor(self):
        dados_forn = DaoFornecedor.ler()
        dados_cat = DaoCategoria.ler()
        for x in dados_forn:
            cat = [y for y in dados_cat if y.id == x.id_categoria]
            print(f'NOME:{x.nome} CNPJ:{x.cnpj} TEL:{x.tel} ENDERECO:{x.endereco} EMAIL:{x.email} CATEGORIA:{cat[0].nome}')
        return True

