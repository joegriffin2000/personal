`/* Joe Griffin
 * 11/4/2023
 * aetg3.java
 * This program implements the AETG algorithm for generating test suites.
 * This program will generate, for a user specified number of features and attributes (where each feature has x number of attributes)
 * a minimum number of test cases such that every combination of attributes between features can be tested at least once.
 * */

import java.util.*;

public class aetg3 {
	public static final int NUM_TESTS = 50; //iterate through each combination 50 times to find best pairing 
	public static final int NUM_SUITES = 100; //iterate through each test suite 100 times to find best setup
	
	public static void main(String[] a) {
		/*
		if ((a.length > 3) || (a.length < 2)) {
			System.out.println("Usage: python aetg3.py num_factors [num_levels]");
			System.out.println("If you desire a multilevel test suite, do not enter a num_levels");
			System.out.println("Otherwise, for a standard test suite, enter the num_levels");
			return;
		}*/
		ArrayList<List<Integer>> the_set;
		
		if (a.length == 2) {
			the_set = create_m_set(Integer.parseInt(a[1]));
		} else {
			the_set = create_set(Integer.parseInt(a[1]),Integer.parseInt(a[2]));
		}
		
		ArrayList<List<List<Integer>>> some_data = create_all_pairs(the_set);
		HashMap<List<Integer>,Boolean> the_dict = create_dictionary(some_data);
		
		System.out.printf("We will iterate this test suite %d number of times, keeping only the optimal solution.\n", NUM_SUITES);
		//these variables are used to store the min cases, max cases, and avg cases.
		//As well as the best test suite, the max time, min time, and total time of execution
		ArrayList<List<Integer>> best = new ArrayList<List<Integer>>();
		int min_cases = 10000;
		int max_cases = 0;
		double total_cases = 0.0;
		double total_time = 0.0;
		double max_time = 0.0;
		double min_time = 100000000.0;
		for (int i=0;i<NUM_SUITES;i++) {
			//start_time = time.time()
			long start_time = System.currentTimeMillis();
			//Create the test suite
			ArrayList<List<Integer>> temp = create_test_suite(the_set,some_data,the_dict);
			//Get the end time
			long end_time = System.currentTimeMillis(); 
			long run_time = end_time - start_time;
			
			//Update total time, and check against min/max
			total_time += run_time;
			if (run_time < min_time) min_time = run_time;
			if (run_time > max_time) max_time = run_time;
			
			//Check against the sizes of other test suites	
			if (temp.size() < min_cases) {
				System.out.printf("We have found a new minimum number of test\\'s required! Our new minimum is now %d\n", temp.size());
				best = temp;
				min_cases = temp.size();
			}
			if (temp.size() > max_cases) {
				max_cases = temp.size();
			}
			total_cases += temp.size();
			
			//Reset the dictionary
			reset_dictionary(the_dict);
		}
		double avg_time = total_time / NUM_SUITES;
		double avg_cases = total_cases / NUM_SUITES;
		System.out.printf("The minimum execution time was %f\n",min_time/1000);
		System.out.printf("The maximal execution time was %f\n",max_time/1000);
		System.out.printf("The average execution time was %f\n",avg_time/1000);
		System.out.printf("The largest test suite was %d\n",max_cases);
		System.out.printf("The minimal test suite was %d\n",min_cases);
		System.out.printf("The average test suite was %f\n",avg_cases);
		System.out.println("\n\n");
		System.out.println(min_cases);
		String result = "";
		
		for (int i=0;i<best.size();i++) {
			result += '\n';
			for (int j=0;j<best.get(i).size();j++) {
				result += best.get(i).get(j);
				result += "\t";
			}
		}
		System.out.println(result);
	}
	
	//This creates the n*m matrix, where n is the number of factors and m is the number of levels per factor
	//This is for conventional n*m arrays, the next method is for multilevel (m not consistent across factors)
	//Tested
	public static ArrayList<List<Integer>> create_set(int factors,int levels) {
		int current = 0;
		ArrayList<List<Integer>> the_set = new ArrayList<List<Integer>>();
		for (int i=0; i < factors; i++) {
			the_set.add(new ArrayList<Integer>());
			for (int j=0; j < levels;j++) {
				the_set.get(i).add(current);
				current++;
			}
		}
		
		return the_set;	
	}
	//This method creates a mixed level array. This method assumes that each factor has 1 less level then it's predecessor
	//Tested
	public static ArrayList<List<Integer>> create_m_set(int start_level) {
		int current = 0;
		int count = 0;
		ArrayList<List<Integer>> the_set = new ArrayList<List<Integer>>();
		int temp_level = start_level; //created to prevent loss of information on the input variable
		while(temp_level > 1) {
			the_set.add(new ArrayList<Integer>());
			//we iterate until the final fa
			for (int j=0;j<temp_level;j++) {
				the_set.get(count).add(current);
				current++;
			}
			count++;
			temp_level--;
		}
		return the_set;
	}
	//This method creates a 2-D array, of length at most n*m, with multiple depths. It will contain all possible pairs for the given test suite
	//Tested
	public static ArrayList<List<List<Integer>>> create_all_pairs(ArrayList<List<Integer>> the_array) {
		ArrayList<List<List<Integer>>> all_pairs = new ArrayList<List<List<Integer>>>();
		for (int i=0; i<the_array.size(); i++) {
			for (int j=0; j<the_array.get(i).size(); j++) {
				all_pairs.add(new ArrayList<List<Integer>>());
			}
		}
		int count = 1;
		
		for (int i=0;i < all_pairs.size();i++) {
			if (i == the_array.get(the_array.size()-1).get(0)) {
				break;
			}
			if (i == the_array.get(count).get(0)) {
				count++;
			}
			for (int j=count; j <the_array.size(); j++) {
				for (int k=0; k <the_array.get(j).size(); k++) {
					ArrayList<Integer> temp = new ArrayList<Integer>(List.of(i,the_array.get(j).get(k)));
					all_pairs.get(i).add(temp);
					all_pairs.get(the_array.get(j).get(k)).add(temp);
				}
			}
		}
		
		return all_pairs;
	}
	//This method will create the dictionary (hash table equivalent), using the set of all possible pairs previously generated
	//Tested
	public static HashMap<List<Integer>,Boolean> create_dictionary(ArrayList<List<List<Integer>>> the_array){
		HashMap<List<Integer>,Boolean> the_dictionary = new HashMap<List<Integer>,Boolean>();
		
		for(int i=0; i<the_array.size(); i++) {
			for(int j=0; j<the_array.get(i).size(); j++) {
				the_dictionary.put(the_array.get(i).get(j), false);
			}
		}
		return the_dictionary;
	}
	//This method will create the test suite which allows for all possible pairs to be tested at least once
	//Tested
	public static ArrayList<List<Integer>> create_test_suite(ArrayList<List<Integer>> factors, ArrayList<List<List<Integer>>> all_pairs, HashMap<List<Integer>,Boolean> dictionary){
		ArrayList<List<Integer>> the_result = new ArrayList<List<Integer>>();//will contain result. Result will be an array of the form [[a0,b0,c0...],[a1,b1,c1,...]...] and so forth. Where each row is a new combination to be tested
		
		boolean all_covered = false; //Will only change to True when all pairs are covered
		ArrayList<Integer> first_row = make_first_row(factors,dictionary);
		the_result.add(first_row);
		
		while(!all_covered) {
			int best_num_added=0;
			ArrayList<Integer> best = new ArrayList<Integer>();
			for (int i=0; i<NUM_TESTS; i++) {
				ArrayList<Integer> temp = create_new_row(factors,all_pairs,dictionary);
				int num_added = new_pairs(temp,dictionary);
				if (num_added > best_num_added) {
					best_num_added = num_added;
					best = temp;
				}
			}
			the_result.add(best);
			add_pairs(best,dictionary);
			all_covered = test_coverage(dictionary);
		}
		
		return the_result;
	}
	//This method creates the first row randomly. It randomly selects a value from each factor and adds it to the test suite. It will then update the corresponding dictionary.
	//Tested
	public static ArrayList<Integer> make_first_row(ArrayList<List<Integer>> factors,HashMap<List<Integer>,Boolean> dictionary) {
		ArrayList<Integer> result = new ArrayList<Integer>();
		
		for (int i=0; i<factors.size(); i++) {
			List<Integer> temp = factors.get(i);
			result.add(temp.get((int)Math.floor(Math.random() * factors.size())));
		}
		add_pairs(result,dictionary);
		
		return result;
	}
	
	//This method creates a new row in the test suite
	//Tested
	public static ArrayList<Integer> create_new_row(ArrayList<List<Integer>> factors, ArrayList<List<List<Integer>>> all_pairs, HashMap<List<Integer>,Boolean> dictionary) {
		ArrayList<Integer> result = new ArrayList<Integer>();
		ArrayList<Integer> to_pick = new ArrayList<Integer>(); //the array will be popped
		
		for (int i=0; i<factors.size();i++) {
			result.add(-1); //placeholder value
			to_pick.add(i);
		}
		int temp = to_pick.remove((int)Math.floor(Math.random() * to_pick.size()));//randomly generate starting factor
		List<Integer> start_set = factors.get(temp);//extract the starting set
		result.set(temp,first_choice(start_set,all_pairs,dictionary));
		//Now that we have successfuly chosen the entry which has the most possible pairs to add, we will proceed
		//The remaining factors will be chosen in random order, and the entry which has the most pairs WITH the values already chosen will be added.
		
		while(to_pick.size() > 0) {
			temp = to_pick.remove((int)Math.floor(Math.random() * to_pick.size()));
			result.set(temp, add_next(factors.get(temp),result,dictionary));
		}
		
		return result;
	}
	//This method finds which element will has the most possible pairs to add to a new test suite. In the event of a tie, it is broken at random
	//Tested
	public static int first_choice(List<Integer> the_list, ArrayList<List<List<Integer>>> all_pairs, HashMap<List<Integer>,Boolean> dictionary) {
		ArrayList<Integer> num_added = new ArrayList<Integer>();
		for (int i=0;i<the_list.size();i++) {
			num_added.add(0);
		}
		ArrayList<Integer> tie = new ArrayList<Integer>(); //will only be filled in if there is a tie
		
		for (int i=0;i<num_added.size();i++) {
			num_added.set(i,potential_pairs(all_pairs.get(i), dictionary));
		}
		int max = -1;//max number of new pairs added
		//note we do not need to keep track of the location in another variable, our tie array will do that for us
		
		for (int i=0; i<num_added.size(); i++) {
			if (num_added.get(i) > max) {
				max = num_added.get(i);
				tie.clear();
				tie.add(the_list.get(i));
			} else if (num_added.get(i) == max) {
				tie.add(the_list.get(i));
			}
		}
		
		if (tie.size() == 1) return tie.get(0);
		else return tie.get((int)Math.floor(Math.random() * tie.size())); 
		
	}
	//This method is used by the first_choice method to detect how many new pairs could be added by each entry
	//Tested
	public static int potential_pairs(List<List<Integer>> the_row, HashMap<List<Integer>,Boolean> dictionary){
		int count=0;
		for (int i=0;i<the_row.size();i++) {
			if (dictionary.get(the_row.get(i)) == false) count += 1;
		}
		
		return count;
	}
	
	//This method will see how many new pairs each entry in the selected row can add to the new test suite
	//It will return the value which will add the most new pairs. In the event of a tie the choice will be randomly selected
	//Tested
	public static int add_next(List<Integer> the_row, ArrayList<Integer> the_test, HashMap<List<Integer>,Boolean> dictionary) {
		int result = -1;
		ArrayList<Integer> scores = new ArrayList<Integer>();
		//We will create a pair for every entry in the_test which is not -1 [aka not a number for our purposes], and check. Each value will get a score.
		
		for(int i=0;i<the_row.size();i++) {
			scores.add(-1);
		}
		ArrayList<Integer> tie = new ArrayList<Integer>();
		//Iterate over the row to score each entry
		int count;
		for(int i=0; i<the_row.size(); i++) {
			count = 0;
			//Iterate through the current test suite to find pairs
			for (int j=0;j<the_test.size();j++) {
				if (the_test.get(j) > -1) {
					//The entry is already in the test suite, let us check if the pair is covered
					if (the_test.get(j) > the_row.get(i)) {
						ArrayList<Integer> temp1 = new ArrayList<Integer>(List.of(the_row.get(i),the_test.get(j)));
						if (dictionary.get(temp1) == false) count++;
					}else {
						ArrayList<Integer> temp2 = new ArrayList<Integer>(List.of(the_test.get(j),the_row.get(i)));
						if (dictionary.get(temp2) == false) count++;
					}
				}
			}
			scores.set(i,count);
		}
		//Now to find the maximal value.
		int max = -1;
		for(int i=0;i<scores.size();i++) {
			if (scores.get(i) > max) {
				tie.clear();
				tie.add(the_row.get(i));
				max = scores.get(i);
			}else if (scores.get(i) == max) {
				tie.add(the_row.get(i));
			}
		}
		//if no tie, return value
		
		if (tie.size()==1) return tie.get(0);
		else return tie.get((int)Math.floor(Math.random() * tie.size()));
		
	}
	//This method adds all pairs from the input test suite to the dictionary, updating values from False to True	
	//Tested
	public static void add_pairs(ArrayList<Integer> pairs, HashMap<List<Integer>,Boolean> dictionary) {
		for (int i=0; i<(pairs.size()-1); i++) {
			for (int j=i+1; j<pairs.size(); j++) {
				ArrayList<Integer> temp = new ArrayList<Integer>(List.of(pairs.get(i),pairs.get(j)));
				dictionary.replace(temp,true);
			}
		}
	}
	//This method counts how many new pairs a new test suite adds to the overal coverage
	//Tested
	public static int new_pairs(ArrayList<Integer> the_row,  HashMap<List<Integer>,Boolean> dictionary) {
		int count=0;
		
		for(int i=0;i<(the_row.size()-1);i++) {
			for(int j=i+1;j<the_row.size();j++){
				ArrayList<Integer> temp = new ArrayList<Integer>(List.of(the_row.get(i),the_row.get(j)));
				if (dictionary.get(temp) == false) count++;
			}
		}
		
		return count;
	}
	//This method returns if the dictionary of all pairs is fully covered, i.e. if it contains only values of True
	//Tested
	public static boolean test_coverage(HashMap<List<Integer>,Boolean> dictionary) {
		boolean result = true; //Standard value
		//iterate through entire dictionary, breaking at first value of False found
		for (Map.Entry<List<Integer>,Boolean> i : dictionary.entrySet()) {
			if (dictionary.get(i.getKey()) == false ) {
				result = false; //set to false as we found a pair that is uncovered
				break; //break out of the loop as we dont need to iterate any more
			}
		}
		return result;
	}
	
	
	public static void reset_dictionary(HashMap<List<Integer>,Boolean> the_dict) {
		for (Map.Entry<List<Integer>,Boolean> i : the_dict.entrySet()) {
			the_dict.put(i.getKey(), false);
		}
	}
	
}
