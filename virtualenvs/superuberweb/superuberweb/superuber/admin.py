# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Funcionario, Cargo, Departamento, Projeto, Cliente, Fornecedor, Custo

class FuncionarioAdmin(admin.ModelAdmin):
	list_display = ('nome', 'email')
	search_fields = ('nome', 'cargo', 'email', 'reg_numbe')r

admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Cargo)
admin.site.register(Departamento)
admin.site.register(Projeto)
admin.site.register(Cliente)
admin.site.register(Fornecedor)
admin.site.register(Custo)
