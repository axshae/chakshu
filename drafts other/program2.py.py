print("\n---FIRST PROGRAM IN CHAKSHU PROGRAMMING LANGUAGE----\n\n")
print("**Find factorial of given number n**\n")
def get_fact( number):
	fact=1
	while number>0 :
		fact=fact*number
		number=number-1
		
	print(fact)
	
input_number=input("\nFind factorial of?\nNumber: ")
get_fact(int(input_number))
___temp___=input()
print("\nProgram terminated!")
