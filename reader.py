import pyttsx3
from PyPDF2 import PdfReader

def read_pdf(file_name: str):

    reader = PdfReader(file_name)
    number_of_pages = len(reader.pages)

    speech_engine = pyttsx3.init()

    clean_text = ''

    for page in range(number_of_pages):
        text = reader.pages[page].extract_text()
        clean_text += text.strip().replace('\n', ' ')

    new_audio = file_name.replace('.pdf', '.mp3') 
    speech_engine.save_to_file(clean_text, new_audio)
    speech_engine.runAndWait()

    speech_engine.stop()