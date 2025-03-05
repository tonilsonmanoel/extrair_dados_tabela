import pandas as pd
import json
from extrair_dados import ExtrairDados
jsonResult = {}

def main():
    jsonIphone = ExtrairDados.extrairDadosIphone()
    jsonLg = ExtrairDados.extrairDadosLg()
    jsonMotorola = ExtrairDados.extrairDadosMotorola()
    jsonSamsungOriginalChina = ExtrairDados.extrairDadosDisplaySamsungOriginalChina()
    jsonXiaomi = ExtrairDados.extrairDadosDisplayXiaomi()
    jsonSamsung_incell= ExtrairDados.extrairDadosSamsungIncell()
    json_Samsung_lcd = ExtrairDados.extrairDadosSamsungLcd()
    json_zenfone = ExtrairDados.extrairDadoszenfone()
    

    jsonResult.update(jsonIphone)
    jsonResult.update(jsonLg)
    jsonResult.update(jsonMotorola)
    jsonResult.update(jsonSamsungOriginalChina)
    jsonResult.update(jsonXiaomi)
    jsonResult.update(jsonSamsung_incell)
    jsonResult.update(json_Samsung_lcd)
    jsonResult.update(json_zenfone)



    with open("json_resultados/dados_extraidos_RESULTADO.json", "w", encoding="utf-8") as f:
      
        json.dump(jsonResult, f, sort_keys=True, indent=4, ensure_ascii=False)
       #f.write(json_str)
        print("Json resutado salvo na pasta")
    # Exibir os dados
  

if __name__ == '__main__':
   main()


