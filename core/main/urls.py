from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>/', views.index_detail, name='index_detail'),
    path('explore/', views.explore, name='explore'),
    path('author/', views.author, name='author'),
    path('create/', views.create, name='create'),
    path('login_request/', views.login_request, name='login_request'),
    path('register_request/', views.register_request, name='register_request'),
    path('logout', views.logout_request, name='logout')
]