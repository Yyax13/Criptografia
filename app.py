def criptografar(texto, deslocamento):
    texto_cifrado = ""
    for char in texto:
        if char.isalpha():
            # Verifique se o caractere é uma letra do alfabeto
            maiuscula = char.isupper()
            char = char.lower()
            char_codificado = chr(
                ((ord(char) - ord('a') + deslocamento) % 26) + ord('a'))
            if maiuscula:
                char_codificado = char_codificado.upper()
            texto_cifrado += char_codificado
        else:
            texto_cifrado += char
    return texto_cifrado


def descriptografar(texto_cifrado, deslocamento):
    return criptografar(texto_cifrado, -deslocamento)


print("#######################################")
print("#                                     #")
print("#    CRIPTOGRAFIA - CIFRA DE CESAR    #")
print("#                                     #")
print("#######################################")

while True:
    print("[1] Criptografar")
    print("[2] Descriptografar")
    print("[3] Informações")
    print("[4] Sair")
    opcao = int(input("Escolha a opção desejada: "))

    if opcao == 1:
        deslocamento = int(input("Escolha um valor de deslocamento: "))
        texto = input("Digite o texto a ser criptografado: ")
        texto_cifrado = criptografar(texto, deslocamento)
        print("Texto criptografado:", texto_cifrado)
        break

    elif opcao == 2:
        deslocamento = int(input("Qual a chave de deslocamento: "))
        texto_cifrado = input("Digite o texto a ser descriptografado: ")
        texto_descriptografado = descriptografar(texto_cifrado, deslocamento)
        print("Texto descriptografado:", texto_descriptografado)
        break

    elif opcao == 3:
        print("Em criptografia, a Cifra de César, também conhecida como cifra de troca, código de César ou troca de César, é uma das mais simples e conhecidas técnicas de criptografia.")
        break

    elif opcao == 4:
        print("Saindo...")
        break

    else:
        print("Opção inválida. Escolha novamente.")
