from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('logout/', views.logout_user, name='logout'),
    path('register_user/', views.register_user, name='register-user'),
    path('update_user/<user_id>', views.update_user, name='update-user'),
    path('delete_user/<user_id>', views.delete_user, name='delete-user'),
    path('list_user/', views.list_user, name='list-user'),
    path('backup/', views.trial, name='backup'),
]