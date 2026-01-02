from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add-record/', views.add_record, name='add-record'),
    path('record-detail/<int:pk>/', views.customer_record, name='record-detail'),
    path('update-record/<int:pk>/', views.update_record, name='update-record'),
    path('delete-record/<int:pk>/', views.delete_record, name='delete-record'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),


]