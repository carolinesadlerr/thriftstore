use onlinethriftshop;

-- MODIFYING THE USER TABLE - DML update + select
update user set email = "dan112@gmail.com" where user_ID = "user1";
select * from user;
select email from user;

-- MODIFYING THE ITEM TABLE - DML delete 
delete from item where item_ID = "item1";
select * from item;

-- FINDING COUNT OF ITEMS IN EACH CATEGORY - aggregate functions
select category, count(item_ID) from item group by category;

select max(price), min(price), avg(price) from item;

-- ORDER ITEMS BY PRICE
select * 
from item
order by price;

-- JOINING USER AND SHIPPING INFO TABLES
select * from user natural join user_shipping_info ;

-- SELECT USER NAMES THAT ORDERED/BOUGHT SOMETHING - nested subquery
select name
from user
where user_ID in (
select buyer_ID
from orders);

-- CREATE VIEW FOR USER 1 TO SHOW WHAT THEY ARE SELLING - view
create view user1_sales as (
select * 
from sale natural join item
where seller_ID = 'user1');

select * from user1_sales;
