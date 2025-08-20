# Nossa lista de aluno vazia no início
alunos = []
linha = 60


def menu():
    """
    Exibe o menu de opções para o usuário.
    """
    print("-" * linha)
    print("        CADASTRO DE ALUNOS       ")
    print("-" * linha)
    print("1.Cadastrar novo aluno")
    print("2.Listar todos os alunos")
    print("3Atualizar dados de um aluno")
    print("4.Excluir aluno")
    print("5.Calcular média geral da turma")
    print("6Sair")
    print("-" * linha)


def adicionar_aluno():

    nome = input("Digite o nome do aluno: ")
    try:
        nota = float(input("Digite a nota do aluno: "))
        novo_aluno = {
            "nome": nome,
            "nota": nota
        }
        alunos.append(novo_aluno)
        print(f"Aluno {novo_aluno['nome']} cadastrado com sucesso!")
    except ValueError:
        print("erro")


def listar_alunos():

    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(f"Nome: {aluno['nome']}, Nota: {aluno['nota']}")


def atualizar_aluno():

    nome_aluno = input("Digitaro nome do aluno que deseja atualizar: ")

    encontrado = False
    for aluno in alunos:
        if aluno['nome'].lower().split() == nome_aluno.lower().split():
            try:
                nova_nota = float(input(f"Digite a nova nota para {aluno['nome']}: "))
                aluno['nota'] = nova_nota
                print(f"Dados do aluno {aluno['nome']} atualizado com sucess")
                encontrado = True
                break
            except ValueError:
                print("erro")
                return

    if not encontrado:
        print(f"Aluno '{nome_aluno}' não encontrado.")


def excluir_aluno():
    nome_aluno = input("Digite o nome do aluno que deseja excluir: ")
    for indice, aluno in enumerate(alunos):
        if aluno['nome'].lower() == nome_aluno.lower():

            del alunos[indice]
            aluno_encontrado = True
            print(f"Aluno '{nome_aluno}' excluído .")
            break

    if not aluno_encontrado:
        print(f"Aluno '{nome_aluno}' não encontrado.")


def calcular_media_turma():

    if not alunos:
        print("sem aluno para calcular a média.")
        return

    soma_das_notas = 0
    alunos_aprovados = 0
    alunos_reprovados = 0

    for aluno in alunos:
        soma_das_notas += aluno['nota']
        if aluno['nota'] >= 7:
            alunos_aprovados += 1
            print(f"{aluno['nome']} - Aprovado (Nota: {aluno['nota']})")
        else:
            alunos_reprovados += 1
            print(f"{aluno['nome']} - Reprovado (Nota: {aluno['nota']})")

    media_geral = soma_das_notas / len(alunos)
    print("---------------------------------")
    print(f"Média geral da turma: {media_geral:.2f}")
    print(f"Total de alunos aprovados: {alunos_aprovados}")
    print(f"Total de alunos reprovados: {alunos_reprovados}")



if __name__ == "__main__":
    while True:
        menu()
        opcao = input("Digite a opcao desejada: ")

        match opcao:
            case '1':
                adicionar_aluno()
            case '2':
                listar_alunos()
            case '3':
                atualizar_aluno()
            case '4':
                excluir_aluno()
            case '5':
                calcular_media_turma()
            case '6':
                print("aindo do programaAte mais")
                break
            case _:
                print("erro .")