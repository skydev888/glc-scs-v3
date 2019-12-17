from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.views import generic
from requests import request
from accounts.models import UserProfile
from .forms import UserCreateForm, UserUpdateForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView
from googletrans import Translator
from django.views.generic.edit import UpdateView
from django.core.mail import send_mail



# ユーザーモデルセット
User = get_user_model()


class TopPage(TemplateView):
    """
    TOPページ
    """
    template_name = 'accounts/top.html'



class Thanks(TemplateView):
    """
    サンクスページ
    """
    template_name = 'accounts/thanks.html'



class Home(TemplateView):
    """
    HOMEページ
    """
    template_name = "accounts/home.html"


def signup(request):
    """
    ユーザー新規登録
    """
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.userprofile.username = form.cleaned_data.get('username')  # added
            user.userprofile.password1 = form.cleaned_data.get('password1')
            user.userprofile.password2 = form.cleaned_data.get('password2')
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

            # メール送信
            send_notification(user.userprofile.username,user.userprofile.phone)

            user.save()
            # d = {
            #     'text': translated_username.text
            # }
            # return render(request, 'accounts/googletrans.html', d) # 表示はせずデータベースに登録させる為グレーアウト

            return redirect('login')
    else:
        form = UserCreateForm()
    return render(request, 'accounts/signup.html', {'form': form})


def index(request):
    """
    ユーザー一覧表示
    """
    members = UserProfile.objects.all().order_by('id')
    return render(request, 'accounts/index.html', {'members':members})


#一覧（ページネーション用に追加）
from django.views.generic import ListView



#一覧表示（l)
class MemberList(ListView):
    model = UserProfile #利用するモデル
    context_object_name='members' #オブジェクト名の設定（標準ではobject_listとなってしまう）
    template_name='members/index.html' #テンプレートページの指定
    paginate_by = 1 #1ページあたりのページ数


# バリデーション・詳細表示・編集更新（テスト）https://narito.ninja/blog/detail/43/
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser



class UserDetail(OnlyYouMixin, generic.DetailView):
    """
    ユーザー詳細表示
    """
    model = UserProfile
    template_name = 'accounts/detail.html'


class UserUpdate(OnlyYouMixin, generic.UpdateView):
    """
    ユーザー情報編集
    """
    model = UserProfile
    form_class = UserUpdateForm
    template_name = 'accounts/form.html'

    def get_success_url(self):
        return resolve_url('accounts:detail', pk=self.kwargs['pk'])



def delete(request, id):
    """
    ユーザー削除
    """
    # return HttpResponse("削除")
    member = get_object_or_404(UserProfile, pk=id)
    member.delete()
    return redirect('accounts:index')



def googletrans(request):
    """
    Googletrans翻訳  method
    """
    translator = Translator()
    translated = translator.translate('Bastian Schweinsteiger', src='de', dest='ja')
    d = {
        'text': translated.text
    }
    return render(request, 'accounts/googletrans.html',d)



class Googletrans(UpdateView):
    """
    Googletrans翻訳 class
    """
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



def send_notification(usernam,phone):
    """
    メール送信
    """
    subject = "SCS Reminde"
    message = "GOT A NEW STUDENT REGISTRTION!!\n\n\n\n" + "=================================================\n" + "・NAME:" + usernam + "\n\n" + "・PHONE: " + phone + "\n\n" + "=================================================\n" + "CALL TO HE/ER, BUY HOUSE!!!"
    from_email = 'toritoritorina@gmail.com'  # 送信者
    recipient_list = ["toritoritorina@gmail.com"]  # 宛先リスト
    send_mail(subject, message, from_email, recipient_list)