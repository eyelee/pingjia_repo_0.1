from dynamic_scraper.spiders.django_spider import DjangoSpider
from open.models import Source, Article, ArticleItem,Product,ProductItem,Category,CategoryItem
from open.models import City, CityItem
from open.base import urls_from_brand, urls_from_priority
from scrapy.contrib.loader.processor import Join,TakeFirst
from scrapy.contrib.loader import XPathItemLoader
from dynamic_scraper.utils import processors
from scrapy import log



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


class ProductLoader(XPathItemLoader):
    #default_output_processor = TakeFirst()
    #url_out=TakeFirst()
    imgurls_out= Join()
    #imgurls_in = Join()
        
class ProductSpider(DjangoSpider):
    
    name = 'product_spider'
    brand = None
    #maker = None
    priority = None
    #defalut_processor = Join()
    
      
    def __init__(self, *args, **kwargs):
        #the following is to set mandatory Vars for DjangoBaseSpider class
        self._set_ref_object(Source, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        #self.scrape_url = 'ganji.com'
        #self.brand ='ford'
        self.brand=self.ref_object.brand
        self.priority=self.ref_object.priority
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = Product
        self.scraped_obj_item_class = ProductItem
        super(ProductSpider, self).__init__(self, *args, **kwargs)          

    def _set_start_urls(self, brand):   
        #generate start_urls based on city urls and prioriy, no pagination needed
        if not self.brand:
            self.scraper.pagination_type = 'N'
            self.start_urls = urls_from_priority(self.scrape_url,self.priority)
        #generate start_urls by calling parent's _set_start_urls,in which pagination will be used.
        else:
            scrape_urls = urls_from_brand(self.scrape_url,self.brand)
            for url in scrape_urls:
                super(ProductSpider, self)._set_start_urls(url)
                
    def _get_processors(self, scraper_elem):
        if (scraper_elem.scraped_obj_attr.name =='imgurls'):
            procs = [Join(), processors.string_strip,]
        else:
            procs = [TakeFirst(), processors.string_strip,]
        
        procs_str = scraper_elem.processors    
        if not procs_str:
            return procs
        procs_tmp = list(procs_str.split(','))
        for p in procs_tmp:
            p = p.strip()
            if hasattr(processors, p):
                procs.append(getattr(processors, p))
            else:
                self.log("Processor '%s' is not defined!" % p, log.ERROR)
        procs = tuple(procs)
        return procs


    def _scrape_item_attr(self, scraper_elem):
        if(self.from_detail_page == scraper_elem.from_detail_page):
            #procs = self._get_processors(scraper_elem.processors)
            procs = self._get_processors(scraper_elem)
            self._set_loader_context(scraper_elem.proc_ctxt)
            
            static_ctxt = self.loader.context.get('static', '')
            if processors.static in procs and static_ctxt:
                self.loader.add_value(scraper_elem.scraped_obj_attr.name, static_ctxt)
            elif(scraper_elem.reg_exp):
                self.loader.add_xpath(scraper_elem.scraped_obj_attr.name, scraper_elem.x_path, *procs,  re=scraper_elem.reg_exp)
            else:
                self.loader.add_xpath(scraper_elem.scraped_obj_attr.name, scraper_elem.x_path, *procs)
            msg  = '{0: <20}'.format(scraper_elem.scraped_obj_attr.name)
            c_values = self.loader.get_collected_values(scraper_elem.scraped_obj_attr.name)
            if len(c_values) > 0:
                msg += "'" + c_values[0] + "'"
            else:
                msg += u'None'
            self.log(msg, log.DEBUG)
            
'''            
    def _set_loader(self, response, xs, item):
        if not xs:
            self.from_detail_page = True
            item = response.request.meta['item']
            self.loader = ProductLoader(item=ProductItem(), response=response)
            #self.loader = ProductLoader(item=item, response=response)
            self.loader.default_output_processor = TakeFirst()
        else:
            self.from_detail_page = False
            self.loader = ProductLoader(item=ProductItem(), selector=xs)
            #self.loader = ProductLoader(item=item, response=response)
            self.loader.default_output_processor = TakeFirst()
'''
        
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
        
        

        