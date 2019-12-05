from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
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


from django.views.generic import TemplateView

class Detail(TemplateView):
    template_name = 'accounts/detail.html'

class Thanks(TemplateView):
    template_name = 'accounts/thanks.html'

class Home(TemplateView):
    template_name = "accounts/home.html"
