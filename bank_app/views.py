from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
import os
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your views here.


def bankregister(request):
    if request.method=='POST':
        a=bankform(request.POST,request.FILES)
        if a.is_valid():
            firstname=a.cleaned_data['fname']
            lastname=a.cleaned_data['lname']
            username=a.cleaned_data['uname']
            em=a.cleaned_data['email']
            phone=a.cleaned_data['ph']
            ac=int("15"+str(phone))
            fl=a.cleaned_data['file']
            pn=a.cleaned_data['pin']
            rpn=a.cleaned_data['repin']
            if pn == rpn:
                b=bankmodel(fname=firstname,lname=lastname,uname=username,email=em,ph=phone,file=fl,pin=pn,balance=0,acc_num=ac)
                b.save()
                subject="Your account has been created"
                message=f"Your New account number is{ac}"
                email_from="skyviewwwww@gmail.com"
                email_to=em
                send_mail(subject,message,email_from,[email_to])
                return redirect(banklogin)
            else:
                return HttpResponse("Password error")
        else:
            return HttpResponse("Registration failed")

    return render(request,'register.html')

def banklogin(request):
    if request.method=='POST':
        a=indexform(request.POST)
        if a.is_valid():
            username=a.cleaned_data['usname']
            pn=a.cleaned_data['psw']
            b=bankmodel.objects.all()
            for i in b:
                if i.uname==username and i.pin==pn:
                    request.session['id']=i.id
                    return redirect(personal)
            else:
                return HttpResponse("Login failed")
    return render(request,'index.html')

def personal(request):
    try:
      id1=request.session['id']  #id1=1
      a=bankmodel.objects.get(id=id1)
      img=str(a.file).split('/')[-1]
      return render(request,'personal details.html',{'a':a,'img':img})
    except:
        return redirect(banklogin)


def editprofile(request,id):
    a=bankmodel.objects.get(id=id)
    if request.method == 'POST':
        a.fname = request.POST.get('fname')
        a.lname = request.POST.get('lname')
        a.ph = request.POST.get('ph')
        a.email = request.POST.get('email')
        a.uname=request.POST.get('uname')
        a.save()
        return redirect(personal)

    return render(request,'edit profile.html',{'a':a})

def profilepic(request,id):
    a=bankmodel.objects.get(id=id)
    img = str(a.file).split('/')[-1]
    if request.method == 'POST':
        if len(request.FILES)!=0:
            if len(a.file)!=0:
                os.remove(a.file.path)
            a.file=request.FILES['file']
        a.save()
        return redirect(personal)
    return render(request,'profile pic.html',{'a':a,'img':img})

def addamount(request,id):
    x=bankmodel.objects.get(id=id)
    if request.method=='POST':
        am=request.POST.get('amount')
        request.session['am']=am
        x.balance+=int(am)
        x.save()
        b=add_amount(amount=am,uid=request.session['id'])
        b.save()
        pincode=request.POST.get('pincode')
        if int(pincode) == x.pin:
            return redirect(amount_added)
        else:
            return HttpResponse("added failed")
    return render(request,'add amount.html')

def amount_added(request):
    am=request.session['am']
    return render(request,'added success.html',{'am':am})

def withdrawamount(request,id):
    x=bankmodel.objects.get(id=id)
    if request.method=='POST':
        am=request.POST.get('amount')
        request.session['am']=am
        if(int(am)<=int(x.balance)):
          x.balance-=int(am)
          x.save()
          b=withdraw_amount(amount=am,uid=request.session['id'])
          b.save()
          pincode=request.POST.get('pincode')
          if int(pincode) == x.pin:
              return redirect(withdrawsuccess)
          else:
              return HttpResponse("password incorrect")
        else:
            return HttpResponse("Insufficient Balance")
    return render(request,'withdraw.html')

def withdrawsuccess(request):
    am = request.session['am']
    return render(request,'withdraw success.html',{'am':am})

def checkbalance(request,id):
    a=bankmodel.objects.get(id=id)
    if request.method=='POST':
        request.session['balance']=a.balance
        request.session['ac']=a.acc_num
        pin=request.POST.get('pin')
        if int(pin)==a.pin:
            return redirect(balance)
        else:
            return HttpResponse("pssword error")
    return render(request,'check balance.html')

def balance(request):
    ac=request.session['ac']
    balance=request.session['balance']
    return render(request,'balance.html',{'ac':ac,'balance':balance})

