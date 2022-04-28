from tinydb import TinyDB, Query
db = TinyDB('employee_db.json')


try:
    items = [
        {"eid":12000,"firstname":"rocky","lastname":"bob","dob":"22/8/1995", "location":"ohio", "salary":"95k","position":"data analyst","experience":"1yrs"},
        {"eid":12001,"firstname":"jackie","lastname":"chan","dob":"12/6/1995", "location":"ohio", "salary":"75k","position":"business analyst","experience":"fresher"},
        {"eid":12002,"firstname":"jim", "lastname":"jo","dob":"18/7/1995","location":"ohio", "salary":"125k","position":"system engineer","experience":"2yrs"},
        {"eid":12003,"firstname":"randy","lastname":"pop","dob":"12/4/1995", "location":"ohio", "salary":"130k","position":"data scientist","experience":"3yrs"},
        {"eid":12010,"lastname":"car","dob":"22/1/1996", "location":"india", "salary":"125k","position":"data admin","experience":"2yrs"},
        {"eid":12011,"lastname":"RAM","dob":"22/11/1996", "location":"india", "salary":"125k","experience":"2yrs"}

              ]
    db.insert_multiple(items)
finally:
    pass

