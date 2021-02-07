import sys
import logging
import pymysql import json

rds_host = ""

username = "admin"
password ="password"
dbname = "Distribuidos"

try:
    conn = pymysql.connect(rds_host, user=username, passwd=password, db=dbname, connect_timeout=10)
except pymysql.MySQLError as e:
    print (e)
    sys.exit()

def lambda_handler(event, context):
    email = string(event["queryStringParameters"]["email"])
    contraseña = string(event["queryStringParameters"]["contraseña"])
    redirectPage = ""
    try:
        with conn.cursor() as cur:
            query = "SELECT email, constraseña FROM usuarios WHERE email = %s and contraseña = %s" 
            data = (email, contraseña)
            cur.execute(query, data)
            cur.commit()
            for row in cur:
                datos = row[0]
    except pymysql.MySQLError as e:
        print(e)
        sys.exit()
    return
        'statusCode':200, 'headers': { 'Access-Control-Allow-Origin' : '*' }, 'body':json.dumps({'datos' :  str(datos)})
