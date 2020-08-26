from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("Welcome to home page")
    context = {
        "x": "This is SENT",
        "y": "Hello!!!!"

    }
    return render(request,"index.html")


def about(request):
    #return HttpResponse("Welcome to About page")
    return render(request,"about.html")

def services(request):
    #return HttpResponse("Welcome to services page")
    return render(request,"services.html")

def contact(request):
    #return HttpResponse("Welcome to contact page")
    return render(request,"contact.html")

def product(request):
    return render(request,"product.html")



