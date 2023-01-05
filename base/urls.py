from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    # path('', views.TaskListView.as_view(), name='tasks'),
    path('', views.TasSearchView.as_view(), name='tasks'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task'),
    path('create-task/', views.TaskCreateView.as_view(), name='task-create'),
    path('edit-task/<int:pk>/', views.TaskUpdateView.as_view(), name='task-edit'),
    path('delete-task/<int:pk>/', views.TaskDelete.as_view(), name='task-delete'),

]
