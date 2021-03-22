# Exercícios 

3.1. Use NumPy para gerar 1000 valores aleatórios em um vetor $\vec{x}$. Depois gere um vetor $\vec{y}$, tal que $y_i = 3x_i + 10 + e_i$, onde $e_i \sim N(0, 1)$. Por fim, estime um modelo de regressão simples de $Y$ em função de $X$.

pass

3.2. Faça uma função que gera uma matriz aleatória $X$ (escolha a distribuição) com $n$ linhas e $p$ colunas e um vetor $\vec{y}$, cujos valores são função das linhas de $X$ com adição de ruído normal, de média $0$ e variância $1$, e.g. $y_i = 3x_{i1} + 5x_{i2} + 10 + e_i$, onde $e_i \sim N(0, 1)$. Os parâmetros da função geradora devem incluir $n$, $p$ e a função geradora de $y$ (dica: use o operador **lambda**).

pass

3.3. Implemente uma classe *LinearRegression*, com os métodos:
   * *fit* que recebe uma matriz $X$ e um vetor $\vec{y}$ e ajusta uma regressão linear pelo [método dos mínimos quadrados](https://pt.wikipedia.org/wiki/M%C3%A9todo_dos_m%C3%ADnimos_quadrados), guardando os coeficientes e o intercept como atributos
   * *predict* que recebe uma matriz $X$ e estima os valores $\hat{y}$ correspondentes
   * *score* que recebe uma matriz $X$ e um vetor $\vec{y}$ e calcula o [erro quadrático médio](https://pt.wikipedia.org/wiki/Erro_quadr%C3%A1tico_m%C3%A9dio) de estimação
   
Use a função geradora da questão anterior para gerar $X_1$ e $\vec{y}_1$ e ajustar o seu modelo e depois gerar $X_2$ e $\vec{y}_2$ e avaliar o modelo ajustado.

pass

3.4. Faça uma função que executa o exercício 3.3 em uma simulação de Monte Carlo com $m$ repetições, armazenando os erros de estimação dos $m$ modelos ajustados. A função deve retornar os $m$ valores de erros obtidos, sua média e seu desvio-padrão.

pass

3.5. Faça uma função que aproxima a integral de uma função qualquer em um intervalo $[a, b]$, usando a [regra de Simpson](https://pt.wikipedia.org/wiki/Integra%C3%A7%C3%A3o_num%C3%A9rica). Use essa função em uma outra função que deve calcular $P(X < x_i)$, para $i = 1, \ldots, n$, onde $X \sim N(\mu, \sigma^2)$.

pass

