#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from models import Category,Product,By_year,By_model
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponseServerError, HttpResponse
from django.utils import simplejson
from django.shortcuts import render_to_response
from function import Average,Normalprice
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt


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
                    values.append(item.name)
            if len(categories)<10:
                if len(categories)==0:
                    deepquery=Category.objects
                    for item in kws:
                        deepquery=deepquery.filter(keywords__icontains=item)
                    parent_slug=deepquery[0].parent
                    parent_item=Category.objects.filter(slug=parent_slug)[0]
                    if parent_item:
                        parent_name=parent_item.name+' '
                    for item in deepquery:
                        values.append(parent_name+item.name)
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
                        values.append(parent_name+item.name)
            values=values[0:10]            
            to_return["values"]=values
            success=True
        else:
            to_return['msg'] = u"Requires keywords"
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
                        categories=categories.filter(keywords__icontains=item) 
                    if len(categories)>1:
                        pass
                    elif len(categories)==1:
                        if categories[0].parent:
                           products_data=By_year.objects.filter(brand_slug=categories[0].parent,model_slug=categories[0].slug)[0]
                           if products_data:
                              products=Product.objects.filter(brand_slug=products_data.brand_slug,model_slug=products_data.model_slug,year=products_data.year).order_by('-time')[0:50]
                              products_dict=[]
                              for item in products: 
                                  product=model_to_dict(item)
                                  products_dict.append(product)
                              products=products_dict
                              excerpt_products= products[0:5]
                              if products:
                                  return render_to_response("search.html",locals())
                              else:
                                  return render_to_response("nothingfound.html",locals())
                           else:
                              return render_to_response("nothingfound.html",locals()) 
                        else:
                           pass
                    else:     
                        return render_to_response("nothingfound.html",locals())      
                else:
                    return render_to_response("nothingfound.html",locals())
            else:
                return HttpResponseRedirect('/')
            
        
