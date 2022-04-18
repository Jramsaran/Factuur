from fastapi import FastAPI
from apps import pdf_reading as Read
from apps import pdf_regex as Regex
import pandas as pd

'''

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
    
'''

if __name__ == '__main__':

    try:

        pdf = Read.Read_PDF(r'C:\\Users\\Jeremy\\Downloads\\CharterKosten-2366.pdf')
        temp_file_path = pdf.rotator(270)

        extracted_text = pdf.read_pdf(temp_file_path)
        decoded_text = pdf.decode_pdf(extracted_text)

        pdf.delete_temp_file(temp_file_path)

    except Exception:

        print("Something went wrong...")
        print(f'\n\n\n\n\n + {extracted_text}')

    x,y = Regex.search_patterns_JPR(decoded_text)

    
    regexs = {}
    
    regexs['Regex_Name'] = [
            're_JPR'
            ,'charterkosten_JPR'
            ,'extrakosten_JPR'
            ,'totaalbedragen_JPR'
            ,'rit_extra_kosten_JPR'
            ,'ritnummers_JSR'
            ,'containernummers_JSR'
            ,'rit_bedragen_JSR'
            ,'totaalbedrag_JSR'
            ]

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
    
    for index, row in regexs.iterrows():

        dict_key = row[0]

        regex_dict[dict_key] = Regex.Regex_Compiler(row)
        
        x[dict_key] = regex_dict[dict_key].regex_search(decoded_text)
     
    print(x['rit_extra_kosten_JPR'])
