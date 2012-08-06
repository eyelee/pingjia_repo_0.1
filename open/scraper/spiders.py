from dynamic_scraper.spiders.django_spider import DjangoSpider
from open.models import Source, Article, ArticleItem,Product,ProductItem,Category,CategoryItem
from open.models import City, CityItem
from open.base import urls_from_brand


class ArticleSpider(DjangoSpider):
    
    name = 'article_spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(Source, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = Article
        self.scraped_obj_item_class = ArticleItem
        super(ArticleSpider, self).__init__(self, *args, **kwargs)

        
class ProductSpider(DjangoSpider):
    
    name = 'product_spider'
    brand = None
    #maker = None
    model = None
      
    def __init__(self, *args, **kwargs):
        #the following is to set mandatory Vars for DjangoBaseSpider class
        self._set_ref_object(Source, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        #self.scrape_url = 'ganji.com'
        #self.brand ='ford'
        self.brand=self.ref_object.brand
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = Product
        self.scraped_obj_item_class = ProductItem
        super(ProductSpider, self).__init__(self, *args, **kwargs)          

    def _set_start_urls(self, brand):   
        #generate scraper_urls based on category 
        scrape_urls = urls_from_brand(self.scrape_url,self.brand)
        for url in scrape_urls:
            super(ProductSpider, self)._set_start_urls(url)
"""   
"""
        
class CategorySpider(DjangoSpider):
    
    name = 'category_spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(Source, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = Category
        self.scraped_obj_item_class = CategoryItem
        super(CategorySpider, self).__init__(self, *args, **kwargs)

class CitySpider(DjangoSpider):
    
    name = 'city_spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(Source, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = City
        self.scraped_obj_item_class = CityItem
        super(CitySpider, self).__init__(self, *args, **kwargs)
        
        

        