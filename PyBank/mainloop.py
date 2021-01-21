#Import OS & CSV
import os
import csv

#Set CSV path
budget_csv = os.path.join('Resources', 'budget_data.csv')

#Set zero
total_months = 0
net_amount = 0
average_change = 0
current_profit = 0
high_profit = 0
high_profit_date = ""
low_profit = 0
low_profit_date = ""

#open and read CSV
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:

        #Total number of months by counting number of lines
        total_months += 1

        #Net profit amount
        net_amount += int(row[1])

        #Find change in monthly amounts
        current_profit = int(row[1])

        if(current_profit >=0):
            if(current_profit > high_profit):
                high_profit = current_profit
                high_profit_date = str(row[0])
        elif(current_profit<0):
            if(current_profit < low_profit):
                low_profit = current_profit
                low_profit_date = str(row[0])

#find average
average_change = round(net_amount / total_months, 2)

print(f"Financial Analysis")
print(f"-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total Profit: $ {net_amount}")
print(f"Average Change: $ {average_change}")
print(f"Greatest Increase in Profit: {high_profit_date} ($ {high_profit})")
print(f"Greatest Decrease in Profit: {low_profit_date} ($ {low_profit})")