Q1 = "SELECT AVG(age) FROM Player;"
Q2 = "SELECT match_no, play_date FROM Match WHERE audience > 50000 ORDER BY match_no ASC;"
Q3 = "SELECT team_id, COUNT(win_lose) FROM MatchTeamDetails WHERE win_lose = 'W' GROUP BY team_id ORDER BY COUNT(win_lose) DESC, team_id ASC;"
Q4 = "SELECT match_no, play_date FROM Match WHERE stop1_sec > (SELECT AVG(stop1_sec) FROM Match) ORDER BY match_no DESC;"
Q5 = "SELECT mc.match_no, t.name,p.name FROM Team t INNER JOIN MatchCaptain mc on t.team_id == mc.team_id INNER JOIN Player p on p.player_id == mc.captain ORDER BY mc.match_no ASC,t.team_id ASC;"
Q6 = "SELECT m.match_no,p.name,p.jersey_no FROM Player p INNER JOIN Match m on p.player_id == m.player_of_match ORDER BY m.match_no ASC"
Q7 = "SELECT t.name, AVG(age) FROM Team t INNER JOIN Player p on t.team_id == p.team_id GROUP BY t.team_id HAVING AVG(age) > 26;"
Q8 = "SELECT p.name, p.jersey_no, p.age, COUNT(gd.goal_id) FROM Player p INNER JOIN GoalDetails gd on p.player_id == gd.player_id GROUP BY p.player_id HAVING age <= 27 ORDER BY COUNT(gd.goal_id) DESC, p.name ASC;"
Q9 = "SELECT t.team_id,(100.0*count(t.team_id))/(SELECT COUNT(team_id) FROM GoalDetails) FROM Team t INNER JOIN GoalDetails gd on gd.team_id == t.team_id GROUP BY t.team_id;"
Q10 = "SELECT AVG(goal_score) AS avg_scr FROM (SELECT COUNT(*) AS goal_score FROM GoalDetails GROUP BY team_id);"

Q11 = '''SELECT p.player_id, p.name, p.date_of_birth 
            FROM Player p 
            WHERE NOT EXISTS(
                SELECT gd.player_id FROM GoalDetails gd 
                WHERE p.player_id  == gd.player_id)
            ORDER BY p.player_id ASC;'''

Q12 = '''SELECT t.name, mtd.match_no, m.audience ,
            m.audience - (SELECT avg(audience) 
            FROM Match m INNER JOIN MatchTeamDetails mtd on
            `m`.`match_no` == `mtd`.`match_no` 
            WHERE `t`.`team_id` == `mtd`.`team_id` GROUP BY `mtd`.`team_id`)
            AS audience FROM Team t INNER JOIN MatchTeamDetails mtd on 
            `t`.`team_id` == `mtd`.`team_id` INNER JOIN Match m on
            `m`.`match_no` == `mtd`.`match_no` ORDER BY mtd.match_no ASC;'''
            