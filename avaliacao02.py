velocidade = int(input("Velocidade: "))
if velocidade > 80:
    multa = (velocidade - 80)*20
    print(f"Você foi multado. Valor da multa: R${multa:.2f}")
else:
    print("Não foi multado.")