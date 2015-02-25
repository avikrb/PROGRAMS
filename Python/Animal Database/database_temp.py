import sqlite3
conn = sqlite3.connect("zoo.sqlite")
cursor = conn.cursor()

#cursor.execute("Create table animal_count (name text, count integer)")

#cursor.execute("insert into animal_count(name, count)values('Elephant',3)")
##animal = input("Enter animal:")
##count = input ("Enter Count")
##cursor.execute("insert into animal_count(name, count)values(?,?)",(animal,count)) #using ? is called placeholder
#cursor.execute("insert into animal_count(name, count)values('"+animal+"',"+count+")")#problem if animal name contains quotes

#animals = [('snake',10),('turtle',4)]
#cursor.executemany("insert into animal_count(name,count) values(?,?)", animals)
result = cursor.execute("select * from animal_count")

for row in result:
    print (row)

conn.commit()


conn.close()

