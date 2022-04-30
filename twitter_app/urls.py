from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('twitter.com/<slug:slug>', views.post_detail, name = 'post_detail_url'),
    path('twitter.com/search_results/', views.search_results, name = 'search_results'),
    path('profile/save_bg/', views.save_bg, name = 'save_bg'),
    path('profile/', views.profile, name = 'profile_url'),
    path('profile/<str:username>', views.user_detail, name = 'user_detail'),
    path('authorisation/', views.authorisation, name = 'authorisation'),
    path('search/', views.search_results, name = 'search_url'),
    path('register/', views.register, name = 'register'),
    path('add_post/', views.add_post, name = 'add_post')
]