from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return  render(request,'home/about.html')

def product(request):
    datalist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    context = {
        'datalist': datalist
    }
    return  render(request,'home/product.html',context)

def activities(request):
    return render(request, 'home/activities.html')



def farmingpractice(request):
    return render(request,'home/farming-practice.html')

def productdetail(request):
    return render(request, 'home/productdetail.html')

def contact(request):
    return render(request,'home/contact.html')