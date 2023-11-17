import pandas as pd
import openpyxl as opyx
import urllib.request

from pprint import pprint

image_urls = []

wb = opyx.load_workbook('test_sheet1.xlsx')
sheets = wb.sheetnames
ws = wb[sheets[0]]

def dl_images(img_urls):
    for link in img_urls:
        urllib.request.urlretrieve(link, "highway.jpg")
        print('Link from dl_images: ', link)

# Iterate through rows
def get_links():
    for i, row in enumerate(ws): 
        # Skip the first row (the row with the column names) 
        if i == 0: 
            continue
        
        # Gets the url values from the links in the 2nd column
        link = row[2].hyperlink.target
        # Add the value to the list 
        image_urls.append(link)

    dl_images(image_urls)


get_links()
# pprint(image_urls)
# https://www.geeksforgeeks.org/get-values-of-all-rows-in-a-particular-column-in-openpyxl-python/
