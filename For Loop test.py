import pyttsx3
import PyPDF2

book= open("Testing.pdf", 'rb')
pdfReader= PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
abc= pyttsx3.init()
page= pdfReader.getPage(21)
text=page.extract_text()
abc.say(text)
abc.runAndWait()