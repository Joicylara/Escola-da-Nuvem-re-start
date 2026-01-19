"""
2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
"""
 #multiplicacao = lambda a,b: a* b

def palindromo(texto:str) -> bool:
    textoLimpo = ""
    for char in texto.lower():
        if char.isalnum():
            textoLimpo = textoLimpo + char
    return textoLimpo == textoLimpo[::-1]

try:

    palavra = input("Digite a palavra: ")
    if palindromo(palavra):
        print("Sim")
    else:
        print("Não")

except ValueError:
    print("Valor inválido")