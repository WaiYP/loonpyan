from datetime import datetime

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from inventory.models import Products, Customer, Categories


class ProductView():
    model = Products

    def list(request):
        # if not request.user.is_authenticated():
        #     return render(request, 'administration/login.html')
        # else:
        try:
            products = Products.objects.filter(active=True)
            # pricegroup= Products.objects.filter(active=True)
        except Products.DoesNotExist:
            raise Http404('This Customer does not exist')

        content = {'products':products,
                        # 'pricegroup':pricegroup,
        }
        return render(request,'inventory/productlist.html',content)

    def create(request):

        # if not request.user.is_authenticated():
        #     return render(request, 'administration/login.html')
        # else:
            userid = request.user.id
            # staff = Staff.objects.get(user_id=userid)
            # staffrole = Role.objects.get(id = staff.role_id)
            # cities = City.objects.all()
            # division= Division.objects.all()
            # township = Township.objects.all()
            # pricegroup = PriceGroup.objects.filter(active=True)
            # context = {
            #     "cities":cities,
            #     'division':division,
            #     'township':township,
            #     'pricegroup':pricegroup,
            #     'role':staffrole.role_name,
            # }

            return render(request, 'inventory/productcreate.html')
    #
    # def edit(request,id):
    #
    #     if not request.user.is_authenticated():
    #         return render(request, 'administration/login.html')
    #     else:
    #         try:
    #             userid = request.user.id
    #             staff = Staff.objects.get(user_id=userid)
    #             staffrole = Role.objects.get(id=staff.role_id)
    #             cust = Customer.objects.get(cust_id=id)
    #             division = Division.objects.all()
    #             township = Township.objects.all()
    #             pricegroup=PriceGroup.objects.filter(active=1)
    #             if cust.photo == '':
    #                 photourl = ''
    #             else:
    #                 photourl = cust.photo
    #
    #             cities = City.objects.all()
    #         except Customer.DoesNotExist:
    #             raise Http404('This Customer does not exist')
    #
    #     context = {
    #         'cust': cust,
    #         'cities': cities,
    #         'photourl': photourl,
    #         'division':division,
    #         'township':township,
    #         'pricegroup':pricegroup,
    #         'edit': 1,
    #         'message': '',
    #         'error_message': '',
    #         'role': staffrole.role_name,
    #     }
    #
    #     return render(request, 'customer/customerdetail.html', context)
    #
    def save (request):

        if request.method == 'POST':

            userid = request.user.id
            name = request.POST.get('name')
            if 'photo_1' in request.FILES:
                photo = request.FILES['photo_1']
            else:
                photo = request.POST.get('photo_id')
            ts = datetime.now()


            if request.POST.get('active') is None:
                active = 0
            else:
                active = request.POST.get('active')
            if request.POST.get('id') is None or request.POST.get('id')=='':
                cust = Products(name=name,photo_1=photo,active=active,ts=ts)
                cust.save()

            else:
                id = request.POST.get('id')
                cust = Products(id=id,name=name, photo_1=photo, active=active, ts=ts)
                cust.save()
            return HttpResponseRedirect(reverse('inventory:product_list'))
        return render(request, 'inventory/productlist.html')

    # def delete(request,cust_id):
    #     if not request.user.is_authenticated():
    #         return render(request, 'administration/login.html')
    #     else:
    #         Customer.objects.filter(cust_id=cust_id).update(active=False)
    #     return HttpResponseRedirect(reverse('customer:customer_list'))

