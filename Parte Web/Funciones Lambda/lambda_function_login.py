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
    email = event["queryStringParameters"]["email"]
    md5 = event["queryStringParameters"]["md5"]
    try:
        with conn.cursor() as cur:
            #Miro el mail primero
            cur.execute("SELECT email FROM usuarios WHERE email ='"+email+"'")
            cur.commit()
            #mail inexistente
            if cur.fetchone() == None:
                return {
                    'statusCode':200, 
                    'headers': { 'Access-Control-Allow-Origin' : '*' },
                    'body':json.dumps({'datosCorrectos' :  'False'})
                }
            else:
                #Si esxiste el mail pasamos a la contraseña
                cur.execute("SELECT email, md5 FROM usuarios WHERE md5 ='"+md5+"' and email='"+email"'")
                cur.commit()
                columnas = 0
                for row in cur:
                    columnas+=1
                if columnas > 0:
                    'statusCode':200, 
                    'headers': { 'Access-Control-Allow-Origin' : '*' },
                    'body':json.dumps({'mail' : email, 'datosCorrectos' :  'True'})
                else:
                    return {
                    'statusCode':200, 
                    'headers': { 'Access-Control-Allow-Origin' : '*' },
                    'body':json.dumps({'datosCorrectos' :  'False'})
    except pymysql.MySQLError as e:
        print(e)
        sys.exit()
    return
        'statusCode':200, 
        'headers': { 'Access-Control-Allow-Origin' : '*' }, 
        'body':json.dumps({'datosCorrectos' :  False})
