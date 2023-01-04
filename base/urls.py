from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='tasks'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task'),
    path('create-task/', views.TaskCreateView.as_view(), name='task-create'),
    path('edit-task/<int:pk>/', views.TaskUpdateView.as_view(), name='task-edit'),
    path('delete-task/<int:pk>/', views.TaskDelete.as_view(), name='task-delete'),

]
