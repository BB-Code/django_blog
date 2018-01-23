from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=100)
	category = models.CharField(max_length=50,blank=True)
	date_time = models.DateField(auto_now_add =True)
	content = models.TextField(blank=True,null=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-date_time']

	def get_absolute_url(self):
		path = reverse('detail',kwargs={'id':self.id})
		return "http://localhost:8000%s" %path

	def __str__(self):
		return self.title
		
	class Meta:
		ordering = ['-date_time']