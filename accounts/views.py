from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, render_to_response
from django.urls import reverse_lazy
from requests import request

from accounts.models import UserProfile
from .forms import UserCreateForm


# 新規登録処理
def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.userprofile.age = form.cleaned_data.get('age')
            user.userprofile.degree = form.cleaned_data.get('degree')
            user.userprofile.city = form.cleaned_data.get('city')
            user.userprofile.state = form.cleaned_data.get('state')
            user.userprofile.country = form.cleaned_data.get('country')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreateForm()
    return render(request, 'accounts/signup.html', {'form': form})


# Thanks処理
from django.views.generic import TemplateView


class Thanks(TemplateView):
    template_name = 'accounts/thanks.html'


# Home処理
class Home(TemplateView):
    template_name = "accounts/home.html"


# 編集処理
from django.views.generic.edit import UpdateView


class Update(UpdateView):
    model = UserProfile
    template_name = 'accounts/update.html'
    fields = ["degree", "city", "state", "country", "age"]
    success_url = reverse_lazy('accounts:home')


# Google trans test
from googletrans import Translator
from requests import request


class Googletrans(TemplateView):
    template_name = 'accounts/googletrans.html'

    def trans(request, pk):
        model = UserProfile

        # p = model.objects.get(pk=pk)
        dic = {
            "country": "日本"
        }
        # return render_to_response('accounts/googletrans.html', {'p': p})
        return render_to_response('accounts/googletrans.html',dic )
            #
            # if request.method == 'POST':
            #     form = UserCreateForm(request.POST)
            #     if form.is_valid():
            #         user = form.save()
            #         user.refresh_from_db()
            #         user.userprofile.age = form.cleaned_data.get('age')
            #         user.userprofile.city = form.cleaned_data.get('city')
            #         user.userprofile.state = form.cleaned_data.get('state')
            #         user.userprofile.country = form.cleaned_data.get('country')

                    # # 翻訳処理
                    # translator = Translator()
                    # src = "Is it possible to translate?"
                    # translated = translator.translate(src, src='en', dest='ja')
                    # # text = translated.text
                    # text = "翻訳できてない"
                    #
                    # context = {
                    #     'japanese': text
                    # }
                    # return render(request, 'accounts/googletrans.html', context)
