--insert into dbo.BOOK values(2,'Biography of Ahmed Alabri','3', 353,3,3);

--insert into dbo.BOOK values(1,'Biography of Jamal Al-Mahroqi','1', 35,3,3);

--update dbo.BOOK set Bk_#ofPages = 353 Where Bk_ID = 1;

--insert into dbo.BOOK values(3,'Biography of Mohammed Al-Yahyai','2',321,3,3)

--delete from dbo.BOOK where Bk_ID = 3

--ALTER TABLE dbo.BOOK ADD Bk_TimeOfAdd Date Default getdate();

--insert into dbo.BOOK values(3,'Biography of Mohammed Al-Yahyai','2',321,3,3,GETDATE())

--insert into dbo.BOOK values(5,'The Hobbit The battle of the five armey','13',NULL,7,7,NULL)

--create table TestToDrop(
--T_1 char(1) PRIMARY KEY,
--T_2 char(1),
--T_3 char(1),
--T_4 char(1),
--);

--alter table TestToDrop add T_ID int not NULL;

--ALTER TABLE TestToDrop ADD CONSTRAINT FK_T_ID FOREIGN KEY (T_ID) REFERENCES dbo.BOOK(Bk_ID);

--insert into dbo.BOOK values(6,'Database Managment System','4',621,1,1,getdate())

--select * from TestToDrop;
--select * from dbo.BOOK;

drop table TestToDrop;