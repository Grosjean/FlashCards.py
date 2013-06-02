import random

d = {}

fileLocation = "C:\Users\AlexGrosjean\Documents\Python\FlashCard\state_capitals.txt"

with open(fileLocation,"r") as textDoc:
	for line in textDoc:
		line = line.strip("\n")
		d[line.split(",")[0]] = line.split(",")[1]

print "Hello and welcome to the flash cards game!\n"

while True:
	try:
		numberAttempts = int(raw_input("  - How many attempts would you like at each question?: "))
		break
	except ValueError:
		print "\tOops! Looks like you did not enter a number..."
		

print "\nLet's begin the flash cards!"

letsContinue = True
questionNumber = 1

while letsContinue:
	
	attempts = 1
	
	key = random.choice(d.keys())
	print "\nQuestion # %i" % questionNumber
	
	while attempts <= numberAttempts:
		
		choice = raw_input("  (%i / %i )\t-%s: " % (attempts, numberAttempts, key))
		
		if choice.lower() == d[key].lower():
			
			print "\n\t****** Correct! ******"
			questionNumber += 1
			break
			
		elif choice[:4].lower() == "exit":
			
			letsExit = raw_input("Are you sure you want to exit? (y / n): ")
			
			if letsExit[0].lower() == "y":
				letsContinue = False
				break
				
		else:
			
			attempts += 1
	
	else:
		
		print "\tOut of turns... The answer is: %s" % d[key]
		questionNumber += 1
else:
	print "\n\nThanks for playing!"
	