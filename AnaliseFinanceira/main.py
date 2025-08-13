import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#Gerando dados fitícios



np.random.seed(42)
datas = pd.date_range(start='2022-01-01', periods=500)
receitas = np.random.normal(5000, 2000, 500).cumsum()
despesas = np.random.normal(4000, 1500, 500).cumsum()

df = pd.DataFrame({
    'Data': datas,
    'Receitas': receitas,
    'Despesas': despesas
})

df['Lucro'] = df['Receitas'] - df['Despesas']
lucro_mensal = df.resample('M', on='Data').sum()


# Estilizando

sns.set_theme(style="whitegrid", font="Arial", font_scale=1.1)
colors = {
    'receitas': "#27ae60",  # verde
    'despesas': "#c0392b",  # vermelho
    'lucro': "#2980b9",     # azul
    'lucro_area': "#2ecc71",
    'prejuizo_area': "#e74c3c"
}

fig, axs = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle(" Painel Financeiro - Análise de Receitas, Despesas e Lucro", fontsize=18, fontweight='bold')

# Gráfico Receitas vs Despesas
axs[0, 0].plot(df['Data'], df['Receitas'], label='Receitas', linewidth=2, color=colors['receitas'])
axs[0, 0].plot(df['Data'], df['Despesas'], label='Despesas', linewidth=2, color=colors['despesas'])
axs[0, 0].fill_between(df['Data'], df['Receitas'], df['Despesas'],
                       where=(df['Receitas'] >= df['Despesas']),
                       interpolate=True, color=colors['lucro_area'], alpha=0.15, label='Lucro')
axs[0, 0].fill_between(df['Data'], df['Receitas'], df['Despesas'],
                       where=(df['Receitas'] < df['Despesas']),
                       interpolate=True, color=colors['prejuizo_area'], alpha=0.15, label='Prejuízo')
axs[0, 0].set_title('Receitas vs Despesas', fontsize=14, fontweight='bold')
axs[0, 0].legend()

#Gráfico Lucro Mensal
sns.barplot(x=lucro_mensal.index, y=lucro_mensal['Lucro'],
            palette=sns.color_palette("RdYlGn", n_colors=len(lucro_mensal)),
            ax=axs[0, 1])
axs[0, 1].axhline(0, color='black', linewidth=1)
axs[0, 1].set_title('Lucro Mensal', fontsize=14, fontweight='bold')
axs[0, 1].set_xticklabels(lucro_mensal.index.strftime('%b %Y'), rotation=45)

#Gráfico Proporção Média
media_receitas = df['Receitas'].mean()
media_despesas = df['Despesas'].mean()
axs[1, 0].pie([media_receitas, media_despesas],
              labels=['Receitas', 'Despesas'],
              autopct='%1.1f%%',
              colors=[colors['receitas'], colors['despesas']],
              textprops={'fontsize': 12})
axs[1, 0].set_title('Proporção Média Receitas x Despesas', fontsize=14, fontweight='bold')

#Gráfico Lucro Acuumulado
df['Lucro Acumulado'] = df['Lucro'].cumsum()
sns.lineplot(x='Data', y='Lucro Acumulado', data=df, linewidth=2, ax=axs[1, 1], color=colors['lucro'])
axs[1, 1].set_title('Lucro Acumulado', fontsize=14, fontweight='bold')
axs[1, 1].grid(True)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
