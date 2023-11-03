# Dr Michaels
# 9/9/2013
# aetg3.py
# This program implements the AETG algorithm for generating test suites.
# This program will generate, for a user specified number of features and attributes (where each feature has x number of attributes)
# a minimum number of test cases such that every combination of attributes between features can be tested at least once.

import random
import sys
import math
import time

NUM_TESTS = 50 #iterate through each combination 50 times to find best pairing
NUM_SUITES = 100 #iterate through each test suite 100 times to find best setup

def main():
	if len(sys.argv) > 3 or len(sys.argv) < 2:
		print('Usage: python aetg3.py num_factors [num_levels]')
		print('If you desire a multilevel test suite, do not enter a num_levels')
		print('Otherwise, for a standard test suite, enter the num_levels')
		sys.exit(1)
	the_set = []
	if len(sys.argv) == 2:
		the_set = create_m_set(int(sys.argv[1]))
	else:
		the_set = create_set(int(sys.argv[1]), int(sys.argv[2]))

	some_data = create_all_pairs(the_set)
	the_dict = create_dictionary(some_data)


	print('We will iterate this test suite %d number of times, keeping only the optimal solution.' % NUM_SUITES)
	# these variables are used to store the min cases, max cases, and avg cases.
	# As well as the best test suite, the max time, min time, and total time of execution
	best = []
	min_cases = 10000
	max_cases = 0
	total_cases = 0.0
	total_time = 0.0
	max_time = 0.0
	min_time = 100000000.0
	for i in range(NUM_SUITES):
		# start timer
		start_time = time.time()
		# Create the test suite
		temp = create_test_suite(the_set,some_data,the_dict)
		# Get the end time
		end_time = time.time()
		run_time = end_time - start_time
		# Update total time, and check against min/max
		total_time += run_time
		if run_time < min_time:
			min_time = run_time
		if run_time > max_time:
			max_time = run_time

		# Check against the sizes of other test suites	
		if len(temp) < min_cases:
			print('We have found a new minimum number of test\'s required! Our new minimum is now %d' % len(temp))
			best = temp
			min_cases = len(temp)
		if len(temp) > max_cases:
			max_cases = len(temp)
		total_cases += len(temp)
			
		# Reset the dictionary
		reset_dictionary(the_dict)
	
	avg_time = total_time / NUM_SUITES
	avg_cases = total_cases / NUM_SUITES
	print('The minimum execution time was %f' % min_time)
	print('The maximal execution time was %f' % max_time)
	print('The average execution time was %f' % avg_time)
	print('The largest test suite was %d' % max_cases)
	print('The minimal test suite was %d' % min_cases)
	print('The average test suite was %f' % avg_cases)
	print('\n\n')
	print(min_cases)
	result = ''
	for i in range(len(best)):
		result += '\n'
		for j in range(len(best[i])):
			result += '%d\t' % best[i][j]
	print(result)


# This creates the n*m matrix, where n is the number of factors and m is the number of levels per factor
# This is for conventional n*m arrays, the next method is for multilevel (m not consistent across factors)
# Tested
def create_set(factors, levels):
	current = 0 #value for each entry, starting at 0
	the_set = [] #array to be returned
	for i in range(factors):
		the_set.append([])
		for j in range(levels):
			the_set[i].append(current)
			current += 1
			
	return the_set

# This method creates a mixed level array. This method assumes that each factor has 1 less level then it's predecessor
# Tested
def create_m_set(start_level):	
	current = 0
	count = 0
	the_set = []
	temp_level = start_level #created to prevent loss of information on the input variable
	while temp_level > 1:
		the_set.append([])
		# we iterate until the final fa
		for j in range(temp_level):
			the_set[count].append(current)
			current += 1
		count += 1
		temp_level -= 1
		# print (the_set[count-1])
	return the_set
	

# This method creates a 2-D array, of length at most n*m, with multiple depths. It will contain all possible pairs for the given test suite
# Tested
def create_all_pairs(the_array):
		all_pairs = []
		for i in range(len(the_array)):
			for j in range(len(the_array[i])):
				all_pairs.append([])
		count = 1 
		for i in range(len(all_pairs)):
			if i == the_array[len(the_array) - 1][0]:
				break
			if i == the_array[count][0]:
				count += 1
			for j in range(count, len(the_array)):
				for k in range(len(the_array[j])):
					the_pair = (i, the_array[j][k])
					all_pairs[i].append(the_pair)
					all_pairs[the_array[j][k]].append(the_pair)
		
		return all_pairs
	
# This method will create the dictionary (hash table equivalent), using the set of all possible pairs previously generated
# Tested
def create_dictionary(the_array):
	the_dictionary = {}
	for i in range(len(the_array)):
		for j in range(len(the_array[i])):
			the_dictionary[the_array[i][j]] = False
	
	return the_dictionary
	
