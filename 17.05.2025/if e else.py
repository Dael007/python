# n1 = float(input("Digite o primeiro numero: "))
# n2 = float(input("Digite o segundo numero: "))
# if n2 != 0:
#     divisao = n1 / n2
#     print(divisao)
# else:
#     print("Nao e possivel fazer a divisao por zero"



#atividade 1 sobre if

#pedindo a senha
senha = input("Digite sua senha")
 
#parte de verificacao
if senha == "senaiCabeludo":
    print("Asseso autorizado")
else:
    print("asseso negado! ")


#atividade 2 sobre if
n1 = float(input("Digite um numero"))
n2 = float(input("Digite um numero"))

operacao = input("digite a operaçao (+, -, *, /): ")


if operacao == "+":
    resultado = n1 + n2 
    print("resultado da soma", resultado)
elif operacao == "-":
  resultado = n1 - n2
  print("resultado da subtracao", resultado)
elif operacao == "*":
    resultado = n1 * n2
    print("Resultado da multiplicacao",resultado )
elif operacao == "/":
    
    if n2 != 0:
        resultado = n1 / n2
        print("Resultado da divisão:", resultado)
        print("Resultado da divisão:", resultado)
    else:
        print("Error na divisao pois 0 nao e permitido")
else:
    print("operacao invalida.") 

# and or not
    numero = float(input("DIgite um numero: "))

if numero >= 0 and numero <= 50 and numero % 2 == 0:
    if numero % 2 == 0:    
        print(f"O numero {numero} e par ")
    elif numero >= 0 and numero <= 50 and numero % 2 == 0:
        print(f"O numero {numero} e impar")
else:
    print(f"O numero {numero}  nao esta no intervalo. ")

        










