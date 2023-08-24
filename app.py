print("#######################################")
print("#                                     #")
print("#    CRIPTOGRAFIA - CIFRA DE CESAR    #")
print("#                                     #")
print("#######################################")

print("[1] Criptografar")
print("[2] Descriptografar")
print("[3] Informações")
print("[4] Sair")
opcao = input("Escolha a opção desejada: ")


if opcao == 1:
    deslocamento = input("Escolha um valor de deslocamento: ")
    print("Você escolheu: " + deslocamento)

elif opcao == 2:
    descrip = input("Qual a chave de deslocamento: ")
    print("Você escolheu: " + descrip)

elif opcao == 3:
    print("Em criptografia, a Cifra de César, também conhecida como cifra de troca, código de César ou troca de César, é uma das mais simples e conhecidas técnicas de criptografia.")

elif opcao == 4:
    exit()
