from django.shortcuts import render

def index(request):
    context = {
        'title':'DISDAG PRO | BETA',
        'heading':'SELAMAT DATANG',
        'subheading':'di DISADG PRO BETA',
    }
    return render(request,'index.html',context)