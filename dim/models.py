# coding=UTF-8
from django.db import models
#from open import models

##################  维度表模型, 现阶段暂不使用  ################## 
class Catype(models.Model):
    name = models.CharField(max_length=50)
    slug_cn = models.CharField(max_length=32)
    slug_en = models.CharField(max_length=32)
    def __unicode__(self):
        return self.name

class Brand(models.Model):
    type = models.ForeignKey(Catype)
    name = models.CharField(max_length=50,blank=True, null=True)
    slug = models.CharField(max_length=32, blank=True, null=True)
    url = models.URLField()
    parent = models.CharField(max_length=32,default='N',blank=True,null=True)
    def __unicode__(self):
        return self.name
    
# Source定义了数据来源，每一个Spider程序抓取数据时候必须用到，一个数据来源往往针对URL中包含的city或者brand参数    
# the source name is decoded to siteCode_typeCode_[Brand/City]slug 
class Source(models.Model):
    src_slug = models.CharField(max_length=32)
    src_type = models.IntegerField()
    domain = models.CharField(max_length=50)
    url = models.URLField()
    def __unicode__(self):
        return self.url
##################  维度表模型 end.  ################## 

##################  fact 表模型  #####################    
class Prod_fact(models.Model):
    """ 
        抽象统计的普遍模型,每天统计当天新发布的同一型号产品的均价和数量
    """  
    # date: to aggregate the product in the same day. <-- group by open_product.time
    date = models.DateField(blank=True, null=True) 
    # 日均价
    avg_price = models.DecimalField(max_digits=10, decimal_places=1,blank=True, null=True)
    # 当日发布量
    units = models.IntegerField(blank=True,default=0)
    class Meta:
        abstract = True

class By_model(Prod_fact):
    """ 
       group by city，品牌，型号，Year
    """  
    year = models.IntegerField(blank=True,default=0)
    brand_slug = models.CharField(max_length=32,blank=True, null=True)
    model_slug = models.CharField(max_length=32,blank=True, null=True)
    def __unicode__(self):
        return self.brand_slug+'/'+self.model_slug+'/'+str(self.year)
    
class By_city(Prod_fact):
    # avoid Foreignkey to simplify data loading 
    city_slug = models.CharField(max_length=32,blank=True, null=True)
    brand_slug = models.CharField(max_length=32,blank=True, null=True)
    model_slug = models.CharField(max_length=32,blank=True, null=True)
    def __unicode__(self):
        return self.brand_slug+'/'+self.model_slug+'/'+self.city_slug



