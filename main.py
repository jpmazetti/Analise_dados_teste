import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt


dados = pd.read_csv('dataset.csv')

## Pergunta 1
filtro_office_supplies = dados[dados['Categoria'] == 'Office Supplies']

vendas_por_cidade = filtro_office_supplies.groupby('Cidade')['Valor_Venda'].sum()

cidade_maior_venda = vendas_por_cidade.idxmax()

maior_valor_venda = vendas_por_cidade.max()

print(f"A cidade com maior valor de venda para produtos da categoria Office Supplies é {cidade_maior_venda} com um total de vendas de US${maior_valor_venda:.2f}")

## Pergunta 2
vendas_por_data = dados.groupby('Data_Pedido')['Valor_Venda'].sum()

dados['Data_Pedido'] = pd.to_datetime(dados['Data_Pedido'], format='%d/%m/%Y')
dados['Ano_Pedido'] = dados['Data_Pedido'].dt.year
vendas_por_ano = dados.groupby('Ano_Pedido')['Valor_Venda'].sum()

plt.figure(figsize=(10, 6))
vendas_por_ano.plot(kind='bar', color='skyblue')
plt.title('Total de Vendas por Ano do Pedido')
plt.xlabel('Ano do Pedido')
plt.ylabel('Total de Vendas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

## Pergunta 3
vendas_por_estado = dados.groupby('Estado')['Valor_Venda'].sum()

plt.figure(figsize=(15, 6))
vendas_por_estado.plot(kind='bar', color='skyblue')
plt.title('Total de Vendas por Estado')
plt.xlabel('Estado')
plt.ylabel('Total de Vendas')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

## Pergunta 4
vendas_por_cidade = dados.groupby('Cidade')['Valor_Venda'].sum()

top_10_cidades = vendas_por_cidade.sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
top_10_cidades.plot(kind='bar', color='skyblue')
plt.title('Top 10 Cidades com Maior Total de Vendas')
plt.xlabel('Cidade')
plt.ylabel('Total de Vendas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

## Pergunta 5
vendas_por_segmento = dados.groupby('Segmento')['Valor_Venda'].sum()
segmento_maior_venda = vendas_por_segmento.idxmax()
vendas_por_segmento = vendas_por_segmento.sort_values(ascending=False)
explode = [0.1 if seg == segmento_maior_venda else 0 for seg in vendas_por_segmento.index]

plt.figure(figsize=(8, 8))
plt.pie(vendas_por_segmento, labels=vendas_por_segmento.index, autopct='%1.1f%%', startangle=140, shadow=True, explode=explode)
plt.title('Total de Vendas por Segmento')
plt.axis('equal')

sb.set_style("whitegrid")
plt.show()

## Pergunta 6 
dados['Data_Pedido'] = pd.to_datetime(dados['Data_Pedido'])

dados['Ano_Pedido'] = dados['Data_Pedido'].dt.year.astype(int)

vendas_por_segmento_ano = dados.groupby(['Segmento', 'Ano_Pedido'])['Valor_Venda'].sum()

print(vendas_por_segmento_ano)

## Pergunta 6 complemento
vendas_por_segmento_ano = vendas_por_segmento_ano.reset_index()
vendas_por_segmento_ano['Ano_Pedido'] = vendas_por_segmento_ano['Ano_Pedido'].astype(int)

plt.figure(figsize=(6, 6))

for segmento in vendas_por_segmento_ano['Segmento'].unique():
    dados_segmento = vendas_por_segmento_ano[vendas_por_segmento_ano['Segmento'] == segmento]
    plt.bar(dados_segmento['Ano_Pedido'], dados_segmento['Valor_Venda'], label=segmento)

plt.title('Total de Vendas por Segmento e Ano')
plt.xlabel('Ano do Pedido')
plt.ylabel('Total de Vendas')
plt.legend(title='Segmento')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

## Pergunta 7
vendas_15_porcento = dados[dados['Valor_Venda'] > 1000]

total_vendas_15_porcento = len(vendas_15_porcento)

print(f"O número de vendas que receberiam 15% de desconto é: {total_vendas_15_porcento}")

## Pergunta 7 complemento
vendas_nao_15_porcento = dados[dados['Valor_Venda'] <= 1000]

total_vendas_nao_15_porcento = len(vendas_nao_15_porcento)

labels = ['Sem Desconto (0%)', 'Com Desconto (15%)']
sizes = [total_vendas_nao_15_porcento, total_vendas_15_porcento]
colors = ['lightcoral', 'lightskyblue']

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Proporção de Vendas com e sem Desconto de 15%')
plt.axis('equal')

plt.show()

## Pergunta 8
media_valor_venda_antes_desconto = dados['Valor_Venda'].mean()

dados['Valor_Venda_Com_Desconto'] = dados['Valor_Venda'] * 0.85

media_valor_venda_apos_desconto = dados['Valor_Venda_Com_Desconto'].mean()

print(f"A média do valor de venda antes do desconto é: {media_valor_venda_antes_desconto:.2f}")
print(f"A média do valor de venda após o desconto de 15% é: {media_valor_venda_apos_desconto:.2f}")

## Pergunta 9
dados['Data_Pedido'] = pd.to_datetime(dados['Data_Pedido'])

dados['Ano_Pedido'] = dados['Data_Pedido'].dt.year
dados['Mês_Pedido'] = dados['Data_Pedido'].dt.month

media_vendas_por_segmento_ano_mes = dados.groupby(['Segmento', 'Ano_Pedido', 'Mês_Pedido'])['Valor_Venda'].mean()

media_vendas_por_segmento_ano_mes = media_vendas_por_segmento_ano_mes.reset_index()

plt.figure(figsize=(17, 6))

for segmento in media_vendas_por_segmento_ano_mes['Segmento'].unique():
    dados_segmento = media_vendas_por_segmento_ano_mes[media_vendas_por_segmento_ano_mes['Segmento'] == segmento]
    plt.plot(dados_segmento['Ano_Pedido'].astype(str) + '-' + dados_segmento['Mês_Pedido'].astype(str), dados_segmento['Valor_Venda'], label=segmento)

plt.title('Média de Vendas por Segmento, Ano e Mês')
plt.xlabel('Ano e Mês do Pedido')
plt.ylabel('Média de Vendas')
plt.legend(title='Segmento')
plt.xticks(rotation=60)
plt.tight_layout()
plt.show()

## Pergunta 10
top_12_subcategorias = dados.groupby('SubCategoria')['Valor_Venda'].sum().nlargest(12).index
dados_filtrados = dados[dados['SubCategoria'].isin(top_12_subcategorias)]

vendas_por_categoria_subcategoria = dados_filtrados.groupby(['Categoria', 'SubCategoria'])['Valor_Venda'].sum()

plt.figure(figsize=(12, 6))
vendas_por_categoria_subcategoria.unstack().plot(kind='bar', stacked=True)
plt.title('Total de Vendas por Categoria e Subcategoria (Top 12)')
plt.xlabel('Categoria')
plt.ylabel('Total de Vendas')
plt.xticks(rotation=45)
plt.legend(title='Subcategoria', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()