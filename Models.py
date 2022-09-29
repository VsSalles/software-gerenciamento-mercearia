from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
import datetime
from locale import setlocale, LC_ALL

setlocale(LC_ALL, 'pt-BR.utf-8')

USUARIO = 'root'
SENHA = 'teste12345678'
HOST = 'localhost'
PORTA = '3306'
BANCO = 'merceariav2'
CON = f'mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORTA}/{BANCO}'
engine = create_engine(CON, echo=True)
Session = sessionmaker(bind=engine) 
Base = declarative_base()


class Pessoa(Base):
    __tablename__ = 'Pessoa'
    id = Column(Integer, primary_key= True)
    nome = Column(String(100))
    cpf = Column(String(11))
    tel = Column(String(15)) 
    endereco = Column(String(100))
    email = Column(String(30))

class Categoria(Base):
    __tablename__ = 'Categoria'
    id = Column(Integer, primary_key= True)
    nome = Column(String(100))
        
class Produtos(Base):
    __tablename__ = 'Produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    preco = Column(Float)
    id_categoria = Column(Integer, ForeignKey('Categoria.id'))

class Estoque(Base):
    __tablename__ = 'Estoque'
    id_estoque = Column(Integer, primary_key= True)
    id_produto = Column(Integer, ForeignKey('Produtos.id'))
    quantidade = Column(Integer)

class Funcionario(Base):
    __tablename__ = 'Funcionarios'
    id = Column(Integer, primary_key= True)
    nome = Column(String(100))
    cpf = Column(String(11))
    tel = Column(String(15))
    endereco = Column(String(100))
    email = Column(String(30))
    clt = Column(String(11))

class Venda(Base):
    __tablename__ = 'Vendas'
    id_venda = Column(Integer, primary_key= True)
    id_produto_vendido = Column(Integer, ForeignKey('Produtos.id'))
    id_comprador = Column(Integer, ForeignKey('Pessoa.id'))
    id_vendedor = Column(Integer, ForeignKey('Funcionarios.id'))
    qtd_vendida = Column(Integer)
    total_venda = Column(Integer)
    data = Column(DateTime, default=datetime.datetime.now())

class Fornecedor(Base):
    __tablename__ = 'Fornecedores'
    id = Column(Integer, primary_key= True)
    nome = Column(String(100))
    cnpj = Column(String(14))
    tel = Column(String(15))
    endereco = Column(String(100))
    email = Column(String(30))
    id_categoria = Column(Integer, ForeignKey('Categoria.id'))

#Base.metadata.create_all(engine)