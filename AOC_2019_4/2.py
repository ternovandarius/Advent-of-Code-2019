def verify(nr):
	prev_digit=nr//100000
	digit_count=[0]*10
	for i in range(4,-1,-1):
		x=10**i
		curr_digit=nr//x%10
		if prev_digit<curr_digit:
			prev_digit=curr_digit
		else:
			if prev_digit==curr_digit:
				digit_count[prev_digit]+=1
			else:
				return False
	for i in digit_count:
		if i==1:
			return True
	return False
	
def main():
	nr=0
	for i in range(402328, 864248, 1):
		if verify(i):
			nr+=1
	print(nr)
	
main()