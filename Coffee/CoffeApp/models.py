from django.db import models

# Create your models here.
class menu(models.Model):
    mid=models.AutoField
    mname=models.CharField(max_length=90)
    category=models.CharField(max_length=50,default=" ")
    subcategory=models.CharField(max_length=50,default=" ")
    price=models.IntegerField(default=0)
    desc=models.CharField (max_length=300)
    image=models.ImageField( upload_to='images/image', height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.mname

class contact1(models.Model):
    name = models.CharField(max_length = 30)
    emailID = models.EmailField(max_length = 30)
    desc = models.TextField(max_length = 50)
    phone = models.IntegerField() 

    def __str__(self):
        return self.name
    
class orders(models.Model):
    oid = models.AutoField
    item_json = models.CharField(max_length = 300)
    amount = models.IntegerField()
    name = models.CharField(max_length = 300)
    address1 = models.TextField(max_length = 300)
    address2 = models.TextField(max_length = 300)
    city = models.CharField(max_length = 300)
    state = models.CharField(max_length = 300)
    zipcode = models.IntegerField()
    paymentdetails = models.IntegerField()
    phonenumber = models.IntegerField()

    def _str_(self):
        return self.name
    
class orderupdate(models.Model):
    updateID = models.AutoField
    oid = models.IntegerField()
    update_desc = models.CharField(max_length = 300)
    delivered = models.BooleanField()
    timestamp = models.DateField()

    def _str_(self):
        return self.oid
