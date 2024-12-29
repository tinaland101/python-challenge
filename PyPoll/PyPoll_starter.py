# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = "/Users/christinaland/Downloads/Starter_Code 11/PyPoll/Resources/election_data.csv"  # Input file path (absolute path)
file_to_output = "/Users/christinaland/Downloads/Starter_Code 11/PyPoll/analysis/election_data.txt"   # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_votes = {}  # Dictionary to hold candidates and their vote counts

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(f"Total Votes: {total_votes}")
    txt_file.write(f"Total Votes: {total_votes}\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate_name, votes in candidate_votes.items():
        # Get the vote count and calculate the percentage
        vote_percentage = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

        # Print and save each candidate's vote count and percentage
        print(f"{candidate_name}: {vote_percentage:.3f}% ({votes})")
        txt_file.write(f"{candidate_name}: {vote_percentage:.3f}% ({votes})\n")

    # Generate and print the winning candidate summary
    print("-------------------------")
    print(f"Winner: {winning_candidate}")
    print(f"Winning Vote Count: {winning_count}")
    print(f"Winning Percentage: {winning_percentage:.3f}%")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winning_candidate}\n")
    txt_file.write(f"Winning Vote Count: {winning_count}\n")
    txt_file.write(f"Winning Percentage: {winning_percentage:.3f}%\n")
