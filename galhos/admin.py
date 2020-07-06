from django.contrib import admin
from .models import Livros


class LivrosAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(Livros, LivrosAdmin)
