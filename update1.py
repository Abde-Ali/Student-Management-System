import sqlite3

class update1:
    def __init__(self):
        self.conn = sqlite3.connect('sms.db')
        self.cur = self.conn.cursor()

    def updatestudent(self,sid,sname=None,email=None,city=None):
        if sname:
            self.cur.execute(f"""
                UPDATE STUDENT
                             SET sname = '{sname}'
                             WHERE sid = '{sid}'
                """)
        if email:
            self.cur.execute(f'''
                UPDATE STUDENT
                             SET email = '{email}'
                             WHERE sid = '{sid}'
    ''')
        if city:
            self.cur.execute(f'''
                UPDATE STUDENT
                             SET city = '{city}'
                             WHERE sid = '{sid}'
''')
        self.conn.commit()
        print("=====Student Data Updated Successfully=====")

    def updatecourse(self,cid,update_data):
        for key, value in update_data:
            self.cur.execute(f""""
                                UPDATE COURSE
                                SET {key} = "{value}"
                                WHERE cid = "{cid}"
                             """)
        self.conn.commit()
        print("=====Course Data Updated Successfully=====")

    def updatetrans(self,tid,update_data):
        for key,value in update_data:
            self.cur.execute(f"""
            UPDATE TRANS
                             SET {key} = "{value}"
                             WHERE tid = "{tid}"
    
""")
        self.conn.commit()
        print("=====Transaction Data Updated Successfully=====")