from open.models import Category,City
from datetime import date

cityList= City.objects.exclude(parent=0).values()
brandList=Category.objects.filter(parent=None).values()


def urls_from_brand(source=None,brand=None):
    scrap_urls=[]
    for city in cityList:
        url= 'http://'+city['slug'] +'.'+ source +'/'+brand+'/'
        scrap_urls.append(url)     
    return scrap_urls  

def print_urls(source=None,brand=None):
    urls= urls_from_brand(source,brand)
    for url in urls:
        print url
        
def urls_from_priority(source=None,priority=None):
    scrap_urls=[]
    pages=range(1,priority+1)
    for page  in pages:
        url = source+'ershouche/o'+ str(page) + '/'
        scrap_urls.append(url)
    return scrap_urls
        
"""   
        for cat in category 
        if self.scraper.pagination_type != 'N':
            append_str = self.scraper.pagination_append_str
            if scrape_url[-1:] == '/' and append_str[0:1] == '/':
                append_str = append_str[1:]

            for page in pages:
                url = scrape_url + append_str.format(page=page)
                self.start_urls.append(url)
            if not self.scraper.pagination_on_start:
                self.start_urls.append(scrape_url)
        
        if self.scraper.pagination_type == 'N':
            self.start_urls.append(scrape_url)
"""
#def urls_from_city():

def process_date(datestring):
    if len(datestring.split('-')) == 2:
        td=date.today()
    return str(td.year)+'-'+datestring

    
    

