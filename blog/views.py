from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from django.views.generic import ListView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import  Post
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.shortcuts import get_list_or_404, get_object_or_404

def home(request):
    Title = "Home"
    context={
        'posts': Post.objects.all(),
        'Title':Title
    }
    return render(request,'blog/Home.html',context)

def about(request):
    Title="about"
    return render(request,'blog/about.html',{"Title":Title})



class PostListView(ListView):
    model= Post
    template_name= 'blog/Home.html'
    context_object_name  = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4

class UserPostListView(ListView):
    model= Post
    template_name= 'blog/Home.html'
    context_object_name  = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model= Post


    # ordering = ['-date_posted']
class PostCreateView(CreateView):
    model= Post
    fields = ['title','image']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'image']

    def form_valid(self, form):

        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model= Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

