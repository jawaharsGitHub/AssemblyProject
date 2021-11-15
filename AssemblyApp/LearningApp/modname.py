from urllib.request import urlopen
import smtplib


the_answer = 10

def email():
    server = smtplib.SMTP('localhost')
    server.sendmail('jawahar.subramanian83@gmail.com', 'jawahar.subramanian83@gmail.com')



class Bus:
    """about class"""
    i = 10

    def __init__(self):
        self.i = 20


    def fn(self):
        print('do action')
        self.i = 45

class Employee:

    def Test(self):
        for x in "567":
            print(x)

    pass


class Reverse:

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
            return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

    def Test(self):
        for x in self:
            print(x)


class WebScrap:

    def GoldRate(self):
        with urlopen('https://www.goodreturns.in/gold-rates/chennai.html') as res:
            for line in res:
                line = line.decode('utf-8')
                if '22ct' in line:
                    print(line)













