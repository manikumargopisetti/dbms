Q1 = '''SELECT p.player_id, p.team_id, p.jersey_no, p.name, p.date_of_birth, p.age
        FROM Player p INNER JOIN MatchCaptain mc on mc.captain == p.player_id 
        AND mc.team_id == p.team_id WHERE player_id NOT IN
        (SELECT player_id FROM GoalDetails);
        '''
Q2 = '''SELECT t.team_id, COUNT(mtd.team_id) As no_of_games FROM
        Team t INNER JOIN MatchTeamDetails mtd on t.team_id == mtd.team_id
        GROUP BY mtd.team_id
        '''
Q3 = '''SELECT gd.team_id, COUNT(gd.goal_id) * 1.0 / (SELECT COUNT(player_id) 
        FROM Player GROUP BY team_id) 
        FROM GoalDetails gd GROUP BY team_id;
     '''    
Q4 = '''SELECT captain, COUNT(captain) AS no_of_times_captain 
        FROM MatchCaptain GROUP BY captain;'''

Q5 = '''SELECT COUNT(DISTINCT captain) AS no_of_players 
        FROM MatchCaptain mc INNER JOIN Match m on m.match_no == mc.match_no 
        WHERE mc.captain == m.player_of_match;
        '''
Q6 = '''SELECT DISTINCT mc.captain FROM MatchCaptain mc 
        WHERE EXISTS(SELECT p.player_id FROM Player p WHERE p.player_id == mc.captain)
        AND NOT EXISTS(SELECT m.player_of_match FROM Match m 
        WHERE m.player_of_match == mc.captain);
        '''
Q7 = '''SELECT strftime('%m', play_date) AS month, COUNT(match_no) as no_of_match FROM 
        Match GROUP BY strftime('%m', play_date) ORDER BY no_of_match DESC;
        '''
Q8 = '''SELECT jersey_no, COUNT(player_id) AS no_of_captains 
        FROM Player p INNER JOIN MatchCaptain mc on p.player_id == mc.captain 
        GROUP BY jersey_no ORDER BY no_of_captains DESC, jersey_no DESC; 
        '''        
Q9 = '''SELECT player_id, AVG(m.audience) AS avg_audience FROM Player p INNER JOIN MatchTeamDetails mtd on
        p.team_id == mtd.team_id INNER JOIN Match m on m.match_no == mtd.match_no 
        GROUP BY player_id ORDER BY avg_audience DESC, player_id DESC;
        '''
Q10= '''SELECT team_id, AVG(age) FROM Player GROUP BY team_id;
        '''
Q11= '''SELECT AVG(age) AS avg_age_of_captains FROM Player p INNER JOIN MatchCaptain mc
        on p.player_id == mc.captain;
        '''
Q12= '''SELECT strftime('%m',date_of_birth) AS month, count(player_id) AS no_of_players
        FROM Player GROUP BY strftime('%m',date_of_birth) 
        ORDER BY no_of_players DESC, month DESC;
        '''
Q13= '''SELECT captain, COUNT(captain) AS no_of_wins FROM MatchCaptain mc INNER JOIN MatchTeamDetails mtd
        on mc.team_id == mtd.team_id WHERE win_lose = 'W' AND mc.match_no = mtd.match_no 
        GROUP BY captain ORDER BY no_of_wins DESC;
        '''
        