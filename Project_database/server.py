import dataset
from bottle import route, run, template, get, post, request, response, redirect

db = dataset.connect("sqlite:///employee_list.db")

@route("/home")
def get_data():
    items = [dict(item) for item in db['list'].find()]
    employee_list = [{"id":item['id'], "eid":item['eid'],"ename":item['name'],"elocation":item['location'],"eposition":item['position'],"esalary":item['salary']} for item in items]
    return template('employee_data.tpl', employee_list=employee_list)



@get("/add")
def get_add():
    return template('add.tpl')

@post("/add")
def post_add():
    eid = request.forms.get("eid")
    name = request.forms.get("name")
    location = request.forms.get("location")
    position = request.forms.get("position")
    salary = request.forms.get("salary")
    db['list'].insert({"eid":eid,"name":name,"location":location,"position":position,"salary":salary})
    redirect("/home")

@route("/delete/<id>")
def get_delete(id):
    db['list'].delete(id=id)
    redirect("/home")

run(host='localhost', port=8080)