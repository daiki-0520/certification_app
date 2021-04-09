from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.generic.edit import (CreateView, FormView)
from django.views.generic.base import TemplateView, View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Users
from .forms import SignUpForm
from .forms import UserLoginForm
from django.contrib.auth.views import LoginView, LogoutView


class UserLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = UserLoginForm

    # def post(self, request, *args, **kwargs):
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     user = authenticate(email=email, password=password)
    #     if user is not None and user.is_active:
    #         login(request, user)
    #     return redirect('certifications:certification_list')


class UserLogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('certifications:certification_list')


class SignUpView(CreateView):
    model = Users
    template_name = 'signup.html'
    login_url = '/login/'
    form_class = SignUpForm
    success_url = reverse_lazy('certifications:certification_list')

