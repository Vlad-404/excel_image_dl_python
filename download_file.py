import urllib.request 
from PIL import Image 

link = "https://www.shutterstock.com/shutterstock/photos/2111339666/display_1500/stock-photo-panoramic-view-of-the-empty-highway-through-the-fields-in-a-fog-at-night-moonlight-clear-sky-2111339666.jpg"

# Retrieving the resource located at the URL 
# and storing it in the file name a.png
urllib.request.urlretrieve(link, "highway.jpg") 
  
# Opening the image and displaying it (to confirm its presence) 
img = Image.open(r"highway.jpg") 
img.show()
