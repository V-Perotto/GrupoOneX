from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/post_list.html', {'posts': posts})
# Create your views here.
<<<<<<< HEAD
# Arthur
=======
# Loraine
>>>>>>> c33eb7f5314650b04be6348e7dbd3cd56ca34b7a
