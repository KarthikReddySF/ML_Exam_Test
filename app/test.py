import psycopg2
from psycopg2.extras import RealDictCursor
try:
     conn=psycopg2.connect(dbname='varun',user='postgres',password='admin123',host='localhost',port='5432',cursor_factory=RealDictCursor)
     print("Database connected successfully")
     cursor=conn.cursor()
except Exception as error:
     print("connection not done")
     print("Error",error)

cursor.execute("""SELECT * FROM public.user""")
rows=cursor.fetchall()
print(rows)

