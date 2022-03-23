from mongita import MongitaClientDisk
client = MongitaClientDisk()

try:
    employee_db = client.employee_db
    employee_list = employee_db.employee_list
    employee_list.delete_many({})
    items = [
        {"eid":12000,"firstname":"rocky","lastname":"bob","dob":"22/8/1995", "location":"ohio", "salary":"95k","position":"data analyst","experience":"1yrs"},
        {"eid":12001,"firstname":"jackie","lastname":"chan","dob":"12/6/1995", "location":"ohio", "salary":"75k","position":"business analyst","experience":"fresher"},
        {"eid":12002,"firstname":"jim", "lastname":"jo","dob":"18/7/1995","location":"ohio", "salary":"125k","position":"system engineer","experience":"2yrs"},
        {"eid":12003,"firstname":"randy","lastname":"pop","dob":"12/4/1995", "location":"ohio", "salary":"130k","position":"data scientist","experience":"3yrs"}

              ]
    employee_list.insert_many(items)
finally:
    pass

