import pandas as pd
import json

class ExtrairDados:

    
    def extrairDadosTabelas():

        # Lista de arquivos Excel
        file_paths = ["tabelas_template/Samsung_Incell.xlsx","tabelas_template/Samsung_lcd.xlsx",
                     
                    "tabelas_template/DISPLAY_SAMSUNG-ORIGINAL_CHINA.xlsx",
                    "tabelas_template/DISPLAY_XIAOMI.xlsx", "tabelas_template/DISPLAY_MOTOROLA.xlsx"
                    ,"tabelas_template/DISPLAY_LG.xlsx", "tabelas_template/DISPLAY_Iphone.xlsx",
                    
                    
                    "tabelas_template/zenfone.xlsx",]

        # Lista para armazenar os DataFrames
        lista_df = []

        # Percorrer os arquivos e processar os dados
        for file_path in file_paths:
            # Carregar o arquivo sem cabeçalhos
            df = pd.read_excel(file_path, header=None)

            # Remover a primeira linha (caso seja um título geral)
            df = df.iloc[1:]

            # Renomear colunas
            df.columns = ["Nome", "Preço"]

            # Preencher valores vazios na coluna "Preço" com "Indisponível"
            df["Preço"] = df["Preço"].astype(str).replace("nan", "Indisponível")

            # Adicionar uma coluna "Fonte" para indicar de qual arquivo veio
            df["Fonte"] = file_path.split("/")[-1]  # Pega apenas o nome do arquivo

            # Resetar os índices
            df.reset_index(drop=True, inplace=True)

            # Adicionar o DataFrame à lista
            lista_df.append(df)

        # Concatenar todos os DataFrames em um único
        df_final = pd.concat(lista_df, ignore_index=True)
            
        # Converter para JSON
        json_resultado = df_final.to_json(orient="records", force_ascii=False, indent=4)

        # Salvar em um arquivo JSON
        with open("json_resultados/dados_combinados.json", "w", encoding="utf-8") as f:
            f.write(json_resultado)

        # Carregar os dados JSON novamente (opcional)
        with open("json_resultados/dados_combinados.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        # Retornar os dados combinados
        print(data)