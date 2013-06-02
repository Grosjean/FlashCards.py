import random
import sys
from urllib2 import urlopen

print "Hello and welcome to the flash cards game!"
print "\nYou may exit at any time by typing \"exit\"."

d = {}
letsContinue = True
questionNumber = 1

def change_attempts():
	#Allows user to change the number of attempts they get at any time. 
	
	while True:
		try:
			numberAttempts = int(raw_input("\n  - How many attempts would you like at each question?: "))		
			
			if numberAttempts < 1:
				return 1
			
			print ""
			return numberAttempts
		except ValueError:
			print "\tOops! Looks like you did not enter a number..."

def help_menu():
	print "\nYou've reached the help menu!"
	print "Type \"Exit\" to exit the game."
	print "Type"
	choice = raw_input("\nWhat do you need help with? : ")
	
	if choice == "":
		pass
	else:
		pass

def parseInput(choice):
	pass
	
def get_TextDoc():
	#prompts user to decide if they want to play an existing game or open a new one
	while True:
		try:
			
			print "\nWhich game would you like to play?  \n\t1: State Capitals \n\t2: Other (web) \n\t3: Other (local hard drive) \n\t0: Exit"
			choice = int(raw_input("\nEnter number: "))
			
			if choice == 1: #state capitals game
				
				print "\nOpening file...\n"
				return urlopen("https://raw.github.com/Grosjean/FlashCards.py/master/state_capitals.txt")
				
			elif choice == 2: #website
				
				while True:
					try:
						url = raw_input("\nPlease enter the url: ")
						
						if url == "exit":
							break
						
						print "\nOpening file...\n"
						return urlopen(url)
						
					except ValueError:
						print "Could not open file... Try again or enter \"exit\" to change game type."
					except:	
						print "Unhandled Error!! " + sys.exc_info()
						
			elif choice == 3: #local hard drive
				
				print "\nOpening file...\n"
				return urlopen("https://raw.github.com/Grosjean/Scrabble.py/master/sowpods.txt")
			
			elif choice == 0:
				letsContinue = False
				return "Exit"
		
		except ValueError:
			print "\nOpps! I did not recognize that input. Please enter a number."
		except:
			print "Unexpected error!"
		
def createDictionary(textDoc):
	try:
		for line in textDoc:
			line = line.strip("\n")
			d[line.split(",")[0]] = line.split(",")[1]
	except:
		print "It looks like the text file you selected was not in the correct format."
		print "Be sure that the format is \"question\",\"answer\""
		textDoc = get_TextDoc()
		createDictionary(textDoc)

def print_introduction():
	print "Let's begin the flash cards!"
	print "You may enter \"exit\", \"change_cards\", \"change_attempts\" or \"help\" at any time."
	
textDoc = get_TextDoc()

if textDoc != "Exit":
	createDictionary(textDoc)
	print "File opened successfully!"
	numberAttempts = change_attempts()
	print_introduction()
else:
	letsContinue = False
	
while letsContinue:
	
	attempts = 1
	
	key = random.choice(d.keys())
	print "\nQuestion # %i" % questionNumber
	
	while attempts <= numberAttempts:
		
		choice = raw_input("  (%i / %i )\t-%s: " % (attempts, numberAttempts, key)).lower()
		
		if choice == d[key].lower():
			
			print "\n\t****** Correct! ******"
			questionNumber += 1
			break
		
		elif choice[:4] == "help":
			help_menu()
		
		elif choice == "change_attempts":
			numberAttempts = change_attempts()
		
		elif choice == "change_cards":
			
			textDoc = get_TextDoc()
			createDictionary(textDoc)
			print_introduction()
			#letsContinue = False
			break
			
		elif choice[:4] == "exit":
			
			letsExit = raw_input("Are you sure you want to exit? (y / n): ")
			
			if letsExit[0] == "y":
				letsContinue = False
				break
				
		else:
			
			attempts += 1
	
	else:
		
		print "\tOut of turns... The answer is: %s" % d[key]
		questionNumber += 1
else:
	print "\n\nThanks for playing!\n"
	