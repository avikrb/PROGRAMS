from wsgiref.simple_server import make_server
import psutil,datetime
import sqlite3


def interview_scores(environ, start_response):
    conn_result=sqlite3.connect("results.sqlite")
    cursor_result = conn_result.cursor()
    print_results = cursor_result.execute("select * from interview_results")
    status = '200 OK'
    headers = [('Content-type', 'html; charset=utf-8')]
    start_response(status, headers)
    message = "<h1>Interview Scores</h1>"
    message +="<table style=\"width:100%\">"
    message += "<tr>"
    message +="<td style=\"background-color:Aqua\"><strong>Username</strong></td>"
    message +="<td style=\"background-color:Aqua\"><strong>Correct Answers</td>"
    message +="<td style=\"background-color:Aqua\"><strong>Total Questions</td>"
    message +="<td style=\"background-color:Aqua\"><strong>Result</td></tr>"
    
    for data in print_results:
        message += "<tr>"
        message += "<td><strong>"+(str(data[0]))+"</td>"
        message += "<td>"+(str(data[1]))+"</td>"
        message += "<td>"+(str(data[2]))+"</td>"
        message += "<td><strong>"+(str(data[3]))+"</td>"
        message += "<tr>"
    return[bytes(message,'utf-8')]

httpd = make_server('', 8000,interview_scores)
print("Serving on port 8000...")


httpd.serve_forever()
