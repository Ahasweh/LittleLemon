from django.contrib import admin

# Register your models here.


from .models import MenuItem, Booking
 
class BookingAdmin(admin.ModelAdmin):
    list_display=['name','no_of_guests','booking_date']


class MenuItemAdmin(admin.ModelAdmin):
    list_display=['title','price','inventory']

admin.site.register(MenuItem,MenuItemAdmin)
admin.site.register(Booking,BookingAdmin)
