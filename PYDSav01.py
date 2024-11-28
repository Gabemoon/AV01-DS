disciplinas = ["Matématica", "Ciências", "História"]
alunos = [] 

while True:
    continuar = int(input("Continuar? 1/0 "))
    if continuar == 0:
        break

    aluno = {} 
    aluno['nome'] = input("Cadastre o nome do aluno: ")
    aluno['idade'] = int(input("Cadastre a idade do aluno: "))

    notas_lista = []
    for i in range(len(disciplinas)):
        notas_lista.append(int(input(f"Digite a nota de {disciplinas[i]} do aluno: ")))
    aluno['notas'] = notas_lista 

    alunos.append(aluno)

while True:
    inp = int(input(
        "Escolha a opção que deseja visualizar.\n"
        "1. Visualizar todos os alunos e todas as notas\n"
        "2. Visualizar todos os alunos e todas as médias\n"
        "3. Visualizar as notas de um aluno\n"
        "0. Sair\n"
    ))
    if inp == 0:
        break
    elif inp == 1:
        for aluno in alunos:
            print(f"Aluno: {aluno['nome']}, Idade: {aluno['idade']}, Notas: {aluno['notas']}")
    elif inp == 2:
        for aluno in alunos:
            media = sum(aluno['notas']) / len(aluno['notas']) 
            print(f"Aluno: {aluno['nome']}, Idade: {aluno['idade']}, Média: {media:.2f}")
    elif inp == 3:
        nome = input("Digite o nome do aluno que deseja visualizar: ")
        found = False
        for aluno in alunos:
            if aluno['nome'].lower() == nome.lower():
                print(f"Aluno: {aluno['nome']}, Notas: {aluno['notas']}")
                found = True
                break
        if not found:
            print("Aluno não encontrado.")
    else:
        print("Opção inválida. Tente novamente.")