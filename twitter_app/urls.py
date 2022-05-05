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
<<<<<<< HEAD
    path('add_post/', views.add_post, name = 'add_post')
=======
    path('favourites/', views.favourites, name = 'favourites'),
    path('favourites/add/<int:post_id>', views.add_to_favourites, name = 'add_to_favourites'),
    path('favourites/delete/<int:post_id>', views.delete_favourites, name = 'delete_favourites'),
    path('messages', views.messages, name = 'messages'),
    path('edit_profile/', views.edit_profile, name = 'edit_profile'),
>>>>>>> 8630e64bc3232cbe471ecfe6a7a6bcb4926f4e81
]