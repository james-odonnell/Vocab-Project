#!/usr/bin/python

#import modules for CGI handling

import cgi, cgitb
import re
import MySQLdb

form = cgi.FieldStorage()

new_word = form.getvalue('t_word')
word_def = form.getvalue('t_def')
grade = form.getvalue('t_grade')
word_syn = form.getvalue('t_syn')
word_ant = form.getvalue('t_ant')
print"Content-type:text/html\r\n\r\n"

if new_word is None or word_def is None or word_ant is None or word_syn is None:
        print "<html>"
        print "<head>"
        print "<title>Error</title>"
        print "</head>"
        print "<body>"
        print "<h2>Please make sure all forms are filled in.</h2>"
        print "</body>"
        print "</html>"


else:

        db = MySQLdb.connect(host="xxx", user="xxx", passwd="", db="spelling")

        cur = db.cursor()

        sql = "INSERT INTO word_table (name, definition, grade_level, synonym, antonym) VALUES ('%s', '%s', '%s', '%s', '%s')" % (new_word, word_def, grade, word_syn, word_ant)
        cur.execute(sql)
        db.commit()
        db.close()
        print "<html>"
        print "<head>"
        print "<title>Successful Add</title>"
        print "</head>"
        print "<body>"
        print "<h2>%s has been added to the database.</h2>" % (new_word)
        print "</body>"
        print "</html>"
