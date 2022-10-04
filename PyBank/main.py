import os
import csv

csvpath = os.path.join( "..", "PyBank", "Resources", "budget_data.csv")

# VARAIBLES
months_total = []
profit_total = []
profit_change = []

with open(csvpath) as csvpath:

    csvreader = csv.reader(csvpath, delimiter=",") 
    header = next(csvreader)  

    for row in csvreader: 
        months_total.append(row[0])
        profit_total.append(int(row[1]))

    # Iterate through profits 
    for i in range(len(profit_total)-1):
        profit_change.append(profit_total[i+1] - profit_total[i])
        
# Max and min for change in profit
max_profit = max(profit_change)
min_profit = min(profit_change)
max_month = profit_change.index(max(profit_change)) + 1
min_month = profit_change.index(min(profit_change)) + 1 

# Print statements
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months_total)}")
print(f"Total: ${sum(profit_total)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {months_total[max_month]} (${(str(max_profit))})")
print(f"Greatest Decrease in Profits: {months_total[min_month]} (${(str(min_profit))})")

text_path = "output.text"
with open(text_path,"w") as file:
    
# Write print statements
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {len(months_total)}\n")
    file.write(f"Total: ${sum(profit_total)}\n")
    file.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}\n")
    file.write(f"Greatest Increase in Profits: {months_total[max_month]} (${(str(max_profit))})\n")
    file.write(f"Greatest Decrease in Profits: {months_total[min_month]} (${(str(min_profit))})")