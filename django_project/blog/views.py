from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the blog home page!")

def about(request):
    return HttpResponse("This is the about page of the blog.")

