lst=(0,1,2,3,4,5,6,7,8,9)
even=0
odd=0
for i in lst:
	if i%2==0:
		even+=1
	else:
		odd+=1
		print("count of odd numbers=",odd)
		print("count of even numbers=",even)
		