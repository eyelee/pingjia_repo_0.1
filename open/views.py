#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import urllib
import urllib2
from models import Category,Product,By_year,By_model,City
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponseServerError, HttpResponse
from django.utils import simplejson
from django.shortcuts import render_to_response
from function import Average,Normalprice,Normaltime
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt

def index(request,name):
    return render_to_response('index.html',locals())
    
@csrf_exempt
def ajax_match(request):
    success = False
    to_return = {'msg':u'No POST data sent.' }
    if request.method == "POST":
        post = request.POST.copy()
        if post.has_key('kw'):
            kw = post['kw'].strip()
            kws=re.split(r'\s+',kw)
            values=[]
            categories=Category.objects.filter(parent=None)
            for item in kws:
                categories=categories.filter(keywords__icontains=item)
            categories=categories[0:10]
            if categories:
                for item in categories:
                    only_brand={}
                    only_brand['name']=item.name
                    only_brand['url']='/cars/'+item.slug+'/'
                    values.append(only_brand)
            if len(categories)<10:
                if len(categories)==0:
                    deepquery=Category.objects
                    for item in kws:
                        deepquery=deepquery.filter(keywords__icontains=item)
                    if deepquery:
                        parent_slug=deepquery[0].parent
                        parent_item=Category.objects.filter(slug=parent_slug)[0]
                        if parent_item:
                            parent_name=parent_item.name+' '
                        for item in deepquery:
                            to_model={}
                            to_model['name']=parent_name+item.name
                            to_model['url']='/cars/'+item.parent+'/'+item.slug+'/'
                            values.append(to_model)
                        if len(deepquery)<10:
                            categories=Category.objects.filter(parent=parent_slug)
                            for item in deepquery:
                                categories=categories.exclude(id=item.id)
                            categories=categories[0:10]         
                else:
                    deepquery=Category.objects
                    for item in kws:
                        deepquery=deepquery.filter(keywords__icontains=item)
                    deepquery=deepquery.order_by('parent')[0]
                    parent_slug=deepquery.slug
                    parent_name=deepquery.name+' '
                    categories=Category.objects.filter(parent=parent_slug)[0:10]
                if categories:
                    for item in categories:
                        to_model={}
                        to_model['name']=parent_name+item.name
                        to_model['url']='/cars/'+item.parent+'/'+item.slug+'/'
                        values.append(to_model)
            values=values[0:10]            
            to_return["values"]=values
            success=True
        else:
            to_return['msg'] = u"Require keywords"
    serialized = simplejson.dumps(to_return)
    if success == True:
        return HttpResponse(serialized, mimetype="application/json")
    else:
        return HttpResponseServerError(serialized, mimetype="application/json")
    
def search(request):
    if request.method=="GET":
        get=request.GET.copy()
        if get.has_key("kw"):
            kw=get['kw'].strip()
            if kw:
                kws=re.split(r'\s+',kw)
                #kws=re.split(r'[^\w\x80-\xff]+',kw),需要更有效的分割方式，剔除标点符号等无意义的符号
                kws=list(set(kws))
                if kws.count(''):
                    kws.remove('')
                if kws:
                    categories=Category.objects
                    for item in kws:
                        categories=categories.filter(keywords__icontains=item).order_by('slug')
                    if not categories:
                        return render_to_response("nothingfound.html",locals()) 
                    brand_categories=categories.filter(parent=None) 
                    if brand_categories:
                        brandinfo=brand_categories[0]
                        return HttpResponseRedirect('/cars/'+brandinfo.slug+'/')
                    else:
                        products_data=By_year.objects.filter(brand_slug=categories[0].parent,model_slug=categories[0].slug).order_by('year')
                        if products_data:
                           products_data_default=products_data.filter(year='2010')
                           if products_data_default:
                              products_data_default=products_data_default[0]
                           else:
                              products_data_default=products_data[len(products_data)-1] 
                           brandcate=Category.objects.filter(slug=products_data_default.brand_slug,parent=None)[0]
                           modeltype=Category.objects.filter(slug=products_data_default.model_slug,parent=products_data_default.brand_slug)[0]                      
                           products_daily=By_model.objects.filter(brand_slug=products_data_default.brand_slug,model_slug=products_data_default.model_slug,year=products_data_default.year).order_by('-date')[0:30]
                           products=Product.objects.filter(brand_slug=products_data_default.brand_slug,model_slug=products_data_default.model_slug,year=products_data_default.year).order_by('-time')[0:50]  
                           excerpt_products= products[0:5]
                           if products and products_daily:
                              return render_to_response("search.html",locals())
                           else:
                              return render_to_response("nothingfound.html",locals())
                        else:
                           return render_to_response("nothingfound.html",locals())     
                else:
                    return render_to_response("nothingfound.html",locals())
            else:
                return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
            
