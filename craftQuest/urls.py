from django.urls import path
from craftQuest import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]