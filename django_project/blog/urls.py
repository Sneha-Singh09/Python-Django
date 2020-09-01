#we will map the urls to eachview func 
from django.urls import path
from .import views 
from .views import (
                    PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView,
)
urlpatterns = [
    #when we open the page then we would be directed to views.home func in which we have returned httpresponse which will be shown
    #this would work only if we map it in main urls that is under django_project
    #we replace views.home by postlistview, we add .as_view() since it is a class and we need to convert it into a view
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    #we made a variable int is the datatype and pk-primary key of the post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]
