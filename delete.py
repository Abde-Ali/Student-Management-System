import sqlite3

class deletedata:
    def __init__(self):
        self.conn = sqlite3.connect('sms.db')
        self.cur = self.conn.cursor()

    def deletestudent(self, sid):
        self.cur.execute(f'''
            DELETE FROM STUDENT
            WHERE sid = ?
        ''', (sid,))
        self.conn.commit()
        print("=====Student Data Deleted Successfully=====")

    def deletecourse(self, cid):
        self.cur.execute(f'''
            DELETE FROM COURSE
            WHERE cid = ?
        ''', (cid,))
        self.conn.commit()
        print("=====Course Data Deleted Successfully=====")

    def deletetransaction(self, tid):
        self.cur.execute(f'''
            DELETE FROM TRANS
            WHERE tid = ?
        ''', (tid,))
        self.conn.commit()
        print("=====Transaction Data Deleted Successfully=====")
