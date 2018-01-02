
import MySQLdb



def executeSQL(conn, sql, params):
        cursor = conn.cursor()
        cursor.execute(sql, params)
        ret = cursor.fetchall()
        cursor.close()
        return ret

def connect():
        db = None
        count = 0
        while not db:
                if count >= 2:
                        pass
                try:
                        db = MySQLdb.connect(host="127.0.0.1", db="chromebooks", user="root", passwd="", connect_timeout=1)
                except:
                        count += 1

        return db



conn = connect()
conn.close()


gotValidChromebook = executeSQL(conn, """SELECT * FROM Assignments WHERE AssigneeName=%s LIMIT 1""", (input,))
