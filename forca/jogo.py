import random

palavras = ['HTML', 'Código', 'CSS', 'Loop', 'Python', 'Cloud', 'Frontend', 'Backend', 'Classe', 'String']

palavra_sorteada = random.choice(palavras).lower()  # Converte para minúsculas para evitar erros com maiúsculas
palavra_escondida = '-' * len(palavra_sorteada)

letras_adivinhadas = []
max_tentativas = 10

while True:
    print(f'\nPalavra: {palavra_escondida}')  # Mostra a palavra com traços
    
    letra = input('Digite uma letra: ').lower()  # Entrada do usuário

    if letra in letras_adivinhadas:
        print('Você já digitou essa letra. Tente outra.')
        continue

    letras_adivinhadas.append(letra)

    if letra in palavra_sorteada:
        lista = list(palavra_escondida)  # Transforma a string em lista para modificar os caracteres
        for indice in range(len(palavra_sorteada)):
            if palavra_sorteada[indice] == letra:
                lista[indice] = letra  # Substitui o traço pela letra correta
        palavra_escondida = ''.join(lista)  # Junta os caracteres de volta em uma string
    else:
        max_tentativas -= 1
        print(f'Letra não encontrada. Você tem mais {max_tentativas} tentativas.')

    # Verifica se o jogador ganhou ou perdeu
    if palavra_escondida == palavra_sorteada:
        print(f'\nParabéns! Você acertou! A palavra era "{palavra_sorteada}".')
        break
    elif max_tentativas == 0:
        print(f'\nVocê perdeu! A palavra era "{palavra_sorteada}".')
        break