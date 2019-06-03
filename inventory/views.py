from datetime import datetime

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from inventory.models import Products, Customer, Categories, ProductGroup, ProductSubGroup, ActivityGroup, Activities, \
    ServiceGroup, Services
from inventory.serializers import ProductGroupSerializer, ProductSubGroupSerializer


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
            raise Http404('This Products does not exist')

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
            category = Categories.objects.filter(active=1)
            pgroup = ProductGroup.objects.filter(active=1)
            psubgroup = ProductSubGroup.objects.filter(active=1)
            context = {
                "category":category,
                'prodgroup':pgroup,
                'psubgroup':psubgroup,

            }

            return render(request, 'inventory/productcreate.html',context)

    def edit(request,id):

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

            try:
                product = Products.objects.get(active=True, id=id)
                if product.photo_1 == '':
                    photourl = ''
                else:
                    photourl = product.photo_1.url
                if product.photo_2 == '':
                    photourl2 = ''
                else:
                    photourl2 = product.photo_2.url
                if product.photo_3 == '':
                    photourl3 = ''
                else:
                    photourl3 = product.photo_3.url
                if product.photo_4 == '':
                    photourl4 = ''
                else:
                    photourl4 = product.photo_4.url
                if product.photo_5 == '':
                    photourl5 = ''
                else:
                    photourl5 = product.photo_5.url

                # pricegroup= Products.objects.filter(active=True)
            except Products.DoesNotExist:
                raise Http404('This Products does not exist')
            category = Categories.objects.filter(active=1)
            pgroup = ProductGroup.objects.filter(active=True)
            psubgroup = ProductSubGroup.objects.filter(active=True)
            # psname = psubgroup.name
            content = {
                'category':category,
                'product':product,
                'photourl':photourl,
                'photourl2':photourl2,
                'photourl3':photourl3,
                'photourl4':photourl4,
                'photourl5':photourl5,
                'edit':1,
                'productgroup':pgroup,
                'psubgroup':psubgroup,
            }

            return render(request, 'inventory/productcreate.html',content)
    def save (request):

        if request.method == 'POST':

            userid = request.user.id
            cat = request.POST.get('category')
            pgroup = request.POST.get('pgroup')
            psubgroup = request.POST.get('psgroup')
            name = request.POST.get('name')
            description = request.POST.get('description')
            technology = request.POST.get('technology')
            made = request.POST.get('made_in')
            standard = request.POST.get('standard')

            if 'photo_1' in request.FILES:
                photo = request.FILES['photo_1']
            else:
                photo = request.POST.get('photoid1')

            if 'photo_2' in request.FILES:
                photo2 = request.FILES['photo_2']
            else:
                photo2 = request.POST.get('photoid2')

            if 'photo_3' in request.FILES:
                photo3 = request.FILES['photo_3']
            else:
                photo3 = request.POST.get('photoid3')

            if 'photo_4' in request.FILES:
                photo4 = request.FILES['photo_4']
            else:
                photo4 = request.POST.get('photoid4')

            if 'photo_5' in request.FILES:
                photo5 = request.FILES['photo_5']
            else:
                photo5 = request.POST.get('photoid5')
            ts = datetime.now()


            if request.POST.get('active') is None:
                active = 0
            else:
                active = request.POST.get('active')
            if request.POST.get('id') is None or request.POST.get('id')=='':
                cust = Products(name=name,photo_1=photo,active=active,ts=ts,
                                cat_id=cat,pgroup_id=pgroup,psubgroup_id=psubgroup,description=description,technology=technology,
                                made_in=made,std_cert=standard,photo_2=photo2,photo_3=photo3,photo_4=photo4,photo_5=photo5)
                cust.save()

            else:
                id = request.POST.get('id')
                cust = Products(id=id,name=name, photo_1=photo, active=active, ts=ts,
                                cat_id=cat, pgroup_id=pgroup, psubgroup_id=psubgroup, description=description,
                                technology=technology,
                                made_in=made, std_cert=standard, photo_2=photo2, photo_3=photo3, photo_5=photo5,
                                photo_4=photo5)
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

