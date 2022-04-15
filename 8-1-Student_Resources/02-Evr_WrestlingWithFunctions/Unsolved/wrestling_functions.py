import os
import csv

# Path to collect data from the Resources folder
file_path = os.path.join('..', 'Resources', 'WWE-Data-2016.csv')

# Define the function and have it accept the 'wrestlerData' as its sole parameter
def print_percentages(wrestlerData):
    wrestler_name = str(wrestlerData[0])
    wrestler_wins = int(wrestlerData[1])
    wrestler_losses = int(wrestlerData[2])
    wrestler_draws = int(wrestlerData[3])

# Find the total number of matches wrestled
    wrestler_totalmatches = wrestler_wins + wrestler_losses + wrestler_draws

# Find the percentage of matches won
    wrestler_percent_won = (wrestler_wins/wrestler_totalmatches)*100

# Find the percentage of matches lost
    wrestler_percent_lost = (wrestler_losses/wrestler_totalmatches)*100

# Find the percentage of matches drawn
    wrestler_percent_drawn = (wrestler_draws/wrestler_totalmatches)*100

# Print out the wrestler's name and their percentage stats
    print(f"Here are the percentage stats for {wrestler_name}:")
    print(f"This wrestler's win percentage is {wrestler_percent_won}.")
    print(f"This wrestler's win percentage is {wrestler_percent_won}.")

# Read in the CSV file
with open(file_path, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if(name_to_check == row[0]):
            print_percentages(row)
