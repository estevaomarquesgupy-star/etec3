nome = input("Digite o seu nome")
cidade = input("Digite a sua cidade")

tarefas = []
qtd = int(input("Digite a quantidade de tarefas que deseja adicionar: "))

for i in range(qtd):
    tarefa = input("Digite a tarefa {i+1}: ")
    tarefas.append(tarefa)

    print("Tarefas Cadastradas")
    for t in tarefas:
        print("-",t)

        if len(tarefas) == 0:
            print("Nenhuma tarefa foi cadastrada")
        elif len(tarefas) <= 3:
            print("{nome} de {cidade}: rotina leve hoje")
        else:
            print("{nome} de {cidade}: rotina cheia! Organize seus estudos")


            

    