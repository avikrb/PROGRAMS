import sqlite3
conn = sqlite3.connect("interview.sqlite")
conn_result=sqlite3.connect("results.sqlite")
cursor_result = conn_result.cursor()
cursor = conn.cursor()

cursor.execute("Create table interview_questions (questions text, answers text, right_answer text)")
cursor_result.execute("Create table interview_results (username text, correct int, total int, pass_fail text)")



question = [("Where is New Haven?", 'Detroit,Idaho,New York,Connecticut', "Connecticut"),("Where is Richmond?", 'California,Ohio,Virginia,Connecticut', "Virginia")]


cursor.executemany("insert into interview_questions(questions,answers,right_answer) values(?,?,?)",question)


conn.commit()
conn_result.commit()

conn.close()
conn_result.close()

