-- https://leetcode.com/problems/movie-rating/description/
(
select name as results  from  (
select m.title , u.name , mr.rating from MovieRating mr left join Movies m on mr.movie_id=m.movie_id left join Users u on  mr.user_id = u.user_id
) tbl group by name order by count(name) desc , name asc  limit 1
)
UNION ALL
(
select title as results  from  (
select m.title , u.name , mr.rating , mr.created_at from MovieRating mr left join Movies m on mr.movie_id=m.movie_id left join Users u on  mr.user_id = u.user_id
) tbl where month(created_at)=2 and year(created_at)=2020 group by title order by avg(rating) desc , title asc limit 1);
