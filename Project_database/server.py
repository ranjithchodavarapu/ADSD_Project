import dataset
import abstraction
from bottle import route, run, template, get, post, request, response, redirect

db = dataset.connect("sqlite:///employee_list.db")

@route("/")
@route("/home")
def get_data():
    employee_list = abstraction.get_employee_list()
    return template('employee_data.tpl', employee_list=employee_list)

@get("/add")
def get_add():
    return template('add.tpl')

@post("/add")
def post_add():
    eid = request.forms.get("eid")
    firstname = request.forms.get("firstname")
    lastname = request.forms.get("lastname")
    dob = request.forms.get("dob")
    location = request.forms.get("location")
    position = request.forms.get("position")
    salary = request.forms.get("salary")
    experience = request.forms.get("experience")
    abstraction.add_employee(eid,firstname,lastname,dob,location,position,salary,experience)
    redirect("/home")

@route("/edit/<id>")
def get_edit(id):
    items = [dict(item) for item in db['list'].find(id=id)]
    if len(items) != 1:
        redirect('/home')
    item = items[0]
    return template('edit.tpl', id=item['id'],dob = item["dob"],location=item['location'],position=item['position'],salary=item['salary'],experience=item["experience"])

@post("/edit/<id>")
def post_edit(id):
    dob = request.forms.get("dob")
    location = request.forms.get("location")
    position = request.forms.get("position")
    salary = request.forms.get("salary")
    experience = request.forms.get("experience")
    abstraction.update_employee(id,dob, location, position, salary,experience)
    redirect("/home")


@route("/delete/<id>")
def get_delete(id):
    abstraction.delete_employee(id)
    redirect("/home")

run(host='localhost', port=8080)








