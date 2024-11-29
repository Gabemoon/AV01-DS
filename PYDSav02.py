equipes = []
medias = []

while True:
    lista_pontuacao = []
    count = 0
    iteration = 0
    equipe = []
    nome = input("Digite o nome da equipe: ")
    equipe.append(nome)

    while True:
        pontuacao = int(input("Digite a pontuação: (-1 para sair) "))
        if pontuacao == -1:
            break
        lista_pontuacao.append(pontuacao)
        count += pontuacao
        iteration += 1
    medias.append(count/iteration)
    equipe.append(lista_pontuacao)
    equipe_tupla = (equipe[0], equipe[1])
    equipes.append(equipe_tupla)
    continuar = int(input("Deseja continuar? 1 - Sim / 0 - Não: "))
    if continuar == 0:
        break

equipes_media = []
lista_medias = []
for equipe in range(len(equipes)):
    lista_media = []
    lista_media.append(equipes[equipe][0])
    lista_media.append(round(medias[equipe], 1))
    tupla_das_medias = (lista_media[0], lista_media[1])
    lista_medias.append(tupla_das_medias)

while True:
    menu = int(input("Digite a operação a ser realizada:\n"
                "1. Calcular a média das pontuações\n"
                "2. Ordernar as médias\n"
                "3. Criar uma lista de classificação\n"
                "4. Exibir classificação final\n"
                "0. Sair\n"
            ))
    if menu == 0:
        break
    elif menu == 1:
        print(lista_medias)
    elif menu == 2:
        equipes_medias = [(equipes[i][0], medias[i]) for i in range(len(equipes))]
        equipes_medias_sorted = sorted(equipes_medias, key=lambda x: x[1], reverse=True) 
        for time, media in equipes_medias_sorted:
            print(f"{media:.1f} - {time}")


