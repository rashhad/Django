from django.urls import path
from . import views
urlpatterns = [
    path('', views.show_tasks, name='show'),
    path('add/', views.add_task, name='add'),
    path('completed/', views.completed_tasks, name='completed'),
    path('del/<int:id>', views.delete_task, name='del'),
    path('com/<int:id>', views.completed, name='com'),
    path('edi/<int:id>', views.edit, name='edi'),
]
