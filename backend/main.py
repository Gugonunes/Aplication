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
try: 
    connection = mysql.connector.connect(
        host="us-cdbr-east-06.cleardb.net",
        database="heroku_948872016d5d23b",
        user="bc612f02f2a92a",
        password="80ced395",
    )
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Conectado com o MySQL, versão:", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Conectado com sucesso, base de dados: ", record)

except Error as erro:
    print("Erro na conexão com o MySQL:", erro)

    
@app.post("/{login}/{senha}")
def login(login, senha):
    cursor = connection.cursor(buffered=True)
    sql = "SELECT SENHA FROM USUARIOS WHERE EMAIL = '" + login + "' OR CPF = '" + login + "' OR PIS = '" + login + "'"
    cursor.execute(sql)
    row = cursor.fetchone()
    if (row[0] == senha):
        print("senha correta")
        return 0

    else:
        print("senha invalida")
        return -1

@app.get("/{id}")
def login(id):
    cursor = connection.cursor(buffered=True)
    sql = "SELECT * FROM USUARIOS WHERE EMAIL = '" + id + "'"
    cursor.execute(sql)
    row = cursor.fetchone()
    return row

@app.get("/update/{NomeCompleto}/{Senha}/{Email}/{Pais}/{Estado}/{Municipio}/{CEP}/{Rua}/{Numero}/{Complemento}/{CPF}/{PIS}/{logado}")
def update(NomeCompleto, Senha, Email, Pais, Estado, Municipio, CEP, Rua, Numero, Complemento, CPF, PIS, logado):
    print(logado)
    if logado == 'true':
        sqlAtual = "SELECT EMAIL FROM USUARIOS WHERE CPF = '" + CPF + "'"
        cursor.execute(sqlAtual)
        EmailAtual = cursor.fetchone()
        print(EmailAtual[0])

        if EmailAtual[0] != Email:
            sqlUnico = "SELECT EXISTS ( SELECT EMAIL FROM USUARIOS WHERE EMAIL = '"+Email+"')"
            cursor.execute(sqlUnico)
            row = cursor.fetchone()
        
            if row[0] == 0:
                print(row)
                sqlUpdate = "UPDATE USUARIOS SET NOME = '" + NomeCompleto + "', SENHA = '" + Senha + "', EMAIL = '" + Email + "', PAIS = '" + Pais + "', ESTADO = '" + Estado + "', MUNICIPIO = '" + Municipio + "', CEP = '" + CEP + "', RUA = '" + Rua + "', NUMERO = '" + Numero + "', COMPLEMENTO = '" + Complemento + "'"
                cursor.execute(sqlUpdate)
                return 0
            else:
                print("email ja existe")
                return -1
        else:
            print("safe")
            sqlUpdate = "UPDATE USUARIOS SET NOME = '" + NomeCompleto + "', SENHA = '" + Senha + "', EMAIL = '" + Email + "', PAIS = '" + Pais + "', ESTADO = '" + Estado + "', MUNICIPIO = '" + Municipio + "', CEP = '" + CEP + "', RUA = '" + Rua + "', NUMERO = '" + Numero + "', COMPLEMENTO = '" + Complemento + "' WHERE CPF = '" + CPF + "'"
            cursor.execute(sqlUpdate)
            return 0       
    else:
        print("nao ta logado")
        sqlUnico = "SELECT EXISTS ( SELECT EMAIL FROM USUARIOS WHERE EMAIL = '"+Email+"'), EXISTS ( SELECT CPF FROM USUARIOS WHERE CPF = '"+CPF+"'), EXISTS ( SELECT PIS FROM USUARIOS WHERE PIS = '"+PIS+"')"
        cursor.execute(sqlUnico)
        row = cursor.fetchone()
        print(row)
        if row[0] == 1:
            print("Email já existe")
            return -1
        
        elif row[1] == 1:
            print("cpf já existe")
            return -2

        elif row[2] == 1:
            print("pis já existe")
            return -3

        else:
            print("deu boa")
            sqlUpdate = "INSERT INTO USUARIOS VALUES('" + NomeCompleto + "', '" + Senha + "', '" + Email + "', '" + Pais + "', '" + Estado + "', '" + Municipio + "', '" + CEP + "', '" + Rua + "', '" + Numero + "', '" + Complemento + "', '" + CPF + "', '" + PIS + "')"
            cursor.execute(sqlUpdate)
            return 0



