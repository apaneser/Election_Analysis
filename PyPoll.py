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

# winning candidate and winning count tracker
winning_candidate = ''
winning_count = 0
winning_percentage = 0

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
    
    #open file in write mode
    with open(file_to_save, "w") as txt_file:

        election_results = (
            f"Election Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n"
        )
        txt_file.write(election_results)

        # get percentage of votes for each candidate through looping
        for candidate_name in candidate_votes:
            # get number of votes for the candidate
            votes = candidate_votes[candidate_name]
            # calculate percentage of total vote
            vote_percentage = float(votes) / float(total_votes) * 100
            # print result for each candidate
            candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
            print(candidate_results)
            txt_file.write(candidate_results)

        
            # determine winning vote count and candidate
            # determine if the votes is greater than the winning count
            #if (votes > winning_count) and (vote_percentage > winning_percentage):
                # if true, set winning count = votes and winning_percent = vote percentage
                #winning_count = votes
                #winning_percentage = vote_percentage
                #winning_candidate = candidate_name

        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n"
        )
        print(winning_candidate_summary)

        txt_file.write(winning_candidate_summary)

        # print the total votes
        #print(total_votes)

        # print candidates
        #print(candidate_options)

        # print candidate vote dictionary
        #print(candidate_votes)