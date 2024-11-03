# 1

class Car:
    def __init__(self, model, rang, yil, narx):
        self.__model = model
        self.__rang = rang
        self.__yil = yil
        self.__narx = narx

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @model.deleter
    def model(self):
        del self.__model

    @property
    def rang(self):
        return self.__rang

    @rang.setter
    def rang(self, value):
        self.__rang = value

    @rang.deleter
    def rang(self):
        del self.__rang

    @property
    def yil(self):
        return self.__yil

    @yil.setter
    def yil(self, value):
        self.__yil = value

    @yil.deleter
    def yil(self):
        del self.__yil

    @property
    def narx(self):
        return self.__narx

    @narx.setter
    def narx(self, value):
        self.__narx = value

    @narx.deleter
    def narx(self):
        del self.__narx

# 2

class Person:
    def __init__(self, ism, yosh, kasb, manzil):
        self.__ism = ism
        self.__yosh = yosh
        self.__kasb = kasb
        self.__manzil = manzil

    @property
    def ism(self):
        return self.__ism

    @ism.setter
    def ism(self, value):
        self.__ism = value

    @ism.deleter
    def ism(self):
        del self.__ism

    @property
    def yosh(self):
        return self.__yosh

    @yosh.setter
    def yosh(self, value):
        self.__yosh = value

    @yosh.deleter
    def yosh(self):
        del self.__yosh

    @property
    def kasb(self):
        return self.__kasb

    @kasb.setter
    def kasb(self, value):
        self.__kasb = value

    @kasb.deleter
    def kasb(self):
        del self.__kasb

    @property
    def manzil(self):
        return self.__manzil

    @manzil.setter
    def manzil(self, value):
        self.__manzil = value

    @manzil.deleter
    def manzil(self):
        del self.__manzil

# 3

class Employee:
    def __init__(self, ism, lavozim="Developer", oylik=0, kompaniya=""):
        self.__ism = ism
        self.__lavozim = lavozim
        self.__oylik = oylik
        self.__kompaniya = kompaniya

    @property
    def ism(self):
        return self.__ism

    @ism.setter
    def ism(self, value):
        self.__ism = value

    @ism.deleter
    def ism(self):
        del self.__ism

    @property
    def lavozim(self):
        return self.__lavozim

    @lavozim.setter
    def lavozim(self, value):
        self.__lavozim = value

    @lavozim.deleter
    def lavozim(self):
        del self.__lavozim

    @property
    def oylik(self):
        return self.__oylik

    @oylik.setter
    def oylik(self, value):
        self.__oylik = value

    @oylik.deleter
    def oylik(self):
        del self.__oylik

    @property
    def kompaniya(self):
        return self.__kompaniya

    @kompaniya.setter
    def kompaniya(self, value):
        self.__kompaniya = value

    @kompaniya.deleter
    def kompaniya(self):
        del self.__kompaniya

# 4

import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    @radius.deleter
    def radius(self):
        del self.__radius

    @property
    def diametr(self):
        return self.__radius * 2

    @property
    def yuzasi(self):
        return math.pi * (self.__radius ** 2)

    @property
    def aylana_uzunligi(self):
        return 2 * math.pi * self.__radius

# 5

class BankAccount:
    def __init__(self, mijoz_ismi, hisob_raqami, balans=0, foiz_stavkasi=0):
        self.__mijoz_ismi = mijoz_ismi
        self.__hisob_raqami = hisob_raqami
        self.__balans = balans
        self.__foiz_stavkasi = foiz_stavkasi

    @property
    def mijoz_ismi(self):
        return self.__mijoz_ismi

    @mijoz_ismi.setter
    def mijoz_ismi(self, value):
        self.__mijoz_ismi = value

    @mijoz_ismi.deleter
    def mijoz_ismi(self):
        del self.__mijoz_ismi

    @property
    def hisob_raqami(self):
        return self.__hisob_raqami

    @hisob_raqami.setter
    def hisob_raqami(self, value):
        self.__hisob_raqami = value

    @hisob_raqami.deleter
    def hisob_raqami(self):
        del self.__hisob_raqami

    @property
    def foiz_stavkasi(self):
        return self.__foiz_stavkasi

    @foiz_stavkasi.setter
    def foiz_stavkasi(self, value):
        self.__foiz_stavkasi = value

    @foiz_stavkasi.deleter
    def foiz_stavkasi(self):
        del self.__foiz_stavkasi

    @property
    def balans(self):
        return self.__balans

    def add_balance(self, amount):
        self.__balans += amount

