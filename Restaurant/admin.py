from django.contrib import admin 

# Register your models here.

from .models import Menu, Booking
 
class BookingAdmin(admin.ModelAdmin):
    list_display=['name','no_of_guests','booking_date']


class MenuAdmin(admin.ModelAdmin):
    list_display=['title','price','inventory']

admin.site.register(Menu,MenuAdmin)
admin.site.register(Booking,BookingAdmin)