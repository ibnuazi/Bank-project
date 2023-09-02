from django.db import models

# Create your models here.

class indexmodel(models.Model):
    fname=models.CharField(max_length=30)
    pin=models.IntegerField()

class bankmodel(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    uname = models.CharField(max_length=20)
    email = models.EmailField()
    ph = models.IntegerField()
    acc_num=models.IntegerField()
    file = models.FileField(upload_to='bank_app/static')
    pin = models.IntegerField()
    balance=models.IntegerField()

class add_amount(models.Model):
    uid = models.IntegerField()
    amount=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.uid

class withdraw_amount(models.Model):
    uid=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.uid

class notificationmodels(models.Model):
    topic=models.CharField(max_length=50)
    content=models.CharField(max_length=1000)
    date=models.DateField(auto_now_add=True)

class ministatement(models.Model):
    choice=[
        ('withdraw','withdraw'),
        ('deposit','deposite')
    ]
    statement=models.IntegerField(choices=choice)

class wishlist(models.Model):
    uid=models.IntegerField()
    newsid=models.IntegerField()
    topic = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    date = models.DateField()


class moneymodel(models.Model):
    name=models.CharField(max_length=20)
    acc=models.IntegerField()
    amount=models.IntegerField()
