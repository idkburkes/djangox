from django.shortcuts import render

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Task


class TaskListView(ListView):
    template_name = "todoapp/task-list.html"
    model = Task


class TaskDetailView(DetailView):
    template_name = "todoapp/task-detail.html"
    model = Task


class TaskCreateView(CreateView):
    template_name = "todoapp/task-create.html"
    model = Task
    fields = ['title', 'description', 'due_date_time', 'creator']


class TaskUpdateView(UpdateView):
    template_name = "todoapp/task-update.html"
    model = Task
    fields = ['title', 'description', 'due_date_time', 'creator']


class TaskDeleteView(DeleteView):
    template_name = "todoapp/task-delete.html"
    model = Task
    success_url = reverse_lazy("task_list")