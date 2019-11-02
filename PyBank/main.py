#Import OS and CSV

import os
import csv

Total = 0
#Set path for file
csvpath = os.path.join("budget_data.csv")
#print(csvpath)
Date = []
diff = []
cr = 0
pr = 0
rd = 0
#Open CSV
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    #print(csvheader)
    for row in csvreader:
        Date.append(row[0])
        Total += int(row[1])
        cr = int(row[1])
        rd = cr - pr
        diff.append(rd)
        pr = int(row[1])
    print("Total Months: " + str(len(Date)))
    print("Total: " + str(Total))
    diff.pop(0)
    Sum = sum(diff)
    AVG = round(sum(diff)/(len(Date)-1),2)
    print("Average Change: $" + str(AVG))
    print("Greatest Increase in Profits: " + Date[diff.index(max(diff))+1] + " ($" + str(max(diff)) + ")")
    print("Greatest Decrease in Profits: " + Date[diff.index(min(diff))+1] + " ($" + str(min(diff)) +")")