from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, DetailView, UpdateView
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


# class CustomLoginView(LoginView):
#     template_name = 'todolist/login.html'
#     fields = '__all__'
#     redirect_authenticated_user = True

#     def get_success_url(self):
#         return reverse_lazy('todolist:tasklist')


class TaskList(LoginRequiredMixin, ListView):
    model = models.Task
    # context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = context['task_list'].filter(
            user=self.request.user)
        context['count'] = context['task_list'].filter(completed=False).count()

        search_input = self.request.GET.get('search_input') or ''

        if search_input:
            context['task_list'] = context['task_list'].filter(
                title__icontains=search_input)
        context['search_input'] = search_input
        return context


class TaskDetails(LoginRequiredMixin, DetailView):
    model = models.Task
    context_object_name = 'task'
    # template_name = 'todolist/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = models.Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('todolist:tasklist')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = models.Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('todolist:tasklist')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = models.Task
    context_object_name = 'task'
    success_url = reverse_lazy('todolist:tasklist')
