soma = 0
qtd_numero = 0
while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    soma += numero
    qtd_numero += 1
print(f"Quantidade: {qtd_numero}\nSoma: {soma}\nMédia: {soma/qtd_numero:.1f}")
