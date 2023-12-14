import numpy as np
import random
import math
import matplotlib.pyplot as plt

def calcula_distancia(cidades, rota):
    distancia_total = 0
    for i in range(len(rota) - 1):
        cidade_atual = rota[i]
        proxima_cidade = rota[i + 1]
        distancia_total += np.linalg.norm(cidades[cidade_atual] - cidades[proxima_cidade])
    return distancia_total

def simulated_annealing(cidades, temperatura_inicial=1000, taxa_resfriamento=0.95, num_iteracoes=1000):
    num_cidades = len(cidades)
    rota_atual = list(range(num_cidades))

    melhor_rota = rota_atual
    melhor_distancia = calcula_distancia(cidades, melhor_rota)

    temperatura = temperatura_inicial

    for _ in range(num_iteracoes):
        vizinho = list(rota_atual)
        i, j = sorted(random.sample(range(1, num_cidades), 2)) 
        vizinho[i:j+1] = reversed(vizinho[i:j+1])

        nova_distancia = calcula_distancia(cidades, vizinho)

        delta_distancia = nova_distancia - melhor_distancia

        if delta_distancia < 0 or random.uniform(0, 1) < math.exp(-delta_distancia / temperatura):
            rota_atual = list(vizinho)
            melhor_distancia = nova_distancia

        if melhor_distancia < calcula_distancia(cidades, melhor_rota):
            melhor_rota = list(rota_atual)

        temperatura *= taxa_resfriamento

    return melhor_rota, melhor_distancia

# Função para plotar o gráfico da melhor rota
def plotar_rota(cidades, rota):
    coordenadas = cidades[rota]
    plt.plot(coordenadas[:, 0], coordenadas[:, 1], 'o-')

    for i, cidade in enumerate(rota):
        plt.annotate(str(cidade), (cidades[cidade, 0], cidades[cidade, 1]), textcoords="offset points", xytext=(0,5), ha='center')

    plt.title('Melhor Rota')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')

    plt.annotate("Início/Fim", (cidades[rota[0], 0], cidades[rota[0], 1]), textcoords="offset points", xytext=(0,10), ha='center')
    plt.plot([cidades[rota[-1], 0], cidades[rota[0], 0]], [cidades[rota[-1], 1], cidades[rota[0], 1]], 'C0')
    plt.show()


np.random.seed(42) 
num_cidades = 10
cidades = np.random.rand(num_cidades, 2)  # Coordenadas x, y das cidades

melhor_rota, melhor_distancia = simulated_annealing(cidades)

print("Melhor rota encontrada:", melhor_rota)

plotar_rota(cidades, melhor_rota)
