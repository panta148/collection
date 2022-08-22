import pyttsx3 #to make the sound(read the pdf)
import PyPDF2 #to choice pdf and open the pdf file
from tkinter.filedialog import *
book=askopenfilename()
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
for num in range(1,pages):
    print("Connecting.....")
    page=pdfReader.getPage(num)
    text=page.extractText()
    player=pyttsx3.init()
    player.say(text)
    player.runAndWait()
print("Thank you for the service...")