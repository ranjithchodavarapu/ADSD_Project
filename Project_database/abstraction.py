import dataset

db = dataset.connect("sqlite:///employee_list.db")

def get_employee_list():
    items = [dict(item) for item in db['list'].find()]
    employee_list = [{"id":item['id'], "eid":item['eid'],"ename":item['name'],"elocation":item['location'],"eposition":item['position'],"esalary":item['salary']} for item in items]
    return employee_list



def add_employee(item,item1,item2,item3,item4):
    db['list'].insert({"eid":item,"name":item1,"location":item2,"position":item3,"salary":item4})

def delete_employee(id):
    db['list'].delete(id=id)

def update_employee(id, location,position,salary):
   db['list'].update({'id':id, "location":location,"position":position,"salary":salary},['id'])


