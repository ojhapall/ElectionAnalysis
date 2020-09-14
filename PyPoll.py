#Add our dependencies 
import csv
import os

# Assign a varible to load a file from a path
file_to_load = os.path.join("Resources/election_results.csv")
file_to_save = os.path.join("Analysis/election_analysis.txt")

#1. Initialize a total vote counter 
total_votes = 0
#Candidate options
candidate_options = []
#declare the empty dictionary
candidate_votes={}
#winning Candidate and winning count tracker 
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load,"r") as election_results:
    print(election_results)
    file_reader = csv.reader(election_results, delimiter=',') 
    
    #read header row
    header = next(file_reader)
    
    #print each row in the csv file
    for row in (file_reader):
        #2. Add to the total vote count 
        total_votes +=1
        #Print the candidate name from each row 
        candidate_name = row[2]
        #add the candidate name to the candidate list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
        
        #begin tracking the candidate's vote count
            candidate_votes[candidate_name] = 0

        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes)/float(total_votes)*100

    #determine winning vote count and candidate
    #1. Determine if the votes are greater than the winning count 
    if (votes>winning_count) and (vote_percentage>winning_percentage):
        #2. if true then set winning count = votes and winning percentage = 
        # vote percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #3. set the winning_candidate equal to the candidate's name 
        winning_candidate = candidate_name

        #votes to the terminal 
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner:{winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# Assign a varible to save a file from a path
with open(file_to_save, "w") as txt_file:
# Write to the file.
    txt_file.write("Counties in the Election\n----------------------------\nArapahoe\nDenver\nJefferson\n") 
print(txt_file)

# Close the file. 
election_results.close()