def ministate(request,id):
    x=bankmodel.objects.get(id=id)
    pin=request.POST.get('pin')
    if request.method=='POST':
        if int(pin)==x.pin:
            choice=request.POST.get('statement')
            if choice=='deposit':
                return redirect(depositmini)
            elif choice=='withdraw':
                return redirect(wstatement)
        else:
            return HttpResponse("Incorrect password")

    return render(request,'mini statement.html')

def depositmini(request):
    x=add_amount.objects.all()
    id=request.session['id']
    return render(request,'deposit.html',{'x':x,'id':id})

def wstatement(request):
    x=withdraw_amount.objects.all()
    id = request.session['id']
    return render(request,'withdraw statement.html',{'x':x,'id':id})

def notificationview(request):
    if request.method=="POST":
        a=notificationform(request.POST)
        if a.is_valid():
            tp=a.cleaned_data['topic']
            cntn=a.cleaned_data['content']
            b=notificationmodels(topic=tp,content=cntn)
            b.save()
            return HttpResponse("News addedd success")
        else:
            return HttpResponse("Failed")
    return render(request,'notification.html')


from django.contrib.auth import authenticate

def adminlogin(request):
    if request.method=='POST':
        a=adminform(request.POST)
        if a.is_valid():
            us=a.cleaned_data['username']
            ps=a.cleaned_data['password']
            user=authenticate(request,username=us,password=ps)
            if User is not None:
                return redirect(notificationview)
            else:
                return HttpResponse("Login failed")

    return render(request,'admin login.html')

def addnews(reques):
    return render(reques,'add news.html')

def displaynews(request):
    a=notificationmodels.objects.all()
    return render(request,'news display.html',{'a':a})

def newsedit(request):
    a = notificationmodels.objects.all()
    return render(request,'admin news display.html',{'a':a})

def admin_news_edit(request,id):
    a = notificationmodels.objects.get(id=id)
    if request.method == 'POST':
        a.topic = request.POST.get('topic')
        a.content = request.POST.get('content')
        a.save()
        return redirect(displaynews)
    return render(request,'admin news edit.html',{'a':a})

def deletenews(request,id):
    a = notificationmodels.objects.get(id=id)
    a.delete()
    return redirect(newsedit)

def wish(request,id):
    a=notificationmodels.objects.get(id=id)
    a1=wishlist.objects.all()
    for i in a1:
        if i.newsid==a.id and i.uid==request.session['id']:
            return HttpResponse("Item already in wishlist")
    b=wishlist(topic=a.topic,content=a.content,date=a.date,newsid=a.id,uid=request.session['id'])
    b.save()
    return HttpResponse("added to wishlist")

def wish_display(request):
    a = wishlist.objects.all()
    id=request.session['id']
    return render(request,'wishlist display.html', {'a': a,'id':id})

from django.contrib.auth import logout
def logout_veiw(request):
    logout(request)
    return redirect(banklogin)

def forgot_password(request):
    a=bankmodel.objects.all()
    if request.method=='POST':
        em=request.POST.get('email')
        # request.session['em']=em
        ac=request.POST.get('acc_num')
        # request.session['ac']=ac
        for i in a:
            if (i.email==em and i.acc_num==int(ac)):
                id=i.id
                subject="Password Change"
                message=f"http://127.0.0.1:8000/bank_app/changePassword/{id}"
                email_from="skyviewwwww@gmail.com"
                email_to=em
                send_mail(subject,message,email_from,[email_to])
                return HttpResponse("check mail")
        else:
                return HttpResponse("Sorry")
    return render(request,'forgetPassword.html')

def change_password(request,id):
    a=bankmodel.objects.get(id=id)
    if request.method=='POST':
        p1=request.POST.get('pin')
        p2=request.POST.get('repin')
        if p1==p2:
            a.pin=p1
            a.save()
            return HttpResponse("Password Changed Successfully")
        else:
            return HttpResponse("Sorry")
    return render(request,'changepin.html')


def money_transfer(request,id):
    a=bankmodel.objects.get(id=id)
    b=bankmodel.objects.all()
    if request.method=='POST':
        nm=request.POST.get('name')
        ac=request.POST.get('acc')
        am=request.POST.get('amount')
        for i in b:
            if int(ac)==i.acc_num and nm==i.uname:
                if a.balance>int(am):
                    a.balance-=int(am)
                    i.balance+=int(am)
                    i.save()
                    a.save()
                    return HttpResponse("Transfered Successfully")
                else:
                    return HttpResponse("Insufficient balance")
        else:
            return HttpResponse("user not found")
    return render(request,'moneytransfer.html')



