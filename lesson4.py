my_integer=9009
IMAX = 1000
IMIN = 100
JMAX = 1000
JMIN = 100

irange = range(IMIN,IMAX)
jrange = range(JMIN,JMAX)
irange = irange[::-1]
jrange = jrange[::-1]
stitch_num = ''
reverse_st = ''
ibreak=0
palin = []

for i in irange:
	for j in jrange:
		test_int = i*j
		number_string=str(test_int)
		reverse_st=number_string[::-1]
		if number_string==reverse_st:
			palin.append(test_int)
		else:
			continue

print max(palin)

