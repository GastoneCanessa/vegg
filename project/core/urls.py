from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_view, name='home'),
    path('users/create_post/', views.create_post_view, name='create_post'),
    path('user/<str:username>/', views.user_profile_view, name='user_profile'),
    path('users/',views.UserList.as_view(), name='user_list'),
    path('user/<str:username>/delate_post/<int:pk>/', views.DelatePost.as_view(), name='delate_post'),
    path('advanced_serch/', views.advanced_serch, name='advanced_serch'),
]
