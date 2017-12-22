from django.shortcuts import render,get_object_or_404
from .models import Post
import markdown
# Create your views here.

def index(request):
    post_list = Post.objects.all().order_by('-create_time')#- 号表示逆序，如果不加 - 则是正序
    return render(request, 'blog/index.html', context={'post_list': post_list})
#安装markdown Pygments 引入样式文件blog\static\blog\css\highlights\...
def detail(request,pk):
	post = get_object_or_404(Post,pk=pk)
	post.content =  markdown.markdown(post.content,extensions=['markdown.extensions.extra',
																'markdown.extensions.codehilite',
																'markdown.extensions.toc',])
	return render(request,'blog/detail.html',context={'post':post})
