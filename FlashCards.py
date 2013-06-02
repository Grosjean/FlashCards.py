import os, os.path, time, sys, random
from urllib2 import urlopen

#Author: Alex Grosjean
#Date: 2 June 2013
#Second Python Program

#This program command prompt based allows user to test themselves in a flash card style game
#The user can select either from three pre-programmed games
#or choose their own file from the internet or local hard drive.

#Be sure to read the readme.txt as the custom files must have a specific format
#The each Q&A must be on their own line, and split by a :
#	Question:Answer
#If it's not in this format, the program will return you an error saying such

d = {}
letsContinue = True
questionNumber = 1
numberAttempts = 1

def get_TextDoc():
	"""prompts user to decide if they want to play an existing game or open a new one.
	loops indefinitely until a proper selection is made."""
	
	while True:
		
		try:
			
			print("\nWhich game would you like to play?"  
			"\n\t1: State Capitals" 
			"\n\t2: History Quiz" 
			"\n\t3: Basic Math Quiz" 
			"\n\t-"
			"\n\t8: Other (from web url)" 
			"\n\t9: Other (from local hard drive)" 
			"\n\t0: Exit")
				
			choice = int(raw_input("\nEnter number: "))
			
			if choice == 1: #state capitals game
				
				print "\nOpening file...\n"
				return urlopen("https://raw.github.com/Grosjean/FlashCards.py/master/Quizzes/state_capitals.txt")
				
			elif choice == 2: #state history quiz
				
				print "\nOpening file...\n"
				return urlopen("https://raw.github.com/Grosjean/FlashCards.py/master/Quizzes/history_quiz.txt")
			
			elif choice == 3: #basic math quiz
				print "\nOpening file...\n"
				return urlopen("https://raw.github.com/Grosjean/FlashCards.py/master/Quizzes/math_quiz.txt")
			
			elif choice == 7:  #testing a non-working file
				
				print "\nOpening file...\n"
				return urlopen("https://raw.github.com/Grosjean/Scrabble.py/master/sowpods.txt")
			
			elif choice == 8: #website
				
				print "\n\tYou may exit this function at any time by typing \"exit\"."
				
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
						print "Un-handled Error!! " + sys.exc_info()
						
			elif choice == 9: #local hard drive
				
				fileLocation = get_fileLocation()
				
				if fileLocation != "Exit":
					print "\nOpening File..."
					textFile = open(fileLocation,"r")
					return textFile

			elif choice == 0:
				
				letsContinue = False
				return "Exit"
			
			else:
				print "\n   Oops! Game #%i is not available. Try again." % choice
		
		except ValueError:
			print "\nOops! I did not recognize that input. Please enter a number."
		except:
			print "\nOops! We had trouble opening the file. Please try again..."

def get_fileLocation():
	"""This function is called when user wants to choose file from local hard drive.
	function returns the location of the specified file, using a specified path"""
			
	while True:
		prof_path = os.environ['USERPROFILE']
		
		location1 = raw_input("Enter the top location of your .txt file: (\"Desktop\" or \"Documents\") : ")
		
		if location1 and (location1 == "Desktop" or location1 == "Documents"):
			fileDirectory = os.path.join(prof_path,location1)
		
			moreFolders = True
			
			while moreFolders:
				
				response = raw_input("Enter additional sub folder names, file name or leave blank to finish: ")
						
				if not response: # no response
					moreFolders = False
				else:
					fileDirectory = os.path.join(fileDirectory,response)
					print fileDirectory
			
			if os.path.exists(fileDirectory) and fileDirectory[-3:] == "txt":
				print fileDirectory
				return fileDirectory
				
			else:
				print "Location [ %s ] does not exist. Please try again or press exit to escape." % fileDirectory
		
		elif location1.lower() == "exit":
			return "Exit"
			
