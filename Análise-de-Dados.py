import pandas as pd

#importando os arquivos
vendas_df = pd.read_csv(r'Contoso - Vendas - 2017.csv', sep=';')
produtos_df = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';')
lojas_df = pd.read_csv(r'Contoso - Lojas.csv', sep=';')
clientes_df = pd.read_csv(r'Contoso - Clientes.csv', sep=';')

#limpando apenas as colunas que queremos
clientes_df = clientes_df[['ID Cliente', 'Primeiro Nome', 'Sobrenome', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]

#mesclando e renomeando os dataframes
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente').rename(columns={'E-mail': 'E-mail do Cliente'})
#print(vendas_df)

#Qual cliente que comprou mais vezes?
frequencia_clientes = vendas_df[['Primeiro Nome', 'Sobrenome', 'E-mail do Cliente']].value_counts()
#print(frequencia_clientes)
#frequencia_clientes[:5].plot(figsize=(15, 5), yticks=range(1, 100, 5))
print('\nO cliente que comprou mais vezes foi:')
print(frequencia_clientes[:1])

#Qual a Loja que mais vendeu?
vendas_lojas = vendas_df.groupby('Nome da Loja').sum()
vendas_lojas = vendas_lojas[['Quantidade Vendida']]
#print(vendas_lojas)
vendas_lojas.plot()

#ordenando o dataframe
vendas_lojas = vendas_lojas.sort_values('Quantidade Vendida', ascending=False)
print(vendas_lojas)

#podemos plotar em um gráfico de barras
#vendas_lojas[:5].plot(figsize=(15, 5), kind='bar')

#Qual produto mais vendeu?

# Maneira 1
maior_valor = vendas_lojas['Quantidade Vendida'].max()
melhor_loja = vendas_lojas['Quantidade Vendida'].idxmax()
print(melhor_loja, maior_valor)

# Maneira 2
vendas_lojas[:1]