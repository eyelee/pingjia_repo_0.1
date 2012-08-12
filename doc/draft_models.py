from django.db import models


class Category(models.Model):
    """ 现有Category应改为Brand
                           存储分类如：交通工具，汽车，自行车。
                           汽车，自行车。parent_id=交通工具。ID
                          交通工具。parent_id=0
       slug为英文，如 name=汽车，slug=cars                  
    """
    name=models.CharField()
    slug=models.CharField()
    parent_id=models.IntegerField()
    
    
class Brand(models.Model):
    """ 等同于现有的Category
        category为外键，关联到Catogory模型的ID
        slug为英文或拼音，name=宝马，slug=bmw；name=大众 ，slug=dazhong.
        description为品牌描述
    """
    category=models.ForeignKey(Category)
    name=models.CharField()
    slug=models.CharField()
    description=models.TextField()
  
class City(models.Model):
    """沿用现有的city
       parent_id和Category功能一样，体现 '市-区（县）'的关系，
    """
    name=models.CharField()
    slug=models.CharField()
    parent_id=models.IntegerField()

class Modeltype(models.Model):
    """ 产品型号模型
                          关联到一个品牌
    """
    name=models.CharField()
    brand=models.ForeignKey(Brand)
    
class Productiondate(models.Model):
    """产品生产日期或二手货的购入日期
                      关联到一个品牌，即把生产日期当成像型号一样的属性
                    品牌，型号，生产日期 作为一个整体决定产品到底是个什么东西               
    """
    time=models.CharField()
    brand=models.ForeignKey(Brand)
    
class Product(models.Model):
    """ 沿用，若能更名为Deal最好，因为叫交易信息模型更合适，产品模型的名字更适合下面的中间表
                           增加外键，关暖到'品牌-型号-生产日期'模型
    """
    productinfo=models.ForeignKey(Productinfo)
    
    
      
############################中间表模型开始#################################    
class Product_info(models.Model):
    """ 这个是最重要的模型  
        '品牌-型号-生产日期'模型，用于快速反馈一种产品的均价，价格范围
                             基于现有Product的数据计算 均价，价格范围，交易信息的数量。
    """
    brand=models.ForeignKey(Brand)
    brand_name=model.CharField()
    brand_slug=model.CharField()
    modeltype=models.ForeignKey(Modeltype)
    modeltype_name=model.CharField()
    Productiondate=models.ForeignKey(Productiondate)
    Productiondate_time=model.CharField()
    category=models.ForeignKey(Category)
    category_name=model.CharField()
    category_slug=model.CharField()
    averageprice=models.DecimalField()
    pricerange=model.CharField()
    #价格范围可以改为两个字段存，一个存下限一个存上限
    count=models.IntegerField()
    
class Brand_count(models.Model):
    """
              某品牌所有产品的交易信息数量，可基于Productinfo生成，用到其中的count属性
    """  
    brand=models.ForeignKey(Brand)
    brand_name=model.CharField()
    brand_slug=model.CharField()
    category=models.ForeignKey(Category)
    category_name=model.CharField()
    category_slug=model.CharField()
    count=models.IntegerField()
    
class Brand_city_count(models.Model):
    """某品牌在某地的交易信息数量，用于展示某品牌最popular的地方，
    """
    brand=models.ForeignKey(Brand)
    brand_name=model.CharField()
    brand_slug=model.CharField()
    city=models.ForeignKey(City)
    city_name=model.CharField()
    city_slug=model.CharField()
    #目前这里是只需要具体到市的，如果要具体到县区，或是前面增加省，则增加字段。
    count=count=models.IntegerField()
    
class Prodcut_time_price(models.Model):
    """time的最小单位为天，处理后最小单位为‘日’
       price则为某产品，在某天发布的所有交易信息中的平均价格
                       这里的产品即为'品牌-型号-生产日期'，基于Productinfo,可从现有product模型生成，相当于对Product进行了
       select time，AVG(price) from open_product group by parent_id，time
    """
    time=models.DateTimeField()
    price=models.DecimalField()
    productinfo=models.ForeignKey(Productinfo)