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
    ^(?P<first>[\w.-]+)\s
    ([\w.\(\)]+\s)?
    (?P<last>[\w-]+),
    \s*(?P<degree>.*),
    (?P<title>[\w\s]*Professor)[\w\s]*,
    (?P<email>.*)$
''', re.X|re.M|re.I)

faculty_dict = {}
professor_dict = {}
for match in line.finditer(string):
    #Question 6
    last_name = match.group('last')
    values = [match.group(item) for item in match.groupdict() 
              if item in ['degree','title','email']]
    #The following if statement is to handle repeated last names        
    if last_name in faculty_dict:
        faculty_dict[last_name].append(values)
    else:        
        faculty_dict[last_name] = []        
        faculty_dict[last_name].append(values)
    #Question 7
    first_name = match.group('first')
    prof_key = (first_name,last_name)
    #The following if statement is to handle repeated first and last names
    if (first_name, last_name) in professor_dict:
        professor_dict[prof_key].append(values)
    else:
        professor_dict[prof_key] = []        
        professor_dict[prof_key].append(values)
        
def print_dict(dict, count):
#Used to handle the requests for printing x number of key/value pairs
    for idx,k in enumerate(sorted(dict.keys())):
        if idx <count:
            print('{}: {}'.format(k,dict[k]))
        else:
            break

print_dict(faculty_dict, 3)
print_dict(professor_dict, 3)

#Question 8
#Sorting and printing off the second element in the key tuple (last_name)
for k in sorted(professor_dict.keys(),key = lambda x: x[1]):
    print('{}: {}'.format(k,professor_dict[k]))
