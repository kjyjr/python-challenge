import os
import csv
budgetCSV = os.path.join('Resources', 'budget_data.csv')
FinancialAnalysisCSV = os.path.join('FinancialAnalysis.txt')

total_months = 0
net_total = 0
net_changes = []
net_change_list = []
greatest_increase = 0
greatest_decrease = 0
greatest_increase_date = ""
greatest_decrease_date = ""

with open(budgetCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    prev_row = next(csvreader)
    total_months +=1
    net_total += int(prev_row[1])

    for row in csvreader:
        total_months +=1
        net_total += int(row[1])
        net_changes = int(row[1]) - int(prev_row[1])
        prev_row = row
        net_change_list.append(net_changes)
        date = str(row[0])
        if net_changes > greatest_increase:
            greatest_increase = net_changes
            greatest_increase_date = date
        if net_changes < greatest_decrease:
            greatest_decrease = net_changes
            greatest_decrease_date = date
average_change = round(sum(net_change_list) / len(net_change_list), 2)

print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months:}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} $({greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} $({greatest_decrease})")

with open(FinancialAnalysisCSV, 'w') as textfile:
    output = ""
    output += f"Financial Analysis\n"
    output += f"----------------------------\n"
    output += f"Total Months: {total_months}\n"
    output += f"Total: ${net_total}\n"
    output += f"Average Change: ${average_change}\n"
    output += f"Greatest Increase in Profits: {greatest_increase_date} $({greatest_increase})\n"
    output += f"Greatest Decrease in Profits: {greatest_decrease_date} $({greatest_decrease})\n"
    textfile.write(output)