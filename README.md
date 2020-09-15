# ElectionAnalysis
UTOR Data Analytics Module 3 - Python


## Overview of Election Audit: 
The purpose of this election audit analysis is to try and automate the process of election analysis rather than using excel. If this analysis is successful, the process will be used in other districts, senetorial elections and local elections. 

The election audit analysis will take into account mail-in ballots, punch cards and direct recording electonic to create a vote count. The python code will then tabulate and analyze the results to provide Tom and Seth with total votes, total votes per candidate, percentage of votes per candidate and the winner of the election by popular vote. 

----
## Election-Audit Results: 
### How many votes were cast in this congressional election?
* Total Votes: 369,711

### Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct

County Votes:
* Jefferson: 10.5% (38,855)
* Denver: 82.8% (306,055)
* Arapahoe: 6.7% (24,801)

### Which county had the largest number of votes?

* Largest County Turnout: Denver

### Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

* Charles Casper Stockham: 23.0% (85,213)
* Diana DeGette: 73.8% (272,892)
* Raymon Anthony Doane: 3.1% (11,606)

### Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

* Winner: Diana DeGette
* Winning Vote Count: 272,892
* Winning Percentage: 73.8%

----
## Election-Audit Summary: 

This script can easily be used for other district elections without any modifications as long as the format of data is the same. The code uses simple and clean variables that allows it to be used in different districts. Here are some variables that are used throughout the code: 
* total_votes = 0
* candidate_options = []
* candidate_votes = {}
* county = []
* county_vote = {}
* winning_candidate = ""
* winning_count = 0
* winning_percentage = 0

With some modifications this can be used for other elections. For example county could be state or county_vote could be state_vote. This would allow us to do an election audit analysis for state elections. Apart of from changing these variables, the file names would need to be changed so that the data is pulled from the correct files (file_to_load = os.path.join("Resources/election_results.csv"));

This python code can make the election audit analysis, quick and simple for any election. 
