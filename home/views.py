from django.shortcuts import render ,redirect
from .models import Record
# Create your views here.
def signup(request):
    if request.method=="POST":
        name=request.POST['ename']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['pass']
        if Record.objects.filter(mobile=mobile):
            error = 'yes'
            return render(request, 'signup.html', {'error': error})
        else:
            Record(ename=name, email=email, mobile=mobile, password=password).save()
            ok = 'no'
            a = Record.objects.all()
            return render(request, 'showdata.html', {'ok': ok, 'd': a})
    return render(request,'signup.html',locals())


def showdata(request):
    a=Record.objects.all()
    return render(request,'showdata.html',{'d':a})

def update(request,id):
    if request.method=="POST":
        pi=Record.objects.get(pk=id)
        pi.ename=request.POST['ename']
        pi.email=request.POST['email']
        pi.mobile=request.POST['mobile']
        pi.password=request.POST['pass']
    
        pi.save()

        return redirect('signup')


    return render(request,'updatedata.html',{'id':id})

def deletedata(request,id):
    if request.method=="GET":
        pi=Record.objects.get(pk=id)
        pi.delete()
        return redirect('showdata')
    return render(request,'deletedata.html')