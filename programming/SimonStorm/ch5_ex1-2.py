numlist = []

while True:
	try:
		inputvalue = input("Input a non-decimal number: ")
		number = int(inputvalue)
		numlist.append(number)
		print("Number added to list!")
	except ValueError:
		if inputvalue == "done":
			print("OK! YO")
			print(f"Numbers added to list: {len(numlist)}")
			average = sum(numlist) / len(numlist)
			print(f"Total average: {int(average)}")
			print(f"Largest number {max(numlist)}")
			print(f"Smallest number {min(numlist)}")
			break
		else:
			print("Ohh ohh, somtink rooong!!")
			break
	except KeyboardInterrupt:
		print("Exiting.....")
		break