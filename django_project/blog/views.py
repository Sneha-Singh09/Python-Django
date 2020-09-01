from django.shortcuts import render,get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.models import User
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# dummy data
'''posts=[
    {
        'author':'SNEHA SINGH',
        'title':'DJANGO',
        'content':'I finally started this project',
        'date_of_post':'3rd may'
    },
     {
        'author':'AUASS',
        'title':'STARTUP',
        'content':'Think about it',
        'date_of_post':'23rd may'
    }
]'''

#home func will handle the traffic from our home page blog
#it will take the request arg,even if we don't use request we need to add it in order for our home func to work
#and within the func we will return what the user has to see when they are sent to this route
def home(request):
    context={ 
        'posts': Post.objects.all() 
    }
    return render(request,'blog/home.html',context)
class PostListView(ListView):
    model=Post
    template_name='blog/home.html'  #<app>/<model>_<viewtype>.html
    context_object_name= 'posts'
    ordering=['-date_of_post'] #minus sign is given so that the post are seen from new to old
    paginate_by=5
class UserPostListView(ListView):
    model=Post
    template_name='blog/user_posts.html'  #<app>/<model>_<viewtype>.html
    context_object_name= 'posts'
    paginate_by=5
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_of_post')

# now this view manages detail of each post, 
# and we write this code by sticking to conventions so the code becomes shorter,doing it by another method
# not giving the template name instead creating the new template
class PostDetailView(DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    # added this to redirct directly to home page--success_url= reverse_lazy('blog-home')
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
    success_url='/'

def about(request):
    return render(request,'blog/about.html',{'title':'about'})
