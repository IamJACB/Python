import barcode
from barcode.writer import ImageWriter
from barcode import EAN13

number = input("Ingrese codigo")


my_barcode = EAN13(number, writer=ImageWriter())

my_barcode.save("Codigo generado")


