class Car:

	def __init__(self, make, model, year):
		"""Iniciarlizar"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Devuelve un nombre descriaptivo con formato adecuado"""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		print(f"El coche lleva {self.odometer_reading} computados")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

class ElectricCar(Car):
	"""Herencia entre clases"""
	def __init__(self, make, model, year):
		"""Inicializa los atributos de la clase base"""
		super().__init__(make, model, year) #atributos de la clase base
		self.battery_size = 75

	def describe_battery(self):
		print(f"El tamaño de la bateria es de {self.battery_size}")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()