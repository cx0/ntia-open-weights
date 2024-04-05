# pip install --upgrade pymupdf
import fitz
import os

for file in os.listdir('docs'):
    # 'NTIA-2023-0009-0001_RFC' is the RFC file and not a comment
    if file.endswith('.pdf') and not file.startswith('NTIA-2023-0009-0001_RFC'):
        # print(f"Filename is {file}")
        doc = fitz.open('docs/' + file)
        file = file.replace('.pdf', '')
        out = open('texts2/' + file + '.txt', 'wb')
        for page in doc:
            text = page.get_text().encode('utf-8')
            out.write(text)
        out.close()