Painel Financeiro - Análise de Receitas e Despesas

Este projeto é um painel de visualização de dados que oferece uma visão geral das finanças de uma empresa, com foco na análise de receitas, despesas e lucro ao longo do tempo. O painel é gerado a partir de dados fictícios, mas a estrutura e as análises podem ser aplicadas a qualquer conjunto de dados financeiros.

O objetivo é demonstrar habilidades em manipulação de dados com **Pandas** e criação de visualizações com **Matplotlib** e **Seaborn** para extrair insights financeiros.



💻 Tecnologias Utilizadas

 **Python**: Linguagem principal para a análise de dados.
 **Pandas**: Para manipulação e preparação dos dados.
 **Matplotlib**: Para a criação de gráficos e sub-gráficos.
 **Seaborn**: Para aprimorar a estética e o estilo dos gráficos.

<img width="1600" height="787" alt="Figure_1" src="https://github.com/user-attachments/assets/f38c6ced-a66e-4db8-9dc2-0927051f07b5" />



#📊 Análises e Visualizações

O painel é composto por quatro gráficos principais que apresentam diferentes perspectivas sobre os dados:

**Receitas vs. Despesas**: Gráfico de linha que mostra a evolução diária das receitas e despesas, destacando visualmente os períodos de lucro e prejuízo.
**Lucro Mensal**: Gráfico de barras que compara o lucro total de cada mês, facilitando a identificação de picos e quedas no desempenho.
**Proporção Média**: Gráfico de pizza que exibe a participação média das receitas e despesas sobre o valor total, dando uma visão rápida da proporção entre os dois.
**Lucro Acumulado**: Gráfico de linha que mostra a tendência do lucro total acumulado, essencial para entender a saúde financeira a longo prazo.

1. Lucro é a diferença entre Receitas e Despesas.
Essa é a regra de negócio mais fundamental. A fórmula Lucro = Receitas - Despesas é a base do seu projeto. Seu código a aplica de duas maneiras:

No gráfico de linha de Receitas vs Despesas, a área colorida entre as linhas (verde para lucro, vermelho para prejuízo) mostra visualmente se a empresa está no azul ou no vermelho em um período específico.

No gráfico de barras de Lucro Mensal, você aplica essa mesma regra para resumir o resultado financeiro de cada mês, facilitando a identificação de períodos de bom ou mau desempenho.

2. A tendência é tão importante quanto o valor atual.
Um número isolado, como o lucro de hoje, não diz muito. O que importa é a tendência.

O gráfico de linha de Lucro Acumulado reflete essa regra de negócio. Ele mostra o crescimento constante do lucro ao longo do tempo. Se essa linha estivesse caindo, a regra de negócio diria que a empresa tem um problema de longo prazo.

3. Proporção é essencial para o controle de custos.
Entender a proporção entre o que entra (receitas) e o que sai (despesas) é crucial para gerenciar a empresa.

O gráfico de pizza de Proporção Média te dá uma visão rápida. A regra de negócio aqui é: "Se as despesas representam uma porcentagem muito alta das receitas, a margem de lucro é pequena e a empresa pode estar em risco." No seu painel, as receitas são maiores, o que é um bom sinal.

link codigo: https://github.com/MateusHeloi/python/blob/main/AnaliseFinanceira/main.py
