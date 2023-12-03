from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LogoutView


from .forms import SignupForm


class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'account_app/signup.html'
    success_url = reverse_lazy('diagnosis')

class CustomLogoutView(LogoutView):
    # ログアウト後のリダイレクト先を指定するためのget_success_urlメソッドをオーバーライドします。
    def get_success_url(self):
        # ログアウト後にリダイレクトしたいURLを指定します。
        return reverse_lazy('recommend_videos')  # このURLをカスタマイズしてください
