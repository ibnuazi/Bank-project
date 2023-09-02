from django.urls import path
from .views import *


urlpatterns=[
    path('login/',banklogin),
    path('register/',bankregister),
    path('personal details/',personal),
    path('edit profile/<int:id>',editprofile),
    path('edit pic/<int:id>',profilepic),
    path('add amount/<int:id>',addamount),
    path('amount added/',amount_added),
    path('withdraw amount/<int:id>',withdrawamount),
    path('withdraw success/',withdrawsuccess),
    path('check balance/<int:id>',checkbalance),
    path('balance/',balance),
    path('mini statement/<int:id>',ministate),
    path('deposite statement/',depositmini),
    path('withdraw statement/',wstatement),
    path('notifications/',notificationview),
    path('adminlogin/',adminlogin),
    path('addnews/',addnews),
    path('newsdisplay/',displaynews),
    path('admin news view/',newsedit),
    path('admin news edit/<int:id>',admin_news_edit),
    path('admin news delete/<int:id>',deletenews),
    path('wish/<int:id>',wish),
    path('wishlist display/',wish_display),
    path('logout/',logout_veiw),
    path('forget_password/',forgot_password),
    path('changePassword/<int:id>',change_password),
    path('moneytransfer/<int:id>',money_transfer)
    ]