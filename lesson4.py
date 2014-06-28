my_integer=9009

number_string=str(my_integer)
stitch_num = ''
str_length=len(number_string)

for ch in number_string:
	print ch
	stitch_num = stitch_num+ch
	reverse_st=stitch_num[::-1]
	
print stitch_num, reverse_st

if stitch_num==reverse_st:
	print "They the same!!"
else:
	print "They ain't the same bro!!"