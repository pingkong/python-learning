sum_3 = 0
sum_5 = 0
sum_15 = 0
i = 1
mult3=3
mult5=5
mult15=15

LIMIT=1000

while mult3 < LIMIT:
	sum_3 = sum_3 + mult3
	i = i+1
	mult3=3*i
	print mult3

i=1	
while mult5 < LIMIT:
	sum_5 = sum_5 + mult5
	i=i+1
	mult5=5*i
	print mult5

i=1	
while mult15 < LIMIT:
	sum_15 = sum_15 + mult15
	i=i+1
	mult15=15*i
	print mult15
	
		
sum = sum_3 + sum_5 - sum_15

print sum