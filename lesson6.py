testrange = range(1,101)

sumrange=sum(testrange)

sumrangesquared=sumrange*sumrange

print sumrangesquared

squaresum=0

for i in testrange:
	squareterm=i*i
	squaresum=squaresum+squareterm
	
print sumrangesquared-squaresum