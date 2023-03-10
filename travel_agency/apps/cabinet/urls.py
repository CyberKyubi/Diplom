from django.urls import path

from . import views


urlpatterns = [
    path('registration/', views.register_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('cabinet/', views.cabinet, name='cabinet'),

]