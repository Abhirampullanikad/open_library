from django.contrib import admin
from django.urls import path
from . import views

app_name = 'userapp'

urlpatterns = [
    path('',views.userlistBook,name='list'),
    path('userlist/',views.userlistBook,name='userlist'),
    path('books/<int:book_id>/', views.userDetailView, name='details'),
    path('user/', views.user,name='user'),
    path('search/', views.search_Book, name='search'),
    path('add_to_cart/<int:book_id>/',views.add_to_cart,name='addtocart'),
    path('view_cart/',views.view_cart,name='viewcart'),
    path('increase/<int:item_id>/',views.increase_quantity,name='increase_quantity'),
    path('decrease/<int:item_id>/',views.decrease_quantity,name='decrease_quantity'),
    path('remove_cart/<int:item_id>/',views.remove_from_cart,name='remove_cart'),
    path('checkout/',views.create_checkout_session,name='create-checkout-session'),
    path('success/', views.success, name='success'),  
    path('cancel/', views.cancel, name='cancel'),  
]