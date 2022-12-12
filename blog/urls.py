from django.urls import path
from . import views
from .views import PostsListView,PostsDetailView,PostsCreateView, PostsUpdateView, PostsDeleteView, UserPostsListView

urlpatterns = [

    path('', PostsListView.as_view(), name='blog-home'),
    path('user/<username>', UserPostsListView.as_view(), name='user-posts'),
    path('posts/<int:pk>/', PostsDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostsCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/update/', PostsUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/Delete/', PostsDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]
