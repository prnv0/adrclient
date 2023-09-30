# needs tesseract and ocrmypdf libraries
# import os
# os.system('ocrmypdf --sidecar output.txt ehr.pdf output.pdf')
import fitz 
doc = fitz.open("Python\ADRDetection\ehr.pdf")
all_text = ""
for page in doc:
    all_text += page.get_text() + chr(12)
print(all_text.splitlines())
splittext=all_text.splitlines()
s=splittext.index("Additional Notes")
prompt=splittext[4]+"|"+splittext[5]+"|"+splittext[23]+"|"+splittext[24]+"|"
for i in range(s+3, len(splittext)-3):
    prompt+=splittext[i]+" "
print(prompt)

