# coding: utf-8
from django.db import models
from django.contrib.auth.models import User #内置的应用
from django.urls import reverse
# Create your models here.
class Category(models.Model):
	"""分类"""
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Tag(models.Model):
	"""标签 """
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Post(models.Model):
	"""文章"""
	title = models.CharField(max_length=70)#标题
	content = models.TextField()#文章内容
	create_time = models.DateTimeField()#创建时间
	modified_time = models.DateTimeField()#最后修改时间
	excerpt = models.CharField(max_length=200,blank=True)#文章摘要
	category = models.ForeignKey(Category)#ForeignKey，即一对多的关联关系
	tags = models.ManyToManyField(Tag,blank=True)#ManyToManyField，表明这是多对多的关联关系
	author = models.ForeignKey(User)#
	def __str__(self):
		return self.title
	# 自定义 get_absolute_url 方法
	def get_absolute_url(self):
		return reverse('blog:detail',kwargs={'pk':self.pk}) #注意是冒号