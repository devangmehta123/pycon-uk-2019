from django.urls import path

from contrib.polls import views

urlpatterns = [
    path('', views.index, name='index'),
]