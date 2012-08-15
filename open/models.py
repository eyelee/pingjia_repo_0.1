# coding=UTF-8
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from scrapy.contrib_exp.djangoitem import DjangoItem
from dynamic_scraper.models import Scraper, SchedulerRuntime

"""
    Source为搜索爬虫用来抓取数据url来源，一般通过url里含有的品牌 brand，城市city_slug，或者产品类别(cat_slug)等特征信息构建出来
"""
class Source(models.Model):
    name = models.CharField(max_length=32)
    #url = models.URLField()
    url = models.CharField(max_length=50)
    brand = models.CharField(max_length=32,null=True,blank=True)
    city_slug = models.CharField(max_length=32,null=True,blank=True)
    cat_slug = models.CharField(max_length=32,null=True,blank=True)
    #model = models.CharField(max_length=50,null=True,blank=True)
    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
    scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)
    
    def __unicode__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    source = models.ForeignKey(Source,null=True) 
    description = models.TextField(blank=True)
    url = models.URLField()
    thumbnail = models.CharField(max_length=200,null=True,blank=True)
    checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)
    
    def __unicode__(self):
        return self.title
    

class Product(models.Model):
    source = models.ForeignKey(Source) 
    title = models.CharField(max_length=200,blank=True, null=True)
    meta = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True,default=0)
    url = models.URLField()
    #time = models.CharField(max_length=100,blank=True, null=True)
    ### car details
    time = models.DateTimeField(blank=True, null=True)
    mile = models.DecimalField(max_digits=5, decimal_places=2,blank=True, null=True)
    volume = models.DecimalField(max_digits=5, decimal_places=2,blank=True, null=True)
    color = models.CharField(max_length=32,blank=True, null=True)
    # control = (手动,自动,手自一体)
    control = models.CharField(max_length=32,blank=True, null=True)
    ### car details end
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    brand_slug = models.CharField(max_length=32,blank=True, null=True)
    model_slug = models.CharField(max_length=32,blank=True, null=True)
    city = models.CharField(max_length=50,blank=True, null=True)
    city_slug = models.CharField(max_length=32,blank=True, null=True)
    region = models.CharField(max_length=50,blank=True, null=True)
    region_slug = models.CharField(max_length=32,blank=True, null=True)
    thumbnail = models.CharField(max_length=200,null=True,blank=True)
    checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)
    
    def __unicode__(self):
        return self.title
    
class Catype(models.Model):
    name = models.CharField(max_length=50)
    slug_cn = models.CharField(max_length=32)
    slug_en = models.CharField(max_length=32)
    def __unicode__(self):
        return self.name

class Category(models.Model):
    source = models.ForeignKey(Source)
    name = models.CharField(max_length=50,blank=True, null=True)
    slug = models.CharField(max_length=32, blank=True, null=True)
    url = models.URLField()
    parent = models.CharField(max_length=32,default='N',blank=True,null=True)
    #type = models.ForeignKey(Catype)
    #type_slug = models.CharField(max_length=32,default ='car',blank=True, null=True)
    checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)  
    def __unicode__(self):
        return self.slug
    
class City(models.Model):
    source = models.ForeignKey(Source)
    name = models.CharField(max_length=50,blank=True, null=True)
    slug = models.CharField(max_length=32, blank=True, null=True)
    url = models.URLField()
    parent = models.CharField(max_length=50,default='N',blank=True,null=True)
    checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)  
    def __unicode__(self):
        return self.slug
    
class ArticleItem(DjangoItem):
    django_model = Article

class ProductItem(DjangoItem):
    django_model = Product
    
class CategoryItem(DjangoItem):
    django_model = Category
     
class CityItem(DjangoItem):
    django_model = City

@receiver(pre_delete)
def pre_delete_handler(sender, instance, using, **kwargs):
    if isinstance(instance, Source):
        if instance.scraper_runtime:
            instance.scraper_runtime.delete()
    
    if isinstance(instance, Article):
        if instance.checker_runtime:
            instance.checker_runtime.delete()
            
pre_delete.connect(pre_delete_handler)