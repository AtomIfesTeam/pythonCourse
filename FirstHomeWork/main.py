from accounts import Account



a = Account()

print(a.total)

a.credit(10)

a.write_off(15)

a.credit(3)

print(a.total)

for charge in a:
	print(charge.value)