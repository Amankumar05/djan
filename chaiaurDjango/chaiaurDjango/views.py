from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, Django! welcome to Home Page")

def About(request):
    return HttpResponse("Hello, Django! welcome to About Page")


def contact(request):
    return HttpResponse("Hello, Django! contact Page")
