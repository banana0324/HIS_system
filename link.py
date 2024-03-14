# import cx_Oracle
# # cx_Oracle.init_oracle_client(lib_dir="./instantclient_19_8") # init Oracle instant client 位置
# cx_Oracle.init_oracle_client()
# connection = cx_Oracle.connect('GROUP5', 'EPAepUAIaB', cx_Oracle.makedsn('140.117.69.60', 1521, service_name='ORCLPDB1'))
# cursor = connection.cursor()
import pymssql
import pysftp
from pymssql import _mssql
from pymssql import _pymssql

connection = pymssql.connect(
    server='127.0.0.1:1433',
    user='sa',
    password='admin123@',
    database='HisDemo',
    charset="UTF-8"
) 
cursor = connection.cursor()
# cursor = connection.cursor(as_dict = True)

# cursor.execute("select * from dbo.AccountDemo")

# re = cursor.fetchall()
# for row in re:
#     print(f"{row['UserId']}\t{row['Password']}\t{row['IdFlag']}\t{row['Name']}")