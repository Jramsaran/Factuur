from tokenize import String
import pdfplumber
import PyPDF2
import os
import random

class Read_PDF:

    def __init__(self, pdf_file: str) -> None:
        
        self.pdf_file = pdf_file


class Rotate_PDF(Read_PDF):

    def __init__(self, pdf_file: str) -> None:

        super().__init__(pdf_file)
        self.pdf_file = pdf_file

    def create_temp_file(self, pdf_file: str, file_num: int = 0) -> str:

        file_number = random.randint(234523 * 323, 234523 * 656)
        file_path = os.path.dirname(pdf_file)

        temp_file_path = file_path + f'\\tmp_rotated_{file_number}.pdf'

        if os.path.exists(temp_file_path) is True:

            file_number += 1
            self.create_temp_file(self, pdf_file, file_num = file_number)

        print(f"Temp file {temp_file_path} created.")
        return temp_file_path

    def delete_temp_file(self, tmp_file_path: str) -> None:

        if os.path.exists:

            os.remove(tmp_file_path)

        print(f"Temp file {tmp_file_path} deleted.")

    def rotator(self, rotation_degree: int) -> str:

        pdf_file = self.pdf_file

        try:
            int_rotation = int(rotation_degree)

        except ValueError:

            f"ValueError: {rotation_degree} is not a number."

        temp_file_path = self.create_temp_file(pdf_file)
        
        with open(pdf_file, 'rb') as pdf_in:
            pdf_reader = PyPDF2.PdfFileReader(pdf_in)
            pdf_writer = PyPDF2.PdfFileWriter()

            for pagenum in range(pdf_reader.numPages):
                page = pdf_reader.getPage(pagenum)
                page.rotateClockwise(int_rotation)
                pdf_writer.addPage(page)

            with open(temp_file_path, 'wb') as pdf_out:
                pdf_writer.write(pdf_out)
                pdf_out.close()

        print(f"Temp file {temp_file_path} created")
        return temp_file_path


if __name__ == '__main__':

    XD = Rotate_PDF(r'C:\\Users\\Jeremy\\Downloads\\CharterKosten-2366.pdf')

    temp_file_path = XD.rotator(180)
    XD.delete_temp_file(temp_file_path)