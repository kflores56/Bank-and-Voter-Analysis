#Import OS & CSV
import os
import csv

#Set CSV path
budget_csv = os.path.join('PyBank', 'Resources', 'budget_data.csv')

#Set variables 
total_months = 0
month = []
amount = []

#open and read CSV
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:

        #Total number of months by counting number of lines
        total_months += 1
        
        #append to lists
        month.append(row[0])
        amount.append(float(row[1]))      

net_amount = amount[0]
monthly_change = 0
high_profit = 0
low_profit = 0
average_monthly_change = 0 

for n in range (1, total_months):

    #Net profit amount
    net_amount += amount[n]

    #Find change in monthly amounts
    current_change = amount[n] - amount[n-1]
    monthly_change += current_change

    #greatest increase and decrease
    if current_change > high_profit:
        high_profit = current_change
        high_profit_date = month [n]
    elif current_change < low_profit:
        low_profit = current_change
        low_profit_date = month[n]
    
    #average change 
    average_monthly_change = round(monthly_change/total_months,3)

print(f"Financial Analysis")
print(f"-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total Profit: $ {net_amount}")
print(f"Average Change: $ {average_monthly_change}")
print(f"Greatest Increase in Profits: {high_profit_date} $ {high_profit}")
print(f"Greastest Decrease in Profits: {low_profit_date} $ {low_profit}")