def createDictionary(textDoc):
	"""creates a dictionary of quesitons and answers based on textfile"""
	
	d.clear()
	
	try:
		for line in textDoc:
			line = line.strip("\n")
			d[line.split(":")[0]] = line.split(":")[1]
	except:
		print "It looks like the text file you selected was not in the correct format."
		print "Be sure that the format is \"question\":\"answer\""
		textDoc = get_TextDoc()
		createDictionary(textDoc)
			
def initialize(textDoc):
	"""If user did not seelct "exit" from the get_TextDoc then it will create the dictionary"""
	
	if textDoc == "Exit":
		return False
	else:
		createDictionary(textDoc)
		print "File opened successfully!"
		return True

def change_attempts():
	"""Allows user to change the number of attempts they get at a question
	Can call this command at any time."""
	
	while True:
		try:
			numAttempts = int(raw_input("\n  - How many attempts would you like at each question?: "))		
			
			if numAttempts < 1:
				return 1
			
			print ""
			return numAttempts
			
		except ValueError:
			print "\tOops! Looks like you did not enter a number..."

def help_menu():
	"""Menu is called during game play by type "help"
	Displays to user any commands that they can enter during game play"""
	
	print "\n\n%s" % ("~"*75)
	print "You can type any of the following commands during game play.\n"
	print "\"Exit\": to exit the game."
	print "\"change_cards\": change the current game that you're playing."
	print "\"change_attempts\": change the number of attempts you get at a question."
	print "\nYou can also leave an answer blank, and set change_attempts to 1 to study."
	print "\n%s\n" % ("~"*75)
	return
	
def print_introduction():
	print "Let's begin the flash cards!"
	print "You may enter \"exit\", \"change_cards\", \"change_attempts\" or \"help\" at any time."

####################################################################################################
#########################################BEGIN PROGRAM##############################################
####################################################################################################

print "Hello and welcome to the flash cards game!"

textDoc = get_TextDoc() ##Open up input to find a textfile game to play
letsContinue = initialize(textDoc) ##initialize the textdoc by creating a dictionary based on it

if letsContinue:
	numberAttempts = change_attempts() ##number attempts user gets at guessing answer
	print_introduction() ##welcome's user to the game

while letsContinue:
	
	attempts = 1
	
	key = random.choice(d.keys()) ##pull a random question and answer from the dictionary
	print "\nQuestion # %i" % questionNumber
	
	while attempts <= numberAttempts:
		
		try:
			choice = raw_input("  (%i / %i )\t  %s: " % (attempts, numberAttempts, key)).lower() ##spits out number of attempts and the question
		except:
			pass
		
		if choice == d[key].lower(): ##guessed right
			print "\t****** Correct! ******"
			questionNumber += 1
			break
		
		elif choice[:4] == "help": ##user wants to go to help menu
			help_menu()
		
		elif choice == "change_attempts":
			numberAttempts = change_attempts()
		
		elif choice == "change_cards":
			textDoc.close() ##ensure we close the existing text document
			
			textDoc = get_TextDoc() ##open new text document
			letsContinue = initialize(textDoc)
			
			questionNumber = 1
			
			break
			
		elif choice[:4] == "exit":
			
			letsExit = raw_input("Are you sure you want to exit? (y / n): ")
			
			if letsExit[0] == "y":
				letsContinue = False
				break
				
		else:
			attempts += 1
	
	else: #number attempts loop
		
		print "\tANSWER: %s" % d[key]
		questionNumber += 1
	
	time.sleep(.5)
	
else:
	print "\n%s" % ("-"*75)
	print "%sProgram shutting down...%s" % (" "*25," "*25)
	#print "%s" % ("-"*75)
	time.sleep(1)
	try:
		print "%sClosing Text Document...%s" % (" "*25," "*25)
		time.sleep(.5)
		textDoc.close()
	except:
		pass
	print "%sDocument Closed!%s" % (" "*25," "*25)
	print "%s" % ("-"*75)
	print "Thanks for playing!\n"
	time.sleep(1)
	print "Goodbye\n"
	