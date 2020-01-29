#!/usr/bin/python

import MySQLdb
import cgi, cgitb

form = cgi.FieldStorage()

grade = form.getvalue('grade')


db = MySQLdb.connect(host="xxx", user="xxx", passwd="", db="spelling")

cur = db.cursor()

sql = "SELECT * from word_table where grade_level = ('%s') order by name" % (grade)
cur.execute(sql)
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Results</title>")
print("</head>")
print("<body>")
print("<h2> List of words for Grade %s </h2>" % (grade))
for row in cur.fetchall():
        print ("<strong>Word:</strong> " +  row[0])
        print ("<br>")
        print ("<strong>Definition:</strong> " + row[1])
        print ("<br>")
        print ("<strong>Synonym:</strong> " + row[3])
        print ("<br>")
        print ("<strong>Antonym:</strong> " + row[4])
        print ("<br>")
        print ("<br>")
        print ("<br>")
        print ("<br>")
print ("</body>")
print ("</html>")

db.close()
