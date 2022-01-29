
from django.shortcuts import render


def error_404(request, exception,*args, **kwargs):
   context = {}
   return render(request,'home/error.html', context)

def error_500(request,*args, **kwargs):
   context = {}
   return render(request,'home/error.html', context)

