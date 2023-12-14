from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Your custom fields go here

    class Meta:
        # Other meta options go here
        pass

class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self):
        return self.first_name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['reservation_date', 'reservation_slot'], name='unique_booking_date_slot')
        ]

class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    menu_item_description = models.TextField(max_length=1000, default='')

    def __str__(self):
        return self.name

    def __str__(self):
        return f'{self.name} : {str(self.price)}'  # Fixed the method name and formatting

class Booking_Table(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=11)
    bookingdate = models.DateTimeField(default=timezone.now)  # Using timezone.now as the default value

    def __str__(self):
        return self.name

class Menu_Table(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=5)  # Assuming a default value of 5 for inventory

    def __str__(self):
        return self.title

class MenuItemS(models.Model):  # Update the class name
    # Your model fields here
    name = models.CharField(max_length=255)
    # ... other fields ...

    def __str__(self):
        return self.name

User._meta.get_field('groups').remote_field.related_name = 'restaurant_user_groups'
User._meta.get_field('user_permissions').remote_field.related_name = 'restaurant_user_user_permissions'
