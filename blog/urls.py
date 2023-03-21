from django.urls import path
from . import views
urlpatterns = [
    path('', views.StartingPageView.as_view() , name='starting-page'),
    path('posts/', views.AllPostsView.as_view() , name='posts-page'),
    
    # the first slug just to trigger it is a name with some dashes -- and the second we will pass it in views
    path('posts/<slug:slug>/', views.SinglePostView.as_view(), name='post-detail-page'),

]
