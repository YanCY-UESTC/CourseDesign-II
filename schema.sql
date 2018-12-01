drop table if exists entires;
create table entires (
    id varchar(20) primary key autoincrement,
    title char(20) not null,
    text varchar(50) not null 
);