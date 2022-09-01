import pyqrcode
import png
import PIL
from PIL import Image




link = input("Ingrese cualquier cosa:")
qr_code = pyqrcode.create(link)
qr_code.png("Qrcode.png", scale=5)

PIL.Image.open(r"C:\Users\PRACTICANTE.SISTEMAS\Documents\Juan\Python\Curso Python\Interfaces graficas\Qrcode.png")


 