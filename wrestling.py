import os
import csv

# Path to collect data from the Resources folder
data_path = os.path.join('resources', 'WWE-Data-2016.csv')

# Define the function and have it accept the 'wrestler_data' as its sole parameter
def get_percentages(wrestler_data):

    # Total matches can be found by adding wins, losses, and draws together
    total_matches = int(wrestler_data[1]) + int(wrestler_data[2]) + int(wrestler_data[3])

    # Win percent can be found by dividing the the total wins by the total matches and multiplying by 100
    
    win_percent = round((int(wrestler_data[1])/total_matches)*100,0)
    # Loss percent can be found by dividing the total losses by the total matches and multiplying by 100
    
    loss_percent = round((int(wrestler_data[2])/total_matches)*100,0)
    # Draw percent can be found by dividing the total draws by the total matches and multiplying by 100
    
    draw_percent = round((int(wrestler_data[3])/total_matches)*100,0)
    # If the loss percentage is over 50, wrestler_type is "Jobber". Otherwise it is "Superstar".
    
    if(loss_percent > 50):
        wrestler_type = 'Jobber'
    else:
        wrestler_type = 'Superstar'
    # Print out the wrestler's name and their percentage stats
    
    print(f"{wrestler_data[0]} has total of {total_matches} and {win_percent} % of win, {loss_percent} % of loss and {draw_percent} % of draw. He is a {wrestler_type}!!!")


# Read in the CSV file
with open(data_path, 'r') as csvfile:
   
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Prompt the user for what wrestler they would like to search for
    user_input = input('What wrestler do you look for? ')

    # Loop through the data
    for row in csvreader:
    
        # If the wrestler's name in a row is equal to that which the user input, run the 'get_percentages()' function
        if(user_input == row[0]):
            get_percentages(row)
