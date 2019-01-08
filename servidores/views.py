from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404
from .forms import ServerCreationForm
from .models import Servidor
# Create your views here.


def servidores(request):
    if not  request.user.is_authenticated:
        return HttpResponseRedirect("/")
    if request.method == "POST":
        serverForm = ServerCreationForm(request.POST)
        if serverForm.is_valid():
              server = serverForm.save(commit=False)
              server.save()
    serverForm = ServerCreationForm()
    server = Servidor()
    context = {'form':serverForm,
               'servers':Servidor.objects.all() 
               }
    return render(request,'servidores.html',context=context)


def serverInfo(request,serverName):
    if not  request.user.is_authenticated:
        return HttpResponseRedirect("/")
    server = get_object_or_404(Servidor,name=serverName)
    context = {'server':server}
    return render(request,'serverInfo.html',context=context)