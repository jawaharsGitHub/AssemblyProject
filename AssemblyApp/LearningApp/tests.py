from django.test import TestCase
import keyword
#
# print(keyword.kwlist)
# print('--------------')
# print(keyword.softkwlist)
#
# break_ = 8
# print(break_)

class Time:
    def __init__(self, year, month):
        print('calling base class..')
        self.year = year
        self._month = month
        self.__day = 1
        print(year, month)

    # def __str__(self):
    #     return "{}".format(self._month)

    def __repr__(self):
        return "{}".format(self.year)


class TimeSubclass(Time):
    def __init__(self, year, month):
        super().__init__(year, month)
        self._year = 2020
        self.__day = 30

#
# time = Time(2020, 7)
# print(dir(time))

time_subclass = TimeSubclass(2020, 7)
print(dir(time_subclass))
#

# print(time._Time__day)
