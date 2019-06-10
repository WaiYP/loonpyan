from _datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from administration.models import LearningPagePicture, AboutPagePicture
from home.custom import ParentChild
from inventory.models import Categories, ProductGroup, ProductSubGroup, Products, Customer


def sidemenu():
    sidemenu = []
    sidemenu.clear()
    pgroups = ProductGroup.objects.filter(active=True)
    for pgroup in pgroups:
        psubgrps = ProductSubGroup.objects.select_related().filter(pgroup=pgroup, active=True).order_by('id')
        sidemenu.append(ParentChild(pgroup, psubgrps))
    return  sidemenu

def index(request):
    pics = LearningPagePicture.objects.last()
    context = {'pics':pics}
    return render(request, 'home/index.html',context)

def about(request):
    abt = AboutPagePicture.objects.last()
    context = {'abt':abt}
    return  render(request,'home/about.html',context)

def product(request,pgrpid,psubgrpid):
    side_menu  = sidemenu()
    products = Products.objects.filter(pgroup=pgrpid,psubgroup=psubgrpid,active=True)
    context = {
        'sidemenu': side_menu,
        'products':products,
    }
    # return  render(request,'home/producttest.html',context)
    return render(request, 'home/product.html', context)

def productshow(request,pgrpid,psubgrpid):
    side_menu = sidemenu()
    products = Products.objects.filter(pgroup=pgrpid,psubgroup=psubgrpid,active=True)
    context = {
        'sidemenu':side_menu,
        'products':products}
    return render(request, 'home/products-img.html', context)

def activities(request):
    return render(request, 'home/activities.html')

def farmingpractice(request):
    return render(request,'home/farming-practice.html')

def productdetail(request,pid):
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
               'photo1_url':photo1_url,
               'photo2_url' : photo2_url,
               'photo3_url' : photo3_url,
               'photo4_url' : photo4_url,
               'photo5_url' : photo5_url}
    return render(request, 'home/productdetail.html',context)

def contact(request):
    return render(request,'home/contact.html')

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
        context = {'products':products}
    return render(request,'home/productdetail.html',context)