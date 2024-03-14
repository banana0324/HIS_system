from typing import Optional
from link import *

class DB():
    def connect():
        cursor = connection.cursor()
        return cursor

    def prepare(sql):
        cursor = DB.connect()
        cursor.prepare(sql)
        return cursor

    def execute(cursor, sql,values):
        cursor.execute(sql,values)
        return cursor

    def execute_input(cursor, input):
        cursor.execute(None, input)
        return cursor

    def fetchall(cursor):
        return cursor.fetchall()

    def fetchone(cursor):
        return cursor.fetchone()

    def commit():
        connection.commit()

class Member():
    def get_member(account):
        sql = 'SELECT USERID, PASSWORD, IDFLAG, NAME FROM DBO.ACCOUNTDEMO WHERE USERID = (%s)'
        values = account
        return DB.fetchall(DB.execute(DB.connect(),sql,values))
    
    def get_all_account():
        sql = "SELECT USERID FROM DBO.ACCOUNT"
        values = ''
        return DB.fetchall(DB.execute(DB.connect(), sql, values))

    def create_member(input):
        sql = 'INSERT INTO DBO.ACCOUNTDEMO (UserId, Password, IdFlag, Name) VALUES (%s, %s, %s, %s)'
        print(sql)
        values = (input["userid"],input["password"],input["identity"],input["name"])
        DB.execute(DB.connect(),sql,values)
        DB.commit()
    
    def delete_product(tno, pid):
        sql = 'DELETE FROM RECORD WHERE TNO=:tno and PID=:pid '
        DB.execute_input(DB.prepare(sql), {'tno': tno, 'pid':pid})
        DB.commit()
        
    def get_order(userid):
        sql = 'SELECT * FROM ORDER_LIST WHERE MID = :id ORDER BY ORDERTIME DESC'
        return DB.fetchall(DB.execute_input( DB.prepare(sql), {'id':userid}))
    
    def get_role(userid):
        sql = 'SELECT IDFLAG, NAME FROM DBO.ACCOUNTDEMO WHERE USERID = (%s) '
        values = userid
        return DB.fetchone(DB.execute(DB.connect(),sql,values))


class Product():
    def count():
        sql = 'SELECT COUNT(*) FROM DBO.PATIENT'
        values = ''
        return DB.fetchone(DB.execute( DB.connect(), sql, values))
    
    def get_patient(pno):
        sql ='SELECT * FROM DBO.PATIENT WHERE PatientNo = (%s)'
        values = pno
        return DB.fetchone(DB.execute(DB.connect(), sql, values))
    
    def get_doctor(dno):
        sql ='SELECT * FROM DOCTOR WHERE DOCTORNO = (%s)'
        values = dno
        return DB.fetchone(DB.execute(DB.connect(), sql, values))
    
    def get_bed(bno):
        sql ='SELECT * FROM DBO.BED WHERE BEDNO = (%s)'
        values = bno
        return DB.fetchone(DB.execute(DB.connect(), sql, values))
    
    def get_bedno(pno):
        sql ='SELECT BEDNO FROM DBO.BED WHERE PATIENTNO = (%s)'
        values = pno
        return DB.fetchone(DB.execute(DB.connect(), sql, values))
    
    def get_vital_sign(pno):
        sql ='SELECT * FROM DBO.VITALSIGN WHERE PATIENTNO = (%s)'
        values = pno
        return DB.fetchone(DB.execute(DB.connect(), sql, values))

    def get_all_patient():
        sql = 'SELECT * FROM DBO.PATIENT'
        values = ''
        return DB.fetchall(DB.execute( DB.connect(), sql, values))
    
    def get_all_vital_sign():
        sql = 'SELECT * FROM DBO.VITALSIGN'
        values = ''
        return DB.fetchall(DB.execute( DB.connect(), sql, values))
    
    def get_all_doctor():
        sql = 'SELECT * FROM DOCTOR'
        values = ''
        return DB.fetchall(DB.execute( DB.connect(), sql, values))
    
    def get_all_bed():
        sql = 'SELECT * FROM DBO.BED'
        values = ''
        return DB.fetchall(DB.execute( DB.connect(), sql, values))
    
    def get_name(pid):
        sql = 'SELECT NAME FROM PATIENT WHERE PNO = :id'
        return DB.fetchone(DB.execute_input( DB.prepare(sql), {'id':pid}))[0]

    def add_patient(input):
        sql = 'INSERT INTO DBO.PATIENT(PatientNo,PatientName,PGender,PBirthDate,PDescription,PDOCTORNO,PDISCHARGE) VALUES (%s, %s, %s, %s, %s, %s)'
        values = (input["pno"],input["name"],input["gender"],input["birthdate"],input["description"],input["doctor"],input["discharge"])
        DB.execute(DB.connect(), sql, values)
        DB.commit()

    def add_vital_sign(input):
        sql = 'INSERT INTO VITALSIGN (PATIENTNO, SEQTIME, RR, BP, SPO2, BT, SCORE, RISK, PULSE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        values=(input["pno"], input["seqtime"], input["rr"], input["bp"], input["spo2"], input["bt"], input["score"], input["risk"], input["pulse"])
        DB.execute(DB.connect(), sql, values)
        DB.commit()

    def add_doctor(input):
        sql = 'INSERT INTO DOCTOR (DOCTORNO, DOCTORNAME, DOCTORDEPT) VALUES (%s, %s, %s)'
        values=(input["dno"], input["dname"], input["dept"])
        DB.execute(DB.connect(), sql, values)
        DB.commit()

    def add_bed(input):
        sql = 'INSERT INTO BED (BEDNO, PATIENTNO, STARTTIME, ENDTIME) VALUES (%s, %s, %s, %s)'
        values=(input["bno"], input["pno"], input["starttime"], input["starttime"])
        DB.execute(DB.connect(), sql, values)
        DB.commit()

    def delete_vital_sign(pno):
        sql = 'DELETE FROM DBO.VITALSIGN WHERE SEQTIME = (%s) '
        values = pno
        DB.execute(DB.connect(), sql, values)
        DB.commit()
    
    def delete_product(pno):
        sql = 'DELETE FROM DBO.PATIENT WHERE PATIENTNO = (%s) '
        values = pno
        DB.execute(DB.connect(), sql, values)
        DB.commit()

    def delete_doctor(dno):
        sql = 'DELETE FROM DOCTOR WHERE DOCTORNO = (%s) '
        values = dno
        DB.execute(DB.connect(), sql, values)
        DB.commit()

    def delete_bed(bno):
        sql = 'DELETE FROM BED WHERE BEDNO = (%s) '
        values = bno
        DB.execute(DB.connect(), sql, values)
        DB.commit()

    def update_patient(input):
        sql = 'UPDATE DBO.PATIENT SET PATIENTNAME=(%s), PGENDER=(%s), PBIRTHDATE=(%s), PDESCRIPTION=(%s), PDOCTORNO=(%s), PDISCHARGE=(%s) WHERE PATIENTNO=(%s)'
        values = (input["name"],input["gender"],input["birthdate"],input["description"],input["doctor"],input["discharge"],input["pno"])
        DB.execute(DB.connect(),sql,values)
        DB.commit()

    def update_vital_sign(input):
        sql = 'UPDATE DBO.VITALSIGN SET RR=(%s), BP=(%s), SPO2=(%s), BT=(%s), SCORE=(%s), RISK=(%s), PULSE=(%s) WHERE SEQTIME=(%s)'
        values = (input["rr"],input["bp"],input["spo2"],input["bt"],input["score"],input["risk"],input["pulse"],input["seqtime"])
        DB.execute(DB.connect(),sql,values)
        DB.commit()

    def update_doctor(input):
        sql = 'UPDATE DOCTOR SET DOCTORNAME=(%s), DOCTORDEPT=(%s) WHERE DOCTORNO=(%s)'
        values = (input["dname"],input["dept"],input["dno"])
        DB.execute(DB.connect(),sql,values)
        DB.commit()

    def update_bed(input):
        sql = 'UPDATE DBO.BED SET PATIENTNO=(%s), STARTTIME=(%s), ENDTIME=(%s) WHERE BEDNO=(%s)'
        values = (input["pno"],input["starttime"],input["endtime"],input["bno"])
        DB.execute(DB.connect(),sql,values)
        DB.commit()

