import numpy as np

# Função objetivo: minimizar a soma dos quadrados dos elementos de um vetor
# Essa função atinge seu valor mínimo quando todos os elementos de x são zero.
def esfera(x):
    return sum(x**2)

# Função para inicializar a população de vetores candidatos (soluções)
# tamanho_pop: quantidade de vetores (soluções)
# dimensao: número de variáveis em cada vetor (dimensão do problema)
# limites: intervalo [min, max] para os valores dos vetores
def inicializa_populacao(tamanho_pop, dimensao, limites):
    # Gera uma matriz aleatória com valores entre limites[0] e limites[1]
    return np.random.uniform(limites[0], limites[1], (tamanho_pop, dimensao))

# Implementação do algoritmo de Evolução Diferencial (DE)
# tamanho_pop: número de soluções na população
# dimensao: número de variáveis em cada vetor
# limites: limites inferior e superior para os valores dos vetores
# F: fator de mutação (controle de variação)
# CR: taxa de cruzamento (probabilidade de trocar valores com o vetor mutante)
# geracoes: número máximo de gerações (iterações do algoritmo)
def evolucao_diferencial(tamanho_pop, dimensao, limites, F, CR, geracoes):
    # Inicializa a população aleatoriamente
    populacao = inicializa_populacao(tamanho_pop, dimensao, limites)
    melhor_solucao = populacao[0]  # Inicializa a melhor solução como o primeiro indivíduo da população
    
    for g in range(geracoes):
        for i in range(tamanho_pop):
            # Seleciona três vetores aleatórios da população, excluindo o vetor atual (i)
            candidatos = np.random.choice(np.delete(np.arange(tamanho_pop), i), 3, replace=False)
            x1, x2, x3 = populacao[candidatos]
            
            # Mutação: cria um vetor mutante combinando os três vetores selecionados
            mutante = x1 + F * (x2 - x3)
            # Garante que o vetor mutante esteja dentro dos limites permitidos
            mutante = np.clip(mutante, limites[0], limites[1])
            
            # Cruzamento: combina o vetor original com o vetor mutante
            trial = np.copy(populacao[i])
            for j in range(dimensao):
                # Se um número aleatório for menor que CR, substitui a posição por um valor do mutante
                if np.random.rand() < CR:
                    trial[j] = mutante[j]
            
            # Seleção: se o vetor de teste (trial) for melhor que o original, substitui o original
            if esfera(trial) < esfera(populacao[i]):
                populacao[i] = trial
        
        # Após cada geração, atualiza a melhor solução encontrada
        melhor = populacao[np.argmin([esfera(ind) for ind in populacao])]
        if esfera(melhor) < esfera(melhor_solucao):
            melhor_solucao = melhor
    
    return melhor_solucao

# Definindo os parâmetros do problema
dimensao = 2  # Dimensão do problema (2 variáveis a serem otimizadas)
limites = [-5, 5]  # Limites de cada variável entre -5 e 5
F = 0.8  # Fator de mutação
CR = 0.9  # Taxa de cruzamento
geracoes = 1000  # Número de iterações do algoritmo
tamanho_pop = 20  # Número de soluções na população

# Executa o algoritmo de Evolução Diferencial
melhor_solucao = evolucao_diferencial(tamanho_pop, dimensao, limites, F, CR, geracoes)
print("Melhor solução encontrada:", melhor_solucao)
print("Valor da função objetivo:", esfera(melhor_solucao))