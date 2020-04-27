from django.shortcuts import render
from .forms import PostForm
from django.utils import timezone
from .models import Post
from django.shortcuts import redirect
from django.http import HttpResponse

def about(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_list(request):
    search = request.GET.get('search')

    if search:
        posts = Post.objects.filter(title__icontains=search)
    else:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post', post})
# Create your views here.

@login_required