class Surgery():
    def count():
        sql = 'SELECT COUNT(*) FROM DBO.Surgery'
        values = ''
        return DB.fetchone(DB.execute( DB.connect(), sql, values))
    
    def get_undergoes(pid):
        sql ='SELECT * FROM UNDERGOES WHERE PNO = :id'
        return DB.fetchone(DB.execute_input(DB.prepare(sql), {'id': pid}))

    def get_all_undergoes():
        sql = 'SELECT * FROM DBO.Surgery'
        values = ''
        return DB.fetchall(DB.execute( DB.connect(), sql, values))
    
    def get_name(pid):
        sql = 'SELECT SURGEON FROM UNDERGOES WHERE PNO = :id'
        return DB.fetchone(DB.execute_input( DB.prepare(sql), {'id':pid}))[0]
    


class Analysis():
    def month_price(i):
        sql = 'SELECT EXTRACT(MONTH FROM ORDERTIME), SUM(PRICE) FROM ORDER_LIST WHERE EXTRACT(MONTH FROM ORDERTIME)=:mon GROUP BY EXTRACT(MONTH FROM ORDERTIME)'
        return DB.fetchall( DB.execute_input( DB.prepare(sql) , {"mon": i}))

    def month_count(i):
        sql = 'SELECT EXTRACT(MONTH FROM ORDERTIME), COUNT(OID) FROM ORDER_LIST WHERE EXTRACT(MONTH FROM ORDERTIME)=:mon GROUP BY EXTRACT(MONTH FROM ORDERTIME)'
        return DB.fetchall( DB.execute_input( DB.prepare(sql), {"mon": i}))
    
    def category_discharge():
        sql = 'SELECT COUNT(*), PDISCHARGE FROM DBO.PATIENT GROUP BY PDISCHARGE'
        values = ''
        return DB.fetchall(DB.execute( DB.connect(), sql, values))
    
    def category_sex():
        sql = 'SELECT COUNT(*), PGENDER FROM PATIENT GROUP BY PGENDER'
        values = ''
        return DB.fetchall(DB.execute( DB.connect(), sql, values))

    def member_sale():
        sql = 'SELECT SUM(PRICE), MEMBER.MID, MEMBER.NAME FROM ORDER_LIST, MEMBER WHERE ORDER_LIST.MID = MEMBER.MID AND MEMBER.IDENTITY = :identity GROUP BY MEMBER.MID, MEMBER.NAME ORDER BY SUM(PRICE) DESC'
        return DB.fetchall( DB.execute_input( DB.prepare(sql), {'identity':'user'}))

    def member_sale_count():
        sql = 'SELECT COUNT(*), MEMBER.MID, MEMBER.NAME FROM ORDER_LIST, MEMBER WHERE ORDER_LIST.MID = MEMBER.MID AND MEMBER.IDENTITY = :identity GROUP BY MEMBER.MID, MEMBER.NAME ORDER BY COUNT(*) DESC'
        return DB.fetchall( DB.execute_input( DB.prepare(sql), {'identity':'user'}))