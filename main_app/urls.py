from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_wish/', views.AddWish.as_view(), name='add_wish'),
    path('delete_wish/<int:wishlist_id>', views.delete_wish, name='delete_wish')
]
