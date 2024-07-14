
import sqlite3

class insertdata:
    def __init__(self):
        self.conn = sqlite3.connect('sms.db')
        self.cur = self.conn.cursor()

    def insertstudent(self,sid,sname,email,city):
        self.cur.execute(f'''
                INSERT INTO STUDENT VALUES(
                         '{sid}',
                         '{sname}',
                         '{email}',
                         '{city}'
                )''')
        self.conn.commit()
        print("=====Data Added Sucessfully=====")


    def insertcourse(self,cid,cname,sid,price):
        self.cur.execute(f'''
                INSERT INTO COURSE VALUES(
                         '{cid}',
                         '{cname}',
                         '{sid}'
                         
                         )''')
        self.conn.commit()
        print("=====Data Added Sucessfully=====")
#after sid in insertcourse need to add price col

    def insertransaction(self,tid,sid,cid,method):
        self.cur.execute(f'''
                INSERT INTO TRANS VALUES(
                         '{tid}',
                         '{sid}',
                         '{cid}',
                         '{method}'
                        )''')
        self.conn.commit()
        print("=====Data Added Sucessfully=====")





