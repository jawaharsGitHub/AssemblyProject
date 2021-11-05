import math


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

    def parappu_sum(self, hec_sum, ares_sum):
        hec = (hec_sum + ares_sum // 100)
        ares = ares_sum % 100
        # sf = sqft
        return f"{int(hec)}.{format(round(ares,2), '.2f')}"
        #return f"{int(hec)}.{round(ares, 2)}"

    def calc_ins_detail(self):
        # https://www.legendfoundations.in/post/all-you-need-to-know-about-land-measurements-in-tamil-nadu
        # hectare.ares.sqft
        # 1 hectare	= 247.10538 cents
        # 1 Ares = 2.47 Cent

        hectare = []
        ares = []

        # hectare, ares, sqft = [int(p.split('.')[0]), int(p.split('.')[1]), int(p.split('.')[2]) for p in
        # parappu_list.splitlines()]

        for p in self.parappu_list.splitlines():
            hectare.append(int(p[:p.index('.')]))
            ares.append(float(p[p.index('.') + 1:]))

        hectare_cent = sum(hectare) * 100 * 2.47
        ares_cent = sum(ares) * 2.47

        self.total_cent = round(hectare_cent + ares_cent,2)
        self.total_acre = self.total_cent / 100
        self.total_amount = self.total_acre * int(self.acre_amount)
        self.round_amount = "ரூ.{}".format(round(self.total_amount))
        self.total_parappu = self.parappu_sum(sum(hectare), sum(ares))
