import os
import csv


csvpath = r"C:\Users\HollyerRuthAnn\HW_Python\python-challenge\PyPoll\election_data.csv"

with open(csvpath, newline ='' ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)



    VoteTallies ={"Khan": 0,"Correy": 0, "Li": 0, "O'Tooley": 0}

    totalVotes = 0
 

    for  row in csvreader:
         totalVotes = totalVotes + 1
         candidate = row[2]
         VoteTallies[candidate]= VoteTallies[candidate] + 1
         
    for candidate in VoteTallies.keys(): 
        "Khan"
        Percentage = ' {:.3%}'.format (VoteTallies[candidate] / totalVotes)
        VoteTallies[candidate] / totalVotes
        votes = ("Percentage  " + str(Percentage))
        print(candidate +':  '+ str(votes)) 

        if VoteTallies[candidate]==max(VoteTallies.values()):
            winner = candidate
        

print("Total Votes:  " + str(totalVotes))
print("VoteTallies"+ str(VoteTallies))
print("Winner:  " + winner)