use onlinethriftshop;

insert into user values
("user1", "Dan", "4014443322", "dan@gmail.com"),
("user2", "Zoe", "4014443311", "zoe@gmail.com"),
("user3", "John", "4012345322", "john@gmail.com");

select * from user;

insert into user_shipping_info values
("user1", "123 Some St.", '02891', 'Rhode Island', 'Somecity', 2),
("user2", "45 Upper College Rd.", '02881', 'Rhode Island', 'Kingston', null),
("user3", "365 Rose St.", '92110', "Calfornia", 'San Diego', null);

select * from user_shipping_info;

insert into item values
("item1", "shirt", "clothing", "good", 5.5),
("item2", "shirt", "clothing", "good", 6.7),
("item3", "pants", "clothing", "okay", 7),
("item4", "necklace", "jewelry", "very good", 12.0),
("item5", "bracelet", "jewelry", "okay", 3.22),
("item6", "sneakers", "shoes", "brand new", 25.00),
("item7", "iPhone 5", "technology", "good", 50.00),
("item8", "TV", "technology", "like new", 100.00),
("item9", "boots", "shoes", "very good", 10.00);

select * from item;

insert into technology values 
('item7', 2012, 'Apple', 56),
('item8', 2018, 'Samsung', null);

select * from technology;

insert into jewelry values 
("item4", 40, 'silver'),
("item5", 20, 'gold');

select * from jewelry;

insert into clothes values 
('item1', 'S', 'T-shirt', 'Vans'),
('item2', 'M', 'Long Sleeve', 'Eddie Bauer'), 
('item3', 'XL', 'Jeans', "Levi's");

select * from clothes;

insert into shoes values 
("item6", 12.0, 'Nike'),
("item9", 7, 'LL Bean');

select * from shoes;

insert into sale values
('item1', 'user1'),
('item2', 'user1'),
('item3', 'user1'),
('item4', 'user2'),
('item5', 'user2'),
('item6', 'user3'),
('item7', 'user3'),
('item8', 'user3'),
('item9', 'user3');

select * from sale;

insert into orders values
('user1', 'order1', 'item4', 12.0),
('user2', 'order2', 'item6', 25.0);

select * from orders;
