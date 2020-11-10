from django.urls import path
from .views import (PostListView, PostDetailView, PostCreateView,
                    PostUpdateView,
                    PostDeleteView)  #importing class view directly

from . import views  #from current directory import views.py

urlpatterns = [
    # empty path indicates homepage, views.home is the
    # fxn created in views file to get the http response
    # unique name = 'blog-home' to avoid colliding with
    # other app routes
    path('', PostListView.as_view(), name='blog-home'),
    #by convention PostDetailView expects primary key as 'pk' eg. for first post, url will be localhost:8000/post/1
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),
         name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),
         name='post-delete'),
    path('about/', views.about, name='blog-about'),
]
