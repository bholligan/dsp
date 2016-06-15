# Pull data out of the csv
import csv
import re

string = ''
first_line = 1
with open('faculty.csv', newline = '') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        #Importing the entire file as a string with comma separation to
        #prepare for the regex filtering.
        string = string + ','.join(row) + '\n'
#Regex that goes through each line of the string and puts values into groups
line = re.compile(r'''
    ^(?P<name>.*),\s*
    (?P<degree>.*),
    (?P<title>.*),
    (?P<email>[-\w\d+.]+@(?P<domain>[-\w\d.]+))$
''', re.X|re.M|re.I)

#dictionary that will contain all the raw data
mydict = {'name': [], 'degree': [], 'title': [], 'email': [], 'domain': []}

#Initializing filtered outputs
degree_output = {}
title_output = {}
domain_output = []

for match in line.finditer(string):
    for key in match.groupdict():
        match_string = match.group(key)
        #Populate dictionary with match values
        mydict[key].append(match_string)
        #Question 1
        #Make a dictionary with each degree and its frequency        
        if key == 'degree':
            #Make sure the entry is actually a string.
            if match_string.isnumeric() == False:
                #Replace periods, make lower case
                degree_clean = match_string.replace(".","").lower()
                #Handle multiple degrees
                degree_list = degree_clean.split(" ")
                #Check if it's in degree dict
                for degree in degree_list:
                    if degree in degree_output:
                        degree_output[degree] += 1
                    else:
                        degree_output[degree] = 1
        #Question 2
        #Make a dictionary with each title and its frequency
        if key == 'title':
            if match_string in title_output:
                title_output[match_string] += 1
            else:
                title_output[match_string] = 1
        #Question 4
        #Make a list with each domain name
        if key == 'domain':
            if match_string not in domain_output:
                domain_output.append(match_string)
                
print("There are {} different degrees".format(len(degree_output)))
print("The degree frequencies are:\n", degree_output)
print("The title frequencies are:\n", title_output)
print("The domain names are:\n", domain_output)
#Question 3
print('The list of emails is:\n',mydict['email'])
