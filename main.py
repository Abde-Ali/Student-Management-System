from insert import insertdata
from update import updatedata
from delete import deletedata

obj = insertdata()
obj1 = updatedata()
obj2 = deletedata()

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
        # price = float(input('Enter price: '))
        obj.insertcourse(cid,cname,sid) #if u are uncommenting the price so include the price in this line too as a var 

elif num == 2:
    print("Choose 1 for Student: \nChoose 2 for Course\nChoose 3 for Transaction")
    table_choice = int(input('Please enter option: '))

    if table_choice == 1:
        sid = int(input('Please enter the ID of the student to update: '))
        columns = ['sname', 'email', 'city']
        update_data = {}
        for column in columns:
            value = input(f'Enter new {column} (leave blank if no change): ')
            if value:
                update_data[column] = value
        obj1.updatestudent(sid, **update_data)
        
    elif table_choice == 2:
        cid = int(input('Please enter the ID of the course to update: '))
        columns = ['cname', 'sid', 'price']
        update_data = {}
        for column in columns:
            value = input(f'Enter new {column} (leave blank if no change): ')
            if value:
                update_data[column] = value
        obj1.updatecourse(cid, **update_data)
        
    elif table_choice == 3:
        tid = int(input('Please enter the ID of the transaction to update: '))
        columns = ['sid', 'cid', 'method']
        update_data = {}
        for column in columns:
            value = input(f'Enter new {column} (leave blank if no change): ')
            if value:
                update_data[column] = value
        obj1.updatetransaction(tid, **update_data)


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
