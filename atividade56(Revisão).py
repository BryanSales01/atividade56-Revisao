# Receba uma frase e mostre:
# Quantas letras possui (ignorando espaços).
# Quantas vezes a letra “a” aparece (maiúscula ou minúscula).
# Em que posição ocorre a primeira e a última letra “a”.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 3

if media >= 7:
    print("Aprovado")
elif media == 6:
    print("Recuperação")
else:
    print("Reprovado")