import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

# Carregar credenciais do banco de dados
DATABASE_URL = os.getenv("DATABASE_URL")

def criar_conexao():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="rootpassword",
        db="mydb",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn

def salvar_log(info):
    try:
        conn = criar_conexao()
        with conn.cursor() as cursor:
            sql = "INSERT INTO logs (informacao, datahora) VALUES (%s, NOW())"
            cursor.execute(sql, (info,))
        conn.commit()
    except Exception as e:
        print(f"Erro ao salvar log: {e}")
    finally:
        conn.close()
