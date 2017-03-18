
class Charge(object):
	def __init__(self, new_value):
		self._value = new_value

	@property
	def value(self):
		rounded_value = round(self._value, 2)
		return rounded_value