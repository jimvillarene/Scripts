#! /usr/bin/env python3
import PyPDF2,os

dir_path = os.path.dirname(os.path.realpath(__file__))
pdfFile1=os.path.join(dir_path,'meetingminutes1.pdf')
pdfFile2=os.path.join(dir_path,'meetingminutes2.pdf')
pdfFileJoined=os.path.join(dir_path,'combinedminutes.pdf')
pdf1=open(pdfFile1,'rb')
pdf2=open(pdfFile2,'rb')
reader1=PyPDF2.PdfReader(pdf1)
reader2=PyPDF2.PdfReader(pdf2)

print(len(reader1.pages))
page=reader1.pages[0]
print(page.extract_text())
for pagenum in range(len(reader1.pages)):
    page=reader1.pages[pagenum]
    print(page.extract_text())

writer=PyPDF2.PdfWriter()
for pagenum in range(len(reader1.pages)):
    page=reader1.pages[pagenum]
    writer.add_page(page)

for pagenum in range(len(reader2.pages)):
    page=reader2.pages[pagenum]
    writer.add_page(page)

outpufile=open(pdfFileJoined,'wb')
writer.write(outpufile)
outpufile.close()