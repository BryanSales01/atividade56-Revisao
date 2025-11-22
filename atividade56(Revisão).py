# Receba uma frase e mostre:
# Quantas letras possui (ignorando espaços).
# Quantas vezes a letra “a” aparece (maiúscula ou minúscula).
# Em que posição ocorre a primeira e a última letra “a”.



frase = input("Digite uma frase: ")
semespaco = frase.replace(" ", "")
quantidadea = frase.count("a")
quantidadeletras = len(frase)
posição = frase.find("a")
posicao_a = frase.rfind("a")


print(f"{frase}")
print(f"Quantidade de letras:{quantidadeletras}")
print(f"Quantidade de letras (a):{quantidadea}")
print(f"Primeira letra (a):{posição+1}")
print(f"Última letra (a):{posicao_a+1}")
