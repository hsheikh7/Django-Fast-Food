from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Menu(models.Model):
    food_name = models.CharField(max_length=255)
    price = models.BigIntegerField()
    description = models.TextField(blank = True , null=True)
    created_date = models.DateTimeField(auto_now_add= True)
    update_date = models.DateTimeField(auto_now= True)

    class Meta: 
        ordering = ('created_date',) 
        
    def __str__(self):
        return self.food_name 

# class Customer(models.Model):
#     name = models.CharField(max_length=255)
#     family_name = models.CharField(max_length=255)
#     email = models.EmailField()
#     # password = models.CharField(max_length=255)
#     membership_id = models.CharField(max_length=255)
#     join_date = models.DateTimeField(auto_now_add= True)
    
#     class Meta: 
#         ordering = ('family_name',) 
        
#     def __str__(self):
#         return self.family_name 

class Order(models.Model):
    order_number = models.IntegerField()
    customer = models.ForeignKey(User, on_delete= models.CASCADE)    
    created_date = models.DateTimeField(auto_now_add=True) 
    items = models.IntegerField()
    total_price = models.IntegerField()
    status = models.BooleanField(default=False)
    time_needed = models.DurationField()

    class Meta: 
        ordering = ('order_number',) 
        
    def __str__(self):
        return self.family_name 
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    family_name = models.CharField(max_length=255, blank = True , null=True)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add= True)
    update_date = models.DateTimeField(auto_now= True)

    class Meta: 
        ordering = ('created_date',) 
        
    def __str__(self):
        return self.name 
        
