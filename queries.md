mysqldump -uroot -p superuber > superuber.sql

create database superuber;

use superuber;

show tables;

describe Funcionario

create table Funcionario (
id_func int not null auto_increment primary key, 
cpf_func varchar(11) not null, 
nome_func varchar(50) not null, 
endereco_func varchar(50) not null, 
sexo_func varchar(1) not null, 
datanasc_func date not null, 
salario_func double, 
terceirizado tinyint(1) not null, 
dep_id int, cargo_id int, 
CONSTRAINT dep_id FOREIGN KEY (dep_id) REFERENCES Departamento (id_dep),
CONSTRAINT cargo_id FOREIGN KEY (cargo_id) REFERENCES Cargo (id_cargo));

create table Cargo (id_cargo int not null auto_increment primary key, nome_cargo varchar(20) not null);

create table Departamento (id_dep int not null auto_increment, nome_dep varchar(30) not null, PRIMARY KEY (id_dep));

create table Projeto (id_projeto int not null auto_increment primary key, nome_proj varchar(20) not null);

create table Cliente (id_cli int not null auto_increment primary key, nome_cli varchar(50) not null);

create table Fornecedor (id_fornec int not null auto_increment primary key, nome_fornec varchar(50) not null);

create table Custo (id_custo int not null auto_increment primary key, valor_custo double not null, nome_custo varchar(30) not null);

insert into Departamento (nome_dep) values (‘Financeiro’);

insert into Cargo (nome_cargo) values (‘Contador’);

insert into Funcionario (cpf_func, nome_func, endereco_func, sexo_func, datanasc_func, salario_func, terceirizado, dep_id, cargo_id) values ('12345678912', 'Alfredo Cedo', 'Rua tal', 'M', 07/04/1990, 2000, 0, 1, 1);

delete from funcionario where id_func = 1;