class PgroupView():
    model = ProductGroup

    def list(request):
        # if not request.user.is_authenticated():
        #     return render(request, 'administration/login.html')
        # else:
        try:
            pgroups = ProductGroup.objects.filter(active=True)
            # pricegroup= Products.objects.filter(active=True)
        except ProductGroup.DoesNotExist:
            raise Http404('This ProductGroup does not exist')

        content = {'pgroups':pgroups,
                        # 'pricegroup':pricegroup,
        }
        return render(request,'inventory/productgrouplist.html',content)

    def edit(request,id):

        try:
            pgroup = ProductGroup.objects.get(active=True,id=id)

            # pricegroup= Products.objects.filter(active=True)
        except ProductGroup.DoesNotExist:
            raise Http404('This ProductGroup does not exist')
        category = Categories.objects.filter(active=1)
        content = {'pgroup': pgroup,
                   'category':category,
                   'edit':1,
                   # 'pricegroup':pricegroup,
                   }
        return render(request, 'inventory/productgroupcreate.html', content)

    def save (request):

        if request.method == 'POST':

            userid = request.user.id
            name = request.POST.get('name')
            cate = request.POST.get('category')
            ts = datetime.now()


            if request.POST.get('active') is None:
                active = 0
            else:
                active = request.POST.get('active')
            if request.POST.get('id') is None or request.POST.get('id')=='':
                cats = ProductGroup(name=name,active=active,ts=ts,cat_id=cate)
                cats.save()

            else:
                id = request.POST.get('id')
                cats = ProductGroup(id=id,name=name, active=active, ts=ts,cat_id=cate)
                cats.save()
            return HttpResponseRedirect(reverse('inventory:pgroup_list'))
        return render(request, 'inventory/productgrouplist.html')

    def create(request):

        # try:
        #     category = Categories.objects.get(active=True)
        #     # pricegroup= Products.objects.filter(active=True)
        # except Categories.DoesNotExist:
        #     raise Http404('This Categories does not exist')
        #
        category = Categories.objects.filter(active=1)
        content = {'category': category,
                   # 'edit':1,
                   # 'pricegroup':pricegroup,
                   }
        return render(request, 'inventory/productgroupcreate.html',content)


    # def delete(request,cust_id):
    #     if not request.user.is_authenticated():
    #         return render(request, 'administration/login.html')
    #     else:
    #         Customer.objects.filter(cust_id=cust_id).update(active=False)
    #     return HttpResponseRedirect(reverse('customer:customer_list'))

class PsubgroupView():
    model = ProductGroup

    def list(request):
        # if not request.user.is_authenticated():
        #     return render(request, 'administration/login.html')
        # else:
        try:
            psubgroups = ProductSubGroup.objects.filter(active=True)
            # pricegroup= Products.objects.filter(active=True)
        except ProductSubGroup.DoesNotExist:
            raise Http404('This ProductSubGroup does not exist')

        content = {'psubgroups':psubgroups,
                        # 'pricegroup':pricegroup,
        }
        return render(request,'inventory/psubgrouplist.html',content)

    def edit(request,id):

        try:
            psubgroup = ProductSubGroup.objects.get(active=True,id=id)
            pgroup = ProductGroup.objects.filter(active=1)
            # pricegroup= Products.objects.filter(active=True)
        except ProductSubGroup.DoesNotExist:
            raise Http404('This ProductSubGroup does not exist')

        content = {'psubgroup': psubgroup,
                   'productgroup':pgroup,
                   'edit':1,
                   # 'pricegroup':pricegroup,
                   }
        return render(request, 'inventory/psubgroupcreate.html', content)

    def save (request):

        if request.method == 'POST':

            userid = request.user.id
            name = request.POST.get('name')
            pgroup = request.POST.get('pgroup')
            ts = datetime.now()


            if request.POST.get('active') is None:
                active = 0
            else:
                active = request.POST.get('active')
            if request.POST.get('id') is None or request.POST.get('id')=='':
                cats = ProductSubGroup(name=name,pgroup_id=pgroup,active=active,ts=ts)
                cats.save()

            else:
                id = request.POST.get('id')
                cats = ProductSubGroup(id=id,name=name,pgroup_id=pgroup, active=active, ts=ts)
                cats.save()
            return HttpResponseRedirect(reverse('inventory:psubgroup_list'))
        return render(request, 'inventory/psubgrouplist.html.html')

    def create(request):

        # try:
        #     category = Categories.objects.get(active=True)
        #     # pricegroup= Products.objects.filter(active=True)
        # except Categories.DoesNotExist:
        #     raise Http404('This Categories does not exist')
        #
        pgroup = ProductGroup.objects.filter(active=1)
        content = {'productgroup': pgroup,
                   # 'pricegroup':pricegroup,
                   }
        return render(request, 'inventory/psubgroupcreate.html',content)


    # def delete(request,cust_id):
    #     if not request.user.is_authenticated():
    #         return render(request, 'administration/login.html')
    #     else:
    #         Customer.objects.filter(cust_id=cust_id).update(active=False)
    #     return HttpResponseRedirect(reverse('customer:customer_list'))

