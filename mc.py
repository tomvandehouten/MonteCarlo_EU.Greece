import random
import sys
import math
import csv

master_List = []


#make_Chart is strictly an output function, no MC Alg functionality
def make_Chart(master_List):
	"""
	make_Chart(master_List)

	Called at the conclussion of the main()function. 
	"""
	Matrix = [[[] for x in range(10)] for y in range(10)]
	for entry in master_List:
		#If Greek proportion is 0-.1
		if entry[2] <= .1:
			row = 0
		#If Greek proportion is .1-.2
		if entry[2] > .1 and entry[2] <= .2:
			row = 1
		#If Greek proportion is .2-.3
		if entry[2] > .2 and entry[2] <= .3:
			row = 2
		#If Greek proportion is .3-.4
		if entry[2] > .3 and entry[2] <= .4:
			row = 3
		#If Greek proportion is .4-.5
		if entry[2] > .4 and entry[2] <= .5:
			row = 4
		#etc
		if entry[2] > .5 and entry[2] <= .6:
			row = 5
		#etc
		if entry[2] > .6 and entry[2] <= .7:
			row = 6
		#etc
		if entry[2] > .7 and entry[2] <= .8:
			row = 7
		if entry[2] > .8 and entry[2] <= .9:
			row = 8
		if entry[2] > .9 and entry[2] <= 1:
			row = 9

		#If EU proportion is 0-.1
		if entry[3] <= .1:
			column = 0
		#If EU proportion is .1-.2
		if entry[3] > .1 and entry[3] <= .2:
			column = 1
		if entry[3] > .2 and entry[3] <= .3:
			column = 2
		if entry[3] > .3 and entry[3] <= .4:
			column = 3
		if entry[3] > .4 and entry[3] <= .5:
			column = 4
		if entry[3] > .5 and entry[3] <= .6:
			column = 5
		if entry[3] > .6 and entry[3] <= .7:
			column = 6
		if entry[3] > .7 and entry[3] <= .8:
			column = 7
		if entry[3] > .8 and entry[3] <= .9:
			column = 8
		if entry[3] > .9 and entry[3] <= 1:
			column = 9

		#greek_Payoff is entry 0 and eu_Payoff is entry 1
		greek_Payoff = entry[0]
		eu_Payoff = entry[1]
		count = 1
		#Reference to 
		former_Entry = Matrix[row][column]
		if not former_Entry:
			Matrix[row][column] = [greek_Payoff, eu_Payoff, count]
		else:
			new_Greek = former_Entry[0] + greek_Payoff
			new_Eu = former_Entry[1] + eu_Payoff
			new_Count = former_Entry[2] + count
			Matrix[row][column] = [new_Greek, new_Eu, new_Count]
			former_Entry = []

	row_Counter = 0
	row_1 = []
	row_2 = []
	row_3 = []
	row_4 = []
	row_5 = []
	row_6 = []
	row_7 = []
	row_8 = []
	row_9 = []
	row_10 = []
	for item in Matrix:
		for entry in item:
			final = []
			avg_Greek = float(entry[0]) / float(entry[2])
			avg_Greek = float(avg_Greek)
			avg_Greek = float("{0:.2f}".format(avg_Greek))
			avg_EU = float(entry[1]) / float(entry[2])
			avg_EU = float(avg_EU)
			avg_EU = float("{0:.2f}".format(avg_EU))
			count = entry[2]
			final.append(avg_Greek) 
			final.append(avg_EU)
			final.append(count)
			final = tuple(final)
			if row_Counter < 10:
				row_1.append(final)
			if row_Counter >= 10 and row_Counter < 20:
				row_2.append(final)
			if row_Counter >= 20 and row_Counter < 30:
				row_3.append(final)
			if row_Counter >= 30 and row_Counter < 40:
				row_4.append(final)
			if row_Counter >= 40 and row_Counter < 50:
				row_5.append(final)
			if row_Counter >= 50 and row_Counter < 60:
				row_6.append(final)
			if row_Counter >= 60 and row_Counter < 70:
				row_7.append(final)
			if row_Counter >= 70 and row_Counter < 80:
				row_8.append(final)
			if row_Counter >= 80 and row_Counter < 90:
				row_9.append(final)
			if row_Counter >= 90 and row_Counter <= 99:
				row_10.append(final)
			row_Counter += 1

	with open('GameTheoryOut.csv', 'wb') as outfile:
		writer = csv.writer(outfile)
		writer.writerow(row_1)
		writer.writerow(row_2)
		writer.writerow(row_3)
		writer.writerow(row_4)
		writer.writerow(row_5)
		writer.writerow(row_6)
		writer.writerow(row_7)
		writer.writerow(row_8)
		writer.writerow(row_9)
		writer.writerow(row_10)




