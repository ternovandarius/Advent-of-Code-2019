def verify(nr):
	prev_digit=nr//100000
	has_double=False
	for i in range(4,-1,-1):
		x=10**i
		curr_digit=nr//x%10
		if prev_digit<curr_digit:
			prev_digit=curr_digit
		else:
			if prev_digit==curr_digit:
				has_double=True
			else:
				return False
	return has_double
	
def main():
	nr=0
	for i in range(402328, 864248, 1):
		if verify(i):
			nr+=1
	print(nr)
	
main()