class ActivityGroupView():
    model = ActivityGroup

    def list(request):
        # if not request.user.is_authenticated():
        #     return render(request, 'administration/login.html')
        # else:
        try:
            actgroup = ActivityGroup.objects.filter(active=True)
            # pricegroup= Products.objects.filter(active=True)
        except ActivityGroup.DoesNotExist:
            raise Http404('This ActivityGroup does not exist')

        content = {'actgroup':actgroup,
                        # 'pricegroup':pricegroup,
        }
        return render(request,'inventory/activitygrouplist.html',content)

    def edit(request,id):

        try:
            actgroup = ActivityGroup.objects.get(active=True,id=id)
            # pricegroup= Products.objects.filter(active=True)
        except ActivityGroup.DoesNotExist:
            raise Http404('This ActivityGroup does not exist')

        content = {'actgroup': actgroup,
                   'edit':1,
                   # 'pricegroup':pricegroup,
                   }
        return render(request, 'inventory/activitygroupcreate.html', content)

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
                cats = ActivityGroup(name=name,active=active,ts=ts)
                cats.save()

            else:
                id = request.POST.get('id')
                cats = ActivityGroup(id=id,name=name, active=active, ts=ts)
                cats.save()
            return HttpResponseRedirect(reverse('inventory:actgroup_list'))
        return render(request, 'inventory/activitygrouplist.html')

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
        return render(request, 'inventory/activitygroupcreate.html')


    # def delete(request,cust_id):
    #     if not request.user.is_authenticated():
    #         return render(request, 'administration/login.html')
    #     else:
    #         Customer.objects.filter(cust_id=cust_id).update(active=False)
    #     return HttpResponseRedirect(reverse('customer:customer_list'))

