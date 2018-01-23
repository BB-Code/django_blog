from django.shortcuts import render
from django.views.generic import View
from .models import Article
from datetime import datetime
from django.http import Http404
from django.db.models import Q
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

class HomeView(View):
	def get(self,request):
		article_list = Article.objects.all()
		paginator = Paginator(article_list,2)
		page = request.GET.get('page')
		try:
			article_list = paginator.page(page)
		except PageNotAnInteger:
			article_list = paginator.page(1)
		except EmptyPage:
			article_list = paginator.paginator(paginator.num_pages)
		return render(request,'home.html',{'article_list':article_list})

class DetailView(View):
	def get(self,request,id):
		try:
			article = Article.objects.get(id=str(id))
		except Article.DoesNotExist:
			raise Http404
		return render(request,'detail.html',{'article':article})


class ArchivesView(View):
	def get(self,request):
		try:
			article_list = Article.objects.all()
		except Article.DoesNotExist:
			raise Http404
		return render(request,'archives.html',{'article_list':article_list})

class Search_Tag_View(View):
	def get(self,request,my_tag):
		try:
			article_list = Article.objects.filter(category=my_tag)
		except Article.DoesNotExist:
			raise Http404
		return render(request,'tag.html',{'article_list':article_list})

class SearchView(View):
	def get(self,request):
		kw = request.GET.get('kw')
		if not kw:
			return render(request,'home.html', {'error_msg': error_msg})
		article_list = Article.objects.filter(Q(category__icontains = kw)| Q(title__icontains = kw))
		return render(request,'archives.html',{'article_list':article_list,'error_msg':'请输入关键词'})

class RessView(Feed):
	title = "RSS feed - article"
	link = "feeds/articles/"
	desc = "RSS feed - blog article"

	def items(self):
		return Article.objects.order_by('-date_time')
	def item_title(self,item):
		return item.title
	def item_pudate(self,item):
		return item.date_time
	def item_desc(self,item):
		return item.content


		