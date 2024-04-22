import csv
import math

def read_from_csv(filename):
    coordinates = []
    with open(filename, newline='') as source_csvfile:
        reader = csv.reader(source_csvfile)
        for row in reader:
            coordinates.append((float(row[0]), float(row[1])))
    return coordinates

def write_to_csv(filename, coordinates):
    with open(filename, 'w', newline='') as new_csvfile:
        writer = csv.writer(new_csvfile)
        for row in coordinates:
            writer.writerow(row)

def from_polar_to_cartesian(coordinates):
    cartesian = []
    for i in range(len(coordinates)):
        distance = coordinates[i][0]
        angle = coordinates[i][1]
        x = distance * math.cos(angle)
        y = distance * math.sin(angle)
        cartesian.append((x, y))
    return cartesian

def from_cartesian_to_polar(coordinates):
    polar = []
    for i in range(len(coordinates)):
        x = coordinates[i][0]
        y = coordinates[i][1]
        distance = math.sqrt(x**2 + y**2)
        angle = math.atan2(y, x)
        polar.append((distance, angle))
    return polar

def filter_scan(coordinates, lower_limit, upper_limit):
    filtered_coordinates = []
    for i in range(len(coordinates)):
        angle = coordinates[i][1]
        if angle >= lower_limit and angle <= upper_limit:
            filtered_coordinates.append(coordinates[i])
    return filtered_coordinates


x = read_from_csv('laserscan.csv')
print(x)
b= from_cartesian_to_polar(x)
print('Done Printing X which is in Cartesian coordinate', "Now printing b-coordinates in polar coordinate(Polar cordinate with angle in Radian and not degree")
print(b)
             