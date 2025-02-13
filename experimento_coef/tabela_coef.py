import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# Dados da tabela
data = {
    ' ': ['Tênis', 'Borracha', 'Golf 1', 'Golf 2'],
    'RL M(s*m^-1/2)': [4.45, 8.87, 3.84, 3.84],
    'R^2': [0.99, 0.66, 0.87, 0.87],
    'CDR médio': [0.82, 0.90, 0.79, 0.79]
}

# Criando o DataFrame
df = pd.DataFrame(data)

# Criando a figura e o eixo
fig, ax = plt.subplots()

# Ocultando o eixo
ax.axis('off')

# Criando a tabela
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

# Ajustando o layout
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.2, 1.2)

# Estilizando os cabeçalhos e células
for key, cell in table.get_celld().items():
    if key[0] == 0 or key[1] == 0:
        cell.set_facecolor('#d3d3d3')  
        cell.set_text_props(weight='bold', fontproperties=FontProperties(family='serif', size=12))

# Salvando a tabela como uma imagem .svg
plt.savefig('tabela.svg', format='svg')

# Exibindo a tabela
plt.show()