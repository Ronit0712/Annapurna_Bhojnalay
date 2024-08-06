from django.db import models

# Create your models here.
class CustomerListModel(models.Model):
    cname = models.CharField(max_length= 100)
    cmobile = models.CharField(max_length= 15)
    caddress = models.TextField()
    cmtype = models.CharField(max_length= 20)
    cperiod = models.CharField(max_length= 20)
    cjoindate = models.DateField()
    cpaymode = models.CharField(max_length= 20)
    tamount = models.CharField(max_length= 10)
    payment_status = models.CharField(max_length=20,default="pending")


class AboutModel(models.Model):
    abimg = models.ImageField(upload_to="static/user/uploads/")
    abdis = models.TextField()


class GalleryModel(models.Model):
    galleryimg = models.ImageField(upload_to="static/user/uploads/") 


class SliderModel(models.Model):
    sliderimg = models.ImageField(upload_to="static/user/uploads/")

class ContactModel(models.Model):
    ctname = models.CharField(max_length=100)
    ctmno = models.CharField(max_length=15)
    ctemail = models.EmailField(default="true")
    ctsubject = models.CharField(max_length=100)
    ctmsg = models.TextField(default="true")


class MaincourseModel(models.Model):
    mcimg = models.ImageField(upload_to="static/user/uploads/")

class RotiModel(models.Model):
    rotiimg = models.ImageField(upload_to="static/user/uploads/")

class RiceModel(models.Model):
    riceimg = models.ImageField(upload_to="static/user/uploads/")