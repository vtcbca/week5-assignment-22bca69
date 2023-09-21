import csv

#create and write the records in csv file
with open("c://sqlite3//student_csv.csv","w",newline="")as stud:
    write=csv.writer(stud)
    #create header of a csv file
    header=['S_Id','S_Name','City','Contact']
    write.writerow(header)
    #5 record's insert directly in csv file
    rows=[
          [1,'dhaval','bardoli',9879966543],
          [2,'arjun','Kadod',8866993321],
          [3,'jay','surat',9955678234],
          [4,'himal','Gangadhara',9056462245],
          [5,'dev','Palsana',7069816636]
         ]
    write.writerows(rows)
    print('Record Inserted successful')
    
    #5 records insert using user input
    #create empty list
    l=[]
    #iterate the loop for entering multiple records
    for record in range(5):
        n=int(input('Enter Student ID:'))
        name=input('Enter Student Name: ')
        city=input('Enter City Name: ')
        contact=int(input('Enter Contact Number:'))
        #append records in a variable 'store'
        store=[n,name,city,contact]
        #append the records in list
        l.append(store)
        #write the rows in a csv file
    write.writerows(l)
    print('Record Inserted successful')

#read csv file using DictrReader()
with open("c://sqlite3//student_csv.csv","r")as stud:
    r=csv.DictReader(stud)
    for i in r:
        print(i)
print()

