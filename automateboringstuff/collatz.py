def collatz(number): 
	if (int(number)%2 == 0):
		return int(number)//2
	else :
		return 3*int(number) + 1
print "enter number: "
a= raw_input()
while(a > 1): 	
	print str(collatz(a))
	a = collatz(a)
 
