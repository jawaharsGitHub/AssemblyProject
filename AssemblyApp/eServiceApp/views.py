from django.shortcuts import render, HttpResponse
from . import CropIns


# Create your views here.


def eservice(request):
    crop = None
    if request.method == 'POST':
        crop = CropIns.CropIns()
        crop.parappu_list = request.POST['parappu']
        crop.acre_amount = request.POST['acreAmount']
        CropIns.CropIns.calc_ins_detail(crop)

    return render(request, 'eservice/cropinscalc.html', {'crop': crop})
