from _datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from administration.models import LearningPagePicture
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
    content = {'pics':pics}
    return render(request, 'home/index.html',content)

def about(request):
    return  render(request,'home/about.html')

def product(request,pgrpid,psubgrpid):
    side_menu  = sidemenu()
    products = Products.objects.filter(pgroup=pgrpid,psubgroup=psubgrpid,active=True)
    context = {
        'sidemenu': side_menu,
        'products':products,
    }
    return  render(request,'home/product.html',context)

def productshow(request,pgrpid,psubgrpid):
    side_menu = sidemenu()
    products = Products.objects.filter(pgroup=pgrpid,psubgroup=psubgrpid,active=True)
    content = {
        'sidemenu':side_menu,
        'products':products}
    return render(request, 'home/products-img.html', content)

def activities(request):
    return render(request, 'home/activities.html')

def farmingpractice(request):
    return render(request,'home/farming-practice.html')

def productdetail(request,pid):
    products = Products.objects.get(id=pid)
    content = {'products' : products }
    return render(request, 'home/productdetail.html',content)

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
        content = {'products':products}
    return render(request,'home/productdetail.html',content)