class CustomerView():
    model = Customer

    def list(request):
        # if not request.user.is_authenticated():
        #     return render(request, 'administration/login.html')
        # else:
        try:
            customers = Customer.objects.filter(active=True)
            # pricegroup= Products.objects.filter(active=True)
        except Customer.DoesNotExist:
            raise Http404('This Customer does not exist')

        content = {'customers':customers,
                        # 'pricegroup':pricegroup,
        }
        return render(request,'inventory/customerlist.html',content)

    def detail(request,id):

        try:
            customers = Customer.objects.get(active=True,id=id)
            # pricegroup= Products.objects.filter(active=True)
        except Customer.DoesNotExist:
            raise Http404('This Customer does not exist')

        content = {'customers': customers,
                   # 'pricegroup':pricegroup,
                   }
        return render(request, 'inventory/customerdetail.html', content)


    #
    # def edit(request,id):
    #
    #     if not request.user.is_authenticated():
    #         return render(request, 'administration/login.html')
    #     else:
    #         try:
    #             userid = request.user.id
    #             staff = Staff.objects.get(user_id=userid)
    #             staffrole = Role.objects.get(id=staff.role_id)
    #             cust = Customer.objects.get(cust_id=id)
    #             division = Division.objects.all()
    #             township = Township.objects.all()
    #             pricegroup=PriceGroup.objects.filter(active=1)
    #             if cust.photo == '':
    #                 photourl = ''
    #             else:
    #                 photourl = cust.photo
    #
    #             cities = City.objects.all()
    #         except Customer.DoesNotExist:
    #             raise Http404('This Customer does not exist')
    #
    #     context = {
    #         'cust': cust,
    #         'cities': cities,
    #         'photourl': photourl,
    #         'division':division,
    #         'township':township,
    #         'pricegroup':pricegroup,
    #         'edit': 1,
    #         'message': '',
    #         'error_message': '',
    #         'role': staffrole.role_name,
    #     }
    #
    #     return render(request, 'customer/customerdetail.html', context)
    #
    def save (request):

        if request.method == 'POST':

            userid = request.user.id
            name = request.POST.get('name')
            if 'photo_1' in request.FILES:
                photo = request.FILES['photo_1']
            else:
                photo = request.POST.get('photo_id')
            ts = datetime.now()


            if request.POST.get('active') is None:
                active = 0
            else:
                active = request.POST.get('active')
            if request.POST.get('id') is None or request.POST.get('id')=='':
                cust = Products(name=name,photo_1=photo,active=active,ts=ts)
                cust.save()

            else:
                id = request.POST.get('id')
                cust = Products(id=id,name=name, photo_1=photo, active=active, ts=ts)
                cust.save()
            return HttpResponseRedirect(reverse('inventory:product_list'))
        return render(request, 'inventory/productlist.html')

    # def delete(request,cust_id):
    #     if not request.user.is_authenticated():
    #         return render(request, 'administration/login.html')
    #     else:
    #         Customer.objects.filter(cust_id=cust_id).update(active=False)
    #     return HttpResponseRedirect(reverse('customer:customer_list'))

class CategoryView():
    model = Categories

    def list(request):
        # if not request.user.is_authenticated():
        #     return render(request, 'administration/login.html')
        # else:
        try:
            categories = Categories.objects.filter(active=True)
            # pricegroup= Products.objects.filter(active=True)
        except Customer.DoesNotExist:
            raise Http404('This Customer does not exist')

        content = {'categories':categories,
                        # 'pricegroup':pricegroup,
        }
        return render(request,'inventory/categorylist.html',content)

    def edit(request,id):

        try:
            category = Categories.objects.get(active=True,id=id)
            # pricegroup= Products.objects.filter(active=True)
        except Categories.DoesNotExist:
            raise Http404('This Categories does not exist')

        content = {'category': category,
                   'edit':1,
                   # 'pricegroup':pricegroup,
                   }
        return render(request, 'inventory/categorydetail.html', content)

    def save (request):

        if request.method == 'POST':

            userid = request.user.id
            name = request.POST.get('name')
            ts = datetime.now()


            if request.POST.get('active') is None:
                active = 0
            else:
                active = request.POST.get('active')
            if request.POST.get('id') is None or request.POST.get('id')=='':
                cats = Categories(name=name,active=active,ts=ts)
                cats.save()

            else:
                id = request.POST.get('id')
                cats = Categories(id=id,name=name, active=active, ts=ts)
                cats.save()
            return HttpResponseRedirect(reverse('inventory:category_list'))
        return render(request, 'inventory/categorylist.html')

    def create(request):

        # try:
        #     category = Categories.objects.get(active=True)
        #     # pricegroup= Products.objects.filter(active=True)
        # except Categories.DoesNotExist:
        #     raise Http404('This Categories does not exist')
        #
        # content = {'category': category,
        #            'edit':1,
        #            # 'pricegroup':pricegroup,
        #            }
        return render(request, 'inventory/categorydetail.html')


    # def delete(request,cust_id):
    #     if not request.user.is_authenticated():
    #         return render(request, 'administration/login.html')
    #     else:
    #         Customer.objects.filter(cust_id=cust_id).update(active=False)
    #     return HttpResponseRedirect(reverse('customer:customer_list'))

