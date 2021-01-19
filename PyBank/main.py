#Import OS & CSV
import os
import csv

#Set CSV path
budget_csv = os.path.join('PyBank', 'Resources', 'budget_data.csv')

#Set zero
total_months = 0
net_amount = 0

#Define Variables
def financial_analysis(budget_csv):

    total_months = str(budget_csv[0])
    amount = int(budget_csv[1])

#Open and read CSV
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    month = []
    amount = []

    for row in csvreader:

        month.append(row[0])
        amount.append(int(row[1]))

        #Total number of months
        total_months = len(list(csvreader)) + 1

        #Net profit amount
        net_amount = sum(amount)


    print(f"Total Months: {total_months}")
    print(f"Total: {net_amount}")
    

