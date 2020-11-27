from django.shortcuts import render, redirect
from .models import  Contests

def webcam(request):
    return render("webcam.html")