from django.shortcuts import render
from django.views.generic import TemplateView,RedirectView
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from allauth.account.views import LoginView,SignupView
# Create your views here.
class LoginPageView(LoginView):
    extra_context = {
        'site_name' : 'ShareCMS demo'
    }
    template_name = 'user/login.html'
    def get_context_data(self,**kwargs):
        return super().get_context_data()

class LogoutView(RedirectView):
    url = '/'
    
    def get(self,request):
        logout(request)
        return HttpResponseRedirect( self.url)
      
class SignUpView(SignupView):
    template_name = 'user/signup.html'
    extra_context = {
        'site_name' : 'ShareCMS demo'
    }
     
        