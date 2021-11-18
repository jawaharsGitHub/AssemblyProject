from django.shortcuts import render, HttpResponse

# Create your views here.


def adangal(request):
    return render(request, 'adangal/adangal_home.html')

