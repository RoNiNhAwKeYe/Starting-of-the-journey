import mysql.connector as c
con=c.connect(host="localhost", user="root", passwd="", database="school")
if con.is_connected():
              print("Successfully Connected...")
else:
    print("Some Connectivity Issue...")
import os
exit='n'
while exit=='n':
    os.system('cls')
    print('-' * 90)
    print('|'+' '*31+'STUDENT MANAGEMENT SYSTEM'+' ' * 32+ '|')
    print('-' * 90)
    print('| [I]nsert Record |', end='')
    print('  [V]iew Record   |', end='')
    print('  [U]pdate Record |',end='')
    print('  [D]elete Record |',end='')
    print('    [E]XIT   |')
    print('-' * 90)
    ch=input('YOUR Choice (I/V/U/D/E):')
    ch = ch.upper()
    if ch == 'I':
       
        connection=c.connect(host="localhost", user="root", passwd="", db="school")
        mycursor=connection.cursor()
        choice='y'
        while choice=='y':
        
            sno=input('enter the roll number of student ')
            sname=input('enter the name of student ')
            Qry = ("INSERT INTO class12 "\
                   "VALUES (%s, %s)") 
            data = (sno,sname) 
            mycursor.execute(Qry,data) 
            print('RECORD INSERTED SUCCESSFULLY')
            choice=input('do you with to insert more records (y/n)')
            if choice=='y':
                continue
            connection.commit()
            connection.close()
    elif ch == 'V':
        
        connection=c.connect(host="localhost", user="root", passwd="", db="school")
        mycursor=connection.cursor()
        #mycursor.execute("""create table class12 (rno int, name varchar(45))""")
        choice='y'
        while choice=='y':
        
            rno=int(input('enter the roll number of student whose record you want to search '))
 
            Qry = ("""select * from class12 WHERE sno = %s""") 
            data = (sno,) 
            mycursor.execute(Qry,data) 
 
            count=0
            for(rno,name)in mycursor:
                count+=1
                print('===========')
                print('Student Roll No  ',rno)
                print('Student Name     ',name)
                print('===========')
                if count%2==0:
                    print('press any key to continue')
                    clrscreen()
                print('total records',count,'found')
        
            choice=input('do you with to search more record(y/n)')
            if choice=='y':
                continue
 
            connection.commit()
            connection.close()
    elif ch == 'U':
        
        connection=c.connect(host="localhost", user="root", passwd="", db="school")
        mycursor=connection.cursor()
        #mycursor.execute("""create table class12 (rno int, name varchar(20))""")
        choice='y'
        while(choice=='y'):
        
            rno=int(input('enter the roll number of student whose record you want to change '))
            name=input('enter new name')
 
            Qry = ("""UPDATE class12 set name=%s WHERE rno = %s""") 
            data = (name,rno) 
            mycursor.execute(Qry,data) 
            print('RECORD UPDATED SUCCESSFULLY')
        
            choice=input('do you wish to update more records(y/n)')
            if choice=='y':
                continue
            connection.commit()
            connection.close()
    elif ch == 'D':
        
        connection=c.connect(host="localhost", user="root", passwd="", db="school")
        mycursor=connection.cursor()
        #mycursor.execute("""create table class12 (rno int, name varchar(20))""")
        choice='y'
        while choice=='y':
        
            rno=int(input('enter the roll number of student whose record you want to delete '))
 
            Qry = ("""DELETE FROM class12 WHERE rno = %s""") 
            data = (rno,) 
            mycursor.execute(Qry,data) 
            print('RECORD DELETED SUCCESSFULLY')
            choice=input('Do you wish to delete more records(y/n) ?')
            if choice=='y':
                continue
            connection.commit()
            connection.close()
    elif ch == 'E':
        print("\n\t\t Thanks for using Student Management System...")
        print("\t\t-------------------------------------------")
        print("\t\t-------------------------------------------")
        break
    else:
        print('\t\t\t Error : Not a Valid Option ')
        print('\t\t Valid option are "I", "V", "U", "D", or "E" only')
        exit=input('\t\t Do you wish to exit the program(y/n)')
        if exit=='n':
            continue

