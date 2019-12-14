from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response, get_object_or_404, resolve_url
from django.urls import reverse_lazy
from django.views import generic
from requests import request
from accounts.models import UserProfile
from .forms import UserCreateForm, UserUpdateForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin




User = get_user_model()




# 削除
def delete(request, id):
    # return HttpResponse("削除")
    member = get_object_or_404(UserProfile, pk=id)
    member.delete()
    return redirect('accounts:index')


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


# # 編集テスト
# @login_required
# def edit(request, user_id):
#     user = get_object_or_404(UserProfile, pk=user_id)
#     if request.method == "POST":
#         form = UserEditForm(request.POST, instance=user)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.userprofile.password1 = form.cleaned_data.get('password1')
#             user.userprofile.password2 = form.cleaned_data.get('password2')
#             user.userprofile.password3 = form.cleaned_data.get('password3')
#             user.userprofile.phone = form.cleaned_data.get('phone')
#             user.save()
#             return redirect('login')
#     else:
#         form = UserEditForm(request.GET, instance=user)
#     return render(request, 'accounts/edit.html', {'form': form})


# バリデーション・詳細表示・編集更新（テスト）https://narito.ninja/blog/detail/43/
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


class UserDetail(OnlyYouMixin, generic.DetailView):
    model = UserProfile
    template_name = 'accounts/detail.html'


class UserUpdate(OnlyYouMixin, generic.UpdateView):
    model = UserProfile
    form_class = UserUpdateForm
    template_name = 'accounts/form.html'

    def get_success_url(self):
        return resolve_url('accounts:detail', pk=self.kwargs['pk'])












# 新規登録
def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.userprofile.username = form.cleaned_data.get('username')  # added
            user.userprofile.password1 = form.cleaned_data.get('password1')
            user.userprofile.password2 = form.cleaned_data.get('password2')
            user.userprofile.password3 = form.cleaned_data.get('password3')
            user.userprofile.phone = form.cleaned_data.get('phone')
            user.save()
            password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=password)
            login(request, user)

            # Google翻訳
            user.refresh_from_db()
            translator = Translator()
            translated = translator.translate(user.userprofile.username, src='vi', dest='ja')
            user.userprofile.username_jp = translated.text
            user.save()
            # d = {
            #     'text': translated_username.text
            # }
            # return render(request, 'accounts/googletrans.html', d) # 表示はせずデータベースに登録させる為グレーアウト

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

def googletrans(request):

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