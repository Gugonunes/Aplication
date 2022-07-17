from array import array
import email
from typing import Optional
from typing import List
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import mysql.connector
from mysql.connector import Error

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:4200",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Conexão com banco
#Foi utilizado um banco local, com wampserver e o mysql workbench
try: 
    connection = mysql.connector.connect(
        host="",
        database="aplicacaodb",
        user="root",
        password="",
    )
    #verificando a conexão
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Conectado com o MySQL, versão:", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Conectado com sucesso, base de dados: ", record)

except Error as erro:
    print("Erro na conexão com o MySQL:", erro)

#Teste de conexão com a api
@app.get("/")
def read_root():
    return {"Olá": ", página de backend"}

#função de login
@app.post("/{login}/{senha}")
def login(login, senha):
    cursor = connection.cursor(buffered=True)
    #como o login pode ser feito com email, cpf ou pis, fiz essa consulta para procurar a senha em qualquer um dos casos, visto que esses valores sao unicos
    sql = "SELECT SENHA FROM USUARIOS WHERE EMAIL = '" + login + "' OR CPF = '" + login + "' OR PIS = '" + login + "'"
    cursor.execute(sql)
    row = cursor.fetchone()
    #caso nao ache nenhuma das informaçoes, retorna -2
    if (row == None):
        return -2
    #caso ache, e a senha esteja correta, retorna 0
    elif (row[0] == senha):
        print("senha correta")
        return 0
    #caso ache, mas a senha esteja diferente, retorna -1
    else:
        print("senha invalida")
        return -1

#função para pegar os dados do usuario na pagina de editar dados
@app.get("/{id}")
def dados(id):
    cursor = connection.cursor(buffered=True)
    sql = "SELECT * FROM USUARIOS WHERE EMAIL = '" + id + "' OR CPF = '" + id + "' OR PIS = '" + id + "'"
    cursor.execute(sql)
    row = cursor.fetchone()
    return row

#função para atualizar dados do usuario ou para criar um novo usuario
@app.get("/update/{NomeCompleto}/{Senha}/{Email}/{Pais}/{Estado}/{Municipio}/{CEP}/{Rua}/{Numero}/{Complemento}/{CPF}/{PIS}/{logado}")
def update(NomeCompleto, Senha, Email, Pais, Estado, Municipio, CEP, Rua, Numero, Complemento, CPF, PIS, logado):
    if logado == 'true':
        #se o usuario esta logado, verificamos se ele esta tentando mudar o email para um novo, comparando o novo digitado com o atual email
        sqlAtual = "SELECT EMAIL FROM USUARIOS WHERE CPF = '" + CPF + "'"
        cursor.execute(sqlAtual)
        EmailAtual = cursor.fetchone()
        print(EmailAtual[0])
        #se o email atual do banco for diferente do novo:
        if EmailAtual[0] != Email:
            sqlUnico = "SELECT EXISTS ( SELECT EMAIL FROM USUARIOS WHERE EMAIL = '"+Email+"')"
            cursor.execute(sqlUnico)
            row = cursor.fetchone()
            #se nao existe esse email no banco, significa que pode ser utilizado
            if row[0] == 0:
                print(row)
                sqlUpdate = "UPDATE USUARIOS SET NOME = '" + NomeCompleto + "', SENHA = '" + Senha + "', EMAIL = '" + Email + "', PAIS = '" + Pais + "', ESTADO = '" + Estado + "', MUNICIPIO = '" + Municipio + "', CEP = '" + CEP + "', RUA = '" + Rua + "', NUMERO = '" + Numero + "', COMPLEMENTO = '" + Complemento + "' WHERE CPF = '" + CPF + "'"
                cursor.execute(sqlUpdate)
                return 0
            #caso contrario, informamos que ja existe
            else:
                print("email ja existe")
                return -1
        #se ele nao tentou mudar o email, apenas atualizar os dados
        else:
            sqlUpdate = "UPDATE USUARIOS SET NOME = '" + NomeCompleto + "', SENHA = '" + Senha + "', EMAIL = '" + Email + "', PAIS = '" + Pais + "', ESTADO = '" + Estado + "', MUNICIPIO = '" + Municipio + "', CEP = '" + CEP + "', RUA = '" + Rua + "', NUMERO = '" + Numero + "', COMPLEMENTO = '" + Complemento + "' WHERE CPF = '" + CPF + "'"
            cursor.execute(sqlUpdate)
            return 0      
    #se o usuario nao esta logado, significa que esta sendo criado um novo usuario 
    else:
        print("nao ta logado")
        #verificamos se o email, cpf e pis digitados estao disponiveis
        sqlUnico = "SELECT EXISTS ( SELECT EMAIL FROM USUARIOS WHERE EMAIL = '"+Email+"'), EXISTS ( SELECT CPF FROM USUARIOS WHERE CPF = '"+CPF+"'), EXISTS ( SELECT PIS FROM USUARIOS WHERE PIS = '"+PIS+"')"
        cursor.execute(sqlUnico)
        row = cursor.fetchone()
        print(row)
        #row é retornado como um vetor do tipo [x,y,z], se for '1' aquele valor ja existe, portanto basta verificar cada caso:
        if row[0] == 1:
            print("Email já existe")
            return -1
        
        elif row[1] == 1:
            print("cpf já existe")
            return -2

        elif row[2] == 1:
            print("pis já existe")
            return -3
        #se todos os valores forem 0, significa que está tudo certo para criar o novo usuario
        else:
            sqlUpdate = "INSERT INTO USUARIOS VALUES('" + NomeCompleto + "', '" + Senha + "', '" + Email + "', '" + Pais + "', '" + Estado + "', '" + Municipio + "', '" + CEP + "', '" + Rua + "', '" + Numero + "', '" + Complemento + "', '" + CPF + "', '" + PIS + "')"
            cursor.execute(sqlUpdate)
            return 1

#função para deletar usuario
@app.get("/delete/{data}/{logado}")
def delete(data, logado):
    #para deletar, ele deve estar logado
    if logado == 'true':
        #como cpf é unico, utilizei ele para fazer o delete
        sql = "DELETE FROM USUARIOS WHERE CPF = '" + data +"'"
        cursor.execute(sql)
        return 0

#função para informar o nome do usuario na home
@app.get("/nome/{id}")
def getNome(id):
    #como o login pode ser feito por email, cpf ou pis, tive que verificar qualquer um dos casos e selecionar o nome do usuario
    sql="SELECT NOME FROM USUARIOS WHERE EMAIL = '"+id+"' OR CPF = '"+id+"' OR PIS = '"+id+"'"
    cursor.execute(sql)
    row = cursor.fetchone()
    print(row)
    return row


