#Prime nos in the range a to b

#Numbers in the range from 1 to 50
for num in range (2 , 200):	
	#modulus divide the number with all the numbers that are smaller than that number
	for i in range (2 , num):
		if num%i == 0:
			j=num/i
			print("%d equals %d*%d")%(num,i,j)
			break
        else:
    		#print("%d is a prime number")%(num) 
    		print num, 'is a prime number'
