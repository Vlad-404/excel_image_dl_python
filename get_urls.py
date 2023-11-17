import pandas as pd
import openpyxl as opyx
from pprint import pprint

image_urls = []

wb = opyx.load_workbook('test_sheet1.xlsx')
sheets = wb.sheetnames
ws = wb[sheets[0]]

# Iterate through rows 
for i, row in enumerate(ws): 
    # Skip the first row (the row with the column names) 
    if i == 0: 
        continue
    
    # Gets the url values from the links in the 2nd column
    link = row[2].hyperlink.target
    # Add the value to the list 
    image_urls.append(link) 

pprint(image_urls)
# https://www.geeksforgeeks.org/get-values-of-all-rows-in-a-particular-column-in-openpyxl-python/