class ActivityView():
    model = Activities

    def list(request):
        # if not request.user.is_authenticated():
        #     return render(request, 'administration/login.html')
        # else:
        try:
            acivity = Activities.objects.filter(active=True)
            # pricegroup= Products.objects.filter(active=True)
        except Activities.DoesNotExist:
            raise Http404('This Activities does not exist')

        content = {'activity':acivity,
                        # 'pricegroup':pricegroup,
        }
        return render(request,'inventory/activitylist.html',content)

    def edit(request,id):

        try:
            acivity = Activities.objects.get(active=True,id=id)
            if acivity.photo_1 == '':
                photourl = ''
            else:
                photourl = acivity.photo_1.url
            if acivity.photo_2 == '':
                photourl2 = ''
            else:
                photourl2 = acivity.photo_2.url
            if acivity.photo_3 == '':
                photourl3 = ''
            else:
                photourl3 = acivity.photo_3.url
            if acivity.photo_4 == '':
                photourl4 = ''
            else:
                photourl4 = acivity.photo_4.url
            if acivity.photo_5 == '':
                photourl5 = ''
            else:
                photourl5 = acivity.photo_5.url
            # pricegroup= Products.objects.filter(active=True)
        except Activities.DoesNotExist:
            raise Http404('This Activities does not exist')
        actgroup = ActivityGroup.objects.filter(active=1)
        content = {'activity': acivity,
                   'actgroup':actgroup,
                   'edit':1,
                   'photourl': photourl,
                   'photourl2': photourl2,
                   'photourl3': photourl3,
                   'photourl4': photourl4,
                   'photourl5': photourl5,
                   # 'pricegroup':pricegroup,
                   }
        return render(request, 'inventory/activitycreate.html', content)

    def save (request):

        if request.method == 'POST':

            userid = request.user.id
            name = request.POST.get('name')
            agroup  = request.POST.get('agroup')
            description = request.POST.get('description')

            if 'photo_1' in request.FILES:
                photo = request.FILES['photo_1']
            else:
                photo = request.POST.get('photoid1')

            if 'photo_2' in request.FILES:
                photo2 = request.FILES['photo_2']
            else:
                photo = request.POST.get('photoid2')

            if 'photo_3' in request.FILES:
                photo3 = request.FILES['photo_3']
            else:
                photo3 = request.POST.get('photoid3')

            if 'photo_4' in request.FILES:
                photo4 = request.FILES['photo_4']
            else:
                photo4 = request.POST.get('photoid4')

            if 'photo_5' in request.FILES:
                photo5 = request.FILES['photo_5']
            else:
                photo5 = request.POST.get('photoid5')
            ts = datetime.now()


            if request.POST.get('active') is None:
                active = 0
            else:
                active = request.POST.get('active')
            if request.POST.get('id') is None or request.POST.get('id')=='':
                cats = Activities(name=name,active=active,ts=ts,agroup_id=agroup,description=description,
                                  photo_1=photo,photo_2=photo2,photo_3=photo3,photo_4=photo4,photo_5=photo5)
                cats.save()

            else:
                id = request.POST.get('id')
                cats = Activities(id=id,name=name, active=active, ts=ts,agroup_id=agroup,description=description,
                                  photo_1=photo, photo_2=photo2, photo_3=photo3, photo_4=photo4, photo_5=photo5)
                cats.save()
            return HttpResponseRedirect(reverse('inventory:activity_list'))
        return render(request, 'inventory/activitylist.html')

    def create(request):

        # try:
        #     category = Categories.objects.get(active=True)
        #     # pricegroup= Products.objects.filter(active=True)
        # except Categories.DoesNotExist:
        #     raise Http404('This Categories does not exist')
        #
        actgroup = ActivityGroup.objects.filter(active=1)
        content = {'actgroup': actgroup,

                   # 'pricegroup':pricegroup,
                   }
        return render(request, 'inventory/activitycreate.html',content)


    # def delete(request,cust_id):
    #     if not request.user.is_authenticated():
    #         return render(request, 'administration/login.html')
    #     else:
    #         Customer.objects.filter(cust_id=cust_id).update(active=False)
    #     return HttpResponseRedirect(reverse('customer:customer_list'))

class ServiceGroupView():
    model = ServiceGroup

    def list(request):
        # if not request.user.is_authenticated():
        #     return render(request, 'administration/login.html')
        # else:
        try:
            sergroup = ServiceGroup.objects.filter(active=True)
            # pricegroup= Products.objects.filter(active=True)
        except ServiceGroup.DoesNotExist:
            raise Http404('This ServiceGroup does not exist')

        content = {'sergroup':sergroup,
                        # 'pricegroup':pricegroup,
        }
        return render(request,'inventory/servicegrouplist.html',content)

    def edit(request,id):

        try:
            sergroup = ServiceGroup.objects.get(active=True,id=id)
            # pricegroup= Products.objects.filter(active=True)
        except ServiceGroup.DoesNotExist:
            raise Http404('This ServiceGroup does not exist')

        content = {'sergroup': sergroup,
                   'edit':1,
                   # 'pricegroup':pricegroup,
                   }
        return render(request, 'inventory/servicegroupcreate.html', content)

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
                cats = ServiceGroup(name=name,active=active,ts=ts)
                cats.save()

            else:
                id = request.POST.get('id')
                cats = ServiceGroup(id=id,name=name, active=active, ts=ts)
                cats.save()
            return HttpResponseRedirect(reverse('inventory:sergroup_list'))
        return render(request, 'inventory/servicegrouplist.html')

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
        return render(request, 'inventory/servicegroupcreate.html')


    # def delete(request,cust_id):
    #     if not request.user.is_authenticated():
    #         return render(request, 'administration/login.html')
    #     else:
    #         Customer.objects.filter(cust_id=cust_id).update(active=False)
    #     return HttpResponseRedirect(reverse('customer:customer_list'))

