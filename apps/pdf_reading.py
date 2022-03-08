import pdfplumber
import PyPDF2
import os
import random
import re


class Read_PDF:

    def __init__(self, pdf_file: str) -> None:

        self.pdf_file = pdf_file

    def create_temp_file(self, pdf_file: str, file_num: int = 0) -> str:

        file_number = random.randint(234523 * 323, 234523 * 656)
        file_path = os.path.dirname(pdf_file)

        temp_file_path = file_path + f'\\tmp_rotated_{file_number}.pdf'

        if os.path.exists(temp_file_path) is True:

            file_number += 1
            self.create_temp_file(self, pdf_file, file_num=file_number)

        print(f"Temp file {temp_file_path} created.")
        return temp_file_path

    def delete_temp_file(self, tmp_file_path: str) -> None:

        if os.path.exists:

            os.remove(tmp_file_path)

        print(f"Temp file {tmp_file_path} deleted.")

    def rotator(self, rotation_degree: int) -> str:

        pdf_file = self.pdf_file

        temp_file_path = self.create_temp_file(pdf_file)

        with open(pdf_file, 'rb') as pdf_in:
            pdf_reader = PyPDF2.PdfFileReader(pdf_in)
            pdf_writer = PyPDF2.PdfFileWriter()

            for pagenum in range(pdf_reader.numPages):
                page = pdf_reader.getPage(pagenum)
                page.rotateClockwise(rotation_degree)
                pdf_writer.addPage(page)

            with open(temp_file_path, 'wb') as pdf_out:
                pdf_writer.write(pdf_out)
                pdf_out.close()

        print(f"Temp file {temp_file_path} created")
        return temp_file_path

    def read_pdf(self, pdf_file: str) -> str:

        with pdfplumber.open(pdf_file) as pdf:

            compiled_text = ""

            for n in range(len(pdf.pages)):

                page = pdf.pages[n]
                text = page.extract_text()
                compiled_text += text

            return compiled_text

    def cidToChar(self, cidx):
        return chr(int(re.findall(r'\(cid\:(\d+)\)', cidx)[0]) + 29)

    def decode_pdf(self, extracted_text: str) -> str:

        text = {}
        compiled_text = ""

        for index, line in enumerate(extracted_text.split('\n')):
            text[index] = []
            if line != '':
                regex_result = re.findall(r'\(cid\:\d+\)', line)
                if len(regex_result) > 0:
                    for cid in regex_result:
                        line = line.replace(cid, self.cidToChar(cid))
                        text[index].append(line)

                compiled_text += repr(line).strip("'").replace('Ù', '€')
                compiled_text += '\n'

        compiled_text = compiled_text.rstrip()  # remove trailing newline

        return compiled_text


if __name__ == '__main__':

    pdf = Read_PDF(r'C:\\Users\\Jeremy\\Downloads\\CharterKosten-2366.pdf')
    temp_file_path = pdf.rotator(270)

    extracted_text = pdf.read_pdf(temp_file_path)
    decoded_text = pdf.decode_pdf(extracted_text)

    pdf.delete_temp_file(temp_file_path)

    print(decoded_text)
