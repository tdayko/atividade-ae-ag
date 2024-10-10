import random

# Parâmetros do problema
TAMANHO_POPULACAO = 10  # Número de indivíduos em cada geração
TAMANHO_GENOMA = 8  # Número de itens, cada genoma tem 8 bits (1 ou 0 para cada item)
TAXA_MUTACAO = 0.1  # Probabilidade de mutação de cada gene
GERACOES = 20  # Quantidade de gerações a serem simuladas
CAPACIDADE_MIN = 10  # Capacidade mínima da mochila (aleatória)
CAPACIDADE_MAX = 20  # Capacidade máxima da mochila (aleatória)

# Definição dos itens: cada tupla representa (peso, valor)
itens = [(2, 3),  # peso 2, valor 3
         (3, 4),  # peso 3, valor 4
         (4, 5),  # peso 4, valor 5
         (5, 8),  # peso 5, valor 8
         (9, 10),  # peso 9, valor 10
         (4, 7),  # peso 4, valor 7
         (2, 6),  # peso 2, valor 6
         (1, 2)]  # peso 1, valor 2

# Função que calcula a aptidão (fitness) de um genoma (indivíduo)
def calcular_aptidao(genoma, capacidade_mochila):
    peso_total = 0  # Acumula o peso total dos itens selecionados
    valor_total = 0  # Acumula o valor total dos itens selecionados
    
    # Itera sobre cada item para verificar se ele está na mochila
    for i in range(TAMANHO_GENOMA):
        if genoma[i] == 1:  # Se o bit for 1, o item está na mochila
            peso_total += itens[i][0]  # Soma o peso do item ao peso total
            valor_total += itens[i][1]  # Soma o valor do item ao valor total
    
    # Penaliza soluções que excedem a capacidade da mochila
    if peso_total > capacidade_mochila:
        return 0  # Soluções inválidas têm aptidão 0
    
    return valor_total  # Retorna o valor total como aptidão se o peso for válido

# Função para gerar a população inicial de forma aleatória
def gerar_populacao_inicial():
    # Cria uma população de 10 indivíduos, cada um com um genoma aleatório de 8 bits
    return [[random.randint(0, 1) for _ in range(TAMANHO_GENOMA)] for _ in range(TAMANHO_POPULACAO)]

# Função de seleção por torneio: escolhe dois indivíduos e retorna o mais apto
def selecao_torneio(populacao, aptidoes):
    melhor = random.randint(0, TAMANHO_POPULACAO - 1)  # Escolhe um indivíduo aleatoriamente
    for _ in range(2):  # Compara com outro indivíduo aleatório
        rival = random.randint(0, TAMANHO_POPULACAO - 1)
        if aptidoes[rival] > aptidoes[melhor]:  # Mantém o mais apto
            melhor = rival
    return populacao[melhor]  # Retorna o indivíduo mais apto

# Função de crossover (cruzamento) entre dois pais
def crossover(pai1, pai2):
    # Escolhe um ponto de corte aleatório para dividir os genomas
    ponto_corte = random.randint(1, TAMANHO_GENOMA - 1)
    # Gera dois filhos trocando genes após o ponto de corte
    filho1 = pai1[:ponto_corte] + pai2[ponto_corte:]
    filho2 = pai2[:ponto_corte] + pai1[ponto_corte:]
    return filho1, filho2  # Retorna os dois filhos gerados

# Função de mutação: altera bits aleatórios do genoma com uma pequena probabilidade
def mutacao(genoma):
    # Itera sobre cada gene do genoma
    for i in range(TAMANHO_GENOMA):
        if random.random() < TAXA_MUTACAO:  # Aplica mutação com uma probabilidade de 10%
            genoma[i] = 1 - genoma[i]  # Inverte o bit (0 -> 1, 1 -> 0)

# Função principal que executa o algoritmo genético
def algoritmo_genetico():
    populacao = gerar_populacao_inicial()  # Gera a população inicial
    
    # Executa o ciclo evolutivo por um número de gerações
    for geracao in range(GERACOES):
        # Capacidade de mochila aleatória para cada geração
        capacidade_mochila = random.randint(CAPACIDADE_MIN, CAPACIDADE_MAX)
        print(f'Capacidade da mochila na geração {geracao+1}: {capacidade_mochila}')

        # Calcula a aptidão de cada indivíduo na população com base na capacidade aleatória
        aptidoes = [calcular_aptidao(individuo, capacidade_mochila) for individuo in populacao]
        
        nova_populacao = []
        # Gera a nova população cruzando e mutando os indivíduos mais aptos
        while len(nova_populacao) < TAMANHO_POPULACAO:
            pai1 = selecao_torneio(populacao, aptidoes)  # Seleciona o primeiro pai
            pai2 = selecao_torneio(populacao, aptidoes)  # Seleciona o segundo pai
            filho1, filho2 = crossover(pai1, pai2)  # Aplica crossover para gerar dois filhos
            mutacao(filho1)  # Aplica mutação no primeiro filho
            mutacao(filho2)  # Aplica mutação no segundo filho
            nova_populacao.append(filho1)  # Adiciona o primeiro filho à nova população
            nova_populacao.append(filho2)  # Adiciona o segundo filho à nova população

        populacao = nova_populacao[:TAMANHO_POPULACAO]  # Substitui a população pela nova

        # Exibe a melhor aptidão da geração atual
        melhor_aptidao = max(aptidoes)
        print(f'Geração {geracao+1}: Melhor aptidão = {melhor_aptidao}')
    
    # Após todas as gerações, encontra e retorna o indivíduo com a maior aptidão
    melhor_indice = aptidoes.index(max(aptidoes))
    return populacao[melhor_indice]

# Executa o algoritmo genético
melhor_solucao = algoritmo_genetico()  # Executa o processo evolutivo
print('Melhor solução encontrada:', melhor_solucao)  # Exibe a melhor solução encontrada
capacidade_final = random.randint(CAPACIDADE_MIN, CAPACIDADE_MAX)  # Capacidade aleatória final
print('Capacidade final da mochila:', capacidade_final)  # Exibe a capacidade final
print('Valor total:', calcular_aptidao(melhor_solucao, capacidade_final))  # Exibe o valor total da melhor solução
