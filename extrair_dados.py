import pandas as pd
import json

class ExtrairDados:

   
    def extrairDadosLg():
        # Caminho do arquivo Excel
        file_path = "tabelas_template/DISPLAY_LG.xlsx"

        # Carregar o arquivo sem cabeçalhos
        df = pd.read_excel(file_path, header=None)

        # Remover a primeira linha (caso seja um título geral)
        df = df.iloc[1:]

        # Renomear colunas
        df.columns = ["Nome", "Preço"]

        # Preencher valores vazios na coluna "Preço" com "Indisponível"
        df["Preço"] = df["Preço"].astype(str).replace("nan", "Indisponível")

        # Resetar os índices
        df.reset_index(drop=True, inplace=True)
      
        json_resultado = df.to_json(orient="records", force_ascii=False, indent=4)

        # Salvar em um arquivo JSON
        with open("dados_extraidos.json", "w", encoding="utf-8") as f:
            f.write(json_resultado)
        with open("dados_extraidos.json", "r", encoding="utf-8") as f:
            dataLG = json.load(f)
        
        return {"LG": dataLG}



    def extrairDadosIphone():
    
        file_path2 = "tabelas_template/DISPLAY_IPHONE.xlsx"

        df2 = pd.read_excel(file_path2, header=None)

        df2 = df2.iloc[1:]
       
        df2.columns = ["Nome", "Preço"]

        df2["Preço"] = df2["Preço"].astype(str).replace("nan", "Indisponível")

        df2.reset_index(drop=True, inplace=True)

        json_resultado2 = df2.to_json(orient="records", force_ascii=False, indent=4)

        with open("dados_extraidosIphone.json", "w", encoding="utf-8") as f:
            f.write(json_resultado2)
       
        with open("dados_extraidosIphone.json", "r", encoding="utf-8") as f:
            dataIphone = json.load(f)

        return {"IPHONE": dataIphone}

    def extrairDadosMotorola():
    
        file_path2 = "tabelas_template/DISPLAY_MOTOROLA.xlsx"

        df2 = pd.read_excel(file_path2, header=None)

        df2 = df2.iloc[1:]

        df2.columns = ["Nome", "Preço"]

        df2["Preço"] = df2["Preço"].astype(str).replace("nan", "Indisponível")

        df2.reset_index(drop=True, inplace=True)

        json_resultado2 = df2.to_json(orient="records", force_ascii=False, indent=4)

        with open("dados_extraidosMotorola.json", "w", encoding="utf-8") as f:
            f.write(json_resultado2)

        with open("dados_extraidosMotorola.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        return {"MOROTOLA": data}
    
    def extrairDadosDisplaySamsungOriginalChina():

        file_path2 = "tabelas_template/DISPLAY_SAMSUNG-ORIGINAL_CHINA.xlsx"

        df2 = pd.read_excel(file_path2, header=None)

        df2 = df2.iloc[1:]

        df2.columns = ["Nome", "Preço"]

        df2["Preço"] = df2["Preço"].astype(str).replace("nan", "Indisponível")

        df2.reset_index(drop=True, inplace=True)

        json_resultado2 = df2.to_json(orient="records", force_ascii=False, indent=4)

        with open("json_resultados/dados_extraidos_DISPLAY_SAMSUNG-ORIGINAL_CHINA.json", "w", encoding="utf-8") as f:
            f.write(json_resultado2)
            print("Salvo na pasta")

        with open("json_resultados/dados_extraidos_DISPLAY_SAMSUNG-ORIGINAL_CHINA.json", "r", encoding="utf-8") as f:
            data = json.load(f)


        return {"DISPLAY_SAMSUNG-ORIGINAL_CHINA": data}

    def extrairDadosDisplayXiaomi():

        file_path2 = "tabelas_template/DISPLAY_XIAOMI.xlsx"

        df2 = pd.read_excel(file_path2, header=None)

        df2 = df2.iloc[1:]

        df2.columns = ["Nome", "Preço"]

        df2["Preço"] = df2["Preço"].astype(str).replace("nan", "Indisponível")

        df2.reset_index(drop=True, inplace=True)

        json_resultado2 = df2.to_json(orient="records", force_ascii=False, indent=4)

        with open("dados_extraidos_DISPLAY_XIAOMI.json", "w", encoding="utf-8") as f:
            f.write(json_resultado2)

        with open("dados_extraidos_DISPLAY_XIAOMI.json", "r", encoding="utf-8") as f:
            data = json.load(f)


        return {"DISPLAY_XIAOMI": data}
    
    def extrairDadosSamsungIncell():

        file_path2 = "tabelas_template/Samsung_Incell.xlsx"

        df2 = pd.read_excel(file_path2, header=None)

        df2 = df2.iloc[1:]

        df2.columns = ["Nome", "Preço"]

        df2["Preço"] = df2["Preço"].astype(str).replace("nan", "Indisponível")

        df2.reset_index(drop=True, inplace=True)

        json_resultado2 = df2.to_json(orient="records", force_ascii=False, indent=4)

        with open("dados_extraidos_Samsung_Incell.json", "w", encoding="utf-8") as f:
            f.write(json_resultado2)

        with open("dados_extraidos_Samsung_Incell.json", "r", encoding="utf-8") as f:
            data = json.load(f)


        return {"Samsung_Incell": data}
    
    def extrairDadosSamsungLcd():
        
        file_path2 = "tabelas_template/Samsung_lcd.xlsx"

        df2 = pd.read_excel(file_path2, header=None)

        df2 = df2.iloc[1:]

        df2.columns = ["Nome", "Preço"]

        df2["Preço"] = df2["Preço"].astype(str).replace("nan", "Indisponível")

        df2.reset_index(drop=True, inplace=True)

        json_resultado2 = df2.to_json(orient="records", force_ascii=False, indent=4)

        with open("dados_extraidos_Samsung_lcd.json", "w", encoding="utf-8") as f:
            f.write(json_resultado2)

        with open("dados_extraidos_Samsung_lcd.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        return {"Samsung_lcd": data}

    def extrairDadoszenfone():
        
        file_path2 = "tabelas_template/zenfone.xlsx"

        df2 = pd.read_excel(file_path2, header=None)

        df2 = df2.iloc[1:]

        df2.columns = ["Nome", "Preço"]

        df2["Preço"] = df2["Preço"].astype(str).replace("nan", "Indisponível")

        df2.reset_index(drop=True, inplace=True)

        json_resultado2 = df2.to_json(orient="records", force_ascii=False, indent=4)

        with open("dados_extraidos_zenfone.json", "w", encoding="utf-8") as f:
            f.write(json_resultado2)

        with open("dados_extraidos_zenfone.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        return {"zenfone": data}