import os
import csv

# Set path for file
file_path = os.path.join("Resources", "election_data.csv")
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#Initialize variables to store the data:

total_votes = 0
total_candidates = []
candidate_votes = {}

#Read the CSV file and store the data in the initialized variables:

with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate not in total_candidates:
            total_candidates.append(candidate)
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1

#Calculate the percentage of votes that each candidate won:

percentages = {}
for candidate in candidate_votes:
    vote_count = candidate_votes[candidate]
    percentage = round((vote_count / total_votes) * 100, 2)
    percentages[candidate] = percentage


#Find the total number of votes each candidate won and the winner of the election based on popular vote:

winner = ""
winning_votes = 0
for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    if votes > winning_votes:
        winning_votes = votes
        winner = candidate

#Print the results:
print("------------------------------------------")
print("Election Results")
print("------------------------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------------------------")
for candidate in candidate_votes:
    print(f"{candidate}: {percentages[candidate]}% ({candidate_votes[candidate]})")
print("------------------------------------------")
print(f"Winner: {winner}")
print("------------------------------------------")


