import os
import csv


csvpath = r"C:\Users\HollyerRuthAnn\HW_Python\budget_data.csv"

with open(csvpath, newline ='' ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    countMonths = 0
    netTotalAmount = 0
    lastValue = 0
    lastDelta = 0
    SumDelta = 0
    Delta = 0

    MaxDelta = 0
    MaxDeltaDate = " "
    MinDelta = 99999999999
    MinDeltaDate = " "

    for row in csvreader:
        #Count the number of months int the loop
        countMonths = countMonths +1

        #Get P&L from the table
        P_L = int(row[1])  #column 0 is Date, column 1 is P&L

        #Add current P&L to the total amount 
        netTotalAmount = netTotalAmount + P_L

        #Delta Logic
        if countMonths > 1:  #start the Delta logic on the 2nd row of data
           Delta = P_L - lastValue
           SumDelta = SumDelta + Delta

           #Min Value
           if MinDelta > Delta:
               MinDelta = Delta
               MinDeltaDate = row[0]
           #Max Value
           if MaxDelta < Delta:
              MaxDelta = Delta
              MaxDeltaDate = row[0]

        #Last items before end of loop
        lastValue = P_L
print("Months:" + str(countMonths))
print("Net Total Amount: $" +str(netTotalAmount))
print("Avg Change: $" + str(SumDelta/(countMonths -1)))
print("Greatest Increase in Profits: " + MaxDeltaDate + " ($"+ str(MaxDelta) +")")
print("Greatest Decrease in Profits: " + MinDeltaDate + " ($"+ str(MinDelta) +")")