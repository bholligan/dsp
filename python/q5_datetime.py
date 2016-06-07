# Hint:  use Google to find python function

import datetime as dt

def days_diff(date_start, date_stop, part):
    # Convert creates a list in the order of Month, Day, Year from the date string
    if part == 'a':
        # Create list by spltting via the hyphen
        convert = lambda date_string: [int(date) for date in date_string.split('-')]
    elif part == 'b':
        # Create a a list by slicing the date string
        convert = lambda date_string: [int(date) for date in [
                                date_string[:2],
                                date_string[2:4],
                                date_string[4:]]]
    else:
        # Create a list with only the numeric elements of the date string
        convert = lambda date_string: [int(date) for date in date_string.split('-') if date.isnumeric()]
    
    d_start_list = convert(date_start)
    d_stop_list = convert(date_stop)
    
    if part == 'c':
        # Exception to insert the month number of the date based on the 3-letter month abbreviation
        d_start_list.insert(0,dt.datetime.strptime(date_start[3:6], '%b').month)
        d_stop_list.insert(0,dt.datetime.strptime(date_stop[3:6], '%b').month)
    
    #Convert the start and stop dates to datetime.date elements
    d_start = dt.date(d_start_list[2],
                      d_start_list[0],
                      d_start_list[1])
    d_stop = dt.date(d_stop_list[2],
                     d_stop_list[0],
                     d_stop_list[1])
    
    # Print the difference in days
    print((d_stop - d_start).days)
####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

days_diff(date_start,date_stop,'a')

####b)  
date_start = '12312013'  
date_stop = '05282015'  

days_diff(date_start,date_stop,'b')

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015' 

days_diff(date_start,date_stop,'c')