# 6

import math

class Calculator:
    pi = 3.14159

    def __init__(self, raqam1, raqam2, operatsiya):
        self.__raqam1 = raqam1
        self.__raqam2 = raqam2
        self.__operatsiya = operatsiya

    @property
    def raqam1(self):
        return self.__raqam1

    @raqam1.setter
    def raqam1(self, value):
        self.__raqam1 = value

    @raqam1.deleter
    def raqam1(self):
        del self.__raqam1

    @property
    def raqam2(self):
        return self.__raqam2

    @raqam2.setter
    def raqam2(self, value):
        self.__raqam2 = value

    @raqam2.deleter
    def raqam2(self):
        del self.__raqam2

    @property
    def operatsiya(self):
        return self.__operatsiya

    @operatsiya.setter
    def operatsiya(self, value):
        self.__operatsiya = value

    @operatsiya.deleter
    def operatsiya(self):
        del self.__operatsiya

    def hisobla(self):
        try:
            if self.__operatsiya == "+":
                return self.__raqam1 + self.__raqam2
            elif self.__operatsiya == "-":
                return self.__raqam1 - self.__raqam2
            elif self.__operatsiya == "*":
                return self.__raqam1 * self.__raqam2
            elif self.__operatsiya == "/":
                return self.__raqam1 / self.__raqam2
            else:
                return "Noto'g'ri operatsiya turi yuborildi!"
        except Exception as e:
            return e

    @classmethod
    def aylana_yuzasi(cls, radius):
        return cls.pi * (radius ** 2)

# 7

class MathUtils:
    def __init__(self, raqam1, raqam2):
        self.__raqam1 = raqam1
        self.__raqam2 = raqam2
        self.__kopaytma = self.__raqam1 * self.__raqam2
        self.__yigindi = self.__raqam1 + self.__raqam2

    @property
    def raqam1(self):
        return self.__raqam1

    @raqam1.setter
    def raqam1(self, value):
        self.__raqam1 = value
        self.__update_values()

    @property
    def raqam2(self):
        return self.__raqam2

    @raqam2.setter
    def raqam2(self, value):
        self.__raqam2 = value
        self.__update_values()

    @property
    def kopaytma(self):
        return self.__kopaytma

    @property
    def yigindi(self):
        return self.__yigindi

    def __update_values(self):
        self.__kopaytma = self.__raqam1 * self.__raqam2
        self.__yigindi = self.__raqam1 + self.__raqam2

# 8

class Book:
    def __init__(self, nomi, muallifi, nashr_yili, narxi):
        self.__nomi = nomi
        self.__muallifi = muallifi
        self.__nashr_yili = nashr_yili
        self.__narxi = narxi

    @property
    def nomi(self):
        return self.__nomi

    @nomi.setter
    def nomi(self, value):
        self.__nomi = value

    @nomi.deleter
    def nomi(self):
        del self.__nomi

    @property
    def muallifi(self):
        return self.__muallifi

    @muallifi.setter
    def muallifi(self, value):
        self.__muallifi = value

    @muallifi.deleter
    def muallifi(self):
        del self.__muallifi

    @property
    def nashr_yili(self):
        return self.__nashr_yili

    @nashr_yili.setter
    def nashr_yili(self, value):
        self.__nashr_yili = value

    @nashr_yili.deleter
    def nashr_yili(self):
        del self.__nashr_yili

    @property
    def narxi(self):
        return self.__narxi

    @narxi.setter
    def narxi(self, value):
        self.__narxi = value

    @narxi.deleter
    def narxi(self):
        del self.__narxi

    def __str__(self):
        return (f"Kitob: {self.__nomi}\nMuallif: {self.__muallifi}\nNashr Yili: {self.__nashr_yili}\nNarxi: {self.__narxi}")

