from django.shortcuts import render
from django.views import generic

from . import models


class HomePage(generic.ListView):
    template_name = 'home/home.html'
    context_object_name = 'homepage'

    def get_queryset(self):
        return models.Countries.objects.all()

    def get_context_data(self, object_list=None, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({'replies': models.Replies.objects.all()})
        return context


def info_section(request):
    return render(request, 'home/info-section/tickets.html')


def booking_rules(request):
    return render(request, 'home/info-section/booking-rules.html')


def sales_department(request):
    return render(request, 'home/info-section/sales-department.html')


def booking_conditions(request):
    return render(request, 'home/info-section/booking-conditions.html')


def about_company(request):
    return render(request, 'home/info-section/about-company.html')


def department_contacts(request):
    return render(request, 'home/info-section/department-contacts.html')


def address(request):
    return render(request, 'home/info-section/address.html')