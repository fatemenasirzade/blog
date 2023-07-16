from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

def post_list(request):
    p=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print(p)
    return render(request, 'blog/post_list.html', {'posts':p})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})



# Create your views here.
