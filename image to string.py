try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Muhammet Ali Kaya\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
img = pytesseract.image_to_string(Image.open('veri.jpeg'), lang='tur')
x = img.split()
print("Okunan Veri:\n",x,"\n")