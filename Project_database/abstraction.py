import dataset

db = dataset.connect("sqlite:///employee_list.db")

def get_employee_list():
    items = [dict(item) for item in db['list'].find()]
    employee_list = [{"id":item['id'], "eid":item['eid'],"ename":item['name'],"elocation":item['location'],"eposition":item['position'],"esalary":item['salary'],"experience":item["experience"]} for item in items]
    return employee_list



def add_employee(item,item1,item2,item3,item4,item5):
    db['list'].insert({"eid":item,"name":item1,"location":item2,"position":item3,"salary":item4,"experience":item5})

def delete_employee(id):
    db['list'].delete(id=id)

def update_employee(id, location,position,salary,experience):
   db['list'].update({'id':id, "location":location,"position":position,"salary":salary,"experience":experience},['id'])


