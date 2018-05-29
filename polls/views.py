from django.http import HttpResponse

def greet(request):
    return HttpResponse("Hello, adventurer!.")
