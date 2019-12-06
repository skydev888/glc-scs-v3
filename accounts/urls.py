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



    # path('detail/', views.Detail.as_view(template_name='accounts/detail.html'), name='detail'),  # ログイン後遷移ページとして使用
    path('thanks/', views.Thanks.as_view(), name='thanks'),  # ログアウト後遷移ページとして使用


]
