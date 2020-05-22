class DoesNotExist(Exception):
    pass
class MultipleObjectsReturned(Exception):
    pass
class InvalidField(Exception):
    pass
class Student:
    
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        self.student_id = None
        
        
    @classmethod
    def get(cls, **kwargs):
        
        for k,v in kwargs.items():
            x = k
            y = v
        if x not in ('student_id','name','age','score'):
            raise InvalidField
        query = read_data(f'SELECT * FROM Student WHERE {x} =\'{y}\'')
            
        if len(query) == 0:
            raise DoesNotExist
        elif len(query) > 1:
            raise MultipleObjectsReturned
        else:
            b =Student(query[0][1],query[0][2],query[0][3])
            b.student_id=query[0][0]
            return b
    
    def save(self):
        import sqlite3
        connection = sqlite3.connect('students.sqlite3')
        crsr = connection.cursor()
        if self.student_id == None:
            query = 'INSERT INTO Student (name,age,score) values("{}",{},{})'.format(self.name, self.age,self.score)
            crsr.execute(query)
            self.student_id = crsr.lastrowid
        else:
            query ='UPDATE Student SET name="{}", age = {}, score = {} WHERE student_id = {}'.format(self.name,self.age,self.score,self.student_id)
            crsr.execute(query)
        
        connection.commit() 
        connection.close()
        
    def delete(self):
        query = (f'DELETE FROM Student WHERE student_id = {self.student_id}')
        write_data(query)
        
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
student_object = Student.get(student_id=1)
print(student_object.name)


import sqlite3
        connection = sqlite3.connect("students.sqlite3")
        crsr = connection.cursor()

        if student_id != None:
            query=read_data(f'SELECT * FROM Student WHERE student_id ={student_id}')
        elif name != None:
            query=read_data(f'SELECT * FROM Student WHERE name=\'{name}\'')
        elif age != None:
            query=read_data(f'SELECT * FROM Student WHERE age={age}')
        elif score != None:
            query=read_data(f'SELECT * FROM Student WHERE score={score}')

cls, student_id=None, name=None, age=None, score=None
'''