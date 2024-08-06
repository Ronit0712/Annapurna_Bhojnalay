from django.shortcuts import redirect, render
from tifin_app.models import AboutModel, ContactModel, CustomerListModel, GalleryModel, MaincourseModel, RiceModel, RotiModel, SliderModel
# from Http import HttpResponse

# Create your views here.
def home(r):
    customers = CustomerListModel.objects.all()
    abouts = AboutModel.objects.get(id=1) 
    gallerys = GalleryModel.objects.all()
    sliderimages = SliderModel.objects.all()
    contacts = ContactModel.objects.all()
    mccourse = MaincourseModel.objects.all()
    rotis = RotiModel.objects.all()
    rices = RiceModel.objects.all()
    return render(r,"home.html",{"customers":customers, "abouts":abouts, "gallerys":gallerys, "sliderimages":sliderimages, "contacts":contacts, "mccourse":mccourse, "rotis":rotis, "rices":rices})

def save_customer(r):
    newcustomer = CustomerListModel(
        cname = r.POST['cname'],
        cmobile = r.POST['cmobile'],
        caddress = r.POST['caddress'],
        cmtype = r.POST['cmtype'],
        cperiod = r.POST['cperiod'],
        cjoindate = r.POST['cjoindate'],
        cpaymode = r.POST['cpaymode'],
        tamount = r.POST['tamount']
    )
    newcustomer.save()
    return redirect("/#registration")
    
def save_contact(r):
    newcontact = ContactModel(
        ctname = r.POST['ctname'],
        ctmno = r.POST['ctmno'],
        ctemail = r.POST['ctemail'],
        ctsubject = r.POST['ctsubject'],
        ctmsg = r.POST['ctmsg']
    )
    newcontact.save()
    return redirect("/#contact")