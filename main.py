import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo CSV
df = pd.read_csv('gasolina.csv')

# Imprimir a primeira linha do DataFrame
print(df.head(1))

# Plotar o gráfico de linha
plt.plot(df['dia'], df['venda'], marker='o', linestyle='-', color='b')

# Adicionar rótulos e título
plt.xlabel('Dia')
plt.ylabel('Preço de Venda')
plt.title('Preço Médio de Venda da Gasolina (Julho de 2021)')

# Salvar o gráfico como uma imagem PNG
plt.savefig('gasolina.png')

# Exibir o gráfico
plt.show()
