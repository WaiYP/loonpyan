from _datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from administration.models import LearningPagePicture, AboutPagePicture
from home.custom import ParentChild
from inventory.models import Categories, ProductGroup, ProductSubGroup, Products, Customer, Activities, ActivityGroup, \
    ServiceGroup, Services


def productsmenu():
    productsmenu = []
    productsmenu.clear()
    pgroups = ProductGroup.objects.filter(active=True)
    for pgroup in pgroups:
        psubgrps = ProductSubGroup.objects.select_related().filter(pgroup=pgroup, active=True).order_by('id')
        productsmenu.append(ParentChild(pgroup, psubgrps))
    return  productsmenu

def activitymenu():
    activitymenu = []
    activitymenu.clear()
    agroups = ActivityGroup.objects.filter(active=True)
    for agroup in agroups:
        activities = Activities.objects.select_related().filter(agroup=agroup, active=True).order_by('id')
        activitymenu.append(ParentChild(agroup, activities))
    return  activitymenu

def servicemenu():
    servicemenu = []
    servicemenu.clear()
    sgroups = ServiceGroup.objects.filter(active=True)
    for sgroup in sgroups:
        services = Services.objects.select_related().filter(sgroup=sgroup, active=True).order_by('id')
        servicemenu.append(ParentChild(sgroup, services))
    return  servicemenu

def index(request):
    pics = LearningPagePicture.objects.last()
    actvgroup = ActivityGroup.objects.all()
    p_menu = productsmenu()
    a_menu=activitymenu()
    s_menu = servicemenu()
    servgroup = ServiceGroup.objects.all()
    context = {'pics':pics,
               'prodmenu':p_menu,
               'actmenu':a_menu,
               'sermenu':s_menu,
               'actvgroup':actvgroup,
               'servgroup':servgroup}
    return render(request, 'home/index.html',context)

def about(request):
    pics = LearningPagePicture.objects.last()
    abt = AboutPagePicture.objects.last()
    actvgroup = ActivityGroup.objects.all()
    p_menu = productsmenu()
    a_menu = activitymenu()
    s_menu = servicemenu()
    servgroup = ServiceGroup.objects.all()
    context = {'abt':abt,
               'pics':pics,
               'prodmenu':p_menu,
               'sermenu':s_menu,
               'actmenu':a_menu,
               'actvgroup':actvgroup,
               'servgroup':servgroup}
    return  render(request,'home/about.html',context)

def product(request,pgrpid,psubgrpid):
    side_menu  = productsmenu()
    s_menu = servicemenu()
    pics = LearningPagePicture.objects.last()
    actvgroup = ActivityGroup.objects.all()
    servgroup = ServiceGroup.objects.all()
    p_menu = productsmenu()
    a_menu = activitymenu()
    products = Products.objects.filter(pgroup=pgrpid,psubgroup=psubgrpid,active=True)
    context = {
        'pics':pics,
        'prodmenu':p_menu,
        'actmenu':a_menu,
        'sermenu':s_menu,
        'sidemenu': side_menu,
        'actvgroup':actvgroup,
        'servgroup':servgroup,
        'products':products,
    }
    # return  render(request,'home/producttest.html',context)
    return render(request, 'home/product.html', context)

def productshow(request,pgrpid,psubgrpid):
    side_menu = productsmenu()
    s_menu = servicemenu()
    pics = LearningPagePicture.objects.last()
    actvgroup = ActivityGroup.objects.all()
    servgroup = ServiceGroup.objects.all()
    p_menu = productsmenu()
    a_menu = activitymenu()
    products = Products.objects.filter(pgroup=pgrpid,psubgroup=psubgrpid,active=True)
    context = {
        'pics':pics,
        'prodmenu':p_menu,
        'actmenu':a_menu,
        'sermenu':s_menu,
        'actvgroup':actvgroup,
        'servgroup':servgroup,
        'sidemenu':side_menu,
        'products':products}
    return render(request, 'home/products-img.html', context)

