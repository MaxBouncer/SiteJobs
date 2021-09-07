from django.contrib import admin

# Register your models here.
from .models import Cliente, Produto


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Produto, ProdutoAdmin)
