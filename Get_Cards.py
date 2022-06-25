import random
import csv

str1 = ""
str2 = ""


#gets columns from csv file, puts them into lists, randomly chooses one
#then sends both the question and answer back.
def generateCard():
	#Get the file
	filename = open('data.csv', 'r')

	#Read through the file
	file = csv.DictReader(filename)

	#Variables
	questions = []
	answers = []

	#parse through the entries and add them to lists
	for col in file:
		questions.append(col['questions'])
		answers.append(col['answers'])

	#Get total number of questions to be used for random number generation
	total_questions = len(questions)
	rand_num = random.randrange(0, total_questions)


	question = questions[rand_num]
	answer = answers[rand_num]

	return(question,answer)


#Gets all the cards from the csv file and returns them as two lists
def getAllCards():
	#Get the file
	filename = open('data.csv', 'r')

	#Read through the file
	file = csv.DictReader(filename)

	#Variables
	questions = []
	answers = []

    #parse through the entries and add them to lists
	for col in file:
		questions.append(col['questions'])
		answers.append(col['answers'])

	#return both lists	
	return(questions,answers)