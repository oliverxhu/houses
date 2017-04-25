from django.conf.urls import url
from . import views

app_name = 'index'
urlpatterns = [

    url(r'home/$', views.Home.as_view(), name='home'),
    url(r'signup/$', views.Signup.as_view(), name='signup'),
    url(r'login/$', views.Login.as_view(), name='login'),

]