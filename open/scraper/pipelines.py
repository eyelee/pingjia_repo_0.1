from django.db.utils import IntegrityError
from scrapy import log
from scrapy.exceptions import DropItem
from dynamic_scraper.models import SchedulerRuntime
from open.scraper.spiders import ProductSpider
from open.base import process_date
#from open.models import ArticleItem
#from dynamic_scraper.pipelines import ImagesPipeline
#from dynamic_scraper.pipelines import DjangoImagesPipeline

class DjangoWriterPipeline(object):
    
    def process_item(self, item, spider):
        
        if isinstance(spider,ProductSpider):
            #spider.log("spider: " + spider.name)
            spider.log("item time is: " + item['time'])
            item['time']=process_date(item['time'])
            # to do:
            # drop item if price is null
            # drop item if time > no            
        try:
            #if (item == ArticleItem):
                #item['news_website'] = spider.ref_object
            #else:
            item['source'] = spider.ref_object
            
            checker_rt = SchedulerRuntime(runtime_type='C')
            checker_rt.save()
            item['checker_runtime'] = checker_rt
            
            item.save()
            spider.action_successful = True
            spider.log("Item saved.", log.INFO)           
                
        except IntegrityError, e:
            spider.log(str(e), log.ERROR)
            raise DropItem("Missing attribute.")
                
        return item