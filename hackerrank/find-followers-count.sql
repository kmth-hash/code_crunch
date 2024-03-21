-- https://leetcode.com/problems/find-followers-count/?envType=study-plan-v2&envId=top-sql-50

select USER_ID , count(follower_ID) AS FOLLOWERS_COUNT from Followers group by user_id ORDER BY USER_ID ASC;
