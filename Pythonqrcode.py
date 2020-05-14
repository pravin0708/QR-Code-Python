import pyqrcode 
import pypng 
from pyqrcode import QRCode 


domain = "www.pravinpandit.site"

# Generate QR code 
url = pyqrcode.create(domain) 

# Create and save the svg file naming "myqr.svg" 
url.svg("myqr.svg", scale = 8) 

# Create and save the png file naming "myqr.png" 
url.png('myqr.png', scale = 6) 
