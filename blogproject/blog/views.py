from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    post_list = Post.objects.all().order_by('-created_time')#- 号表示逆序，如果不加 - 则是正序
    return render(request, 'blog/index.html', context={'post_list': post_list})
