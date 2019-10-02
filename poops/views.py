from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'Main/index.html')

def Poopsindex(request):
    return render(request,'Poops/Poopsindex.html')