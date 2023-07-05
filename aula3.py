import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumtrapz

"""
Essa função é responsável por criar um gráfico do sinal f em relação ao eixo do tempo t. Aqui está o funcionamento de cada linha:
fig, ax1 = plt.subplots(): Cria uma nova figura e um conjunto de eixos para o gráfico.
ax1.plot(t, f, 'c-', linewidth=2, color='blue'): Plota o sinal f em relação ao tempo t com uma linha de cor azul.
ax1.axhline(y=0, color='k'): Adiciona uma linha horizontal em y=0 para representar o eixo horizontal.
ax1.axvline(x=0, color='k'): Adiciona uma linha vertical em x=0 para representar o eixo vertical.
ax1.set_xlabel(xLabel): Define o rótulo do eixo x (horizontal) do gráfico.
ax1.set_ylabel(yLabel): Define o rótulo do eixo y (vertical) do gráfico.
ax1.grid(True): Adiciona uma grade ao gráfico.
ax1.set_title(titulo): Define o título do gráfico.
fig.tight_layout(): Ajusta o espaçamento dos elementos do gráfico para que eles se ajustem adequadamente.
plt.show(): Mostra o gráfico na tela.
"""
def plotaSinal(f,t,titulo, xLabel, yLabel):
    fig, ax1 = plt.subplots()
    ax1.plot(t, f, 'c-', linewidth=2, color='blue')
    ax1.axhline(y=0, color='k')
    ax1.axvline(x=0, color='k')
    ax1.set_xlabel(xLabel)
    ax1.set_ylabel(yLabel)
    ax1.grid(True)
    ax1.set_title(titulo)
    fig.tight_layout()
    plt.show()


def main():
    t = np.linspace(0,7.97,1000)
    v = np.zeros(len(t))
    v2 = t**2
    for i in range (0,len(t)):
        if t[i]<=2.61:
            v[i] = 0.80*t[i]+1.5*np.sin(0.60*t[i])
        else:
            v[i]=3.59-0.45*t[i]

    plotaSinal(v,t,"gráfico de v(t)", "tempo", "velocidade")

    y = cumtrapz(v, t, initial=0)
    y2=cumtrapz(v2, t, initial=0)
    v2_dt = np.gradient(v, t)

    plotaSinal(y2,t,"Integral de v = y(t)", "tempo", "posicao")
    plotaSinal(v2_dt,t,"Derivada de x = dx/dt", "tempo", "aceleracao")

    velocidadeMaxima = max_velocidade = np.max(v)
    velocidadeMedia = np.mean(v)

main()