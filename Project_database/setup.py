import dataset

db = dataset.connect("sqlite:///employee_list.db")

try:
    db.begin()
    db['list'].drop()
    table = db['list']
    items = [
        {"eid":12000,"name":"rocky", "location":"ohio", "salary":"95k","position":"data analyst","experience":"1yrs"},
        {"eid":12001,"name":"jackie", "location":"ohio", "salary":"75k","position":"business analyst","experience":"fresher"},
        {"eid":12002,"name":"jim", "location":"ohio", "salary":"125k","position":"system engineer","experience":"2yrs"},
        {"eid":12003,"name":"randy", "location":"ohio", "salary":"130k","position":"data scientist","experience":"3yrs"}

              ]
    table.insert_many(items)
    db.commit()
except Exception as e:
    db.rollback()

print("done.")
#insurance,policy package