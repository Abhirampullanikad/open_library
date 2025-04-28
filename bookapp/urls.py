from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/1', views.listBook, name='booklist'),

    path('create-book/', views.createBook, name='createbook'),
    path('author/', views.create_Author, name='author'),

    path('detailsview/<int:book_id>/', views.detailsview, name='details'),
    path('updateview/<int:book_id>/', views.updateBook, name='update'),
    path('deleteview/<int:book_id>/', views.DeleteView, name='delete'),
    

    path('index/', views.index,name='index'),
    path('search/',views.search_Book,name='search'),
    path('search/',views.search_Author,name='search'),
    
    


]
