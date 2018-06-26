def scope(n): #calculate n iteratively
	result=1
	if n>1:
		for i in range(2,n+1):
			result=result*i
	return result

def factorial(n): # n! can be defined as n*(n-1)!
	if n<=1:
		return 1
	else:
		return n*factorial(n-1)

def fib(n):
	result=0
	if n<=2:
		return 1
	else:
		return fib(n-1)+fib(n-2)

for i in range(35):
	print(i,fib(i))
