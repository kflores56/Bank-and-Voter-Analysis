#import systems
import os
import csv

#create file path
poll_data = os.path.join('PyPoll', 'Resources', 'election_data.csv')

votes = []
county = []
candidates = []
total_votes = 0
khan_count = 0
correy_count = 0
li_count = 0
otooley_count = 0

#read file
with open(poll_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        votes.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
    
        #total number of votes by counting lines
        total_votes += 1

        if(row[2] == "Khan"):
            khan_count = khan_count + 1
        elif(row[2]=="Correy"):
            correy_count = correy_count + 1
        elif(row[2]=="Li"):
            li_count = li_count + 1
        elif(row[2]=="O'Tooley"):
            otooley_count = otooley_count + 1
        
        khan_percent =round((khan_count/total_votes)*100,3)
        correy_percent = round((correy_count/total_votes)*100,3)
        li_percent = round((li_count/total_votes)*100,3)
        otooley_percent = round((otooley_count/total_votes)*100,3)

candidate_counts = [khan_count, correy_count, li_count, otooley_count]
winnercount = max(candidate_counts)
winner = ""
if winnercount == khan_count:
    winner = "Khan"
elif winnercount == correy_count:
    winner = "Correy"
elif winnercount == li_count:
    winner = "Li"
elif winnercount == otooley_count:
    winner = "O'Tooley"

print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent}% ({khan_count})")
print(f"Correy: {correy_percent}% ({correy_count})")
print(f"Li: {li_percent}% ({li_count})")
print(f"O'Tooley:{otooley_percent}% ({otooley_count})")
print(f"----------------------------")
print(f"Winner: {winner}")
print(f"----------------------------")