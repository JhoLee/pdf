from django.urls import path

from . import views

app_name = 'mask'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('request/', views.RequestFormView.as_view(), name='request'),
    path('request/<int:pk>/', views.DetailView.as_view(), name='detail'),

]
