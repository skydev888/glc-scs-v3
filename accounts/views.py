from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from accounts.models import UserProfile
from .forms import UserCreateForm


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




# 追加
from django.views.generic import TemplateView

class Thanks(TemplateView):
    template_name = 'accounts/thanks.html'

class Home(TemplateView):
    template_name = "accounts/home.html"


# 更新
from django.views.generic.edit import UpdateView


class Update(UpdateView):
    model = UserProfile
    template_name = 'accounts/update.html'
    fields = ["degree", "city", "state", "country", "age"]
    success_url = reverse_lazy('accounts:home')