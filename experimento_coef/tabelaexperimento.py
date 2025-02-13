import matplotlib.pyplot as plt
import numpy as np

# Dados da tabela
data = [
    [1.132, 0.001582, 1.063955, 0.000743],
    [1.601, 0.000120, 1.265306, 0.000474],
    [0.966, 0.000635, 0.982853, 0.000323],
    [1.463, 0.000585, 1.209545, 0.000242],
    [1.038, 0.000646, 1.018823, 0.000317],
    [1.361, 0.000573, 1.166619, 0.000246],
]

# Cabeçalhos
columns = ["$\overline{H_{0}}$ (m)", "$\sigma_{H_{0}}$ (m)", "$\sqrt{H_{0}}$ ($\mathrm{m^{1/2}}$) ", "$\delta_{\\sqrt{H_{0}}}$ ($\mathrm{m^{1/2}}$)"]

# Criação da figura
fig, ax = plt.subplots(figsize=(8, 5))
ax.axis('tight')
ax.axis('off')

# Adiciona a tabela à figura
table = ax.table(cellText=data, colLabels=columns, loc='center', cellLoc='center')

# Estiliza a tabela
table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width(col=list(range(len(columns))))

# Define cor de fundo para os cabeçalhos
header_color = "#D3D3D3"  
for col_idx in range(len(columns)):
    cell = table[(0, col_idx)]  
    cell.set_facecolor(header_color)

plt.show()