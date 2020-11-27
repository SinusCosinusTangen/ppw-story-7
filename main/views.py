from django.http import request
from django.shortcuts import render, redirect

# Create your views here.
def main(request):
    return render(request, 'main/index.html')