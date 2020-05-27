class InvalidField(Exception):
    pass
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.student_id = None
        self.age = age
        self.score = score
    
    @classmethod
    def filter(cls, **kwargs):
        li=[]
        for key,value in kwargs.items():
            a = key
            b = value
            
            n = a.split('__')   
        
            if n[0] not in ('student_id', 'name', 'age', 'score'):
                raise InvalidField
                
            if len(n) == 1:
                sql_query = (f'{n[0]} == "{b}"')
            
            elif n[1] == 'lt':
                sql_query = f"{n[0]} < {b}"
                
            elif n[1] == 'lte':
                sql_query = f"{n[0]} <= {b}"
                
            elif n[1] == 'gt':
                sql_query = f"{n[0]} > {b}"
                
            elif n[1] == 'gte':
                sql_query = f"{n[0]} >= {b}"
                
            elif n[1] == 'neq':
                sql_query = f"{n[0]} != {b}"
                
            elif n[1] == 'in':
                b=tuple(b)
                sql_query = f"{n[0]} in {b}"
                
            elif n[1] == 'contains':
                sql_query = f"{n[0]} LIKE '%{b}%'"
        
            li.append(sql_query)
            
        li_query=' and '.join(li)
        return li_query
            
    
    @classmethod    
    def avg(cls,field, **kwargs):
        if field not in ('student_id','name','age','score'):
            raise InvalidField
        elif len(kwargs) == 0:
            query = read_data(f'SELECT AVG({field}) FROM Student')
        else:    
            x=Student.filter(**kwargs)
            query = read_data(f'SELECT AVG({field}) FROM Student WHERE {x}')
        return query[0][0]
            
    @classmethod
    def count(cls, field=None, **kwargs):
        if field == None:
            query = read_data('SELECT COUNT(*) FROM Student')

        elif field not in ('student_id','name','age','score'):
            raise InvalidField
        elif len(kwargs) == 0:
            query = read_data(f'SELECT COUNT({field}) FROM Student')
        else:    
            x=Student.filter(**kwargs)
            query = read_data(f'SELECT COUNT({field}) FROM Student WHERE {x}')
        return query[0][0]    
            
    @classmethod
    def max(cls, field, **kwargs):
        if field not in ('student_id','name','age','score'):
            raise InvalidField
        elif len(kwargs) == 0:
            query = read_data(f'SELECT MAX({field}) FROM Student')
        else:    
            x=Student.filter(**kwargs)
            query = read_data(f'SELECT MAX({field}) FROM Student WHERE {x}')
        return query[0][0]    
            
    @classmethod
    def min(cls, field, **kwargs):
        
        if field not in ('student_id','name','age','score'):
            raise InvalidField 
        elif len(kwargs) == 0:
            query = read_data(f'SELECT MIN({field}) FROM Student')
        else:    
            x=Student.filter(**kwargs)
            query = read_data(f'SELECT MIN({field}) FROM Student WHERE {x}')
        return query[0][0]    
            
    @classmethod
    def sum(cls, field, **kwargs):
        if field not in ('student_id','name','age','score'):
            raise InvalidField      
        elif len(kwargs) == 0:
            query = read_data(f'SELECT SUM({field}) FROM Student')
        else:    
            x=Student.filter(**kwargs)
            query = read_data(f'SELECT SUM({field}) FROM Student WHERE {x}')
        return query[0][0]    
        

def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans    
'''
count = Student.count()
print(count)
'''