from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('home/', views.Home.as_view(), name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),  # contrib.auth使用
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),  # contrib.auth使用

    path('update/<int:pk>', views.Update.as_view(), name='update'),

    # google trans test
    path('googletrans/', views.googletrans, name='googletrans'),
    # edit test




    # path('detail/', views.Detail.as_view(template_name='accounts/detail.html'), name='detail'),  # ログイン後遷移ページとして使用
    path('thanks/', views.Thanks.as_view(), name='thanks'),  # ログアウト後遷移ページとして使用



    #　CRUDテスト　https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92
    url(r'^$', views.MemberList.as_view(), name='index'),
    url(r'^add/$', views.edit, name='add'),
    # url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
    path('edit/<int:user_id>', views.edit, name='edit'),





]