class ServiceView():
    model = Services

    def list(request):
        # if not request.user.is_authenticated():
        #     return render(request, 'administration/login.html')
        # else:
        try:
            services = Services.objects.filter(active=True)
            # pricegroup= Products.objects.filter(active=True)
        except Services.DoesNotExist:
            raise Http404('This Services does not exist')

        content = {'services':services,
                        # 'pricegroup':pricegroup,
        }
        return render(request,'inventory/servicelist.html',content)

    def edit(request,id):

        try:
            services = Services.objects.get(active=True,id=id)
            if services.photo_1 == '':
                photourl = ''
            else:
                photourl = services.photo_1.url
            if services.photo_2 == '':
                photourl2 = ''
            else:
                photourl2 = services.photo_2.url
            if services.photo_3 == '':
                photourl3 = ''
            else:
                photourl3 = services.photo_3.url
            if services.photo_4 == '':
                photourl4 = ''
            else:
                photourl4 = services.photo_4.url
            if services.photo_5 == '':
                photourl5 = ''
            else:
                photourl5 = services.photo_5.url
            # pricegroup= Products.objects.filter(active=True)
        except Services.DoesNotExist:
            raise Http404('This Services does not exist')
        sergroup = ServiceGroup.objects.filter(active=1)
        content = {'services': services,
                   'sergroup':sergroup,
                   'edit':1,
                   'photourl': photourl,
                   'photourl2': photourl2,
                   'photourl3': photourl3,
                   'photourl4': photourl4,
                   'photourl5': photourl5,
                   # 'pricegroup':pricegroup,
                   }
        return render(request, 'inventory/servicecreate.html', content)

    def save (request):

        if request.method == 'POST':

            userid = request.user.id
            name = request.POST.get('name')
            sgroup  = request.POST.get('sgroup')
            description = request.POST.get('description')

            if 'photo_1' in request.FILES:
                photo = request.FILES['photo_1']
            else:
                photo = request.POST.get('photoid1')

            if 'photo_2' in request.FILES:
                photo2 = request.FILES['photo_2']
            else:
                photo = request.POST.get('photoid2')

            if 'photo_3' in request.FILES:
                photo3 = request.FILES['photo_3']
            else:
                photo3 = request.POST.get('photoid3')

            if 'photo_4' in request.FILES:
                photo4 = request.FILES['photo_4']
            else:
                photo4 = request.POST.get('photoid4')

            if 'photo_5' in request.FILES:
                photo5 = request.FILES['photo_5']
            else:
                photo5 = request.POST.get('photoid5')
            ts = datetime.now()


            if request.POST.get('active') is None:
                active = 0
            else:
                active = request.POST.get('active')
            if request.POST.get('id') is None or request.POST.get('id')=='':
                cats = Services(name=name,active=active,ts=ts,sgroup_id=sgroup,description=description,
                                  photo_1=photo,photo_2=photo2,photo_3=photo3,photo_4=photo4,photo_5=photo5)
                cats.save()

            else:
                id = request.POST.get('id')
                cats = Services(id=id,name=name, active=active, ts=ts,sgroup_id=sgroup,description=description,
                                  photo_1=photo, photo_2=photo2, photo_3=photo3, photo_4=photo4, photo_5=photo5)
                cats.save()
            return HttpResponseRedirect(reverse('inventory:service_list'))
        return render(request, 'inventory/servicelist.html')

    def create(request):

        # try:
        #     category = Categories.objects.get(active=True)
        #     # pricegroup= Products.objects.filter(active=True)
        # except Categories.DoesNotExist:
        #     raise Http404('This Categories does not exist')
        #
        sergroup = ServiceGroup.objects.filter(active=1)
        content = {'sergroup': sergroup,

                   # 'pricegroup':pricegroup,
                   }
        return render(request, 'inventory/servicecreate.html',content)


    # def delete(request,cust_id):
    #     if not request.user.is_authenticated():
    #         return render(request, 'administration/login.html')
    #     else:
    #         Customer.objects.filter(cust_id=cust_id).update(active=False)
    #     return HttpResponseRedirect(reverse('customer:customer_list'))


@api_view(['GET', 'POST'])
def get_productgroup(request):
        if request.method == 'GET':
            productgroup = ProductGroup.objects.filter(active=True)
            serializer = ProductGroupSerializer(productgroup, many=True)
            return Response(serializer.data)

@api_view(['GET','POST'])
def get_productsubgroup(request,id):
    if request.method == 'GET':
        pgrpid = int(id)
        prouductsubgroup = ProductSubGroup.objects.filter(pgroup=pgrpid,active=True)
        serializer = ProductSubGroupSerializer(prouductsubgroup,many=True)
        return Response(serializer.data)