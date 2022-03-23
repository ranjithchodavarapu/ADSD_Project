from mongita import MongitaClientDisk
client = MongitaClientDisk()
from bson.objectid import ObjectId



def get_employee_list():
    try: 
        employee_db = client.employee_db
        employee_list = employee_db.employee_list
        the_list = list(employee_list.find({}))
        for item in the_list:
                item['id'] = str(item['_id'])         
        return the_list
    finally:
        pass



def add_employee(item,item0,item1,item2,item3,item4,item5,item6):
    try:
        employee_db = client.employee_db
        employee_list = employee_db.employee_list
        employee_list.insert_one({"eid":item,"firstname":item0,"lastname":item1,"dob":item2,"location":item3,"position":item4,"salary":item5,"experience":item6})
    finally:
        pass

def get_item(id):
    employee_db = client.employee_db
    employee_list = employee_db.employee_list
    try:
        item = employee_list.find_one({"_id":ObjectId(id)})
    except Exception as e:
        print(e)
        item = None
    if item == None:
        return None
    item['id'] = str(item['_id'])
    return item


def delete_employee(id):
    try:
        employee_db = client.employee_db
        employee_list = employee_db.employee_list
        _id = ObjectId(id)
        employee_list.delete_one({"_id":_id})
    finally:
        pass


def update_employee(id,dob,location,position,salary,experience):
    try:
        employee_db = client.employee_db
        employee_list = employee_db.employee_list
        _id = ObjectId(id)
        employee_list.update_one({'_id':_id},{'$set':{"dob":dob,"location":location,"position":position,"salary":salary,"experience":experience}})
    finally:
        pass