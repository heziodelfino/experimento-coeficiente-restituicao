# Importando as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Dados do experimento
H = np.array([1.064, 1.265, 0.983, 1.210, 1.024, 1.167])  # Alturas em metros
t_total_tenis = np.array([4.65, 5.07, 4.47, 4.95, 4.57, 4.87])  # Tempos totais em segundos para a bola de tênis
t_total_golf1 = np.array([6.55, 7.07, 6.47, 6.75, 6.57, 6.77])  # Tempos totais em segundos para a bola de golf 1
t_total_golf2 = np.array([7.55, 8.07, 7.47, 7.75, 7.57, 7.77])  # Tempos totais em segundos para a bola de golf 2
t_total_borracha = np.array([9.05, 10.47, 8.87, 9.25, 9.07, 9.37])  # Tempos totais em segundos para a bola de borracha

# Cálculo de X = sqrt(H)
X = np.sqrt(H)

# Ajuste linear para cada tipo de bola
slope_tenis, intercept_tenis, r_value_tenis, _, _ = linregress(X, t_total_tenis)
slope_golf1, intercept_golf1, r_value_golf1, _, _ = linregress(X, t_total_golf1)
slope_golf2, intercept_golf2, r_value_golf2, _, _ = linregress(X, t_total_golf2)
slope_borracha, intercept_borracha, r_value_borracha, _, _ = linregress(X, t_total_borracha)

# Calculando R^2
r_squared_tenis = r_value_tenis**2
r_squared_golf1 = r_value_golf1**2
r_squared_golf2 = r_value_golf2**2
r_squared_borracha = r_value_borracha**2

print(f'R^2 para Bola de Tênis: {r_squared_tenis:.4f}')
print(f'R^2 para Bola de Golf 1: {r_squared_golf1:.4f}')
print(f'R^2 para Bola de Golf 2: {r_squared_golf2:.4f}')
print(f'R^2 para Bola de Borracha: {r_squared_borracha:.4f}')