from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignupForm


class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'account_app/signup.html'
    success_url = reverse_lazy('recommend_videos')


def logout_view(request):
    logout(request)
    return redirect('index')
