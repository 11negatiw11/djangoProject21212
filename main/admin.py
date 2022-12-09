from django.contrib import admin
from .models import *

class AdminItem(admin.ModelAdmin):
    list_display = ( 'id','name', 'description','category','price')
    list_filter =('category',)
    search_fields = ('name__contains',)

admin.site.register(Item , AdminItem)
admin.site.register(Category)
