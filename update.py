import sqlite3

class updatedata:
    def __init__(self):
        self.conn = sqlite3.connect('sms.db')
        self.cur = self.conn.cursor()

    def studentupate(self,sid,sname,email,city):#=None should be return if needed
        self.cur.execute(f'''
                UPDATE STUDENT
                         SET '{col}' =         
                        ''')