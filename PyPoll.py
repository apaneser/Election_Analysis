import csv
import os

# Assign variable for the file to load
file_to_load = os.path.join("Resources", "election_results.csv")

#open file 
with open(file_to_load) as election_data:

    # read the file object with the reader function
    file_reader = csv.reader(election_data)

    # print each row in the csv file
    headers = next(file_reader)
    print(headers) 

    # The data we want to receive
    # 1. The total number of votes cast
    # 2. A complete list of candidates who received votes
    # 3. The percentage of votes each candidate won
    # 4. The total number of votes each candidate won
    # 5. The winner of the election based on popular vote

    # print the file object
    print(election_data)

#save path of file to open in variable
file_to_save = os.path.join("analysis", "election_analysis.txt")
#open file in write mode
with open(file_to_save, "w") as txt_file:

    # write data to file
    txt_file.write("Arapahoe\nDenver\nJefferson")