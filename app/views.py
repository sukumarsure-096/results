from django.shortcuts import render

# Create your views here.
from app.models import *
from app import forms

def ml(request):
    d = exam.objects.all()
    return render(request,'h1.html',context={'d':d})
'''
def c_ml(request):
    d = exam.objects.all()
    if request.method == 'POST':
        ht = request.POST.get('ht')
        n = request.POST.get('n')
        t = request.POST.get('t')
        h = request.POST.get('h')
        e = request.POST.get('e')
        m = request.POST.get('m')
        s = request.POST.get('s')
        so = request.POST.get('so')
        a = exam.objects.get_or_create(hallticket=ht,Name=n,t=t,h=h,e=e,m=m,s=s,so=so)[0]
        a.save()
        d = exam.objects.all()
        return render(request,'c_m.html')
    return render(request,'c_m.html')

def f_ml(request):
    form = forms.flist()
    if request.method == 'POST':
        form = forms.flist(request.POST)
        if form.is_valid():
            ht = form.cleaned_data.get('hall')
            d = exam.objects.filter(hallticket=ht)
            #d = exam.objects.filter(Name=nam)
            return render(request,'r.html',context={'d':d})
        
    return render(request,'form.html',context={'form':form})'''

def v_ml(request):
    form = forms.valid()
    if request.method == 'POST':
        form = forms.valid(request.POST)
        if form.is_valid():
            ans = form.cleaned_data.get('hall')
            d = exam.objects.filter(hallticket=ans)
            return render(request,'r.html',context={'d':d})
    return render(request,'form.html',context={'form':form})

def home(request):
    return render(request,'home.html')