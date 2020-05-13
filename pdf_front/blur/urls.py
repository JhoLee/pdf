from django.urls import path

from . import views

app_name = 'blur'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('request/<int:pk>/', views.DetailView.as_view(), name='detail'),
]
