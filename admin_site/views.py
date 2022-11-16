from django.shortcuts import render, redirect
from admin_site.models import Category,Vendor
import math
from admin_site.category_form import Category_Form


def dashboard(request):
    return render(request,'dashboard.html')

def category(request):
    no_of_category_dispaly=10
    page=request.GET.get('page')
    if page is None:
        page=1
    else:
        page=int(page)


    categorys=Category.objects.all()
    lenght=len(categorys)
    categorys=categorys[(page-1)*no_of_category_dispaly:page*no_of_category_dispaly]
    if page>1:
        prev=page-1
    else:
        prev=None
    if page<math.ceil(lenght/no_of_category_dispaly):
        nxt=page+1
    else:
        nxt=None


    context={'categorys_data':categorys ,'prev':prev,'nxt':nxt}
    return render(request,'category.html',context)

def add_category(request):
    context={'success':False}

    if request.method=="POST":
        context={'success':True}
        name=request.POST['category_name']
        description = request.POST['category_description']
        instance=Category(name=name,description=description)
        instance.save()
        return redirect(category)


    return render(request,'addcategory.html' ,context)

def edit_category(request ,c_id):
    context={}
    category_obj =Category.objects.get(c_id=c_id)
    category_form = Category_Form(instance=category_obj)
    if request.method=="POST":
        category_form = Category_Form(request.POST,request.FILES,instance=category_obj)
        if category_form.is_valid():
            category_form.save()

            return redirect(category)
    context = {'category_form': category_form}

    return render(request, 'edit_category.html', context)

def delete_category(request, c_id):

    category_del=Category.objects.get(c_id=c_id)
    print(type(category_del))
    category_del.delete()
    print("deleted")


    #return redirect(category)
    context = {'delete_token': True ,'categorys_data':Category.objects.all()}
    return render(request,'category.html',context)


def services(request):
    return render(request,'services.html')

def vendors(request):
    no_of_vendors_dispaly = 10
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)

    vendors = Vendor.objects.all()
    lenght = len(vendors)
    vendors = vendors[(page - 1) * no_of_vendors_dispaly:page * no_of_vendors_dispaly]
    if page > 1:
        prev = page - 1
    else:
        prev = None
    if page < math.ceil(lenght / no_of_vendors_dispaly):
        nxt = page + 1
    else:
        nxt = None

    context = {'vendors_data': vendors, 'prev': prev, 'nxt': nxt}
    return render(request,'vendors.html',context)
