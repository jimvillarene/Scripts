#! /usr/bin/env python3
import PyPDF2,os, pyperclip

dir_path = os.path.dirname(os.path.realpath(__file__))
pdfFile1=os.path.join(dir_path,'Golden Standard IGNITE 2023-1.pdf')
pdf1=open(pdfFile1,'rb')
reader1=PyPDF2.PdfReader(pdf1)

print(len(reader1.pages))
page=reader1.pages[0]
text=""
print(page.extract_text())
for pagenum in range(len(reader1.pages)):
    page=reader1.pages[pagenum]
    print(page.extract_text())
    text += page.extract_text() + " "  # Agrega el texto de la página actual junto con un espacio

print(text)
pyperclip.copy(text)#! /usr/bin/env python3
