# 1

# from mainClass import Car
#
# car = Car("Toyota", "Qizil", 2021, 20000)
# print(car.__dict__)

# car.model = "Tesla"
# car.rang = "Qora"
# car.yil = 2023
# car.narx = 100000
# print(car.__dict__)

# del car.model
# del car.rang
# del car.yil
# del car.narx
# print(car.__dict__)

# 2

# from mainClass import Person
#
# person = Person("Toxir", 30, "Dasturchi", "Toshkent")
# print(person.__dict__)

# person.ism = "Sobir"
# person.yosh = 35
# person.kasb = "Muhandis"
# person.manzil = "Samarqand"
# print(person.__dict__)

# del person.ism
# del person.yosh
# del person.kasb
# del person.manzil
# print(person.__dict__)

# 3

# from mainClass import Employee
#
# employee = Employee("Toxir", "Manager", 3000, "UZCARD")
# print(employee.__dict__)
#
# employee.ism = "Sobir"
# employee.lavozim = "Senior Developer"
# employee.oylik = 4000
# employee.kompaniya = "CCTLD"
# print(employee.__dict__)
#
# del employee.ism
# del employee.lavozim
# del employee.oylik
# del employee.kompaniya
# print(employee.__dict__)

# 4

# from mainClass import Circle
#
# circle = Circle(5)
# print(circle.__dict__)
# circle.radius = 10
# print(circle.__dict__)
# del circle.radius
# print(circle.__dict__)

# 5

# from mainClass import BankAccount
#
# account = BankAccount("Toxir", "UZ123456789", 1000, 5)
# print(account.__dict__)
#
# account.mijoz_ismi = "Sobir"
# account.hisob_raqami = "UZ987654321"
# account.add_balance(500)
# print(account.__dict__)
#
# del account.mijoz_ismi
# del account.foiz_stavkasi
# del account.hisob_raqami
# print(account.__dict__)

# 6

# from mainClass import Calculator
#
# calc = Calculator(10, 2, "/")
# print(f"Natija: {calc.hisobla()}\nAylananing yuzasi: {Calculator.aylana_yuzasi(5)}")

# 7

from mainClass import MathUtils

math = MathUtils(2, 3)
print(f"Yig'indisi: {math.yigindi}\nKo'paytmasi: {math.kopaytma}")

# 8

# from mainClass import Book
#
# book = Book("Shum bola", "G'ofir G'ulom", 1951, 50000)
# print(book)