from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy

from .models import Task


# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'base/task_list.html'
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'base/task.html'
    context_object_name = 'task'


class TaskCreateView(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'base/edit_task.html'
    success_url = reverse_lazy('tasks')


class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
