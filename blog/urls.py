from django.urls import path
from . import views
from .views import (PostListView,PostCreateView,PostUpdateView,PostDetailView,PostDeleteView,UserPostListView)

urlpatterns = [
    path('',PostListView.as_view(),name='blog_home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('about/',views.about,name='blog_about'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(),name='post-update'),
    path('post/new/', PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete')

    # path('test/',views.home,name='blog_home')
]

