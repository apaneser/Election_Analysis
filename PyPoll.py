# The data we want to receive
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

# Assign variable for the file to load
file_to_load = os.path.join("Resources", "election_results.csv")
#save path of file to open in variable
file_to_save = os.path.join("analysis", "election_analysis.txt")

# # of votes counter
total_votes = 0

# list of candidates
candidate_options = []

# dictionary of candidates and number of votes
candidate_votes = {}

#open file 
with open(file_to_load) as election_data:

    # read the file object with the reader function
    file_reader = csv.reader(election_data)

    # read the header row
    headers = next(file_reader)

    # print each row in the csv file
    for row in file_reader:
        total_votes += 1

        candidate_name = row[2]

        # add candidate to list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # begin tracking candidate vote count
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1

    # print the total votes
    print(total_votes)

    # print candidates
    print(candidate_options)

    # print candidate vote dictionary
    print(candidate_votes)


#open file in write mode
with open(file_to_save, "w") as txt_file:

    # write data to file
    txt_file.write("Arapahoe\nDenver\nJefferson")