#Task1: check-digits

def menu1():

	print("         Welcome to the Validator!                   ")
	print(" Choose the desired category                         ")
	print(" 1) Credit Card Validator (using Luhn Algorithm)     ")
	print(" 2) Bar Code Validator for GTIN-13                   ")
	print(" 3) Bar Code Validator for GSIN                      ")
    
	option = input("Please enter the type of validator: ")
	number = input("Please enter the account number: ")
    
	return int(option), number

def generateSum(number): 

	sumOdd = 0
	sumEven = 0

	for i, char in enumerate(number):
			
		pos = i + 1
		if( pos % 2 == 0 ): sumEven += int(char)
		else:
			value = int(char) * 2
			part = (value // 10) 
			part += (value % 10)
			sumOdd += part

	sumTotal = sumOdd + sumEven
	return sumTotal

def LuhnAlgorithm(number): # it is mod10 checksum algorithm

	valid = False
	sumTotal = generateSum(number) # use checksum formula to validate credit card numbers

	if( sumTotal % 10 == 0 ): valid = True
	else: valid = False
	
	return valid

def generateBarCode(number): 

    sumOdd = 0
    sumEven = 0

    for i, char in enumerate(number):

        pos = i + 1
        if( pos % 2 == 0 ): sumEven += int(char)
        else: sumOdd += int(char)

    sumTotal = (sumOdd * 3) + sumEven

    modulo = sumTotal % 10
    checkDigit = 10 - modulo

    if( checkDigit == 10 ): checkDigit = 0

    return ( number + str(checkDigit) )

def GTIN13(number): 

	valid = False
	GTIN13 = generateBarCode(number[0:12])

	if( str(GTIN13) == number ): valid = True
	else: valid = False

	return valid

def GSIN(number):

	valid = False
	GSIN = generateBarCode(number[0:16])

	if( str(GSIN) == number ): valid = True
	else: valid = False

	return valid

option, number = menu1()

if option == 1:

	check = LuhnAlgorithm(number) #16-digit number
	if(check): print('The account number is well-formed.')
	else: print('The account number is not well-formed.')

elif option == 2:

	check = GTIN13(number) #13-digit number
	if(check): print('The account number is well-formed.')
	else: print('The account number is not well-formed.')

elif option == 3:

	check = GSIN(number) #17-digit number 
	if(check): print('The account number is well-formed.')
	else: print('The account number is not well-formed.')

else:
	print('Error')