# This method will create the test suite which allows for all possible pairs to be tested at least once
# Tested
def create_test_suite(factors, all_pairs, dictionary):
	the_result = [] #will contain result. Result will be an array of the form [[a0,b0,c0...],[a1,b1,c1,...]...] and so forth. Where each row is a new combination to be tested
	all_covered = False # Will only change to True when all pairs are covered
	first_row = make_first_row(factors, dictionary)
	the_result.append(first_row)
	while not all_covered:
		best_num_added = 0
		best = []
		for i in range(NUM_TESTS):
			temp = create_new_row(factors,all_pairs,dictionary)
			num_added = new_pairs(temp,dictionary)
			if num_added > best_num_added:
				best_num_added = num_added
				best = temp
		the_result.append(best)
		add_pairs(best, dictionary)
		all_covered = test_coverage(dictionary)
	
	return the_result
	
	
# This method creates the first row randomly. It randomly selects a value from each factor and adds it to the test suite. It will then update the corresponding dictionary.
# Tested
def make_first_row(factors, dictionary):
	result = []
	for i in range(len(factors)):
		result.append(factors[i][int(math.floor(random.random()*len(factors[i])))])
	add_pairs(result,dictionary)
	return result
	
# This method creates a new row in the test suite	
# Tested
def create_new_row(factors, all_pairs, dictionary):
	result = []
	to_pick = [] #the array will be popped
	for i in range(len(factors)):
		result.append(-1) #placeholder value
		to_pick.append(i)
	temp = to_pick.pop(int(math.floor(random.random() * len(to_pick)))) #randomly generate starting factor
	start_set = factors[temp] # extract the starting set
	result[temp] = first_choice(start_set, all_pairs, dictionary)
	# Now that we have successfuly chosen the entry which has the most possible pairs to add, we will proceed
	# The remaining factors will be chosen in random order, and the entry which has the most pairs WITH the values already chosen will be added.
	while len(to_pick) > 0:
		temp = to_pick.pop(int(math.floor(random.random() * len(to_pick))))
		result[temp] = add_next(factors[temp], result, dictionary)
		
	return result

		
# This method finds which element will has the most possible pairs to add to a new test suite. In the event of a tie, it is broken at random
# Tested
def first_choice(the_list, all_pairs, dictionary):
	num_added = []
	for i in range(len(the_list)):
		num_added.append(0)
	tie = [] #will only be filled in if there is a tie
	for i in range(len(num_added)):
		num_added[i] = potential_pairs(all_pairs[i], dictionary)
	max = -1 #max number of new pairs added
	# note we do not need to keep track of the location in another variable, our tie array will do that for us
	for i in range(len(num_added)):
		if num_added[i] > max:
			max = num_added[i]
			tie = [the_list[i]]
		elif num_added[i] == max:
			tie.append(the_list[i])
	if len(tie) == 1:
		return tie[0]
	else:
		return tie[int(math.floor(random.random() * len(tie)))]
	
# This method is used by the first_choice method to detect how many new pairs could be added by each entry
# Tested
def potential_pairs(the_row, dictionary):
	count = 0
	for i in the_row:
			if dictionary[i] == False:
				count += 1
				
	return count

# This method will see how many new pairs each entry in the selected row can add to the new test suite
# It will return the value which will add the most new pairs. In the event of a tie the choice will be randomly selected	
# Tested
def add_next(the_row, the_test, dictionary):
	result = -1
	scores = []
	# We will create a pair for every entry in the_test which is not -1 [aka not a number for our purposes], and check. Each value will get a score.
	for i in range(len(the_row)):
		scores.append(-1)
	tie = []
	# Iterate over the row to score each entry
	for i in range(len(the_row)):
		count = 0
		# Iterate through the current test suite to find pairs
		for j in range(len(the_test)):
			if the_test[j] > -1:
				# The entry is already in the test suite, let us check if the pair is covered
				if the_test[j] > the_row[i]:
					if dictionary[(the_row[i],the_test[j])] == False:
						count += 1
				else:
					if dictionary[(the_test[j],the_row[i])] == False:
						count += 1
		scores[i] = count
	
	# Now to find the maximal value.
	max = -1
	for i in range(len(scores)):
		if scores[i] > max:
			tie = [the_row[i]]
			max = scores[i]
		elif scores[i] == max:
			tie.append(the_row[i])
	
	# if no tie, return value
	if len(tie) == 1:
		return tie[0]
	else:
		return tie[int(math.floor(random.random() * len(tie)))]
			
	


	
# This method addes all pairs from the input test suite to the dictionary, updating values from False to True	
# Tested	
def add_pairs(pairs, dictionary):
	for i in range(len(pairs) - 1):
		for j in range(i+1, len(pairs)):
			dictionary[(pairs[i],pairs[j])] = True

			
# This method counts how many new pairs a new test suite adds to the overal coverage
# Tested
def new_pairs(the_row, dictionary):
	count = 0
	for i in range(len(the_row) - 1):
		for j in range(i+1, len(the_row)):
			if dictionary[(the_row[i],the_row[j])] == False:
				count += 1
				
	return count
			
# This method returns if the dictionary of all pairs is fully covered, i.e. if it contains only values of True\
# Tested			
def test_coverage(dictionary):
	result = True # Standard value
	# iterate through entire dictionary, breaking at first value of False found
	for i in dictionary:
		if dictionary[i] == False:
			result = False #set to false as we found a pair that is uncovered
			break # break out of the loop as we dont need to iterate any more
	
	return result

	
def reset_dictionary(the_dict):
	for i in the_dict:
		the_dict[i] = False
			
main()