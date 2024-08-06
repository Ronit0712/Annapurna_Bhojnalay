from django.urls import path
from adminApp import views

urlpatterns=[
    path('',views.login),
    path('do_login/',views.do_login),

    path('home/',views.home),
    path('save_sliderimg/',views.save_sliderimg),

    path('menu/',views.menu),
    path('save_mcourse/',views.save_mcourse),
    path('save_roti/',views.save_roti),
    path('save_rice/',views.save_rice),

    path('delete_mcimg/',views.delete_mcimg),
    path('delete_rotiimg/',views.delete_rotiimg),
    path('delete_riceimg/',views.delete_riceimg),


    path('customer_list/',views.customer_list),
    path('delete_customer/',views.delete_customer),
    
    path('about_us/',views.about_us),
    path('save_about/',views.save_about),

    path('gallery/',views.gallery),
    path('save_galleryimg/',views.save_galleryimg),
    path('delete_galleryimg/',views.delete_galleryimg),


    path('contact_us/',views.contact_us),
    path('change_status_as_paid/',views.change_status_as_paid),


]