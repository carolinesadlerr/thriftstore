drop database if exists onlinethriftshop;
create database if not exists onlinethriftshop;
use onlinethriftshop;

create table if not exists user (
    user_ID varchar(20),
    name varchar(20) NOT NULL,
    phone_number varchar(10),
    email varchar(255) NOT NULL
);

-- ALTER TABLE QUERY
alter table user 
add primary key (user_ID);

create table if not exists item (
    item_ID varchar(20),
    name varchar(20),
    category varchar(20),
    item_condition varchar(20),
    price float,
    PRIMARY KEY(item_ID)
);

create table if not exists technology (
    item_ID varchar(20),
    year int(4),
    brand varchar(50),
    storage_size int,
    Primary key(item_ID),
    FOREIGN KEY(item_ID) REFERENCES item(item_ID) on delete cascade
);

create table if not exists jewelry (
    item_ID varchar(20),
    size int, -- in centimeters
    color varchar(10),
    Primary key(item_ID),
    FOREIGN KEY(item_ID) REFERENCES item(item_ID) on delete cascade
);

create table if not exists clothes (
    item_ID varchar(20),
    size varchar(4),
    clothes_type varchar(20),
    brand varchar(50),
    Primary key(item_ID),
    FOREIGN KEY(item_ID) REFERENCES item(item_ID) on delete cascade
);

create table if not exists shoes (
    item_ID varchar(20),
    size numeric(3,1),
    brand varchar(50),
    Primary key(item_ID),
    FOREIGN KEY(item_ID) REFERENCES item(item_ID)
);

create table if not exists user_shipping_info (
    user_ID varchar(20),
    address varchar(100) NOT NULL,
    zipcode char(5),
    state varchar(20),
    city varchar(30),
    apt_num int,
    PRIMARY KEY(user_ID),
    FOREIGN KEY(user_ID) REFERENCES user(user_ID) on delete cascade
);

create table if not exists orders (
    buyer_ID varchar(20),
    order_num varchar(30),
    item_ID varchar(20),
    order_total numeric(6,2),
    PRIMARY KEY(order_num),
    FOREIGN KEY(buyer_ID) REFERENCES user(user_ID) on delete restrict
);

create table if not exists sale (
    item_ID varchar(20),
    seller_ID varchar(20),
    PRIMARY KEY(item_ID, seller_ID),
    FOREIGN KEY(item_ID) REFERENCES item(item_ID) on delete cascade,
    FOREIGN KEY(seller_ID) REFERENCES user(user_ID) on delete cascade
);
