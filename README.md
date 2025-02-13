# Experimento: Coeficiente de Restituição

Este experimento tem como objetivo determinar o coeficiente de restituição de diferentes materiais, analisando a energia perdida em colisões. Para isso, uma bolinha é solta de várias alturas e o tempo total de queda é registrado até que ela pare de quicar.

## Estrutura do Repositório:

- `experimento_coeficiente_de_rest.py` → Código principal que processa os dados e gera gráficos.
- `layout.py` → Versão do experimento organizada com múltiplos gráficos.
- `R_squared.py` → Cálculo do coeficiente de determinação \( R^2 \) para análise da regressão.
- `tabela_coef.py` → Gera uma tabela com os coeficientes encontrados.

## Como Executar os Scripts:

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/experimento-coeficiente-restituicao.git
   cd experimento-coeficiente-restituicao

2. Instale as dependências (se for necessário):
   ```sh
   pip install numpy matplotlib scipy pandas

3. Execute os scripts conforme necessário:
   ```sh
   python experimento_coeficiente_de_rest.py
   python layout.py
   python R_squared.py
   python tabela_coef.py

## Notas:

O experimento utiliza ajuste linear para estimar a relação entre a altura inicial da bolinha e o tempo total de quique.

Os coeficientes R^2 são calculados para validar a precisão do ajuste.
