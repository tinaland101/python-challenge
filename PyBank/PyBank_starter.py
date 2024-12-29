# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = "/Users/christinaland/Downloads/Starter_Code 11/PyBank/Resources/budget_data.csv"  # Absolute file path
file_to_output = "/Users/christinaland/Downloads/Starter_Code 11/PyBank/analysis/budget_analysis.txt" # Output file path (relative)

# Define variables to track the financial data
total_months = 0
total_net = 0
net_change_list = []
previous_profit = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = ""
greatest_decrease_month = ""

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_profit = int(first_row[1])

    # Process each row of data
    for row in reader:
        # Track the total months and total net profit/loss
        total_months += 1
        current_profit = int(row[1])
        total_net += current_profit

        # Track the net change (current month profit - previous month profit)
        net_change = current_profit - previous_profit
        net_change_list.append(net_change)

        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase:
            greatest_increase = net_change
            greatest_increase_month = row[0]

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease:
            greatest_decrease = net_change
            greatest_decrease_month = row[0]

        # Update previous profit for next iteration
        previous_profit = current_profit

# Calculate the average net change across the months
average_change = sum(net_change_list) / len(net_change_list) if net_change_list else 0

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:,.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase:,.2f})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease:,.2f})\n"
)

# Print the output to the terminal
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
