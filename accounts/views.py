from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.urls import reverse_lazy
from requests import request
from accounts.models import UserProfile
from .forms import UserCreateForm, UserEditForm








# 削除
def delete(request, id):
    # return HttpResponse("削除")
    member = get_object_or_404(UserProfile, pk=id)
    member.delete()
    return redirect('accounts:index')



#詳細表示
def detail(request, id=id):
    member = get_object_or_404(UserProfile, pk=id)
    return render(request, 'accounts/detail.html', {'member':member})


#一覧
def index(request):
    members = UserProfile.objects.all().order_by('id')
    return render(request, 'accounts/index.html', {'members':members})


#一覧（ページネーション用に追加）
from django.views.generic import ListView


class MemberList(ListView):
    model = UserProfile #利用するモデル
    context_object_name='members' #オブジェクト名の設定（標準ではobject_listとなってしまう）
    template_name='members/index.html' #テンプレートページの指定
    paginate_by = 1 #1ページあたりのページ数






# 編集テスト
@login_required
def edit(request, user_id):
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserEditForm()
    return render(request, 'accounts/edit.html', {'form': form})






# 新規登録
def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.userprofile.password1 = form.cleaned_data.get('password1')
            user.userprofile.password2 = form.cleaned_data.get('password2')
            user.userprofile.password3 = form.cleaned_data.get('password3')
            user.userprofile.phone = form.cleaned_data.get('phone')
            user.save()
            password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreateForm()
    return render(request, 'accounts/signup.html', {'form': form})


# Thanks処理
from django.views.generic import TemplateView, ListView


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


# googletran　メソッド
from googletrans import Translator

def googletrans():

    translator = Translator()
    translated = translator.translate('Bastian Schweinsteiger', src='de', dest='ja')
    d = {
        'text': translated.text
    }
    return render(request, 'accounts/googletrans.html',d)



# googletran　クラス
from googletrans import Translator

class Googletrans(UpdateView):

    model = UserProfile
    template_name = 'accounts/googletrans.html'
    fields = ["degree", "city", "state", "country", "age"]
    # success_url = reverse_lazy('accounts:home')
    def trans(self):
        translator = Translator()
        translated = translator.translate('Bastian Schweinsteiger', src='de', dest='ja')
        d = {
            'text': translated.text
        }
        return render(request, 'accounts/googletrans.html',d)