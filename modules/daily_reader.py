import pandas as pd
import csv

# Reader built to read in daily_area.txt
def daily_reader(path):
    # Initialize variables
    year = []
    month = []
    day = []
    total = []
    north = []
    south = []

    # Open text file
    with open(path, newline='') as txtfile:
        # Set up reader 
        reader = csv.reader(txtfile,delimiter=' ')

        # Get header row (not used)
        header = next(reader)
        
        # Read each line of file
        for row in reader:
            # Remove empty strings (no uniform delimiter was found)
            while '' in row:
                row.remove('')

            # Add each remaining element to appropriate list
            year.append(row[0])
            month.append(row[1])
            day.append(row[2])
            total.append(row[3])
            north.append(row[4])
            south.append(row[5])
     
    # Create dataframe 
    df = pd.DataFrame({
    "Year": year,
    "Month": month,
    "Day": day,
    "Total": total,
    "North": north,
    "South": south
    })
    
    # Do we want to remove missing reading?  Code below
    # Remove row with missing readings (represented as -1)
    #df = df.loc[df['Total'] != '-1.0'].reset_index(drop=True)
    
    # Return dataframe
    return df