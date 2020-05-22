Q1 = '''SELECT a.id, a.fname, a.lname, a.gender 
        FROM Actor a INNER JOIN Cast c on a.id == c.pid     
        INNER JOIN Movie m on m.id == c.mid WHERE m.name LIKE 'Annie%';
        '''
Q2 = '''SELECT m.id, m.name, m.rank, m.year 
        FROM Movie m INNER JOIN MovieDirector md on m.id == md.mid
        INNER JOIN Director d on d.id == md.did WHERE (d.fname ='Biff' AND d.lname = 'Malibu')
        AND m.year IN (1999, 1994, 2003) ORDER BY m.rank DESC, m.year ASC;
        '''
Q3 = '''SELECT year, COUNT(id) AS no_of_movies FROM Movie GROUP BY year 
        HAVING AVG(rank) > (SELECT AVG(rank) FROM Movie) ORDER BY year ASC;
        '''
Q4 = '''SELECT id, name, year, rank FROM Movie WHERE 
        year = 2001 AND rank < (SELECT AVG(rank) FROM Movie) 
        ORDER BY rank DESC LIMIT 10;
        '''
Q665 = '''SELECT m.id AS movie_id, (SELECT COUNT(a.gender) FROM Actor a INNER JOIN Cast c on a.id == c.pid WHERE m.id == c.mid AND a.gender= 'F') AS no_of_female_actors ,
        (SELECT COUNT(a.gender) FROM Actor a INNER JOIN Cast c on a.id == c.pid WHERE m.id == c.mid AND a.gender= 'M') AS no_of_male_actors FROM Movie m GROUP BY m.id
        ORDER BY m.id ASC LIMIT 100;
        '''
Q6 = '''SELECT DISTINCT c.pid FROM Cast c 
        INNER JOIN Movie m on m.id == c.mid GROUP BY c.pid,m.id
        HAVING COUNT(DISTINCT role) > 1 
        ORDER BY c.pid ASC;
        '''
Q7 = '''SELECT fname, COUNT(id) FROM Director GROUP BY fname HAVING COUNT(id) > 1;'''
           
Q8 = '''SELECT d.id,d.fname,d.lname FROM Director d
        WHERE EXISTS(
        SELECT * FROM MovieDirector md INNER JOIN Cast c on md.mid == c.mid 
                WHERE md.did == d.id GROUP BY did,md.mid)
        AND NOT EXISTS(
        SELECT * FROM MovieDirector md INNER JOIN Cast c on md.mid == c.mid 
                WHERE md.did == d.id GROUP BY did,md.mid HAVING COUNT(DISTINCT pid) < 100); 
        '''        