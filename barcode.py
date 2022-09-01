import pyqrcode
import png
from PIL import Image




link = input("Ingrese cualquier cosa: ")
qr_code = pyqrcode.create(link)
qr_code.png("Qrcode.png", scale=5)

Image.open("Qrcode.png")


 