def accurate_products(request,brand_slug=None,model_slug=None,year=None): 
       if brand_slug and model_slug:
           products_data=By_year.objects.filter(brand_slug=brand_slug,model_slug=model_slug).order_by('year')
           if products_data:
              brandcate=Category.objects.filter(slug=brand_slug,parent=None)[0]
              brandcate={'brand_name':brandcate.name,'url':'/cars/'+brand_slug+'/'}
              modeltype=Category.objects.filter(slug=model_slug,parent=brand_slug)[0] 
              modeltype={'model_name':modeltype.name,'url':'/cars/'+brand_slug+'/'+model_slug+'/'}
              if year:
                 products_data_default=products_data.filter(year=year)
                 if not products_data_default:
                    return render_to_response("nothingfound.html",locals())
                 products_data_default=products_data_default[0]
                 yeartime={'year':year,'url':'/cars/'+brand_slug+'/'+model_slug+'/'+year+'/'}
              else:
                 products_data_default=products_data.filter(year='2010')
                 if products_data_default:
                    products_data_default=products_data_default[0]
                 else:
                    products_data_default=products_data[len(products_data)-1]
                 yeartime={'year':products_data_default.year,'url':'/cars/'+brand_slug+'/'+model_slug+'/'+str(products_data_default.year)+'/'}                    
              products_daily=By_model.objects.filter(brand_slug=products_data_default.brand_slug,model_slug=products_data_default.model_slug,year=products_data_default.year).order_by('-date')[0:30]
              products=Product.objects.filter(brand_slug=products_data_default.brand_slug,model_slug=products_data_default.model_slug,year=products_data_default.year).order_by('-time')[0:50]  
              excerpt_products= products[0:5]
              if products and products_daily:
                 return render_to_response("search.html",locals())
              else:
                 return render_to_response("nothingfound.html",locals())
           else:
              return render_to_response("nothingfound.html",locals()) 
       else:
           return render_to_response("nothingfound.html",locals())

def guids(request):
    letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    brands_infos=[]
    for item in letters:
        brands_info={}
        brands=Category.objects.filter(slug__istartswith=item,parent=None)
        if len(brands)%4==0:
           num=len(brands)/4
        else:
           num=int(len(brands)/4)+1    
        j=0
        k=4
        temps=[]
        for i in range(num):
           temp=brands[j:k]
           temps.append(temp)
           j=j+4
           k=k+4 
        brands_info['letter']=item
        brands_info['brands']=temps
        brands_infos.append(brands_info)
    return render_to_response("guids.html",locals())   

def brand_models(request,brand_slug):
    if brand_slug:
        brandinfo=Category.objects.filter(slug=brand_slug)
        modeltypes=Category.objects.filter(parent=brand_slug)
        if not modeltypes or not brandinfo:
            return render_to_response("nothingfound.html",locals())
        brandinfo=brandinfo[0]
        if len(modeltypes)%4==0:
           num=len(modeltypes)/4
        else:
           num=int(len(modeltypes)/4)+1    
        j=0
        k=4
        temps=[]
        for i in range(num):
           temp=modeltypes[j:k]
           temps.append(temp)
           j=j+4
           k=k+4
        modeltypes=temps  
        return render_to_response("brand_models.html",locals())
    else:
        return render_to_response("nothingfound.html",locals())    

