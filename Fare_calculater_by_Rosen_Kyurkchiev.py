#--------------------------------------------------------------------------
#------Created  : 19/01/2025 - Rosen Kyurkchiev
#------Modified : 
#------Description : Python file calculating taxi fares based on mileage of the trip
#--------------------------------------------------------------------------

import csv

#---------------Functions-----------------------


#------Calculates the total cost of a trip.---------
def calculate_price(miles, fare):
    if miles < 30:  # Check if the trip is under 30 miles
        return 65  # Fixed price for short trips

    cost = miles * fare  #Formula for calculating of the cost/price
    return cost

#-----Determines the fare based on mileage----------
def check_the_lent_trip(mileage):
    if mileage >= 100:
        return 2  # Fare per mile in £
    elif mileage >= 50:
        return 2.5
    elif mileage >= 30:
        return 3
#-----------End of Functions--------------


#-----Initializing the trips list.
trips = []
#-----Handling the file with trips and distances.
with open('listoftrips.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row

    for row in reader:
        try:
            Pick_up, Dropo_off, Mileage = row
            Mileage = int(Mileage)  # Convert Mileage to integer
            Fare = check_the_lent_trip(Mileage)
            Cost = calculate_price(Mileage, Fare)  # Calculate total cost
            if Cost is not None:  # Only append if cost calculation was successful
                trips.append([Pick_up, Dropo_off, Mileage, Fare, Cost])
        except ValueError:
            print(f"Error: Invalid data in row: {row}. Skipping this row.")

#----Transfering the data from the sorce file and entering the calculeted cost/prices
with open('calculated_rates.csv', 'w', newline='') as file:
    writer = csv.writer(file) # Create a CSV writer object
    writer.writerow(['Pick_up', 'Drop_off', 'Mileage', 'Fare', 'Cost']) # Write the header row to the CSV file
    writer.writerows(trips)# Write the data rows (from the 'trips' list) to the CSV file
    print('Results saved to calculated_rates.csv') # Print a confirmation message