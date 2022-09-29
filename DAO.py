from Models import *

session = Session()


class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        x = Categoria(nome=categoria)
        session.add(x)
        session.commit()
         
    @classmethod
    def ler(cls):
        x = session.query(Categoria).all()
        return x 
  
class DaoPessoa:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        x = Pessoa(nome=pessoa.nome, cpf=pessoa.cpf, endereco=pessoa.endereco, tel=pessoa.tel, email=pessoa.email)
        session.add(x)
        session.commit()

    @classmethod
    def ler(cls):
       x = session.query(Pessoa).all()
       return x

class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        x = Venda(id_produto_vendido=venda.id_produto_vendido ,id_comprador=venda.id_comprador ,id_vendedor=venda.id_vendedor, qtd_vendida=venda.qtd_vendida, total_venda=venda.total_venda)
        session.add(x)
        session.commit()

    @classmethod
    def ler(cls):
        x = session.query(Venda).all()
        return x

class DaoProduto:
    @classmethod
    def salvar(cls, nome, preco, id_categoria):
        x = Produtos(nome=nome, preco=preco, id_categoria=id_categoria)
        session.add(x)
        session.commit()
    
    @classmethod
    def ler(cls):
        x = session.query(Produtos).all()
        return x 

class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        x = Fornecedor(nome=fornecedor.nome, cnpj=fornecedor.cnpj, tel=fornecedor.tel, endereco=fornecedor.endereco, email=fornecedor.email, id_categoria=fornecedor.id_categoria)
        session.add(x)
        session.commit()

    @classmethod
    def ler(cls):
        x = session.query(Fornecedor).all()
        return x

class DaoEstoque:
    @classmethod
    def salvar(cls, id_pro, qtd):
        x = Estoque(id_produto=id_pro, quantidade=qtd)
        session.add(x)
        session.commit()

    @classmethod
    def ler(cls):
       x = session.query(Estoque).all()
       return x

class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        x = Funcionario(nome=funcionario.nome, cpf=funcionario.cpf, tel=funcionario.tel, endereco=funcionario.endereco, email=funcionario.email, clt=funcionario.clt)
        session.add(x)
        session.commit()
       
    
    @classmethod
    def ler(cls):
        x = session.query(Funcionario).all()
        return x