def main():
	"""
	def main():

	Algorithm for actual simulation of the game. Calls make_Chart() upon conclussion.
	make_Chart parameter is master_List, a combination of all draw lists (choice_List) in
	the game organized as: [greek_Payoff, eu_Payoff, greek_Prop, eu_Prop], where greek_Payoff
	is the payoff for the Greeks, eu_Payoff is the payoff for the EU, greek_Prop is the proportion
	of draws the Greeks choose a stringent strategy, and eu_Prop is the proporiton of draws the
	Greeks chose a stringent strategy. 
		"""
	num_Games = 1000000

	num_Rounds = 15

	lenient_Matches = 0
	lenient_Matches = float(lenient_Matches)
	stringent_Matches = 0
	stringent_Matches = float(stringent_Matches)
	no_Agreement = 0
	no_Agreement = float(no_Agreement)
	total_Rounds = 0
	total_Rounds = float(total_Rounds)

	draws_Till_Success = 0
	draws_Till_Success = float(draws_Till_Success)
	draws_Till_Failure = 0
	draws_Till_Failure = float(draws_Till_Failure)



	for i in range(num_Games):
		choice_List = []
		matched = 0
		num_Draws = 0
		for j in range(num_Rounds):
			while(matched != 1):
				num_Draws+=1
				greek_Choice = random.random()
				eu_Choice = random.random()
				greek_Prop = random.random()
				eu_Prop = random.random()

				if(greek_Choice <= greek_Prop and eu_Choice <= eu_Prop):
					matched=1
					stringent_Matches+=1
					greek_Payoff = -1
					eu_Payoff = 1
					choice_List.append(greek_Payoff)
					choice_List.append(eu_Payoff)
					choice_List.append(greek_Prop)
					choice_List.append(eu_Prop)
					master_List.append(choice_List)
					choice_List = []
					draws_Till_Success += num_Draws
					break;

				if(greek_Choice > greek_Prop and eu_Choice > eu_Prop):
					matched=1
					lenient_Matches+=1
					greek_Payoff = 1
					eu_Payoff = -1
					choice_List.append(greek_Payoff)
					choice_List.append(eu_Payoff)
					choice_List.append(greek_Prop)
					choice_List.append(eu_Prop)
					master_List.append(choice_List)
					choice_List = []
					draws_Till_Success += num_Draws
					break
				
				if (num_Draws == num_Rounds):
					no_Agreement+=1
					greek_Payoff = -5;
					eu_Payoff = -5;
					choice_List.append(greek_Payoff)
					choice_List.append(eu_Payoff)
					choice_List.append(greek_Prop)
					choice_List.append(eu_Prop)
					master_List.append(choice_List)
					choice_List = []
					draws_Till_Failure += num_Draws
					break;
	
				else:
					greek_Payoff = -5
					eu_Payoff = -5
					choice_List.append(greek_Payoff)
					choice_List.append(eu_Payoff)
					choice_List.append(greek_Prop)
					choice_List.append(eu_Prop)
					master_List.append(choice_List)
					choice_List = []
					continue

	prop_Stay = stringent_Matches/num_Games;
	prop_Leave = lenient_Matches/num_Games;
	prop_Noagreement = no_Agreement/num_Games;
	total_Success = stringent_Matches + lenient_Matches;
	avg_On_Success = draws_Till_Success/total_Success;
	avg_On_Failure = draws_Till_Failure/no_Agreement;
	print ("In " + str(num_Games) + " games consisting of" + str(num_Rounds) + "rounds: ")
	print ("-----------------------------------------")
	print ("Proportion that both stringent: "+ str(prop_Stay))
	print ("Proportion that both lenient: "+ str(prop_Leave))
	print ("Reference - num_Games: " + str(num_Games) + " num_Rounds: " + str(num_Rounds) + " stringent_Matches: " + str(stringent_Matches) + " lenient_Matches: " + str(lenient_Matches) + " no_Agreement: " + str(no_Agreement))
	print ("Proportion no agreement is met: " + str(prop_Noagreement))
	print ("In a successful game, the average number of draws is: " + str(avg_On_Success))
	print ("In a failed game, the average number of draws is: " + str(avg_On_Failure))
	print ("-----------------------------------------")
	print ("")
	make_Chart(master_List)
	

if __name__ == "__main__":
    main()
