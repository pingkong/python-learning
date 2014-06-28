a=1
b=1
LIMIT = 4000000
c=1
print a
print b
fib_sum = a+b

while c < LIMIT:
	a=b
	b=c
	c = b+a
	if c>=LIMIT:
		break
	else:
		if c % 2:
			fib_sum = fib_sum + c
		#	print c, fib_sum
		else:
			fib_sum = fib_sum
		#	print c, fib_sum
			
print fib_sum