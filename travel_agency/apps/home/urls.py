from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='homepage'),
    path('info/bilety/pravila', views.info_section, name='tickets'),
    path('info/bilety/pravila_bronirovanija_aviabiletov', views.booking_rules, name='booking-rules'),
    path('info/turistam/otdel_prodazh', views.sales_department, name='sales-department'),
    path('info/turistam/usloviya_bronirovaniya', views.booking_conditions, name='booking-conditions'),
    path('info/o_kompanii/o_nas', views.about_company, name='about-company'),
    path('info/o_kompanii/kontakty_otdelov', views.department_contacts, name='department-contacts'),
    path('info/o_kompanii/adres', views.address, name='address'),
]