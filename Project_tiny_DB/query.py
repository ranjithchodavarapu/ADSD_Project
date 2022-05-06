from tinydb import TinyDB, Query,where
from tinydb.operations import delete,increment,decrement,set
data = TinyDB('employee_db.json')


#return all the data from the database in json format 
print(data.all())

# iterating over the data
for i in data:
    print(i)


employee = Query()


# retrive data from the database that matches query 
# can be done for every column name in the database 

print(data.search(employee.eid == 12010 )) 
print(data.search(employee.firstname == 'rocky' )) 
print(data.search(employee.dob == '18/7/1995'))

# another syntax to retrive particular data 
print(data.search(employee['firstname']=='jim'))

# another way to retrive particular data using where clause
print(data.search(where('salary')=='130k'))


# check whether field exists like column's
print(data.search(employee.firstname.exists()))
print(data.search(employee.position.exists()))

# match the full regular expression 
print(data.search(employee.lastname.matches('[az]*')))

#  only a part of item to match re
print(data.search(employee.firstname.search('a+')))

# fetch atleast one document that matches the query using one_of in the list of data
print(data.search(employee.firstname.one_of(['jim', 'jack'])))

# implemention of logical operators 
print(data.search(~ (employee.lastname == 'jackie')))
print(data.search((employee.firstname == 'jin') & (employee.salary < '135k')))
print(data.search((employee.salary == '135k') | (employee.eid == 12010)))

# get the no of docs in the database
print(len(data))

# retrive one random data from database even if the query matches mulitple documents 
print(data.get(employee.location == 'india'))

# check the data is stored in db or not 
print(data.contains(employee.salary == '130k'))

# check number of documents that match the query 
print(data.count(employee.location == 'ohio'))

# table implementation 
table = data.table('employee_ssn')
#table.insert({'ssn': "00123458"})
print(table.all())
#data.drop_table('employee_ssn')
print(data.tables())


# insert data
data.insert({"eid":12012,"firstname":"roman","lastname":"reigns","dob":"22/9/1990", "location":"CA", "salary":"195k","position":"data engineer","experience":"7yrs"})
data.insert({"eid":12013,"firstname":"vicky","lastname":"rao","dob":"2/12/1991", "location":"CA", "salary":"165k","position":"database admin","experience":"7yrs"})

# updata data
data.update({'firstname':'raju'},where('eid')==12003)
data.update(delete('salary'), employee.lastname == 'RAM')
data.update(increment('eid'),employee.lastname == 'rao') 
data.update(decrement('eid'),employee.lastname == 'car') 
data.update(set('position','database admin'),employee.lastname == 'car')
print(data.search(employee.eid == 12011 ))
print(data.search(employee.eid == 12003 ))
print(data.search(employee.eid == 12015 ))

#upsert
data.upsert({'firstname': 'sri'}, employee.lastname == 'RAM')
print(data.search(employee.eid == 12011 ))
