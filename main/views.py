import email
from hmac import new
from multiprocessing import context
from urllib import request
from django.contrib import messages
from http import client
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from.models import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

def Register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    r=request.user
    info = '<strong>{}</strong>. You have successfully registered!'.format(r)
    messages.success(request,info)
    return render(request, 'registration/register.html', {'form': form})

def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
    else:
        form = AuthenticationForm()
    r = request.user
    info = ' You have successfully logined !'
    messages.success(request,info)
    return render(request, 'registration/login.html', {'form': form})


def Logout(request):
    r=request.user
    logout(request)
    info = ' You have successfully loged out!'
    messages.success(request,info)
    print(messages)
    return redirect('/')

def Index(request):
    info = Info.objects.first()
    product=Product.objects.all()
    new_product=[]
    for i in product:
        
        if i.discount > 0:
            new_price = i.price * ((100-i.discount)/100)
            item = {
                'id':i.id,
                'category':i.category,
                'name':i.name,
                'photo':i.photo,
                'price':i.price,
                'discount':new_price,
               
            }
        else:
            item={
                'id':i.id,  
                'category':i.category,
                'name':i.name,
                'photo':i.photo,
                'price':i.price,
                

            }
        new_product.append(item)
    context={
        # 'product':product,
        'info':info,
        'category':Category.objects.all(),
        'categ':Category.objects.all(),
        'product':new_product,
        # 'prod':prod,
        # 'filteredprod':product1,
        'new-price':new_price,
        # 'count':count,
        'production':product,
        'main':Main.objects.all(),
        'bloger':Bloging.objects.all()

    }
    return render(request,'index.html',context)

def About(request):
    context={
        'bloger':Bloging.objects.all()

    }
    return render(request,'shop.html',context)
def Shopping(request):
    product=Product.objects.all()
    new_product=[]
    for i in product:
        
        if i.discount > 0:
            new_price = i.price * ((100-i.discount)/100)
            item = {
                'id':i.id,
                'category':i.category,
                'name':i.name,
                'photo':i.photo,
                'price':i.price,
                'discount':new_price,
               
            }
        else:
            item={
                'id':i.id,  
                'category':i.category,
                'name':i.name,
                'photo':i.photo,
                'price':i.price,
                

            }
        new_product.append(item)
    context={
    'product':new_product,
    'proding':pricing,
    'prod':Product.objects.all()
        
    }
    return render(request,'shop-four-columns.html',context)
def FilterCategory(request,id):
    filter = Product.objects.filter(category_id=id)

    context = {
        'filter':filter
    }

    return render(request,'shop.html',context)

def Contact(request):
    context={
        'bloger':Bloging.objects.all()

    }
    return render(request,'contact.html',context)
def Sending(request):
    if request.method == 'POST':
        r = request.POST
        name = r['name']
        email = r['email']
        subject = r['subject']
        text = r['text']
        Contacting.objects.create(name = name,email=email,subject=subject,text=text)
    info = '<strong>{}</strong>. Your Message Has Been Sent! , Soon We Will Connected'.format(name)
    messages.success(request,info)
    return redirect ('/contact/')

def pricing(product):
    only_discount=(product.price-product.discount)/(product.price/100)
    return only_discount
def new_price(product):
    new_price = product.price * ((100-product.discount)/100)

    return new_price
def AddToCart(request):
    get = request.GET.get('product')
    prod  = Product.objects.get(id=get)
    savat = Shop.objects.filter(client = request.user, status = 0)
    if len(savat) == 0:
        svt = Shop.objects.create(client = request.user)
    else:
        svt = savat[0]
    new_p = new_price(prod)
    svt.total +=new_p
    my_items = ShopItems.objects.filter(shop__client = request.user , shop__status = 0, product = prod)
    if len(my_items)==0:
        ShopItems.objects.create(shop=svt,product = prod,quantity = 1,totalPay=new_p)
    else:
        current_item = my_items[0]
        current_item.quantity +=1
        current_item.totalPay +=new_p
        current_item.save()
    svt.save()

    messages.success(request,f"To The Cart <strong>{prod.name}</strong> Added. ")


    return redirect('/')

def Base(request):
    context={
        'order':ShopItems.objects.first(),
        'bloger':Bloging.objects.all()
    }
    return render(request,'base.html',context)
def Cart(request):
     
    try:
        count =Shop.objects.filter(client=request.user, status=0)[0].item_savatcha.all().count()
    except:
        count = 0
    product1 = ShopItems.objects.filter(shop__client = request.user,shop__status = 0)
    # shopping = Shop.objects.get()
    try:
        shop1=Shop.objects.filter(client=request.user, status=0)[0]
        print('try ishladi')
    except:
        print('except ishladi')
        shop1={'total':0}
    print(shop1)
    

    context = {
        'order':product1,
        'shop':Shop.objects.first(),
        'count':count,
        'bloger':Bloging.objects.all()

    }
    return render(request,'shop-cart.html',context) 

def Delete(request,id):
    delete = ShopItems.objects.get(id=id)
    shop = Shop.objects.get(client = request.user)
    shop.total-=delete.totalPay

    shop.save()
    delete.delete()
    messages.success(request,f"From The Cart <strong>{delete.product.name}</strong> Removed. ")

    return redirect('/cartpage/')

class ProductDetail(DetailView):
    model = Product
    template_name='single-product.html'
    context_object_name='product'

def CountSavatcha(request):
    count = ShopItems.objects.filter(shop__client=request.user, shop__status=0)
    s = 0
    for c in count:
        s += c.total
    data = {
        'count': count.count(),
        'total': s
    }

    return JsonResponse(data)



def Blog(request):
    blog = Bloging.objects.all()
    context = {
        'blog':blog,
        'bloger':Bloging.objects.all()

    }
    return render(request,'blog.html',context)
class BlogDetail(DetailView):
    model = Bloging
    template_name='blog-details.html'
    context_object_name='blog'


def customhandler404(request, exception, template_name='404.html'):
    response = render(request, template_name)
    response.status_code = 404
    return response
