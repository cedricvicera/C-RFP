import cgi

form = cgi.FieldStorage()

#user input
sex = form.getValue("sex")
age = form.getValue("age")
race = form.getValue("race")
