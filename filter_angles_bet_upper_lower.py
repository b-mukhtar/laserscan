#Code for part 2 question 2
import csv
import math

def filter_scan(coordinates, lower_limit1, upper_limit1, lower_limit2, upper_limit2):
    filtered_coordinates = []
    for i in range(len(coordinates)):
        angle = coordinates[i][1]
        if (angle >= lower_limit1 and angle <= upper_limit1) or (angle >= lower_limit2 and angle <= upper_limit2):
            filtered_coordinates.append(coordinates[i])
    return filtered_coordinates

lower_limit1 = -math.pi/2
upper_limit1 = -math.pi/4
lower_limit2 = math.pi/4
upper_limit2 = math.pi/2

with open("laserscan.csv", "r") as file:
    reader = csv.reader(file)
    next(reader) # skip the header
    data = [row for row in reader]

coordinates = [(float(row[0]), float(row[1])) for row in data]
filtered_coordinates = filter_scan(coordinates, lower_limit1, upper_limit1, lower_limit2, upper_limit2)

#header = ["X", "Y"]

with open("filtered_laserscan_final.csv", "w", newline='') as file:
    writer = csv.writer(file)
    #writer.writerow(header)
    writer.writerows(filtered_coordinates)
