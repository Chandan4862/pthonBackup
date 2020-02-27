x = int(input("Enter a number to check grades"))
if x<=300:
	print("A+")
else:
	if x<=500:
		print("B+")
	else:
		if x<=800:
			print("c+")
		else:
			print("TRY AGAIN")
