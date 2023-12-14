from django.urls import path
from .views import MenuItemView, SingleMenuItemView, home, reservations, about, bookings
from . import views

urlpatterns = [
    path('home/', home, name="home"),
    path('about/', about, name="about"),
    path('book/', bookings, name="book"),  # Change 'book' to 'bookings'
    path('reservations/', reservations, name="reservations"),
    path('menu/', MenuItemView.as_view(), name="menu"),  # Use .as_view() for class-based views
    path('menu/<int:item_id>/', SingleMenuItemView.as_view(), name="single_menu_item"),
    path('api/menu_items/', views.MenuItemsAPIView.as_view(), name='menu_items_api'),
    # ... other paths
]
