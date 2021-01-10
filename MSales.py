#!/usr/bin/env python
"""mapper.py"""

# The structure of the input dataset
# TransDate     = Transaction Date
# Country       = Transaction Country
# SaleAmt       = Sale amount
 
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
	
# read the data and split the line by tab 
    TransDate, Country, SaleAmt = line.split("\t")

# Create the rating and count key-value pair
    sale_result = [Country, SaleAmt]

# Print the result to the STDOUT
    print ("\t".join(sale_result))
