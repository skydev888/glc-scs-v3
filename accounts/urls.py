from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.TopPage.as_view(), name='top'),
    path('home/', views.Home.as_view(), name='home'),
    path('thanks/', views.Thanks.as_view(), name='thanks'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),  # contrib.auth使用
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),  # contrib.auth使用
    path('detail/<int:pk>/', views.UserDetail.as_view(), name='detail'),
    path('update/<int:pk>/', views.UserUpdate.as_view(), name='update'),
    path('googletrans/', views.googletrans, name='googletrans'),
    path('index/', views.MemberList.as_view(), name='index'),  # あとで修正必要
]
