from django.contrib import admin
from website.models import Menu, Order

from website.models import Contact 

# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('food_name', 'price', 'created_date') 
    list_filter = ('food_name',)
    search_fields = ('food_name', 'price', )

admin.site.register(Menu, MenuAdmin)

class OrderAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('created_date',) 
    list_filter = ('order_number',)
    search_fields = ('food_name', 'price', )

admin.site.register(Order, OrderAdmin)

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'email', 'created_date') 
    list_filter = ('email',)
    search_fields = ('name', 'email', 'massage')

admin.site.register(Contact, ContactAdmin)

    