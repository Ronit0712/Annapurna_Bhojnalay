from django.http import HttpResponse
from django.shortcuts import redirect, render
from adminApp.models import AdminModel
from tifin_app.models import AboutModel, ContactModel, CustomerListModel, GalleryModel, MaincourseModel, RiceModel, RotiModel, SliderModel
# Create your views here.
def login(r):
    return render(r,"admin/login.html")

def do_login(r):
    # newuser = AdminModel()
    # newuser.username = r.POST['username'],
    # newuser.password = r.POST['password']
    # newuser.save()
    # return HttpResponse ("loged in ")

    check_admin = AdminModel.objects.filter(
        username= r.POST['username'],
        password = r.POST['password']
    )
    if(len(check_admin)>0):
        r.session['user_id']=check_admin[0].id
        # return HttpResponse ("loged in ")
        return redirect("/admin/home")
    else:
        return redirect("/admin")
    

def home(r):
    if(not r.session.has_key('user_id')):
        return redirect("/admin")
    
    sliderimages = SliderModel.objects.all()
    
    return render(r,"admin/home.html",{"sliderimages":sliderimages})

def save_sliderimg(r):
    newsliderimg = SliderModel(
        sliderimg = r.FILES['sliderimg']
    )
    newsliderimg.save()
    return redirect("/admin/home")




# MENU----------------------------------------------------------------------------------
def menu(r):
    if(not r.session.has_key('user_id')):
        return redirect("/admin")
    mccourse = MaincourseModel.objects.all()
    rotis = RotiModel.objects.all()
    rices = RiceModel.objects.all()
    return render(r,"admin/menu.html",{"mccourse":mccourse,"rotis":rotis,"rices":rices})

def save_mcourse(r):
    newmcourse = MaincourseModel(
        mcimg = r.FILES['mcimg']
    )
    newmcourse.save()
    return redirect("/admin/menu")

def delete_mcimg(r):
    MaincourseModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/menu")

def save_roti(r):
    newroti= RotiModel(
        rotiimg = r.FILES['rotiimg']
    )
    newroti.save()
    return redirect("/admin/menu")

def delete_rotiimg(r):
    RotiModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/menu")


def save_rice(r):
    newrice = RiceModel(
        riceimg = r.FILES['riceimg']
    )
    newrice.save()
    return redirect("/admin/menu")

def delete_riceimg(r):
    RiceModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/menu")






# CUSTOMER LIST-------------------------------------------------------------------------
def customer_list(r):
    if(not r.session.has_key('user_id')):
        return redirect("/admin")
    
    customers = CustomerListModel.objects.all()
    return render(r,"admin/customer_list.html",{"customers":customers})

def delete_customer(r):
    CustomerListModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/customer_list")




def about_us(r):
    if(not r.session.has_key('user_id')):
        return redirect("/admin")
    
    abouts = AboutModel.objects.get(id=1)

    
    return render(r,"admin/about_us.html",{"abouts":abouts})

def save_about(r):
    # newabout = AboutModel(
    #     abimg = r.FILES['abimg'],
    #     abdis = r.POST['abdis']
    # )
    # newabout.save()

    updateabout = AboutModel.objects.get(id=1)
    if "abimg" in r.FILES:
        updateabout.abimg = r.FILES['adimg']
    updateabout.abdis = r.POST['abdis']

    updateabout.save()
    return redirect("/admin/about_us")



# Gallery--------------------------------------------------------------------------------

def gallery(r):
    if(not r.session.has_key('user_id')):
        return redirect("/admin")
    
    gallerys = GalleryModel.objects.all()
    return render(r,"admin/gallery.html", {"gallerys":gallerys})

def save_galleryimg(r):
    newgalleryimg = GalleryModel(
        galleryimg = r.FILES['galleryimg']
    )
    newgalleryimg.save()
    return redirect("/admin/gallery")

def delete_galleryimg(r):
    GalleryModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/gallery")




# Contacts -----------------------------------------------------------------------------
def contact_us(r):
    if(not r.session.has_key('user_id')):
        return redirect("/admin")
    contacts = ContactModel.objects.all()
    return render(r,"admin/contact_us.html",{"contacts":contacts})

def change_status_as_paid(r):
    id = r.GET['id']
    cust = CustomerListModel.objects.get(id=id)
    cust.payment_status = "paid"
    cust.save()
    return redirect("/admin/customer_list")