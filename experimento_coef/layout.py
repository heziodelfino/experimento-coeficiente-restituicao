# Importando as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Dados fictícios do experimento
H = np.array([1.064, 1.265, 0.983, 1.210, 1.024, 1.167])  # Alturas em metros
t_total_tenis = np.array([4.65, 5.07, 4.47, 4.95, 4.57, 4.87])  # Tempos totais em segundos para a bola de tênis
t_total_golf1 = np.array([6.55, 7.07, 6.47, 6.75, 6.57, 6.77])  # Tempos totais em segundos para a bola de golf 1
t_total_golf2 = np.array([7.55, 8.07, 7.47, 7.75, 7.57, 7.77])  # Tempos totais em segundos para a bola de golf 2
t_total_borracha = np.array([9.05, 10.47, 8.87, 9.25, 9.07, 9.37])  # Tempos totais em segundos para a bola de borracha

# Cálculo de X = sqrt(H)
X = np.sqrt(H)

# Erros em X (propagação de incertezas para sqrt(H))
delta_X = np.array([7.448e-4, 5.0e-4, 3.227e-4, 2.419e-4, 3.152e-4, 2.456e-4])  # m^(1/2)

# Erros em t_total
delta_t = np.full_like(t_total_tenis, 0.01)  # 0,01 s para todos

# Ajuste linear para cada tipo de bola
slope_tenis, intercept_tenis, _, _, _ = linregress(X, t_total_tenis)
slope_golf1, intercept_golf1, _, _, _ = linregress(X, t_total_golf1)
slope_golf2, intercept_golf2, _, _, _ = linregress(X, t_total_golf2)
slope_borracha, intercept_borracha, _, _, _ = linregress(X, t_total_borracha)

# Gerando os valores ajustados para o gráfico
X_fit = np.linspace(min(X), max(X), 100)
t_fit_tenis = slope_tenis * X_fit + intercept_tenis
t_fit_golf1 = slope_golf1 * X_fit + intercept_golf1
t_fit_golf2 = slope_golf2 * X_fit + intercept_golf2
t_fit_borracha = slope_borracha * X_fit + intercept_borracha

# Criando a figura e os subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Figura A - Bola de Tênis
axs[0, 0].errorbar(X, t_total_tenis, xerr=delta_X, yerr=delta_t, fmt='o', color='blue', ecolor='gray',
                   elinewidth=1.5, capsize=3, label='Bola de Tênis', markerfacecolor='blue', markeredgecolor='black')
axs[0, 0].plot(X_fit, t_fit_tenis, color='blue', linestyle='--', label=f'Ajuste Linear Tênis: $t_{{total}} = {slope_tenis:.2f}X + {intercept_tenis:.2f}$')
axs[0, 0].set_title('Figura A - Bola de Tênis', fontsize=14)
axs[0, 0].legend(fontsize=10)
axs[0, 0].grid(alpha=0.3)

# Figura B - Bola de Golf 1
axs[0, 1].errorbar(X, t_total_golf1, xerr=delta_X, yerr=delta_t, fmt='s', color='green', ecolor='gray',
                   elinewidth=1.5, capsize=3, label='Bola de Golf 1', markerfacecolor='green', markeredgecolor='black')
axs[0, 1].plot(X_fit, t_fit_golf1, color='green', linestyle='--', label=f'Ajuste Linear Golf 1: $t_{{total}} = {slope_golf1:.2f}X + {intercept_golf1:.2f}$')
axs[0, 1].set_title('Figura B - Bola de Golf 1', fontsize=14)
axs[0, 1].legend(fontsize=10)
axs[0, 1].grid(alpha=0.3)

# Figura C - Bola de Golf 2
axs[1, 0].errorbar(X, t_total_golf2, xerr=delta_X, yerr=delta_t, fmt='d', color='orange', ecolor='gray',
                   elinewidth=1.5, capsize=3, label='Bola de Golf 2', markerfacecolor='orange', markeredgecolor='black')
axs[1, 0].plot(X_fit, t_fit_golf2, color='orange', linestyle='--', label=f'Ajuste Linear Golf 2: $t_{{total}} = {slope_golf2:.2f}X + {intercept_golf2:.2f}$')
axs[1, 0].set_title('Figura C - Bola de Golf 2', fontsize=14)
axs[1, 0].legend(fontsize=10)
axs[1, 0].grid(alpha=0.3)

# Figura D - Bola de Borracha
axs[1, 1].errorbar(X, t_total_borracha, xerr=delta_X, yerr=delta_t, fmt='^', color='red', ecolor='gray',
                   elinewidth=1.5, capsize=3, label='Bola de Borracha', markerfacecolor='red', markeredgecolor='black')
axs[1, 1].plot(X_fit, t_fit_borracha, color='red', linestyle='--', label=f'Ajuste Linear Borracha: $t_{{total}} = {slope_borracha:.2f}X + {intercept_borracha:.2f}$')
axs[1, 1].set_title('Figura D - Bola de Borracha', fontsize=14)
axs[1, 1].legend(fontsize=10)
axs[1, 1].grid(alpha=0.3)

# Ajustando os eixos e rótulos
for ax in axs.flat:
    ax.set(xlabel='$X = \sqrt{H}$ (m$^{-1/2}$)', ylabel='$t_{total}$ (s)')

# Removendo rótulos duplicados
for ax in axs.flat:
    ax.label_outer()

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()