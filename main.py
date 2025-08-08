import pandas as pd
# importa uma planilha genérica - marco antonio - puxa pelo pandas 
# puxa as 5 do science, sigla, lat,long - puxa pelo pandas
# Escolha do nome - não pode estar no Science e as regras são: 
# UF + Primeira letra de cada se tiver 3 nomes e não está contido no Science, se não; UF + primeira letra da primeira palavra, 2 da segunda
generica = pd.read_excel("Macro Automação SOI", sheet_name = "a")
# Lista de caminhos
caminhos = [
    r"C:\Users\40417519\Telefonica\Engenharia de RF LESTE (RJ ES BA SE) - Science\Base_dados\Science_2G.xlsx",
    r"C:\Users\40417519\Telefonica\Engenharia de RF LESTE (RJ ES BA SE) - Science\Base_dados\Science_3G.xlsx",
    r"C:\Users\40417519\Telefonica\Engenharia de RF LESTE (RJ ES BA SE) - Science\Base_dados\Science_4G.xlsx"
    r"C:\Users\40417519\Telefonica\Engenharia de RF LESTE (RJ ES BA SE) - Science\Base_dados\Science_5G.xlsx"
    r"C:\Users\40417519\Telefonica\Engenharia de RF LESTE (RJ ES BA SE) - Science\Base_dados\Science_IoT.xlsx"
]

# Lê e junta todos
df_total = pd.concat([
    pd.read_excel(caminho, usecols=["SIG_SITE", "SIG_ERB", "NUM_LATITUDE_DECIMAL","NUM_LONGITUDE_DECIMAL",])
    for caminho in caminhos
], ignore_index=True)
