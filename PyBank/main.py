#Import OS & CSV
import os
import csv

#Set CSV path
budget_csv = os.path.join('Resources', 'budget_data.csv')

#Set variables 
total_months = 0
month = []
amount = []

#open and read CSV
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        
        #append to lists
        month.append(row[0])
        amount.append(int(row[1])) 

         #Total number of months by counting number of lines
        total_months += 1     

net_amount = amount[0]
monthly_change = 0
high_profit = 0
low_profit = 0
average_monthly_change = 0 

for i in range (1, total_months):

    #Net profit amount
    net_amount += amount[i]

    #Find change in monthly amounts
    current_change = amount[i] - amount[i-1]
    monthly_change += current_change
    
    #greatest increase and decrease
    if current_change > high_profit:
        high_profit = current_change
        high_profit_date = month [i]
    elif current_change < low_profit:
        low_profit = current_change
        low_profit_date = month[i] 

#average change 
average_monthly_change = round(monthly_change/total_months,2)

print(f"Financial Analysis")
print(f"-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total Profit: ${net_amount}")
print(f"Average Change: ${average_monthly_change}")
print(f"Greatest Increase in Profits: {high_profit_date} (${high_profit})")
print(f"Greatest Decrease in Profits: {low_profit_date} (${low_profit})")

output = (
    f"Financial Analysis"

    f"-----------------------------"

    f"Total Months: {total_months}"

    f"Total Profit: ${net_amount}"

    f"Average Change: ${average_monthly_change}"

    f"Greatest Increase in Profits: {high_profit_date} (${high_profit})"
    
    f"Greatest Decrease in Profits: {low_profit_date} (${low_profit})"
)
with open ("output.txt", 'w') as txt_file:
    txt_file.write(output)