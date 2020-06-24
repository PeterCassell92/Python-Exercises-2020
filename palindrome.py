import re
import math

def isPalindrome(text):
	##format string
	text = text.lower()
	pattern =  re.compile(r'\W|\s+')
	text = re.sub(pattern, "", text)

	print(text)
	print(str(len(text)))
	if not len(text) > 1:
		return False

	print(text)
	x = 0
	while ((x + 1) <= (math.ceil(len(text))/2)):
		if not text[x] == text[len(text) -1 -x]:
			return False
		else:
			x +=1
	return True

assert isPalindrome("Hello W;orld") == False
assert isPalindrome("Race car")  == True