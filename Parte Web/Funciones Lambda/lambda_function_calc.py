import sys
import logging
import pymysql
import json
import math

rds_host = "3.83.133.16"

username = "admin"
password ="password"
dbname = "Distribuidos"
dbport = 30623
try:
    conn = pymysql.connect(rds_host, user=username, passwd=password, db=dbname, port=dbport, connect_timeout=10)
except pymysql.MySQLError as e:
    print (e)
    sys.exit()

def suma(a, b):
    return a + b
   
def resta(a, b):
    return a - b
   
def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "No se puede dividir entre 0"
    else: 
        return a / b

def mod(a, b):
    if b == 0:
        return "No se puede dividir entre 0"
    else: 
        return a % b

def root(a):
    if a < 0:
        return "No se puede hacer la raíz de un número negativo"
    else:
        return math.sqrt(a)

def default():
    return "Opcion Invalida"
   
def switch(case, a, b):
    sw = {
        "+": suma(a, b),
        "-": resta(a, b),
        "*": mult(a, b),
        "/": div(a, b),
        "%": mod(a, b),
        "r": root(a),        
    }
    return sw.get(case, default())

    
def lambda_handler(event , context):
    op1=float(event["queryStringParameters"]["op1"])
    op2=float(event["queryStringParameters"]["op2"])
    op=(event["queryStringParameters"]["op"])
    res=switch(op,op1,op2)
    redirectPage=""
    try:
        with conn.cursor() as cur:
            cur.execute("insert into resultados values ( "+str(op1)+","+ str(op2)+",'"+op+"',"+ str(res)+")")
            conn.commit()
            cur.execute("select pagename from webpages where type='success'")
            conn.commit()
            for row in cur:
                redirectPage=row[0]
            #        print(" "+str(col), end='')
            #    print()

    except pymysql.MySQLError as e:    
        print (e)
        sys.exit()
    
    
    return{
	    'statusCode': 200,
        'headers': { 'Access-Control-Allow-Origin' : '*' },
        'body':json.dumps({ 'res' :  str(res) , 'redirect' : redirectPage })
    }

