# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv
with open('football.csv', newline = '') as csvfile:
    reader = csv.reader(csvfile)
    data = [row for row in reader]

gd = [[row[0], abs(int(row[5])-int(row[6]))] for row in data[1:]]
gd_min = min(gd, key = lambda x: x[1])[1]

# I can't seem to figure out a more concise way to handle the scenario
# where there is a tie for the smallest difference.
for row in gd:
    if row[1] == gd_min:
        print(row[0])
