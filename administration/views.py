from django.contrib.auth import authenticate, login, logout
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from datetime import datetime



# Create your views here.
from django.urls import reverse

from inventory.models import LearningPagePicture, AboutPagePicture


def index(request):
    # if not request.user.is_authenticated():
    return render(request, 'administration/login.html')
    # else:
    #     return render(request, 'administration/index.html', {})

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'administration/index.html', {})
            else:
                return render(request, 'administration/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'administration/login.html', {'error_message': 'Invalid login'})
    return render(request, 'administration/login.html')


def user_logout(request):
    logout(request)
    return render(request, 'administration/login.html')


class LearnPageView():
    model = LearningPagePicture

    def list(request):
        # if not request.user.is_authenticated():
        #     return render(request, 'administration/login.html')
        # else:
        try:
            lpagepictures = LearningPagePicture.objects.filter(active=True)
            # pricegroup= Products.objects.filter(active=True)
        except LearningPagePicture.DoesNotExist:
            raise Http404('This LearningPagePicture does not exist')

        content = {'lpagepictures':lpagepictures,
                        # 'pricegroup':pricegroup,
        }
        return render(request,'administration/learningpagepicturelist.html',content)

    def edit(request,id):

        try:
            lpagepictures = LearningPagePicture.objects.get(active=True,id=id)
            if lpagepictures.photo_1 == '':
                photourl = ''
            else:
                photourl = lpagepictures.photo_1.url
            if lpagepictures.photo_2 == '':
                photourl2 = ''
            else:
                photourl2 = lpagepictures.photo_2.url
            if lpagepictures.photo_3 == '':
                photourl3 = ''
            else:
                photourl3 = lpagepictures.photo_3.url
            if lpagepictures.photo_4 == '':
                photourl4 = ''
            else:
                photourl4 = lpagepictures.photo_4.url
            if lpagepictures.photo_5 == '':
                photourl5 = ''
            else:
                photourl5 = lpagepictures.photo_5.url
            if lpagepictures.photo_6 == '':
                photourl6 = ''
            else:
                photourl6 = lpagepictures.photo_6.url
            # pricegroup= Products.objects.filter(active=True)
        except LearningPagePicture.DoesNotExist:
            raise Http404('This LearningPagePicture does not exist')

        content = {'lpagepictures': lpagepictures,
                   'edit':1,
                   'photourl': photourl,
                   'photourl2': photourl2,
                   'photourl3': photourl3,
                   'photourl4': photourl4,
                   'photourl5': photourl5,
                   'photourl6': photourl6,
                   # 'pricegroup':pricegroup,
                   }
        return render(request, 'administration/learningpagepicturecreate.html', content)

    def save (request):

        if request.method == 'POST':

            userid = request.user.id
            description = request.POST.get('description')

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

            if 'photo_6' in request.FILES:
                photo6 = request.FILES['photo_6']
            else:
                photo6 = request.POST.get('photoid6')
            ts = datetime.now()


            if request.POST.get('active') is None:
                active = 0
            else:
                active = request.POST.get('active')
            if request.POST.get('id') is None or request.POST.get('id')=='':
                cats = LearningPagePicture(active=active,ts=ts,description=description,photo_6=photo6,
                                  photo_1=photo,photo_2=photo2,photo_3=photo3,photo_4=photo4,photo_5=photo5)
                cats.save()

            else:
                id = request.POST.get('id')
                cats = LearningPagePicture(id=id, active=active, ts=ts,description=description,photo_6=photo6,
                                  photo_1=photo, photo_2=photo2, photo_3=photo3, photo_4=photo4, photo_5=photo5)
                cats.save()
            return HttpResponseRedirect(reverse('administration:learn_page_list'))
        return render(request, 'administration/learningpagepicturelist.html')

    def create(request):

        # try:
        #     category = Categories.objects.get(active=True)
        #     # pricegroup= Products.objects.filter(active=True)
        # except Categories.DoesNotExist:
        #     raise Http404('This Categories does not exist')
        #
        sergroup = LearningPagePicture.objects.filter(active=1)
        # content = {'sergroup': sergroup,
        #
        #            # 'pricegroup':pricegroup,
        #            }
        return render(request, 'administration/learningpagepicturecreate.html')


    # def delete(request,cust_id):
    #     if not request.user.is_authenticated():
    #         return render(request, 'administration/login.html')
    #     else:
    #         Customer.objects.filter(cust_id=cust_id).update(active=False)
    #     return HttpResponseRedirect(reverse('customer:customer_list'))

class AboutPageView():
    model = AboutPagePicture

    def list(request):
        # if not request.user.is_authenticated():
        #     return render(request, 'administration/login.html')
        # else:
        try:
            apagepictures = AboutPagePicture.objects.filter(active=True)
            # pricegroup= Products.objects.filter(active=True)
        except AboutPagePicture.DoesNotExist:
            raise Http404('This AboutPagePicture does not exist')

        content = {'apagepictures':apagepictures,
                        # 'pricegroup':pricegroup,
        }
        return render(request,'administration/aboutpagepicturelist.html',content)

    def edit(request,id):

        try:
            apagepictures = AboutPagePicture.objects.get(active=True,id=id)
            if apagepictures.photo_1 == '':
                photourl = ''
            else:
                photourl = apagepictures.photo_1.url
            if apagepictures.photo_2 == '':
                photourl2 = ''
            else:
                photourl2 = apagepictures.photo_2.url
            if apagepictures.photo_3 == '':
                photourl3 = ''
            else:
                photourl3 = apagepictures.photo_3.url

            # pricegroup= Products.objects.filter(active=True)
        except AboutPagePicture.DoesNotExist:
            raise Http404('This AboutPagePicture does not exist')

        content = {'apagepictures': apagepictures,
                   'edit':1,
                   'photourl': photourl,
                   'photourl2': photourl2,
                   'photourl3': photourl3,
                   }
        return render(request, 'administration/aboutpagepicturecreate.html', content)

    def save (request):

        if request.method == 'POST':

            userid = request.user.id
            description = request.POST.get('description')

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


            ts = datetime.now()


            if request.POST.get('active') is None:
                active = 0
            else:
                active = request.POST.get('active')
            if request.POST.get('id') is None or request.POST.get('id')=='':
                cats = AboutPagePicture(active=active,ts=ts,description=description,
                                  photo_1=photo,photo_2=photo2,photo_3=photo3)
                cats.save()

            else:
                id = request.POST.get('id')
                cats = AboutPagePicture(id=id, active=active, ts=ts,description=description,
                                  photo_1=photo, photo_2=photo2, photo_3=photo3)
                cats.save()
            return HttpResponseRedirect(reverse('administration:about_page_list'))
        return render(request, 'administration/aboutpagepicturelist.html')

    def create(request):

        # try:
        #     category = Categories.objects.get(active=True)
        #     # pricegroup= Products.objects.filter(active=True)
        # except Categories.DoesNotExist:
        #     raise Http404('This Categories does not exist')
        #
        # sergroup = LearningPagePicture.objects.filter(active=1)
        # content = {'sergroup': sergroup,
        #
        #            # 'pricegroup':pricegroup,
        #            }
        return render(request, 'administration/aboutpagepicturecreate.html')


    # def delete(request,cust_id):
    #     if not request.user.is_authenticated():
    #         return render(request, 'administration/login.html')
    #     else:
    #         Customer.objects.filter(cust_id=cust_id).update(active=False)
    #     return HttpResponseRedirect(reverse('customer:customer_list'))
