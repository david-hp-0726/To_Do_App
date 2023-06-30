from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('log-in/', views.log_in, name='log_in'),
    path('logged-out/', views.logged_out, name='logged_out'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('add-task/', views.add_task, name='add_task'),
    path('edit-task/<item_id>', views.edit_task, name='edit_task'),
    path('delete-confirm/<item_id>', views.delete_confirm, name='delete_confirm'),
    path('delete-task/<item_id>', views.delete_task, name='delete_task'),
    path('switch-status/<item_id>', views.switch_status, name='switch_status'),
]