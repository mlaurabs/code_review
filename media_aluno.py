# Calculadora de média de notas de alunos
def mediaNotas(notas):
    soma = 0
    for i in range(0, len(notas)):
        soma = soma + notas[i]
    media = soma / len(notas)
    if media > 6:
        print("Aprovado")
    elif media == 6:
        print("Na média")
    else:
        print("Reprovado")
    return media

notas = [7, 8, 5, 6, 4]
media = mediaNotas(notas)
print("Media final é: " + str(media))
