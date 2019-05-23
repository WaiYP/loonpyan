from _datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from home.custom import ParentChild
from inventory.models import Categories, ProductGroup, ProductSubGroup, Products, Customer


def index(request):
    return render(request, 'home/index.html')

def about(request):
    return  render(request,'home/about.html')

def product(request,pgrpid,psubgrpid):
    sidemenu = []
    sidemenu.clear()
    pgroups = ProductGroup.objects.filter(active=True)
    for pgroup in pgroups:
        psubgrps = ProductSubGroup.objects.select_related().filter(pgroup=pgroup, active=True).order_by('id')
        sidemenu.append(ParentChild(pgroup, psubgrps))
    products = Products.objects.filter(pgroup=pgrpid,psubgroup=psubgrpid,active=True)

    context = {
        'sidemenu': sidemenu,
        'products':products,
    }
    return  render(request,'home/product.html',context)

def productshow(request,pgrpid,psubgrpid):
    products = Products.objects.filter(pgroup=pgrpid,psubgroup=psubgrpid,active=True)
    content = {}
    return render(request, 'home/product.html', context)

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
        # cust = Customer(name=cust_name,email=cust_email,phone=cust_phone,address=cust_address,message=cust_message,ts=cust_ts,active=cust_active)
        cust.save()
    return HttpResponseRedirect(reverse('home:productdetail'))