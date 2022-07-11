from typing import Optional
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


class User(BaseModel):
    username: str
    password: str
    
@app.post("/{payload}")
def login(payload):
    cursor = connection.cursor(buffered=True)
    sql = "SELECT * FROM USUARIOS WHERE EMAIL = '" + payload + "'"
    cursor.execute(sql)
    row = cursor.fetchall()
    print(row[0])
    return {row[0]}


@app.get("/")
def login():
    return {"teste login"}


