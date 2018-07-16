from django.http import HttpResponse

def hello(request):
	return HttpResponse("Hello, World!")

def homepage(request):
	return HttpResponse("olar")