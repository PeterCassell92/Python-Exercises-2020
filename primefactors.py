
##takes any int and builds its prime factors into an array excluding 1.
def findPrimeFactorArray(num):
	x = 2
	arr = [];

	while (x <= num):

		if not isPrime(x):
			x+=1
			continue;

		if(num % x ==0):
			arr.append(x)
			num = num / x
			x = 2

		x+=1
		#print(arr)
	print(arr)
	return arr


def isPrime(num):
	for x in range (1,num):	
		if(num % x ==0 and x != 1 and x !=num):
			return False
	## if shown to have no factors other than itself and 1 it is prime.
	return True



#Tests
assert (findPrimeFactorArray(630) == [2, 3 ,3 ,5 ,7])
assert (findPrimeFactorArray(13) == [13] )
