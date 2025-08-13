import csv
colunas = ["id", "nome", "idade"]

    # Passo 2: Criando dados no formato dicionário
    dados = [
        {"id": 1, "nome": "Mateus", "idade": 20},
        {"id": 2, "nome": "Ana", "idade": 25}
    ]
    escritor = csv.DictWriter(arquivo.csv, fieldnames=colunas)

    escritor.writeheader()  # Escreve a linha de cabeçalho
    escritor.writerows(dados)  # Escreve todas as linhas
with open('dados.csv', newline='', encoding='utf-8') as file:


    ler_csv = csv.DictReader(file)
    escrever_csv = csv.writer(file)
    for linha in ler_csv:
        print(linha)
