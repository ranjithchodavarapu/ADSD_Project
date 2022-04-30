from tinydb import TinyDB, Query,where
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

# fetch atleast one document that matches the query using one_of in list of data
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


