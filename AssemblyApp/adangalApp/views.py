from django.shortcuts import render, HttpResponse
from Common.Tamilnadu import TNapi
# from static import tnDataSource

# Create your views here.


def adangal(request):
    # if request.method == 'GET':
        districts = TNapi.get_districts()
        taluks = TNapi.get_taluk(17)
        villages = TNapi.get_villages(17, '05')
        print('districts')
        context = {
            'districts': districts,
            'taluks': taluks,
            'villages': villages

        }
        return render(request, 'adangal/adangal_home.html', context)
    # else:
    #     return render(request, 'adangal/adangal_home.html')


