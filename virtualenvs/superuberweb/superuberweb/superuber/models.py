# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Cargo(models.Model):
	nome = models.CharField(max_length=30)

	def __str__(self):
		return self.nome

class Departamento(models.Model):
	nome = models.CharField(max_length=30)

	def __str__(self):
		return self.nome

class Funcionario(models.Model):
	pfpj = models.CharField(
		max_length = 2,
		choices = ( 
			('PF', 'Pessoa Física'),
			('PJ', 'Pessoa Jurídica')
		)
	)
	reg_number = models.CharField(max_length=11)
	nome = models.CharField(max_length=30)
	endereco = models.CharField(max_length=50)
	email = models.CharField(max_length=30)
	genero = models.CharField(
		max_length = 1,
		choices = ( 
			('F', 'Feminino'),
			('M', 'Masculino'),
			('Q', 'Outro')
		)
	)
	nascimento = models.DateField()
	salario = models.CharField(max_length=20)
	vinculo = models.CharField(
		max_length = 1,
		choices = ( 
			('T', 'Terceirizado'),
			('E', 'Efetivo')
		)
	)
	departamento = models.ForeignKey(Departamento, blank=True)
	cargo = models.ForeignKey(Cargo, blank=True)

	def __str__(self):
		return self.nome

class Fornecedor(models.Model):
	nome = models.CharField(max_length=30)
	reg_number = models.CharField(max_length=14)
	pfpj = models.CharField(
		max_length = 2,
		choices = ( 
			('PF', 'Pessoa física'),
			('PJ', 'Pessoa jurídica')
		)
	)

	def __str__(self):
		return self.nome

class Custo(models.Model):
	nome = models.CharField(max_length=30)
	fornecedor = models.ForeignKey(Fornecedor, default='')

	def __str__(self):
		return self.nome

class Cliente(models.Model):
	nome = models.CharField(max_length=30)
	pfpj = models.CharField(
		max_length = 2,
		choices = ( 
			('PF', 'Pessoa física'),
			('PJ', 'Pessoa jurídica')
		),
		default='PF'
	)
	reg_number = models.CharField(max_length=14)

	def __str__(self):
		return self.nome

class Projeto(models.Model):
	nome = models.CharField(max_length=30)
	funcionarios = models.ManyToManyField(Funcionario)
	custo = models.ManyToManyField(Custo)
	cliente = models.ForeignKey(Cliente, default='')

	def __str__(self):
		return self.nome