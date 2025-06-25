peso = float(input("Qual o seu peso? "));
altura = float(input("Qual a sua altura?"));
imc = (peso/(altura*altura));
print(imc);
print(f"Seu IMC é: {imc:.2f}")

if (imc < 18.5):
    print("Magreza")
elif(18.5 <= imc <= 24.9 ):
    print ("Normal")