from django.contrib import admin
from django.urls import path
from project import settings
from userauth import views
from django.conf.urls.static import static

app_name = "userauth"

urlpatterns = [
    path('',views.home, name='home'),
    path('logout_user/', views.logout_user, name='logout'),
    path('login_view/',views.login_view, name='login'),
    path('signup/',views.signup, name='signup'),
    path('profile/<str:username>',views.profile, name='profile'),
    path('submit_hackathon_post/<str:username>', views.submit_hackathon_post, name='post'),
    path('hackathons',views.hackathons_feed, name='hackathons'),
    path('apis',views.apis_feed, name='apis'),
    # path('like-post/<str:id>', views.likes, name='like-post'),
    # path('#<str:id>', views.home_post),
    # path('explore',views.explore),
    # path('profile/<str:id_user>', views.profile, name='profile'),
    # path('profile',views.profile, name='profile'),
    # path('delete/<str:id>', views.delete),
    # path('search-results/', views.search_results, name='search_results'),
    # path('follow', views.follow, name='follow'),
]
