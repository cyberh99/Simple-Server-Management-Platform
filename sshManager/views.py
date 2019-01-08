from django.views.generic import TemplateView
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = 'home.html'

def error404(request):
    data = {}
    return render(request,'error/404.html',context=data)    

def error500(request):
    data = {}
    return render(request,'error/500.html',context=data)    