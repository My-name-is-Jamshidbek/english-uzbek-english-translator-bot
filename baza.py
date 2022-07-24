import sqlite3
from datetime import datetime

def baseadd(user_id,full_name,chat_id,tel_number):
    try:
        connection = sqlite3.connect("botbaza.db")
        crsr = connection.cursor()
        sql_command = f"""INSERT INTO emp VALUES ({str(user_id)}, "{str(full_name)}", "{str(chat_id)}","{str(tel_number)}", "{str(datetime.now())}");"""
        crsr.execute(sql_command)
        connection.commit()
        connection.close()
        return True
    except:return False

def basereturnids():
    try:
        connection = sqlite3.connect("botbaza.db")
        crsr = connection.cursor()
        crsr.execute("SELECT * FROM emp")
        ans = crsr.fetchall()
        rl = set()
        for i in ans:
            rl.add(str(i[2]))
        return rl
    except:return False
def basereturntelnumber():
    try:
        connection = sqlite3.connect("botbaza.db")
        crsr = connection.cursor()
        crsr.execute("SELECT * FROM emp")
        ans = crsr.fetchall()
        rl = set()
        for i in ans:
            rl.add(str(i[3]))
        return rl
    except:return False
def basereturnall():
    try:
        connection = sqlite3.connect("botbaza.db")
        crsr = connection.cursor()
        crsr.execute("SELECT * FROM emp")
        ans = crsr.fetchall()
        return ans
    except:return False
def basereturnlen():
    try:
        connection = sqlite3.connect("botbaza.db")
        crsr = connection.cursor()
        crsr.execute("SELECT * FROM emp")
        ans = crsr.fetchall()
        return len(ans)
    except:return False
#print(basereturnlen())
# baseadd(1,"test","test","test")
# print(basereturnids())