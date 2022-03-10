import dataset

db = dataset.connect("sqlite:///employee_list.db")

def get_employee_list():
    items = [dict(item) for item in db['list'].find()]
    employee_list = [{"id":item['id'], "eid":item['eid'],"firstname":item['firstname'],"lastname":item['lastname'],"dob":item["dob"],"elocation":item['location'],"eposition":item['position'],"esalary":item['salary'],"experience":item["experience"]} for item in items]
    return employee_list



def add_employee(item,item0,item1,item2,item3,item4,item5,item6):
    db['list'].insert({"eid":item,"firstname":item0,"lastname":item1,"dob":item2,"location":item3,"position":item4,"salary":item5,"experience":item6})

def delete_employee(id):
    db['list'].delete(id=id)

def update_employee(id,dob,location,position,salary,experience):
   db['list'].update({'id':id,"dob":dob,"location":location,"position":position,"salary":salary,"experience":experience},['id'])


