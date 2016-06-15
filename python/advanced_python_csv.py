from advanced_python_regex import *

def write_file(filename):
    with open(filename, 'w') as csvfile:    
        data_writer = csv.writer(csvfile, dialect = 'excel')
        for email in mydict['email']:
            data_writer.writerow([email])

write_file('emails.csv')
