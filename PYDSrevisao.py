lista_produtos = []
lista_valores = []
count = 0
while True:
    lista_produtos.append(input("Digite o nome do produto: "))
    valor = int(input("Digite o valor do produto: "))
    if valor >= 1000:
        count += 1
    lista_valores.append(valor)
    continuar = int(input("Continuar? 1 - Sim | 0 - Não "))
    if continuar == 0:
        break
print(f"Total gasto na compra: R${round(sum(lista_valores), 2)}")
print(f"Total de itens acima de R$1000,00 - {count}")
menor = 9999999
for i in range(len(lista_valores)):
    if menor > lista_valores[i]:
        menor = lista_valores[i]
        itemmenor = lista_produtos[i]
        print(itemmenor)
print(f"O item com o menor custo foi: {itemmenor} - R${menor}")