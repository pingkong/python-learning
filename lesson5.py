test_num = 2520

#test_range = range(1,11)
#test_range = [3,4,6,7,8,9]
test_range = [11,12,13,14,15,16,17,18,19]
print test_range
test_complete=[1]
test_num=20

while max(test_complete)<19:
	test_num = test_num+20
	test_complete=[1]
	for i in test_range:
		if test_num % i != 0:
			break
		else:
			test_complete.append(i)
			continue


print test_num
print test_complete