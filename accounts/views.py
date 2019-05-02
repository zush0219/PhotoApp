from django.shortcuts import render

# Create your views here.
import logging

from django.conf import settings

from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import LoginForm, RegisterForm

logger = logging.getLogger(__name__)


class RegisterView(View):
    def get(self, request):
        # すでにログインしている場合はトップ画面へリダイレクト
        if request.user.is_authenticated:
            return redirect(reverse('app:index'))

        context = {
            'form': RegisterForm(),
        }
        return render(request, 'accounts/register.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)

        if not form.is_valid():
            return render(request, 'accounts/register.html', {'form': form})

        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        # ログイン処理（取得した Userオブジェクトをセッションに保存 & Userデータを更新）
        auth_login(request, user)

        return redirect(reverse('app:index'))


register = RegisterView.as_view()


class LoginView(View):
    def get(self, request):
        """GETリクエスト用のメソッド"""
        # すでにログインしている場合はトップ画面へリダイレクト
        if request.user.is_authenticated:
            return redirect(reverse('app:index'))

        context = {
            'form': LoginForm(),
        }
        # ログイン画面用のテンプレートに値が空のフォームをレンダリング
        return render(request, 'accounts/login.html', context)

    def post(self, request):
        """POSTリクエスト用のメソッド"""
        form = LoginForm(request.POST)

        if not form.is_valid():
            return render(request, 'accounts/login.html', {'form': form})

        user = form.get_user()

        # ログイン処理（取得したユーザーオブジェクトをセッションに保存 & ユーザーデータを更新）
        auth_login(request, user)

        # トップ画面にリダイレクト
        return redirect(reverse('app:index'))


login = LoginView.as_view()


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            # ログアウト処理
            auth_logout(request)

        return redirect(reverse('app:index'))


logout = LogoutView.as_view()