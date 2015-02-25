import sqlite3
conn = sqlite3.connect("interview.sqlite")
conn_result=sqlite3.connect("results.sqlite")


cursor_result = conn_result.cursor()
cursor = conn.cursor()

user_name = input ("Enter your Username: ")
print ("Welcome "+str(user_name)+"!")

result = cursor.execute("select * from interview_questions")

count = 0
total = 0
for row in result:
    total +=1
    print (row[0])
    row_1 = row[1].split(",")
    i = 1 
    for options in row_1:
        print (str(i)+". "+str(options)+"\t")
        i = i +1
    choice = input ("Your answer: ")
    choice = int(choice)-1
    if row_1[int(choice)] == row[2]:
        count = count + 1
       
if ((count/total)*100) >= 60:
    grade = "Pass"
else:
    grade = "Fail"
    
interview_results = [(user_name,count, total, grade)]


cursor_result.executemany("insert into interview_results(username,correct,total,pass_fail) values(?,?,?,?)",interview_results)
conn_result.commit()
conn_result.close()
conn.close()
