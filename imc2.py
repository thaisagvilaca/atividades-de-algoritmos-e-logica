peso = float(input('Digite o seu peso (em kg): '))
altura = float(input('Digite a sua altura (em metros): '))
imc = peso / (altura**2)

print(f'O seu imc é: {imc:.2f}')

if imc < 16:
    print('Magreza Grau III')
elif imc >= 16 and imc <= 16.9:
    print('Magreza Grau II')
elif imc >= 17 and imc <= 18.4:
    print('Magreza Grau I')
elif imc >= 18.5 and imc <= 24.9:
    print('Eutrofia')
elif imc >= 25 and imc <= 29.9:
    print('Pré-obesidade')
elif imc >= 30 and imc <= 34.9:
    print('Obesidade Moderada Grau I')
elif imc >= 35 and imc <= 39.9:
    print('Obesidade Severa Grau II')
else:
    imc >= 40
    print('Obesidade Muito Severa Grau III')
