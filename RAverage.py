#!/usr/bin/env python
"""reducer.py"""

# reducer to read and process the data
 
import sys

# initialize and define the variables
HName = None
rating = 0.0
current_HName = None
sum_rating = 0.0
count_rating = 0.0
average_rating = 0.0

# input comes from STDIN (standard input)
for line in sys.stdin:

# remove any spaces or blanks
    line = line.strip()
   
# read the Hotel Name and Rating delimited by tab
    HName, rating = line.split("\t")
    rating = float(rating)
    if current_HName == None:
        current_HName = HName

# Check if the Hotel Name has changed in the sorted stream of data
    if current_HName == HName:
        count_rating += 1
        sum_rating += rating
    else:
        if current_HName:
            average_rating = round(sum_rating / count_rating, 2)
            print (current_HName, '%.2f' %  average_rating)
        current_HName = HName
        count_rating = 1
        sum_rating = rating

# Calculate and print the Hotel Name and Average Rating for the last hotel 
if current_HName == HName:
    average_rating = round(sum_rating/count_rating,2)
    print (current_HName, '%.2f' % average_rating)
