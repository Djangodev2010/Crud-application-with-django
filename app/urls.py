from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('create-task', views.create_task_view, name='create_task'),
    path('complete-task <int:task_id>', views.complete_task, name='complete_task'),
    path('delete-task <int:task_id>', views.delete_task, name='delete_task'),
    path('edit-task <int:task_id>', views.edit_task, name='edit_task')
]

