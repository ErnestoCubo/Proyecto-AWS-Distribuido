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
    
def lambda_handler(event , context):
    email = event["queryStringParameters"]["email"]
    md5 = event["queryStringParameters"]["md5"]
    try:
        with conn.cursor() as cur:
            query = """SELECT email FROM usuarios WHERE email=%s"""
            cur.execute(query, email)
            #mail inexistente
            if cur.fetchone() == None :
                query = """INSERT into usuarios values (%s, %s)"""
                cur.execute(query,(email, md5))
                conn.commit()
                cur.execute("select pagename from webpages where type='login'")
                conn.commit()
                for row in cur:
                    redirectPage=row[0]
                return {
                    'statusCode':200, 
                    'headers': { 'Access-Control-Allow-Origin' : '*' },
                    'body':json.dumps({'usuarioRegistrado' :  'True', 'redirectPage' : redirectPage})
                }
            else:
                return {
                    'statusCode':200, 
                    'headers': { 'Access-Control-Allow-Origin' : '*' },
                    'body':json.dumps({'usuarioRegistrado' :  'False'})
                }


    except pymysql.MySQLError as e:    
        print (e)
        sys.exit()
        return{
    	    'statusCode': 200,
            'headers': { 'Access-Control-Allow-Origin' : '*' },
            'body':json.dumps({ 'res' :  str(res) , 'redirect' : redirectPage })
        }

