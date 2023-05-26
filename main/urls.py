from django.contrib import admin
from django.urls import path
from .views import *
from . import views


# handler404 = views.handler404

urlpatterns=[
    path('',Index),
    path('category/<int:id>/',FilterCategory),
    path('about/',About),
    path('cartpage/',Cart),
    path('addtocart/',AddToCart),
    path('delete/<int:id>/',Delete),
    path('login/',Login),
    path('register/',Register),
    path('logout/',Logout),
    path('shopping/',Shopping),
    path('productsingle/<int:pk>/', ProductDetail.as_view()),
    path('contact/',Contact),
    path('sending_msg/',Sending),
    path('count-savatcha/', CountSavatcha),
    path('blog/',Blog),
    path('blogdetail/<int:pk>/',BlogDetail.as_view())

    # path('mainshop/',MainShop)
    # path('shopfour/',ShopFour),

    # path('base/',Base)
]