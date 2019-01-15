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
    
    actualServerObject = get_object_or_404(Servidor,name=serverName)

    if request.method == "POST":        
        form = ServerCreationForm(request.POST)
        if form.is_valid():
            newData = form.cleaned_data
            if (newData["name"] != actualServerObject.name):
                Servidor.objects.filter(ipAddr=newData["ipAddr"]).update(name=str(newData["name"]))
                Servidor.objects.filter(ipAddr=newData["ipAddr"]).update(password=str(newData["ipAddr"]))
        
            Servidor.objects.filter(name=serverName).update(ipAddr=str(newData["ipAddr"]))
            Servidor.objects.filter(name=serverName).update(password=str(newData["password"]))
            return HttpResponseRedirect("/servidores")
    
    form = ServerCreationForm(initial={
        'name':actualServerObject.name,
        'ipAddr':actualServerObject.ipAddr,
        'password':actualServerObject.password,
    })
    return render(request,'serverInfo.html',{'form':form})