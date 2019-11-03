#import os/csv
import os
import csv

#Set path for file
csvpath = os.path.join("election_data.csv") 

#Set variables
total_votes = []
votes_k = []
votes_c = []
votes_l = []
votes_o = []
results = []
tot_votes = 0
k_perc = 0
c_perc = 0
l_perc = 0
o_perc = 0
winner = ''
#Open CSV
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    #print(csvheader)
    for row in csvreader:
        total_votes.append(row)
        if str(row[2]) == "Khan":
            votes_k.append(row)
            results.append(len(votes_k))
        elif str(row[2]) == "Correy":
            votes_c.append(row)
            results.append(len(votes_c))
        elif str(row[2]) == "Li":
            votes_l.append(row)
            results.append(len(votes_l))
        elif str(row[2]):
            votes_o.append(row)
            results.append(len(votes_o))
        k_perc = round(int(len(votes_k))/int(len(total_votes)),6) *100
        c_perc = round(int(len(votes_c))/int(len(total_votes)),6) *100
        l_perc = round(int(len(votes_l))/int(len(total_votes)),6) *100
        o_perc = round(int(len(votes_o))/int(len(total_votes)),6) *100
        if (len(votes_k) > len(votes_c)) and (len(votes_k) > len(votes_l)) and (len(votes_k) > len(votes_o)): 
            winner = 'Khan'
        elif (len(votes_c) > len(votes_k)) and (len(votes_c) > len(votes_l)) and (len(votes_c) > len(votes_o)):
            winner = 'Correy'
        elif (len(votes_l) > len(votes_k)) and (len(votes_l) > len(votes_c)) and (len(votes_l) > len(votes_o)):
            winner = 'Li'
        elif (len(votes_o) > len(votes_k)) and (len(votes_o) > len(votes_c)) and (len(votes_o) > len(votes_l)):
            winner = "O'Tooley"
print("--------------------------")

print("Election Results")

print("--------------------------")

print("Total Votes: " + str(len(total_votes)))

print("--------------------------")

print("Khan: " + str(k_perc) + "% (" + str(len(votes_k)) + ")")
print("Correy: " + str(c_perc) + "% (" + str(len(votes_c)) + ")")
print("Li: " + str(l_perc) + "% (" + str(len(votes_l)) + ")")
print("O'Tooley: " + str(o_perc) + "% (" + str(len(votes_o)) + ")")

print("----------------------------")

print("WINNER: " + winner)