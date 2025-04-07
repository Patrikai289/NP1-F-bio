def calcular_media():
    numeros = []
    while True:
        numero = input("Digite um número ou 'fim' para terminar: ")
        if numero.lower() == 'fim':
            break
        numeros.append(float(numero))
    
    if numeros:
        media = sum(numeros) / len(numeros)
        print(f"A média é: {media}\n")

def calcular_mediana():
    numeros = []
    while True:
        numero = input("Digite um número ou 'fim' para terminar: ")
        if numero.lower() == 'fim':
            break
        numeros.append(float(numero))
    
    if numeros:
        numeros.sort()
        n = len(numeros)
        mediana = (numeros[n // 2] if n % 2 == 1 
                   else (numeros[n // 2 - 1] + numeros[n // 2]) / 2)
        print(f"A mediana é: {mediana}\n")
        
while True:
    print("Menu:")
    print("1 - Calcular Média")
    print("2 - Calcular Mediana")
    print("3 - Sair")
    
    opcao = input("Qual a sua opção? ")
    
    if opcao == "1":
        calcular_media()
    elif opcao == "2":
        calcular_mediana()
    elif opcao == "3":
        print("Saindo.")
        break