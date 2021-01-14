import pyttsx3
import PyPDF2

speaker = pyttsx3.init()
file3 = open(r"C:\Users\Syeem\Downloads\OOP.pdf", "rb")
pdfreader = PyPDF2.PdfFileReader(file3)
pages = pdfreader.numPages
#print(pages)
for num in range(256,pages):
    page = pdfreader.getPage(256)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
