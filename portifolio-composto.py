import numpy as np

# Definindo os retornos esperados para três ativos
# R1, R2, R3 representam o retorno esperado de cada ativo
R = np.array([0.05, 0.1, 0.2])

# Matriz de covariância entre os ativos (risco conjunto entre eles)
cov_matrix = np.array([[0.1, 0.02, 0.01],
                       [0.02, 0.1, 0.03],
                       [0.01, 0.03, 0.2]])

# Função objetivo para otimizar o portfólio
# A função retorna uma combinação do retorno esperado e do risco (variância)
def objetivo(portfolio):
    retorno_esperado = np.dot(portfolio, R)  # Calcula o retorno esperado do portfólio
    risco = np.dot(portfolio.T, np.dot(cov_matrix, portfolio))  # Calcula o risco (variância)
    # O objetivo é maximizar o retorno e minimizar o risco. Por isso, o retorno é negativo.
    return -retorno_esperado + 0.5 * risco

# Função para inicializar a população de soluções (portfólios)
# Cada solução é um vetor com 3 valores representando a porcentagem de alocação em cada ativo
def inicializa_populacao(tamanho_pop, dimensao):
    # Gera vetores que somam 1, representando as alocações (usamos a distribuição de Dirichlet)
    populacao = np.random.dirichlet(np.ones(dimensao), size=tamanho_pop)
    return populacao

# Implementação da Evolução Diferencial para otimizar o portfólio
def evolucao_diferencial(tamanho_pop, dimensao, F, CR, geracoes):
    populacao = inicializa_populacao(tamanho_pop, dimensao)  # Inicializa a população
    melhor_solucao = populacao[0]  # Assume que a primeira solução é a melhor inicialmente
    
    for g in range(geracoes):
        for i in range(tamanho_pop):
            # Seleciona três vetores aleatórios
            candidatos = np.random.choice(np.delete(np.arange(tamanho_pop), i), 3, replace=False)
            x1, x2, x3 = populacao[candidatos]
            
            # Mutação: cria um novo vetor usando os três selecionados
            mutante = x1 + F * (x2 - x3)
            mutante = mutante / sum(mutante)  # Normaliza para que a soma seja 1 (regra do portfólio)
            
            # Cruzamento: mistura o vetor original com o vetor mutante
            trial = np.copy(populacao[i])
            for j in range(dimensao):
                if np.random.rand() < CR:
                    trial[j] = mutante[j]
            
            # Seleção: substitui se o novo vetor for melhor
            if objetivo(trial) < objetivo(populacao[i]):
                populacao[i] = trial
        
        # Atualiza a melhor solução após cada geração
        melhor = populacao[np.argmin([objetivo(ind) for ind in populacao])]
        if objetivo(melhor) < objetivo(melhor_solucao):
            melhor_solucao = melhor
    
    return melhor_solucao

# Definindo os parâmetros
dimensao = 3  # 3 ativos no portfólio
F = 0.8  # Fator de mutação
CR = 0.9  # Taxa de cruzamento
geracoes = 500  # Número de iterações
tamanho_pop = 20  # Número de portfólios na população

# Executa a Evolução Diferencial para encontrar o melhor portfólio
melhor_solucao = evolucao_diferencial(tamanho_pop, dimensao, F, CR, geracoes)
print("Melhor alocação de portfólio:", melhor_solucao)
print("Retorno esperado:", np.dot(melhor_solucao, R))
print("Risco (variância):", np.dot(melhor_solucao.T, np.dot(cov_matrix, melhor_solucao)))
