nome = input("Qual é o seu nome? ")
altura = int(input("Digite sua altura em centímetros: "))
peso = int(input("Digite seu peso em kg: "))


altura = altura / 100
imc = peso / (altura * altura)

print()
print(nome, ", seu IMC é:", round(imc, 1))

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc >= 18.5 and imc < 25:
    print("Você está com peso normal.")
elif imc >= 25 and imc < 30:
    print("Você está com sobrepeso.")
else:
    print("Você está com obesidade.")	
