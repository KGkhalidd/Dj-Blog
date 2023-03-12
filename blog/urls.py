from django.urls import path
from . import views
urlpatterns = [
    path('', views.starting_page, name='starting-page'),
    path('posts/', views.posts, name='posts-page'),
    
    # the first slug just to trigger it is a name with some dashes -- and the second we will pass it in views
    path('posts/<slug:slug>/', views.post_detail, name='post-detail-page'),

]
