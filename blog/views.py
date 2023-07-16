from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    p=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print(p)
    return render(request, 'blog/post_list.html', {'posts':p})



# Create your views here.
