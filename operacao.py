import mysql.connector
import conexaoBD #Classe que faz a conexão com Banco de Dados

db_connection = conexaoBD.conectar()
con = db_connection.cursor()

def inserir(cpf, nome, telefone, endereco, dataDeNascimento):
    try:
        sql = "Insert into pessoa(cpf, nome, telefone, endereco, dataDeNascimento) values('{}', '{}', '{}', '{}', '{}')".format(cpf, nome, telefone, endereco, tratarData(dataDeNascimento))
        con.execute(sql)
        db_connection.commit()#Inserção de dados no BD
        print("{} Linha Inserida!".format(con.rowcount))#rowcount = Contar quantas linhas foram afetadas

    except Exception as erro:
        return erro

def tratarData(texto):
    separado = texto.split('/')
    dia = separado[0]
    mes = separado[1]
    ano = separado[2]
    return '{}-{}-{}'.format(ano,mes,dia)


def consultar():
    try:
        sql = 'select * from pessoa'
        con.execute(sql)
        for(cpf, nome, telefone, endereco, dataDeNascimento) in con:
            print('CPF: {}, Nome: {}, Telefone: {}, Endereço: {}, Data De Nascimento: {}'.format(cpf, nome, telefone, endereco, dataDeNascimento))
        print('\n')
    except Exception as erro:
        print(erro)

def atualizar(cpf, campo, novoDado):
    try:
        sql = "update pessoa set {} = '{}' where cpf = '{}'".format(campo, novoDado, cpf)
        con.execute(sql)
        db_connection.commit()
        print('{} Atualizado com Sucesso Cria!'.format(con.rowcount))#rowcount = Contar quantas linhas foram afetadas

    except Exception as erro:
        print(erro)

def excluir(cpf):
    try:
        sql = "delete from pessoa where cpf = '{}'".format(cpf)
        con.execute(sql)
        db_connection.commit()
        print('{} Excluido!'.format(con.rowcount))
    except Exception as erro:
        print(erro)