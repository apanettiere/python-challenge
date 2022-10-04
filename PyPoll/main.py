import os
import csv

csvpath = os.path.join( "..", "PyPoll", "Resources", "election_data.csv")

#Variables 
total_votes = 0 
charles_vote = 0
diana_vote = 0
raymon_vote = 0

with open(csvpath) as csvpath:

    csvreader = csv.reader(csvpath, delimiter=",") 
    header = next(csvreader)     

    # Iterate through each row in the csv
    for row in csvreader: 
        total_votes +=1

        if row[2] == "Charles Casper Stockham": 
            charles_vote +=1
        elif row[2] == "Diana DeGette":
            diana_vote +=1
        elif row[2] == "Raymon Anthony Doane": 
            raymon_vote +=1
       
 
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [charles_vote, diana_vote,raymon_vote]

# Zip together the list of candidate
zipvotes = dict(zip(candidates,votes))
key = max(zipvotes, key=zipvotes.get)

# Print a the summary of the analysis
charles_percent = (charles_vote/total_votes) *100
diana_percent = (diana_vote/total_votes) * 100
raymon_percent = (raymon_vote/total_votes)* 100


# Print statments
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_vote})")
print(f"Diana DeGette: {diana_percent:.3f}% ({diana_vote})")
print(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_vote})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

# Write statments
text_path = "output.text"
with open(text_path, "w") as file:

    file.write(f"Election Results\n")
    file.write(f"----------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write(f"----------------------------\n")
    file.write(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_vote})\n")
    file.write(f"Diana DeGette: {diana_percent:.3f}% ({diana_vote})\n")
    file.write(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_vote})\n")
    file.write(f"----------------------------\n")
    file.write(f"Winner: {key}\n")
    file.write(f"----------------------------")