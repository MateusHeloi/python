import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns


# Gerando dados aleatórios para simular receitas, despesas e outras colunas
np.random.seed(42)  # Definindo a semente para reprodução dos mesmos resultados

# Gerando datas fictícias
datas = pd.date_range(start='1/1/2022', periods=500, freq='ME')

# Gerando valores aleatórios para as colunas
receitas = np.random.normal(loc=5000, scale=1500, size=500).round(2)
despesas = np.random.normal(loc=3000, scale=1000, size=500).round(2)
previsto = np.random.normal(loc=4000, scale=1000, size=500).round(2)
real = np.random.normal(loc=3500, scale=1200, size=500).round(2)

# Criando um DataFrame com os dados gerados aleatoriamente
dados = {
    'Data': datas,
    'Receitas': receitas,
    'Despesas': despesas,
    'Previsto': previsto,
    'Real': real
}

df = pd.DataFrame(dados)

# Salvando os dados em um arquivo Excel
df.to_excel('dados_financeiros.xlsx', index=False)

# Visualizar as primeiras linhas do DataFrame
print(df.head())

# Obter informações sobre o DataFrame
print(df.info())

# Realizar estatísticas descritivas básicas
print(df.describe())
# Gerar dados fictícios para o exemplo
data = {
    'Data': pd.date_range(start='1/1/2022', periods=500),
    'Receitas': np.random.normal(5000, 2000, 500).cumsum(),
    'Despesas': np.random.normal(4000, 1500, 500).cumsum()
}
df_generated = pd.DataFrame(data)

# Configuração do estilo do gráfico
plt.style.use('seaborn-v0_8-darkgrid')


# Plotagem do gráfico de linha para Receitas e Despesas ao longo do tempo
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(df_generated['Data'], df_generated['Receitas'], label='Receitas', linewidth=2)
ax.plot(df_generated['Data'], df_generated['Despesas'], label='Despesas', linewidth=2)

# Adicionando título e rótulos dos eixos
plt.title('Análise de Receitas e Despesas ao Longo do Tempo', fontsize=16)
plt.xlabel('Data', fontsize=12)
plt.ylabel('Valor (R$)', fontsize=12)

# Adicionar formatação para os valores do eixo y em reais
formatter = ticker.StrMethodFormatter('R$ {x:,.0f}')
ax.yaxis.set_major_formatter(formatter)

# Adicionando legenda, grid e personalização
plt.legend(fontsize=12)
plt.grid(True)
plt.tight_layout()

# Mostrar o gráfico
plt.show()
df_generated['Lucro'] = df_generated['Receitas'] - df_generated['Despesas']
ax.plot(df_generated['Data'], df_generated['Lucro'], label='Lucro', linewidth=2, linestyle='--', color='green')
max_receita = df_generated['Receitas'].max()
max_receita_data = df_generated.loc[df_generated['Receitas'].idxmax(), 'Data']
ax.annotate(f'Máx Receita: R$ {max_receita:,.0f}',
            xy=(max_receita_data, max_receita),
            xytext=(max_receita_data, max_receita+50000),
            arrowprops=dict(facecolor='black', arrowstyle='->'))

ax.fill_between(df_generated['Data'], df_generated['Receitas'], df_generated['Despesas'],
                where=(df_generated['Receitas'] >= df_generated['Despesas']),
                interpolate=True, color='green', alpha=0.1, label='Lucro')

ax.fill_between(df_generated['Data'], df_generated['Receitas'], df_generated['Despesas'],
                where=(df_generated['Receitas'] < df_generated['Despesas']),
                interpolate=True, color='red', alpha=0.1, label='Prejuízo')
ax.xaxis.set_major_locator(ticker.MaxNLocator(10))  # menos marcas no eixo
fig.autofmt_xdate()  # rotaciona datas automaticamente


plt.savefig('analise_financeira.png', dpi=300)
media_receitas = df_generated['Receitas'].mean()
media_despesas = df_generated['Despesas'].mean()

plt.figure(figsize=(6, 6))
plt.pie([media_receitas, media_despesas],
        labels=['Receitas', 'Despesas'],
        autopct='%1.1f%%',
        colors=['#2ecc71', '#e74c3c'])
plt.title('Proporção Média Receitas x Despesas', fontsize=16)
plt.show()
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Receitas', y='Despesas', data=df_generated, alpha=0.6)
plt.title('Relação entre Receitas e Despesas', fontsize=16)
plt.xlabel('Receitas (R$)')
plt.ylabel('Despesas (R$)')
plt.tight_layout()
plt.show()
df_generated['Lucro Acumulado'] = df_generated['Lucro'].cumsum()

plt.figure(figsize=(12, 6))
sns.lineplot(x='Data', y='Lucro Acumulado', data=df_generated, linewidth=2)
plt.title('Lucro Acumulado ao Longo do Tempo', fontsize=16)
plt.ylabel('Valor (R$)', fontsize=12)
plt.xlabel('Data', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()

