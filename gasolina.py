import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
df = pd.read_csv('gasolina.csv')

# Criar o gráfico de linha
plt.plot(df['dia'], df['venda'], marker='o', linestyle='-', color='b')
plt.title('Preço Médio de Venda da Gasolina - Julho 2021')
plt.xlabel('Dia')
plt.ylabel('Preço de Venda (R$)')
plt.grid(True)

# Salvar o gráfico como gasolina.png
plt.savefig('gasolina.png')

# Exibir o gráfico (opcional)
plt.show()
