from django.contrib import admin
from . import models
# Register your models here.
class FormAdmin(admin.ModelAdmin):
    list_display=['id','title','publish_date','publish_datetime','view']
    list_filter=['publish_date','publish_datetime']
    search_fields=['title','content']
    date_herriority='publish_date'
admin.site.register(models.Post,FormAdmin)