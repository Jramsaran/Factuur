from fastapi import FastAPI
from apps import pdf_reading 
from apps import pdf_regex
import pandas as pd

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

    
    regexs = {}
    
    regexs['Regex'] = [
            '(\d{8}) ([a-zA-Z0-9\W\s]+) (\d+-\d+-\d{4}) ([a-zA-Z0-9\W\s]+) (\w{4}\s\d{6}[-/]\d) ([a-zA-Z0-9\W\s]+) (\d+,\d{2})',
            '^Totaal charterkosten.*',
            'Totaal extra kosten.*',
            'TOTAAL GENERAAL.*',
            '^.+\s(-?\d+,\d{2}) (.+)$',
            '^Ritnummer.*',
            '^\w{4} \d+[-/]\d.*',
            '.\d+,\d{2}$',
            '^Totaal bedrag Route.*'
            ]
    
    regexs['Settings'] = [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0
            ]
    
    
    regexs = pd.DataFrame.from_dict(regexs)
    
    regex_dict = {}

    x = {}

    '''
    for index, regex in enumerate(regexs):

        regex_dict[index] = pdf_regex.Regex_Compiler(regex)
        
        x[index] = regex_dict[index].regex_match(decoded_text)
    '''    
    print(regexs)



