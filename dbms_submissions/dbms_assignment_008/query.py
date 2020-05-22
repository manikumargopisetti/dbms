Q1 = '''SELECT d.id, d.fname 
      FROM Director d 
      WHERE NOT EXISTS (
          SELECT md.did 
          FROM MovieDirector md 
          INNER JOIN Movie m on md.mid == m.id 
          WHERE md.did == d.id AND m.year < 2000
          ) AND EXISTS (
          SELECT md.did 
          FROM MovieDirector md 
          INNER JOIN Movie m on md.mid == m.id 
          WHERE md.did == d.id AND m.year > 2000
          ) ORDER BY d.id ASC;'''

Q2 = '''SELECT d.fname, (
            SELECT m.name FROM MovieDirector md 
            INNER JOIN Movie m on md.mid == m.id 
            WHERE d.id == md.did 
            ORDER BY m.rank DESC) 
            AS name 
            FROM Director d LIMIT 100;   
        '''
Q3 = '''SELECT * FROM Actor a 
            WHERE NOT EXISTS (
            SELECT c.pid FROM Cast c 
            INNER JOIN Movie m on m.id == c.mid 
            WHERE a.id == c.pid AND m.year BETWEEN 1990 AND 2000 
            )
            ORDER BY a.id DESC LIMIT 100; 
        
        '''
          