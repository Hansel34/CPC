while True:
	num,den = [int(x) for x in input().split()]
	if(num==0 and den == 0):
		break
	print(int(num/den),num%den,"/",den)
