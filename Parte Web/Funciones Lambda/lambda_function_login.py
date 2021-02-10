import sys
import logging
import pymysql
import json

rds_host = "IP VM"

username = "admin"
password ="password"
dbname = "Distribuidos"
dbport = 30623
try:
    conn = pymysql.connect(rds_host, user=username, passwd=password, db=dbname, port=dbport, connect_timeout=10)
except pymysql.MySQLError as e:
    print (e)
    sys.exit()

def lambda_handler(event, context):
    email = event["queryStringParameters"]["email"]
    md5 = event["queryStringParameters"]["md5"]
    try:
        with conn.cursor() as cur:
            #Miro el mail primero
            query ="""SELECT email FROM usuarios WHERE email =%s"""
            cur.execute(query, email)
            conn.commit()
            print(cur.rowcount)
            #mail inexistente
            if (cur.rowcount < 1):
                return {
                    'statusCode':200, 
                    'headers': { 'Access-Control-Allow-Origin' : '*' },
                    'body':json.dumps({'datosCorrectos' :  'False'})
                }
            else:
                #Si esxiste el mail pasamos a la contraseña
                query = """SELECT * FROM usuarios WHERE email=%s and md5=%s"""
                cur.execute(query, (email, md5))
                conn.commit()
                print(cur.fetchall())
                print(cur.rowcount)
                if cur.rowcount == 1:
                    redirection =""
                    query = """SELECT pagename FROM webpages WHERE type='calculadora'"""
                    cur.execute(query)
                    conn.commit()
                    for row in cur:
                        redirection = row[0]
                    return{
                        'statusCode':200, 
                        'headers': { 'Access-Control-Allow-Origin' : '*' },
                        'body':json.dumps({'mail' : email, 'datosCorrectos' :  'True', 'redirect' : redirection})
                    }
                else:
                    return {
                        'statusCode':200, 
                        'headers': { 'Access-Control-Allow-Origin' : '*' },
                        'body':json.dumps({'datosCorrectos' :  'False'})
                    }
    except pymysql.MySQLError as e:
        print(e)
        sys.exit()
        return{
            'statusCode':200, 
            'headers': { 'Access-Control-Allow-Origin' : '*' }, 
            'body':json.dumps({'datosCorrectos' :  False})
        }
