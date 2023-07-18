#from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'home.html'

#override get context date method
def get_context_sata(self, **kwargs):
    context = super('').get_context_data(**kwargs) #first call super get contxt data
    context['about'] = About.objects.first()
    context['services'] = Service.objects.all()
    context['works'] = Recent_Work.objects.all()
    return context
