from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from .models import Comment
from .forms import CommentForm


# Create your views here.
def post_comment(request,post_pk):
	post = get_object_or_404(Post,pk=post_pk)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		# 当调用 form.is_valid() 方法时，Django 自动帮我们检查表单的数据是否符合格式要求。
		if form.is_valid():
			# commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
			comment = form.save(commit=False)
			comment.post = post
			comment.save()# 最终将评论数据保存进数据库，调用模型实例的 save 方法
			return redirect(post)
		else:
			comment_list = post.comment_set.all()#post.comment_set.all()也等价于 Comment.objects.filter(post=post)
			context={'post':post,'form':form,'comment_list':comment_list}
			return render(request,'blog/detail.html',context=context)
	return redirect(post)



