import sqlite3

class updatedata:
    def __init__(self):
        self.conn = sqlite3.connect('sms.db')
        self.cur = self.conn.cursor()

    def updatestudent(self, sid, **kwargs):
        for column, value in kwargs.items():
            if value:
                self.cur.execute(f'''
                    UPDATE STUDENT
                    SET {column} = '{value}'
                    WHERE sid = '{sid}'
                ''')
        self.conn.commit()
        print("=====Student Data Updated Successfully=====")

    def updatecourse(self, cid, **kwargs):
        for column, value in kwargs.items():
            if value:
                self.cur.execute(f'''
                    UPDATE COURSE
                    SET {column} = '{value}'
                    WHERE cid = '{cid}'
                ''')
        self.conn.commit()
        print("=====Course Data Updated Successfully=====")

    def updatetransaction(self, tid, **kwargs):
        for column, value in kwargs.items():
            if value:
                self.cur.execute(f'''
                    UPDATE TRANS
                    SET {column} = '{value}'
                    WHERE tid = '{tid}'
                ''')
        self.conn.commit()
        print("=====Transaction Data Updated Successfully=====")