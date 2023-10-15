# import
import PyPDF2, pyttsx3

# pdf path
path = open('YOUR PDF PATH','rb')

# pdfreader object created
pdfReader = PyPDF2.PdfReader(path)

# get an engine instance for the speech synthesis

speak = pyttsx3.init()

for pages in range(len(pdfReader.pages)):
    text = pdfReader.pages[pages].extract_text()
    speak.say(text)
    speak.runAndWait()


speak.stop()


