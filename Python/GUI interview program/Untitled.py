from wsgiref.simple_server import make_server
import psutil,datetime
import sqlite3


def server_health(environ, start_response):
    conn_result=sqlite3.connect("results.sqlite")
    cursor_result = conn_result.cursor()
    print_results = cursor_result.execute("select * from interview_results")
    status = '200 OK'
    headers = [('Content-type', 'html; charset=utf-8')]
    start_response(status, headers)
    message = "<h1>Interview Scores</h1>"
    for data in print_results:
        message += (str(data[0])+" scored "+ data[1]
    
    return[bytes(message,'utf-8')]

httpd = make_server('', 8000,server_health)
print("Serving on port 8000...")


httpd.serve_forever()
