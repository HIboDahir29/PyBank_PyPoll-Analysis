# Importing Libraries
import os
import csv

# navigating and joining the file
budget_data = os.path.join('Resources', 'budget_data.csv')

print(budget_data)

with open(budget_data) as csv_file:
    csv_Reader = csv.reader(csv_file, delimiter=",")
    csv_Header = next(csv_file)
    print(f"Header: {csv_Header}")

# Declaring empty list to store the value
    Profit = []
    totalMonths = []
    average_change = []

    for rows in csv_Reader:
        totalMonths.append(rows[0])
        Profit.append(int(rows[1]))

    # iterating through the months
    for i in range(len(Profit)-1):
        average_change.append(Profit[i+1]-Profit[i])


total_profits = sum(Profit)
total_months = len(totalMonths)
average_profit_change = sum(average_change) / len(average_change)
max_increase_value = max(average_change)
max_decrease_value = min(average_change)


# printing the output
print(total_months)
print(total_profits)
print(average_profit_change)
print(max_increase_value)
print(max_decrease_value)

# printing the output

print("Financial Analysis")

print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*---*--*-*-')

print('Total Months : ' + str(total_months))
print("Total: " + "$" + str(sum(Profit)))
print('Average change: ' + '$' + str(round(average_profit_change, 2)))
print("Greatest Increase in Profits: " + str(totalMonths[average_change.index(
    max(average_change))+1]) + " " + "$" + str(max_increase_value))
print("Greatest Decrease in Profits: " + str(totalMonths[average_change.index(
    min(average_change))+1]) + " " + "$" + str(max_decrease_value))


# output to a text file
output = open("Analysis/Py_Bank_Output.txt", "w")
output.write("Analysis" + "\n")
output.write('Total Months : ' + str(total_months) + "\n")
output.write("Total: " + "$" + str(sum(Profit)) + "\n")
output.write('Average change: ' + '$' +
             str(round(average_profit_change, 2)) + "\n")
output.write("Greatest Increase in Profits: " + str(totalMonths[average_change.index(
    max(average_change))+1]) + " " + "$" + str(max_increase_value) + "\n")
output.write("Greatest Decrease in Profits: " + str(totalMonths[average_change.index(
    min(average_change))+1]) + " " + "$" + str(max_decrease_value))

output.close()
