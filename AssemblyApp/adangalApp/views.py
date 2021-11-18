from django.shortcuts import render, HttpResponse
from Common.Tamilnadu import TNapi
# from static import tnDataSource

# Create your views here.


def adangal(request):
    #data = TNapi.get_subdiv(17, '05', 652, 243)
    #print(data)
    districts = TNapi.get_districts()
    print(districts)
    return render(request, 'adangal/adangal_home.html')


