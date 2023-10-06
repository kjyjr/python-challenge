import os
import csv
electionCSV = os.path.join('Resources', 'election_data.csv')
ElectionResultsCSV = os.path.join('ElectionResults.txt')

total_votes = 0
candidates = []
candidates_votes = {}
most_votes = 0
winner = ""

with open(electionCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidates_votes[candidate_name] = 0
        candidates_votes[candidate_name] = candidates_votes[candidate_name] + 1
       

    with open(ElectionResultsCSV, 'w') as textfile:
        output = ""
        output += f"Election Results\n"
        output += f"----------------------------\n"
        output += f"Total Votes: {total_votes}\n"
        output += f"----------------------------\n"
        for candidate in candidates:
            percent_votes = ((candidates_votes[candidate] / total_votes) * 100)
            output += f"{candidate}: {percent_votes: .3f}%  ({(candidates_votes[candidate])})\n"
            if candidates_votes[candidate] > most_votes:
                most_votes = candidates_votes[candidate]
                winner = candidate
              
        output += f"----------------------------\n"
        output += f"Winner: {winner}\n"
        output += f"----------------------------\n"
        textfile.write(output)
        print(output)