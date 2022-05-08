from tinydb.storages import MemoryStorage
from tinydb import TinyDB, Query,where
from tinydb.operations import delete,increment,decrement,set
db = TinyDB(storage=MemoryStorage)

fetch = Query()

# insert data in to db
items = [
        {"eid":12000,"firstname":"rocky","lastname":"bob","dob":"22/8/1995", "location":"ohio", "salary":"95k","position":"data analyst","experience":"1yrs"},
        {"eid":12001,"firstname":"jackie","lastname":"chan","dob":"12/6/1995", "location":"ohio", "salary":"75k","position":"business analyst","experience":"fresher"},
        {"eid":12002,"firstname":"jim", "lastname":"jo","dob":"18/7/1995","location":"ohio", "salary":"125k","position":"system engineer","experience":"2yrs"},
        {"eid":12003,"firstname":"randy","lastname":"pop","dob":"12/4/1995", "location":"ohio", "salary":"130k","position":"data scientist","experience":"3yrs"},
        {"eid":12010,"lastname":"car","dob":"22/1/1996", "location":"india", "salary":"125k","position":"data admin","experience":"2yrs"},
        {"eid":12011,"lastname":"RAM","dob":"22/11/1996", "location":"india", "salary":"125k","experience":"2yrs"},
        {'name': 'John', 'age': 22}

              ]
db.insert_multiple(items)

db.insert({"eid":12012,"firstname":"roman","lastname":"reigns","dob":"22/9/1990", "location":"CA", "salary":"195k","position":"data engineer","experience":"7yrs"})
db.insert({"eid":12013,"firstname":"vicky","lastname":"shiva","dob":"12/12/1990", "location":"CA", "salary":"165k","position":"database admin","experience":"7yrs"})

# get the document id 
a = db.get(fetch.eid == 12012)
print(a.doc_id)

el = db.all()[-1]
print(el.doc_id)

# updata data
db.update({'firstname':'seth'},where('eid')==12003)
db.update(delete('experience'), fetch.lastname == 'RAM')
db.update(increment('eid'),fetch.lastname == 'shiva') # value goes to 12014 from 12013
db.update(decrement('eid'),fetch.lastname == 'car') # value goes to 12009 from 12010
db.update(set('position','database admin'),fetch.lastname == 'car')
print(db.search(fetch.eid == 12011 ))
print(db.search(fetch.eid == 12003 ))
print(db.search(fetch.eid == 12009 ))


print(db.get(fetch.age == 22 ))

# remove data
db.remove(fetch.age == 22)
print(db.get(fetch.age == 22 )) # returns none 

#upsert data
db.upsert({'firstname': 'sri'}, fetch.lastname == 'RAM')
print(db.search(fetch.eid == 12011 ))

#db.truncate()




#print(db.all())
