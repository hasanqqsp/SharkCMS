from django.urls import path,include
from django.conf.urls import url, include
from . import views as user_views
app_name = 'user'
urlpatterns = [
  path('login',user_views.LoginPageView.as_view(),name = 'login'),
  path('logout',user_views.LogoutView.as_view(),name = 'logout'),
  path('signup',user_views.SignUpView.as_view(),name = 'signup'),
]