import re
import configparser


def search_patterns_JPR(text_file):
    
    config = configparser.ConfigParser()
    config.read('Settings.ini', encoding = 'utf8')

    JPR_data = [[],[],[],[],[],[]]

    JSR_data = [[],[],[],[],[]]

    JPR_extra_data = [[], [], []]

    tweede_tabel = [[],[],[],[]]

    re_JPR1 = config["COMPILERS"]["re_JPR"]
    charterkosten_JPR1 = config["COMPILERS"]["charterkosten_JPR"]
    extrakosten_JPR1 = config["COMPILERS"]["extrakosten_JPR"]
    totaalbedrag_JPR1 = config["COMPILERS"]["totaalbedrag_JPR"]
    rit_extra_kosten_JPR1 = config["COMPILERS"]["rit_extra_kosten_JPR"]
    ritnummers_JSR1 = config["COMPILERS"]["ritnummers_JSR"]
    containernummers_JSR1 = config["COMPILERS"]["containernummers_JSR"]
    rit_bedragen_JSR1 = config["COMPILERS"]["rit_bedragen_JSR"]
    totaalbedrag_JSR1 = config["COMPILERS"]["totaalbedrag_JSR"]

    re_JPR = re.compile(rf"{re_JPR1}")

    charterkosten_JPR = re.compile(rf"{charterkosten_JPR1}")

    extrakosten_JPR = re.compile(rf"{extrakosten_JPR1}")

    totaalbedragen_JPR = re.compile(rf"{totaalbedrag_JPR1}")

    rit_extra_kosten_JPR = re.compile(rf"{rit_extra_kosten_JPR1}")

    for index, line in enumerate(text_file.split("\n")):
        
        line2 = line
        line3 = line
        
        line = re_JPR.search(line)
        line3 = rit_extra_kosten_JPR.search(line3)
        #print(line)
        if line:
        
            # print(line.group(7))
            
            JPR_data[0].append(index)
            
            JPR_data[1].append(line.group(3))
                
            JPR_data[2].append(line.group(1))
                    
            JPR_data[3].append(line.group(5))
            
            JPR_data[4].append("€ " + line.group(7))
            
            JPR_data[5].append(line.group(7))
            
        #extra kosten en aantal en mss nog meer
 
        if line3:
            
            JPR_extra_data[0].append(index)
            
            JPR_extra_data[1].append("€ " + line3.group(1))
            
            JPR_extra_data[2].append(line3.group(2))

        
        if charterkosten_JPR.match(line2):
            
            search_patterns_JPR.charterkost_euro = line2.split()[-1]
            
            search_patterns_JPR.charterkost = float(line2.split()[-1].replace(".", "").replace(",", "."))

            
        elif extrakosten_JPR.match(line2):
            
            search_patterns_JPR.extrakost_euro = line2.split()[-1]
            
            search_patterns_JPR.extrakost = float(line2.split()[-1].replace(".", "").replace(",", "."))
            
            
        elif totaalbedragen_JPR.match(line2):
            
            search_patterns_JPR.totaal_bedrag_euro = line2.split()[-1]
            
            search_patterns_JPR.totaal_bedrag = float(line2.split()[-1].replace(".", "").replace(",", "."))

    return JPR_data, JPR_extra_data
