from django.shortcuts import render

# Create your views here.
def loop(request):
    d={'name':'Nila','age':'6'}
    return render(request,'loop.html',d)