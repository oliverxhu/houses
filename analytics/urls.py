from django.conf.urls import url
from . import views

app_name = 'analytics'
urlpatterns = [

    url(r'^analytics/$', views.MyView.as_view()),
    # url(r'^analytics/$', views.index, name='index'),
]