from django.shortcuts import render, HttpResponse
from . import CropIns
from .models import CropInsModel


# Create your views here.


def eservice(request):
    crop = None
    if request.method == 'POST':
        crop = CropIns.CropIns()
        crop.parappu_list = request.POST['parappu']
        crop.acre_amount = request.POST['acreAmount']
        CropIns.CropIns.calc_ins_detail(crop)

        c = CropInsModel(parappu_list=crop.parappu_list, acre_amount=crop.acre_amount, total_cent=crop.total_cent,
                         total_acre=crop.total_acre,total_amount=crop.total_amount, round_amount=crop.round_amount,
                         total_parappu=crop.total_parappu, device_name=crop.device_name)
        c.save()
        print('save into db successfully!')

    return render(request, 'eservice/cropinscalc.html', {'crop': crop})
