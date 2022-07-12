from array import array
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
        host="localhost",
        database="AplicacaoDB",
        user="root",
        password="",
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

@app.get("/update/{NomeCompleto}/{Senha}/{Email}/{Pais}/{Estado}/{Municipio}/{CEP}/{Rua}/{Numero}/{Complemento}/{CPF}/{PIS}")
def update(NomeCompleto, Senha, Email, Pais, Estado, Municipio, CEP, Rua, Numero, Complemento, CPF, PIS):
    print (NomeCompleto, Senha, Email, Pais, Estado, Municipio, CEP, Rua, Numero, Complemento, CPF, PIS)

    return 0



