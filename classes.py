# class MyFirstClass:
#     a = 5
#     def add_four(self):
#         self.a+=4
#
#
# my_object = MyFirstClass()
#
# print(my_object.a)
# my_object.add_four()
# print(my_object.a)

# class Car:
#     def __init__(self, _engine_power, _volume_of_fuel, _brand):
#         self.engine_power = _engine_power
#         self.volume_of_fuel = _volume_of_fuel
#         self.brand = _brand
#
#     def __str__(self):
#         return "Brand: " + self.brand + ", Volume: " + str(self.volume_of_fuel) + ", Power: " + str(self.engine_power)
#
# class LuxeCar(Car):
#     def __init__(self, _amount_of_passangers, _engine_power, _volume_of_fuel, _brand):
#         super().__init__(_engine_power, _volume_of_fuel, _brand)
#         self.amount_of_passangers = _amount_of_passangers
#
#     def __str__(self):
#         return "Brand: " + self.brand + ", Volume: " + str(self.volume_of_fuel) + ", Power: " + str(self.engine_power) + ", Amount: " + str(self.amount_of_passangers)
#
# maybach = Car(500, 120, "Mercedes")
#
# print(maybach)
#
# audi = LuxeCar(3, 500, 120, "Audi")
#
# print(audi)

