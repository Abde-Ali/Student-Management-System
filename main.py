from insert import insertdata
obj = insertdata()

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
