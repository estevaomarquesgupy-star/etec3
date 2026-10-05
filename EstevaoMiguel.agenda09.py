nomes = ["João", "Bruno", "Maria", "Carlos",]

nomes[1] = "Lucas"
print (nomes[0])
print (nomes[1])
print (nomes[2])
print (nomes[3])


for nome in nomes:
    print(nome)
nomes.append("Carlos")
print(nomes[4])
nomes.insert(2, "Pedro")
print(nomes[2])
nomes.remove("Carlos")

print ("pop")
nomes = ["Julio", "Paula", "Rafael"]
nome_removido = nomes.pop(1)
print(nomes)
print("Nome removido:", nome_removido)

matriz = [
    [7, 8, 6]
    [5, 9, 10]
    [1, 2, 0]
]

print (matriz[1][2])

#Inserir nota de aluno e cálcular a média

aluno = ["Mayara", "Bernardo", "Gabriel"]

notas = []
soma = 0
for i in range(4):
    nota = float(input("Digite a nota do aluno: "))
    notas.append(nota)
    soma += nota

media = soma / len(notas)
print("A média das notas do aluno é:", media)
if media >= 9.5:
    print("Aprovado com destaque")

elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

if media <= 5:
    print("Seu nível de inteligência está caindo tanto, que logo vai ser possível extrair petróleo com ele")
    

