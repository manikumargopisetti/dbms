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
    def __repr__(self):
        return "Student(student_id={0}, name={1}, age={2}, score={3})".format(
            self.student_id,
            self.name,
            self.age,
            self.score)    
      
    @staticmethod
    def is_in(s_id):
        x = read_data(f'SELECT student_id FROM Student WHERE student_id = {s_id}')
        if len(x) != 0:
            return True
        else:
            return False
            
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
        
        if x in ('age'):
            query = read_data(f'SELECT * FROM Student WHERE {x} = \'{y}\'')
        
        elif len(query) > 1:
            raise MultipleObjectsReturned
    
        b =Student(query[0][1],query[0][2],query[0][3])
        b.student_id=query[0][0]
        return b
        
    def save(self):
        import sqlite3
        connection = sqlite3.connect('selected_students.sqlite3')
        crsr = connection.cursor()

        if self.student_id == None:
            query = 'INSERT INTO Student (name,age,score) values("{}",{},{})'.format(self.name, self.age,self.score)       
            crsr.execute(query)
            self.student_id = crsr.lastrowid
            
        else:
            if self.is_in(self.student_id):
                query ='UPDATE Student SET name="{}", age = {}, score = {} WHERE student_id = {}'.format(self.name,self.age,self.score,self.student_id)
                crsr.execute(query)
            else:
                query = 'INSERT INTO Student(student_id, name, age, score) values({},"{}", {}, {})'.format(self.student_id, self.name, self.age, self.score)
                crsr.execute(query)
        
        connection.commit() 
        connection.close()
        
    def delete(self):
        query = (f'DELETE FROM Student WHERE student_id = {self.student_id}')
        write_data(query)    
        
    @classmethod
    def filter(cls, **kwargs):
        for key,value in kwargs.items():
            a = key
            b = value
            
            n = a.split('__')    
        
            if n[0] not in ('student_id', 'name', 'age', 'score'):
                raise InvalidField
            
            if a in ('student_id','name','age','score'): 
               sql_query = read_data(f"SELECT * FROM Student WHERE {a} = '{b}'")
            
            elif n[1] == 'lt':
                sql_query = read_data(f"SELECT * FROM Student WHERE {n[0]} < '{b}'")
                
            elif n[1] == 'lte':
                sql_query = read_data(f"SELECT * FROM Student WHERE {n[0]} <= '{b}'")
                
            elif n[1] == 'gt':
                sql_query = read_data(f"SELECT * FROM Student WHERE {n[0]} > '{b}'")
                
            elif n[1] == 'gte':
                sql_query = read_data(f"SELECT * FROM Student WHERE {n[0]} >= '{b}'")
                
            elif n[1] == 'neq':
                sql_query = read_data(f"SELECT * FROM Student WHERE {n[0]} != '{b}'")
                
            elif n[1] == 'in':
                b=tuple(b)
                sql_query = read_data(f"SELECT * FROM Student WHERE {n[0]} in {b}")
                
            elif n[1] == 'contains':
                sql_query = read_data(f"SELECT * FROM Student WHERE {n[0]} LIKE '%{b}%'")
            
            
            if len(sql_query) == 0:
                return []
            else:
                li = []
                for i in sql_query:    
                    qc =Student(i[1],i[2],i[3])    
                    qc.student_id=i[0]
                    li.append(qc)
        return li
        
def write_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("selected_students.sqlite3")
    crsr = connection.cursor() 
    crsr.execute("PRAGMA foreign_keys=on;") 
    crsr.execute(sql_query) 
    connection.commit() 
    connection.close()
	
def read_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("selected_students.sqlite3")
    crsr = connection.cursor() 
    crsr.execute(sql_query) 
    ans= crsr.fetchall()  
    connection.close() 
    return ans