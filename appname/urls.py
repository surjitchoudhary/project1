from django.urls import path
from appname import views
urlpatterns=[
    path('',views.HomePageView.as_view(), name='index'),
    path('about', views.AboutPageView.as_view(), name='About')

]