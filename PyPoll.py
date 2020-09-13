#Add our dependencies 
import csv
import os

# Assign a varible to load a file from a path
file_to_load = os.path.join("Resources/election_results.csv")
with open(file_to_load,"r") as election_results:
    print(election_results)
    file_reader = csv.reader(election_results, delimiter=',') 
    
    header = next(file_reader)
    print(header)
# Assign a varible to save a file from a path
file_to_save = os.path.join("Analysis/election_analysis.txt")
with open(file_to_save, "w") as txt_file:
# Write to the file.
    txt_file.write("Counties in the Election\n----------------------------\nArapahoe\nDenver\nJefferson\n") 
print(txt_file)

#To Do: Perform Analysis 

# Create a filename variable to a direct or indirect path to the file.


#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular votes

# Close the file. 
election_results.close()