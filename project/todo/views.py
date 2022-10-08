from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib.auth import get_user_model
from .models import *
from django.views.generic.list import ListView

from django.views.decorators.http import require_http_methods
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm

class IndexView(TemplateView):
    template_name = 'index.html'


class Login(LoginView):
    template_name = 'registration/login.html'


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()  # save the user
        return super().form_valid(form)


def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div id='username-error' class='error'>This user is already exists<div>")
    else:
        return HttpResponse("<div id='username-error' class='success'>User is available<div>")



@login_required
def add_task(request):
    task = request.POST.get('name')

    Todo.objects.create(task=task, user=request.user)
    tasks = Todo.objects.filter(user=request.user)

    return render(request, 'partials/todos.html', {'tasks': tasks})


@login_required
@require_http_methods(['DELETE'])
def delete_task(request, pk):
    Todo.objects.get(pk=pk).delete()
    tasks = Todo.objects.filter(user=request.user)
    return render(request, 'partials/todos.html', {'tasks': tasks})


def done(request, pk):
    if Todo.objects.filter(pk=pk, done=False).exists():
        Todo.objects.filter(pk=pk).update(done=True)
    else:
        Todo.objects.filter(pk=pk).update(done=False)

    tasks = Todo.objects.filter(user=request.user)
    return render(request, 'partials/todos.html', {'tasks': tasks})


def sort(request):
    pass



