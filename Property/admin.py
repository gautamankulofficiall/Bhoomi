from django.contrib import admin
from Property.models import State,City,Category,Property,ContactUs

# Register your models here.

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id','name')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id','name','state')
    list_filter = ('state',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'category')

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id','username')

    

    


