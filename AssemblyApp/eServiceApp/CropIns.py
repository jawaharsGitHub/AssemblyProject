import math
import os


class CropIns:
    def __init__(self):
        pass

    parappu_list = []
    acre_amount = 0
    total_cent = 0
    total_acre = 0.0
    total_amount = 0.0
    round_amount = 0
    total_parappu = ''
    device_name = ''

    def parappu_sum(self, hec_sum, ares_sum, ares2_sum):
        hec = (hec_sum + (ares_sum // 100))
        ares = str((ares_sum % 100) + (ares2_sum // 100))
        ares2 = str(ares2_sum % 100)
        return f"{int(hec)}.{ares.zfill(2)}.{ares2}"

    def calc_ins_detail(self):
        # https://www.legendfoundations.in/post/all-you-need-to-know-about-land-measurements-in-tamil-nadu
        # hectare.ares
        # 1 hectare	= 247.10538 cents
        # 1 Ares = 2.47 Cent

        hectare = []
        ares = []
        ares2 = []

        for p in self.parappu_list.splitlines():
            hectare.append(int(p.split('.')[0]))
            ares.append(int(p.split('.')[1]))
            if len(p.split('.')) == 3:
                ares2.append(int(p.split('.')[2]))
            else:
                ares2.append(0)

        hec_sum, ares_sum, ares2_sum = sum(hectare), sum(ares), sum(ares2)

        hectare_cent = hec_sum * 100 * 2.47
        ares_cent = ares_sum * 2.47
        ares2_cent = (ares2_sum/100) * 2.47

        self.total_cent = round(hectare_cent + ares_cent + ares2_cent, 2)
        self.total_acre = self.total_cent / 100
        self.total_amount = self.total_acre * int(self.acre_amount)
        self.round_amount = "ரூ.{}".format(round(self.total_amount))
        self.total_parappu = self.parappu_sum(hec_sum, ares_sum, ares2_sum)
        self.device_name = os.getlogin()