@csrf_exempt
def ajax_image(request):
    """
    about google image api,please look up form
    https://developers.google.com/image-search/v1/jsondevguide?hl=zh-CN#json_snippets_python
    """
    success = False    
    to_return = {'msg':u'No POST data sent.' }
    if request.method =='POST':
       post=request.POST.copy()
       if post.has_key('kw'):
          query={}
          query['q']=post['kw'].encode("utf8")
          query['imgsz']='xlarge'
          query['rsz']='8'
          query['v']='1.0'
          query_str=urllib.urlencode(query)
          url ='https://ajax.googleapis.com/ajax/services/search/images?'+query_str
          request_http = urllib2.Request(url)
          response = urllib2.urlopen(request_http)
          # Process the JSON string.
          data_return = simplejson.load(response)
          # now have some fun with the results...
          pic=data_return['responseData']['results']
          values=[]
          for item in pic:
              try:
                  pic_response = urllib2.urlopen(urllib2.Request(item['url'])) 
              except:
                  continue 
              else:
                  values.append(item['url'])
              if len(values)>3:
                  break  
          to_return['values']=values   
          success=True
       else:
          to_return={'msg':u'Require keywords'}    
          
    serialized = simplejson.dumps(to_return)
    if success:
       return HttpResponse(serialized, mimetype="application/json")  
    else:
       return HttpResponseServerError(serialized, mimetype="application/json")
   
@csrf_exempt
def ajax_search_city(request):
    success = False
    to_return = {'msg':u'No POST data sent.' }
    if request.method == "POST":
        post = request.POST.copy()
        if post.has_key('citykw'):
           citykw=post['citykw']
           if post.has_key('searchtype'):
               city=City.objects.filter(name=citykw).exclude(parent=0)
           else:    
               city=City.objects.filter(Q(name__startswith=citykw)|Q(pinyin__istartswith=citykw)|Q(quhao=citykw)).exclude(parent=0)
           values=[]
           for item in city:
               values.append(item.name)
           to_return['values']=values
           success=True
        else:
           to_return['msg']='Require keywords'
    serialized = simplejson.dumps(to_return)
    if success == True:
        return HttpResponse(serialized, mimetype="application/json")
    else:
        return HttpResponseServerError(serialized, mimetype="application/json")
           

@csrf_exempt        
def ajax_city_filter(request):
    success = False
    to_return = {'msg':u'No POST data sent.' }
    if request.method == "POST":
        post = request.POST.copy()
        if post.has_key('brandslug') and post.has_key('modelslug') and post.has_key('year') and post.has_key('citykw'):
           if post['citykw']:
               products=Product.objects.filter(brand_slug=post['brandslug'],model_slug=post['modelslug'],year=post['year'],city=post['citykw']).order_by('-time')[0:50]
           else:
               products=Product.objects.filter(brand_slug=post['brandslug'],model_slug=post['modelslug'],year=post['year']).order_by('-time')[0:50]    
           values=[]
           for item in products:
               product={}
               product['title']=item.title
               product['url']=item.url
               product['price']=Normalprice(item.price)
               product['place']=item.city
               if item.region:
                  product['place']=item.city+'.'+item.region
               product['time']=Normaltime(item.time)
               values.append(product)
           to_return['values']=values
           success=True
        else:
           to_return['msg']='Not enough conditions for search.'      
    serialized = simplejson.dumps(to_return)
    if success == True:
        return HttpResponse(serialized, mimetype="application/json")
    else:
        return HttpResponseServerError(serialized, mimetype="application/json")
 
           
def testgoogleapi(request):
    return render_to_response('testgoogleapi.html')