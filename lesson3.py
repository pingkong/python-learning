import math

TESTNUM=600851475143

testrange=range(1,775147)

#if TESTNUM % 2==0:
#	print TESTNUM % 2, 1
#else:
#	print TESTNUM % 2, 2
	
#for i in testrange:
#	testfact=TESTNUM/float(i) 
#	testdiff=testfact-math.floor(TESTNUM/i)
#	if testdiff==0:
#		print testfact, "Is a factor"
#		testrange2=range(2,integer(testfact))
#		for j in testrange2:
#	else:
#		continue
		
for i in testrange:
	if TESTNUM % i == 0: 
		is_not_prime = 0
		#print i, "Is a factor"
		testrange2 = range(2,i-1)
		for j in testrange2:
			if i % j == 0:
		#		print i, "is not prime"
				is_not_prime =1
			else:
				continue	
		if is_not_prime == 0:
			print i, "is prime"
		else:
			continue
	else:
		continue