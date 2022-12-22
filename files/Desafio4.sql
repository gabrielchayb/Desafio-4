create database contatos;
use contatos;

create table contatos
(
	#id_contatos int primary key auto_increment,
	email varchar(45) not null unique ,
    nome varchar(45) not null,
    assunto varchar(45) not null
    
);

describe contatos;

insert into contatos (email, nome, assunto) values
('fatec@fatec.sp.gov.br','fatec','Flask'),
('fatec1@fatec.sp.gov.br','fatec','Banco de Dados');

select * from contatos;