from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=500)
    publish_date=models.DateField(default=date.today)
    publish_datetime=models.DateTimeField(default=timezone.now)
    #author
    #comment
    view=models.IntegerField(default=0)
    photo=models.ImageField()
    content=models.TextField(max_length=10000)
    def __str__(self):
        return self.title
    class Meta:
        ordering=('id',)
        verbose_name = 'article'
        verbose_name_plural = 'articles'