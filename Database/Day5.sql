--Q1
select * from dbo.book
select * from dbo.course
select * from dbo.CBlink



SELECT bk_title, cr_title
FROM book, CBlink, course
where bk_id = li_bkId and li_crCode = cr_code;

--Q2
select * from dbo.book



select bk_title from dbo.book
where bk_totalCopies > 50 and bk_totalCopies < 100

--Q3
select * from dbo.borrower

select br_name , br_dept from dbo.borrower
where br_city = 'Seeb'
order by br_dept;

--Q4
Select * from dbo.book
select * from dbo.course
select * from dbo.CBlink


select dp_name,sum(bk_totalCopies)
from course ,book , CBlink, department
where dp_code = cr_dept
and bk_id = li_bkId
and cr_code = li_crCode
group by dp_name;




