from tinydb import TinyDB, Query,where
data = TinyDB('employee_db.json')

table = data.table('employee_ssn')
#table.insert({'ssn': "00123458"})
print(table.all())
#data.drop_table('employee_ssn')
print(data.tables())

