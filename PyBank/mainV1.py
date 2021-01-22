#Import OS & CSV
import os
import csv

#Set CSV path
budget_csv = os.path.join('Resources', 'budget_data.csv')

#Set zero
total_months = 0
month = []
net_profit = 0
monthly_change = 0
profit = []
current_profit = 0
initial_profit = 0
total_monthly_change = []
net_change = 0

#open and read CSV
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:

        #Total number of months by counting number of lines
        total_months += 1

        #Append columns 
        month.append(row[0])
        profit.append(row[1])

        #Net profit amount
        net_profit += int(row[1])

        #Find change in monthly amounts
        current_profit = int(row[1])
        monthly_change = current_profit - initial_profit
        
        #Add monthly changes to new list
        total_monthly_change.append(monthly_change)

        #Add new monthly change to total change 
        net_change = net_change + monthly_change
        
        #Reset initial profit
        initial_profit = current_profit

        #Find average change
        average_change = round(net_change/total_months, 2)

        #Find high & low profits
        high_profit = max(total_monthly_change)
        low_profit = min(total_monthly_change)

        #Find high & low dates
        high_profit_date = month[total_monthly_change.index(high_profit)]
        low_profit_date = month[total_monthly_change.index(low_profit)]

print(f"Financial Analysis")
print(f"-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total Profit: $ {net_profit}")
print(f"Average Change: $ {average_change}")
print(f"Greatest Increase in Profit: {high_profit_date} ($ {high_profit})")
print(f"Greatest Decrease in Profit: {low_profit_date} ($ {low_profit})")

output = (
    f"Financial Analysis"
    f"-----------------------------"
    f"Total Months: {total_months}"
    f"Total Profit: ${net_profit}"
    f"Average Change: ${average_change}"
    f"Greatest Increase in Profits: {high_profit_date} (${high_profit})"
    f"Greatest Decrease in Profits: {low_profit_date} (${low_profit})"
)
with open ("output.txt", 'w') as txt_file_one:
    txt_file_one.write(output)