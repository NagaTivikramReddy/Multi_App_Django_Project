from django.views.generic.edit import CreateView
from .settings import BASE_DIR, TEMPLATE_DIR
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def index(request):
    return render(request, 'allinone_base/index.html')


class CustomLoginView(LoginView):
    template_name = 'allinone_base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')


class CustomRegister(CreateView):
    template_name = 'allinone_base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):

        user = form.save()  # To create a user

        # To auto login as soon as when registration completes
        if user is not None:
            login(self.request, user)

        return super(CustomRegister, self).form_valid(form)

     # To Redirect to index page when user tries to register while he is already logged in
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(CustomRegister, self).get(*args, **kwargs)

    
