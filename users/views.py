from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import ListView,DeleteView,DetailView
from .forms import  UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.models import User
from blog.models import  Post
from django.core.paginator import Paginator
# Create your views here.
def register(request):
    if(request.method=='POST'):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Your account has been Created as user {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})


class PostListbyUser(ListView):
    paginate_by = 2
    model = Post

class UserPostListView(ListView):
    model= Post
    template_name= 'users/Profile.html'
    context_object_name  = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

@login_required
def get_queryset(request):
    user = request.user
    Post_list = Post.objects.filter(author=user).order_by('-date_posted')
    paginator = Paginator(Post_list, 2)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj



@login_required
def profile(request):
    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,
                                 instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated as {request.user.username}')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context= {
            'u_form': u_form,
            'p_form': p_form,
            'posts':  get_queryset(request)
    }
    return render(request,'users/profile.html',context)


