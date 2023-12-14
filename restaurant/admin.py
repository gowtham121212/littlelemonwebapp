from django.contrib import admin
from .models import User, Booking, Menu, Menu_Table, Booking_Table, MenuItemS

admin.site.register(User)
admin.site.register(Booking)
admin.site.register(Menu)
admin.site.register(Menu_Table)
admin.site.register(Booking_Table)
admin.site.register(MenuItemS)
