from fastapi import FastAPI
from apps import pdf_reading 
from apps import pdf_regex


'''

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
    
'''

if __name__ == '__main__':

    try:

        pdf = pdf_reading.Read_PDF(r'C:\\Users\\Jeremy\\Downloads\\CharterKosten-2366.pdf')
        temp_file_path = pdf.rotator(270)

        extracted_text = pdf.read_pdf(temp_file_path)
        decoded_text = pdf.decode_pdf(extracted_text)

        pdf.delete_temp_file(temp_file_path)

    except Exception:

        print("Something went wrong...")
        print(f'\n\n\n\n\n + {extracted_text}')

    x,y = pdf_regex.search_patterns_JPR(decoded_text)
        
    print(x)