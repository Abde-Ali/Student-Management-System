from insert import insertdata
from update import updatedata
from delete import deletedata
from update1 import update1

obj = insertdata()
obj1 = updatedata()
obj2 = deletedata()
obj3 = update1()

print("-----Student Management System-----")
print("For Insertion Press 1, Updation Press 2, \n Deletion Press 3, Reeading Press 4")

num = int(input("Entr Option"))

if num ==1:
    print("Choose 1 for student: \nchoose 2 for Course\nChoose 3 for Tranction")
    n=int(input('Pls ent option'))
    if n==1:
        sid = int(input('pls entr ur ID: '))
        sname = input('pls entr ur name')
        email = input('pls entr ur eamil')
        city = input('entr ur city')
        obj.insertstudent(sid,sname,email,city)
    
    elif n==3:
        tid = int(input('Enter ur Tranction ID: '))
        sid = input('Enter ur Student ID: ')
        cid = input("Enter ur course ID: ")
        method = input('Enter payment MEthod: ')
        obj.insertransaction(tid,sid,cid,method)

    elif n==2:
        cid = int(input('Enter ur Course ID: '))
        cname = input("Enter ur course name: ")
        sid = int(input("Enter ur student ID: "))
        price = float(input('Enter price: '))
        obj.insertcourse(cid,cname,sid,price) #if u are uncommenting the price so include the price in this line too as a var 

elif num == 3:
    print("Choose 1 for Student: \nChoose 2 for Course\nChoose 3 for Transaction")
    table_choice = int(input('Please enter option: '))

    if table_choice == 1:
        sid = int(input('Please enter the ID of the student to delete: '))
        obj2.deletestudent(sid)
        
    elif table_choice == 2:
        cid = int(input('Please enter the ID of the course to delete: '))
        obj2.deletecourse(cid)
        
    elif table_choice == 3:
        tid = int(input('Please enter the ID of the transaction to delete: '))
        obj2.deletetransaction(tid)

elif num==2:
    print("Choose 1 for Student: \nChoose 2 for Course\nChoose 3 for Transaction")
    n = int(input("Ples Enter ur Option: "))
    update_data ={}
    if n ==1:
        sid = int(input('Enter your Student ID: '))
        col_selection = int(input("Selection of column you wantto Updaate:\n Enter 1 to update NAME\n Enter 2 to Update EMAIL \n Enter 3 to Update CITY \n"))
        
        if col_selection==1:
            new_name = input("Enter NEw Name: ")
            obj3.updatestudent(sid,sname=new_name)
        elif col_selection==2:
            new_mail = input("Enter new Email: ")
            obj3.updatestudent(sid=sid,email=new_mail)
        elif col_selection==3:
            new_city=input("Enter New City: ")
            obj3.updatestudent(sid,city=new_city)

    if n==2:
        cid = int(input("Enter ur Course ID: "))
        col_selection = int(input("Selection of column you want to update:\n Enter 1 to update COURSE NAME\n Enter 2 to Update STUDENT ID \n"))

        if col_selection==1:
            new_cname = input("Update ur course name: ")
            update_data['cname']=new_cname
        elif col_selection==2:
            new_sid = int(input("Update ur correct Student ID now: "))
        elif col_selection==3:
            new_price = input('Enter the new price: ')
            update_data['price'] = new_price

        if update_data:
            obj3.updatecourse(cid,update_data)
        else:
            print('No Updates')


'''elif num == 2:
    print("Choose 1 for Student: \nChoose 2 for Course\nChoose 3 for Transaction")
    n1 = int(input('Please enter option: '))

    if n1 == 1:
        sid = int(input('Please enter the ID of the student to update: '))
        columns = (input("Enter 1 if you want to update Name\n Enter 2 if you want to update EMAIL\n Enter 3 if you want to update city: "))
        value = input('Enter new Change): ')
        update_data = {}

        for column in columns:
            if column == '1':
                
                sname = value
            elif column == '2':
                email= value
        obj1.updatestudent(sid, 'sname',email)
        
    elif n1 == 2:
        cid = int(input('Please enter the ID of the course to update: '))
        columns = ['cname', 'sid', 'price']
        update_data = {}
        for column in columns:
            value = input(f'Enter new {column} (leave blank if no change): ')
            if value:
                update_data[column] = value
        obj1.updatecourse(cid, **update_data)
        
    elif n1 == 3:
        tid = int(input('Please enter the ID of the transaction to update: '))
        columns = ['sid', 'cid', 'method']
        update_data = {}
        for column in columns:
            value = input(f'Enter new {column} (leave blank if no change): ')
            if value:
                update_data[column] = value
        obj1.updatetransaction(tid, **update_data)'''
