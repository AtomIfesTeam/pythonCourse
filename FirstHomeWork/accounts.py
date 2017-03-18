
from charges import Charge


class Account(object):
	def __init__(self, new_total=0):
		self.total = 0
		self.charges = []
		self.charges_cnt = 0

	def __calc_new_total(self, value_to_append):
		self.total = max(0, self.total + value_to_append)

	def credit(self, new_value):
		new_charge = Charge(new_value)
		self.charges.append(new_charge)
		self.__calc_new_total(new_charge.value)
		self.charges_cnt += 1

	def write_off(self, new_value):
		self.credit(-new_value)

	def __iter__(self):
		return iter(self.charges)