from django.contrib import admin
from website.models import Menu, Order

from website.models import Contact 

# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'name_farsi' , 'price', 'created_date') 
    list_filter = ('name',)
    search_fields = ('name', 'price', )

admin.site.register(Menu, MenuAdmin)

class OrderAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('created_date',) 
    list_filter = ('order_number',)
    search_fields = ('name', 'price', )

admin.site.register(Order, OrderAdmin)

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'email', 'created_date') 
    list_filter = ('email',)
    search_fields = ('name', 'email', 'message')

admin.site.register(Contact, ContactAdmin)

    