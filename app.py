from random import randint

def rolar_dado():
    # Define os valores mínimo e máximo do dado
    valor_minimo = 1
    valor_maximo = 6
    # Gera e retorna um resultado aleatório entre valor_minimo e valor_maximo
    resultado = randint(valor_minimo, valor_maximo)
    return resultado

# Solicita ao usuário o número de jogadores até obter uma entrada válida (entre 2 e 4 jogadores)
while True:
    jogadores = input('Digite o número de jogadores (2-4):')
    if jogadores.isdigit():
        jogadores = int(jogadores)
        if 2 <= jogadores <= 4:
            break
        else:
            print('Por favor, digite um número de jogadores entre 2 e 4.')
    else:
        print('Número inválido, tente novamente.')

# Define a pontuação máxima do jogo
pontuacao_maxima = 50
# Inicializa as pontuações dos jogadores como uma lista de zeros
pontuacoes_jogadores = [0 for _ in range(jogadores)]

# Loop principal do jogo: continua até que algum jogador alcance a pontuação máxima
while max(pontuacoes_jogadores) < pontuacao_maxima:
    # Loop para cada jogador
    for indice_jogador in range(jogadores):
        print(f'\nJogador nº{indice_jogador + 1}, é a sua vez!\n')
        print(f'Sua pontuação total é: {pontuacoes_jogadores[indice_jogador]}\n')
        pontuacao_atual = 0
    
        # Loop para cada jogada do jogador
        while True:
            # Pergunta ao jogador se ele deseja rolar o dado
            deve_rolar = input('Rolar dado? (S)')
            if deve_rolar.upper() != 'S':
                break
            
            # Gera um valor aleatório e verifica se é 1 (caso em que o jogador perde a vez)
            valor = rolar_dado()
            if valor == 1:
                print('Você tirou o número 1! Passe a vez!')
                pontuacao_atual = 0
                break
            else:
                pontuacao_atual += valor
                print('Você tirou:', valor)
                
            print('Sua pontuação atual é:', pontuacao_atual)
                
        # Adiciona a pontuação do jogador à sua pontuação total
        pontuacoes_jogadores[indice_jogador] += pontuacao_atual
        print('Sua pontuação total é:', pontuacoes_jogadores[indice_jogador])

# Encontra o índice do vencedor (jogador com a pontuação máxima)
pontuacao_maxima = max(pontuacoes_jogadores)
indice_vencedor = pontuacoes_jogadores.index(pontuacao_maxima)
# Imprime o resultado final do jogo
print(f'O jogador nº{indice_vencedor + 1} foi o vencedor com uma pontuação total de: {pontuacao_maxima}')
