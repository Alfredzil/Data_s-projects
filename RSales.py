#!/usr/bin/env python
"""reducer.py"""

# reducer to read and process the data
 
import sys

# initialize and define the variables
current_country = None
current_sum = 0
rating = 0
country = None

# input comes from STDIN (standard input)
for line in sys.stdin:

# remove any spaces or blanks
    line = line.strip()
   
# read the rating and count delimited by tab
    country, SaleAmt = line.split("\t")
    SaleAmt = int(SaleAmt)

# Assign the values from the first line
    if current_country == None:
        current_country = country
        current_sum = SaleAmt

# Check if the rating has changed in the sorted stream of data
    if current_country == country:
        current_sum += SaleAmt
    else:
        if current_country:
            print (current_country, current_sum)
        current_country = country
        current_sum = SaleAmt

# print the last rating count
if current_country == country:
    print (current_country, current_sum)

