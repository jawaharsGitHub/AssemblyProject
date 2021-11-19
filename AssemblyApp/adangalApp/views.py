from django.shortcuts import render, HttpResponse
from Common.Tamilnadu import TNapi


# from static import tnDataSource

# Create your views here.


def adangal(request):
    districts = TNapi.get_districts()
    context = None
    if request.method == 'GET':
        print('GET')
        context = {
            'districts': districts
        }
        return render(request, 'adangal/adangal_home.html', context)
    elif request.method == 'POST':
        print('POST')

        try:
            mid = request.POST['ddlMaavattam'];
            taluks = TNapi.get_taluk(mid.zfill(2))
            context = {
                'districts': districts,
                'taluks': taluks
            }
        except:
            tid = request.POST['ddlVattam'];
            villages = TNapi.get_villages(mid.zfill(2), tid.zfill(2))
            context = {
                'districts': districts,
                'taluks': taluks,
                'villages': villages
            }

        return render(request, 'adangal/adangal_home.html', context)

        #vid = request.POST['ddlVillage'];
