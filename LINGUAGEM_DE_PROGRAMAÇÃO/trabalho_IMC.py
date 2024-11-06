def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = calcular_imc(peso, altura)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso.")
elif 18.5 <= imc < 24.9:
    print("Peso normal.")
elif 25 <= imc < 29.9:
    print("Sobrepeso.")
else:
    print("Obesidade.")
