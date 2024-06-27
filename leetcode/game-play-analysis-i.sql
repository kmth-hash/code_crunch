-- https://leetcode.com/problems/game-play-analysis-i/description/?lang=pythondata

select player_id , min(event_date) as first_login from Activity group by player_id ;
