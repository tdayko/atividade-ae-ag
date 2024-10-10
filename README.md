# Atividade Algoritmos Evolucionários e Geneticos

## - [Esfera Quadratica](/esfera-quadratica.py): 
O Problema da Esfera Quadrática é um problema de otimização amplamente utilizado como benchmark em algoritmos de otimização, como o Algoritmo Evolucionário Diferencial (Differential Evolution, DE). ***O objetivo é minimizar a seguinte função:***

Função Esfera Quadrática:

$$
f(x) = \sum_{i=1}^{n} x_i^2
$$


Onde x=(x1,x2,...,xn)x=(x1​,x2​,...,xn​) é o vetor de entrada, e o objetivo é encontrar o vetor xx que minimiza a soma dos quadrados de seus componentes. O valor mínimo dessa função ocorre quando todos os xi=0xi​=0, resultando em ***f(x)=0f(x)=0***.

## - [Portifolio Composto](portifolio-composto.py):

O problema do portfólio consiste em alocar recursos financeiros entre diferentes ativos de forma a maximizar o retorno esperado e minimizar o risco associado. Este modelo é fundamental em finanças e investimentos, permitindo que os investidores tomem decisões informadas sobre onde investir seu capital.

## - Evolução Diferencial: 

A **Evolução Diferencial (DE)** é um algoritmo de otimização baseado em populações, criado por Storn e Price em 1997. Ele é usado principalmente para resolver problemas de otimização contínua e multidimensional, com a vantagem de ser simples e eficiente para funções complexas, sem precisar de derivadas ou gradientes.

## Como funciona a Evolução Diferencial?

A DE trabalha com uma **população de soluções**, que são vetores representando candidatos para o problema. A cada **iteração**, ela realiza três operações principais: **mutação, cruzamento** e **seleção**.

### 1. Inicialização
- Cria uma população inicial de soluções (vetores) aleatoriamente, dentro de um intervalo definido.
- Cada vetor da população é uma solução possível para o problema.

### 2. Mutação
- Para cada vetor da população, são escolhidos três outros vetores aleatórios.
- Um vetor mutante é gerado combinando as diferenças entre esses três vetores:

```text
mutante = x1 + F × (x2 - x3)
```

- Onde x1, x2 e x3 são os três vetores escolhidos, e F é um fator de escala que controla a intensidade da mutação.

### 3. Cruzamento
- O vetor mutante é cruzado com o vetor original, criando um **vetor de teste** (trial vector).
- Cada componente do vetor mutante tem uma chance de substituir o correspondente do vetor original, controlada por uma **taxa de cruzamento** (CR).

### 4. Seleção
- Avalia-se o vetor de teste usando a **função objetivo**.
- Se o vetor de teste for melhor (por exemplo, tiver um valor menor para funções de minimização), ele substitui o vetor original na próxima geração. Caso contrário, o vetor original é mantido.

### 5. Iteração
- Esse ciclo (mutação, cruzamento, seleção) se repete até que um critério de parada seja atingido, como o número máximo de gerações ou uma solução satisfatória.

## Parâmetros principais
- **Fator de mutação (F):** controla a amplitude da mutação (geralmente entre 0.5 e 1).
- **Taxa de cruzamento (CR):** probabilidade de o vetor mutante substituir o original (geralmente entre 0.7 e 0.9).
- **Tamanho da população:** número de vetores (soluções) por geração, depende da complexidade do problema.

## Vantagens
- **Simplicidade:** fácil de implementar e não precisa de derivadas, ótimo para funções complexas ou ruidosas.
- **Multidimensionalidade:** funciona bem com muitos problemas que envolvem várias variáveis.
- **Exploração e Exploração:** a combinação de mutação e cruzamento garante uma boa busca pelo espaço de soluções.

## Desvantagens
- **Sensível à parametrização:** a escolha dos parâmetros (F, CR, tamanho da população) pode impactar fortemente o desempenho.
- **Convergência lenta em alta dimensionalidade:** em problemas com muitas variáveis, a convergência pode ser mais lenta.


A Evolução Diferencial é muito usada em áreas como controle de sistemas, ajuste de parâmetros de redes neurais e otimização de funções complexas, com aplicações em engenharia e ciências.

## - [Problema Mochila Binaria + Extra](/problema-mochila-binaria.py):

O problema da mochila binária é um clássico em otimização combinatória. O objetivo é selecionar um subconjunto de itens, cada um com um peso e um valor, de forma a maximizar o valor total dos itens na mochila, sem exceder a capacidade de peso da mochila. 