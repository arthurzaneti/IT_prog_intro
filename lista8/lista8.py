#________________________________________1_____________________________________________
import numpy as np
import matplotlib.pyplot as plt

class AproximacaoPolinomial:
    def __init__(self, grau=None):
        self.grau = grau
        self.coeficientes = None

    def ajustar(self, x, y):
        self.coeficientes = np.polyfit(x, y, self.grau)

    def avaliar(self, x):
        p = np.poly1d(self.coeficientes)
        return p(x)

    def plotar(self, x, y):
        if self.coeficientes is None:
            raise ValueError
        plot_x = np.linspace(min(x), max(x), 1000)
        plot_y = self.avaliar(plot_x)
        plt.scatter(x, y, color='red', label='Pontos Originais')
        plt.plot(plot_x, plot_y, color='blue', label=f'Polinômio Grau {self.grau}')
        plt.legend()
        plt.show()
"""
x = np.random.uniform(0, 10, 10)
y = np.random.uniform(0, 10, 10)
ap = AproximacaoPolinomial(10)
ap.ajustar(x, y)
ap.plotar(x, y)
"""
#________________________________________2_____________________________________________

def encontrar_grau_ideal(x, y, erro_tolerancia=1e-3, grau_max=10):
    """A ideia é ir ajustando um polinômio para cada grau e vendo se o erro
    qudrático médio esta abaixo da tolerância. Supostamente o erro vai decrescer 
    monotônicamente conforme o grau aumenta mas para garantir estou guardando essa
    variável melhor grau. Caso algum ajuste tenha MSE abaixo de erro_tolerancia eu
    retorno esse ajuste, mas se nenhum atingir essa cota eu retorno o polinômio do
    melhor_grau"""
    melhor_grau = 0
    menor_erro = float('inf')
    for grau in range(1, grau_max + 1):
        modelo = AproximacaoPolinomial(grau)
        modelo.ajustar(x, y)
        y_pred = modelo.avaliar(x)
        erro = np.mean((y - y_pred) ** 2)
        if erro < erro_tolerancia:
            melhor_grau = grau
            break
        if erro < menor_erro:
            menor_erro = erro
            melhor_grau = grau
    return melhor_grau

"""
# Conjunto de teste
np.random.seed(0)
x = np.random.uniform(0, 10, 20)
y = 3 * x**2 - 5 * x + 2 + np.random.normal(0, 10, len(x))  # Polinômio de grau 2 com ruído

grau_ideal = encontrar_grau_ideal(x, y, erro_tolerancia=1, grau_max=12)
ap = AproximacaoPolinomial(grau_ideal)
ap.ajustar(x, y)
print(f"Grau ideal encontrado: {grau_ideal}")
ap.plotar(x, y)
"""

#________________________________________3_____________________________________________
from scipy.optimize import minimize
from generate_points import generate_points

def aproximar_reta(x, y, error_func = None):
    if error_func == None:
        def erro(params):
            a, b = params
            return np.sum(np.abs(a * x + b - y))
        error_func = erro
    
    inicial = [0, 0]
    resultado = minimize(error_func, inicial, method='BFGS')
    return resultado.x

ms = [64, 128, 256, 512, 1024]
"""
for m in ms:
    x, y = generate_points(m)
    a, b = aproximar_reta(x, y)
    print(f"Para m = {m}, coeficientes encontrados: a = {a}, b = {b}")
    
    reta_y = a * x + b

    plt.scatter(x, y, color='red', label='Pontos Originais')
    plt.plot(x, reta_y, color='blue', label=f'Reta: y = {a:.2f}x + {b:.2f}')
    plt.title(f"Ajuste para m = {m}")
    plt.legend()
    plt.show()
"""


def error_func(params):
    a, b = params
    return np.sum((a * x + b - y)**2)

for m in ms:
    x, y = generate_points(m)
    a, b = aproximar_reta(x, y, error_func)
    print(f"Para m = {m}, coeficientes encontrados: a = {a}, b = {b}")
    
    reta_y = a * x + b

    plt.scatter(x, y, color='red', label='Pontos Originais')
    plt.plot(x, reta_y, color='blue', label=f'Reta: y = {a:.2f}x + {b:.2f}')
    plt.title(f"Ajuste para m = {m}")
    plt.legend()
    plt.show()

""" As vantagens de um ajuste sobre o outro são pequenas. Minimizar o erro absoluto é 
certamente mais simples e é um método mais robusto para lidar com outliers. Porém, em geral
o mais comum é o MSE (ou EQM em português) pois a função que queremos minimizar se torna 
diferenciável. """