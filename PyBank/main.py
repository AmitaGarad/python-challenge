import os
import csv

# Set path for file
file_path = os.path.join("Resources", "budget_data.csv")
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#Initialize variables to store the data:

total_months = 0
total_profit_loss = 0
profit_loss = []
months = []

#Read the CSV file and store the data in the initialized variables:

with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))
        total_months += 1
        total_profit_loss += int(row[1])

#Calculate the changes in profit/losses over the entire period and store them in a list:

change = []
for i in range(1,len(profit_loss)):
    change.append(profit_loss[i]-profit_loss[i-1])


#Calculate the average change in profit/losses over the entire period:

average_change = round(sum(change)/len(change),2)

#Find the greatest increase and decrease in profits (date and amount) over the entire period:

greatest_increase = max(change)
greatest_decrease = min(change)
greatest_increase_date = str(months[change.index(max(change))+1])
greatest_decrease_date = str(months[change.index(min(change))+1])


#Print the results:
print("-----------------------------")
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
print("-----------------------------")

