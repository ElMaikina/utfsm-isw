from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("Hola San Benito!")
    return render(request,"index.html")



