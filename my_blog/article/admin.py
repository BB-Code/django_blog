from django.contrib import admin
from .models import Article
# Register your models here.

# class ArticleAdmin(admin.ModelAdmin):
# 	list_display =['title','cartegory','date_time']

admin.site.register(Article)