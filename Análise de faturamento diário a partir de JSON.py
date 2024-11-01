import json

# Carrega o arquivo JSON com os dados de faturamento diário
with open("faturamento.json") as file:
    faturamento_data = json.load(file)

# Extrai apenas os valores de faturamento para análise
faturamento = [entry["valor"] for entry in faturamento_data if entry["valor"] > 0]

# Calcula o menor, maior e média mensal
menor_valor = min(faturamento)
maior_valor = max(faturamento)
media_mensal = sum(faturamento) / len(faturamento)

# Calcula o número de dias com faturamento acima da média mensal
dias_acima_media = sum(1 for valor in faturamento if valor > media_mensal)

# Exibe os resultados
print("Menor valor de faturamento:", menor_valor)
print("Maior valor de faturamento:", maior_valor)
print("Dias com faturamento acima da média:", dias_acima_media)