def activities(request,actgrp,actid):
    pics = LearningPagePicture.objects.last()
    p_menu = productsmenu()
    a_menu = activitymenu()
    s_menu = servicemenu()
    actvgroup = ActivityGroup.objects.all()
    servgroup = ServiceGroup.objects.all()
    activity = Activities.objects.filter(agroup=actgrp,active=True,id=actid)
    context = {'activites':activity,
               'pics':pics,
               'prodmenu':p_menu,
               'actmenu':a_menu,
               'sermenu':s_menu,
               'actvgroup':actvgroup,
               'servgroup':servgroup}
    return render(request, 'home/activities.html',context)

def services(request,sergrp,serid):
    pics = LearningPagePicture.objects.last()
    actvgroup = ActivityGroup.objects.all()
    p_menu = productsmenu()
    a_menu = activitymenu()
    s_menu = servicemenu()
    servgroup = ServiceGroup.objects.all()
    service = Services.objects.filter(sgroup=sergrp,active=1,id=serid)
    context = {'services':service,
               'pics':pics,
               'prodmenu':p_menu,
               'actmenu':a_menu,
               'sermenu':s_menu,
               'actvgroup':actvgroup,
               'servgroup':servgroup}
    return render(request, 'home/services.html',context)

def farmingpractice(request):
    return render(request,'home/farming-practice.html')

def productdetail(request,pid):
    p_menu = productsmenu()
    a_menu = activitymenu()
    s_menu = servicemenu()
    pics = LearningPagePicture.objects.last()
    actvgroup = ActivityGroup.objects.all()
    servgroup = ServiceGroup.objects.all()
    products = Products.objects.get(id=pid)
    if products.photo_1 == '' :
        photo1_url = ''
    else:
        photo1_url = products.photo_1.url
    if products.photo_2 == '' :
        photo2_url = ''
    else:
        photo2_url = products.photo_2.url
    if products.photo_3 == '':
        photo3_url = ''
    else:
        photo3_url = products.photo_3.url
    if products.photo_4 == '':
        photo4_url = ''
    else:
        photo4_url = products.photo_4.url
    if products.photo_5 == '':
        photo5_url = ''
    else:
        photo5_url = products.photo_5.url

    context = {'products' : products,
               'pics':pics,
               'prodmenu':p_menu,
               'actmenu':a_menu,
               'sermenu':s_menu,
               'actvgroup':actvgroup,
               'servgroup':servgroup,
               'photo1_url':photo1_url,
               'photo2_url' : photo2_url,
               'photo3_url' : photo3_url,
               'photo4_url' : photo4_url,
               'photo5_url' : photo5_url}
    return render(request, 'home/productdetail.html',context)

def contact(request):
    p_menu = productsmenu()
    a_menu = activitymenu()
    s_menu = servicemenu()
    pics = LearningPagePicture.objects.last()
    actvgroup = ActivityGroup.objects.all()
    servgroup = ServiceGroup.objects.all()
    context ={'actvgroup':actvgroup,
              'pics':pics,
              'prodmenu':p_menu,
              'sermenu':s_menu,
              'actmenu':a_menu,
              'servgroup':servgroup}
    return render(request,'home/contact.html',context)

def custsave(request):
    if request.method=="POST":
        cust = Customer()
        cust.name = request.POST.get("name")
        cust.email = request.POST.get("email")
        cust.phone = request.POST.get("phone")
        cust.address = request.POST.get("address")
        cust.message = request.POST.get("message")
        cust.active = 1
        cust.ts = datetime.now()
        cust.save()
        prodid = request.POST.get("pid")
        products = Products.objects.get(id=prodid)
        actvgroup = ActivityGroup.objects.all()
        servgroup = ServiceGroup.objects.all()
        context = {'products':products,
                   'actvgroup':actvgroup,
                   'servgroup':servgroup}
    return render(request,'home/productdetail.html',context)