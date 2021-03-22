# Python para Estatísticos

<!--<a href="https://circleci.com/gh/jupyter/jupyter-book"><img src="https://circleci.com/gh/jupyter/jupyter-book.svg?style=svg" class="left"></a>
<a href="https://codecov.io/gh/jupyter/jupyter-book"><img src="https://codecov.io/gh/jupyter/jupyter-book/branch/master/graph/badge.svg" class="left"></a>
<a href="https://doi.org/10.5281/zenodo.2799972"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.2799972.svg" class="left"></a>
<div style="clear:both;"></div>-->

Este material foi escrito com o objetivo de introduzir estatísticos e estudantes de Estatística aos conceitos fundamentais da linguagem Python, bem como apresentá-los às ferramentas que mais lhe podem ser úteis, incluindo bibliotecas de computação matemática, visualização de dados, manipulação de bases e bancos de dados, ferramentas de  aprendizagem de máquina, computação paralela, computação em GPU, inferência Bayesiana e criação e consumo de API's Web. 

Python é uma linguagem de programação interpretada, de alto nível e de propósito geral. Seu criador, Guido van Rossum, enfatizou **legibilidade** de código e sua abordagem de orientação a objetos permite que projetos de diversos tamanhos sejam desenvolvidos usando código simples, lógico e **fácil de entender**, devido a sua sintaxe clara. Além da orientação a objetos, Python também oferece suporte a outros paradigmas de programação, como programação estruturada e programação funcional. 

A filosofia central da linguagem foi resumida no documento [The Zen of Python (PEP 20)](https://www.python.org/dev/peps/pep-0020/) {cite}`petersZen2004`, que inclui frases como:

* Belo é melhor do que feio.
* Explícito é melhor do que implícito.
* Simples é melhor do que complexo.
* Complexo é melhor do que complicado.
* Legibilidade conta.
* Se a implementação é difícil de explicar, é uma má ideia.
* Se a implementação é fácil de explicar, deve ser uma boa ideia.

Python é visualmente mais "limpa" do que outras linguagens, além de ser mais intuitiva, pois frequentemente usa palavras da língua inglesa onde outras linguagens usariam pontuações. O nome da linguagem é um tributo ao grupo de comédia britânico Monty Python, o que inspirou os desenvolvedores a fazer com que a linguagem seja divertida de usar. Essa abordagem de desenvolvimento inspirou a criação do neologismo "pythonico", que quer dizer que o código é natural e está de acordo com a filosofia minimalita e de ênfase na legibilidade. Por outro lado, códigos difíceis de entender or ler são chamados de não-pythonicos. Usuários e admiradores de Python, sobretudo aqueles considerados mais experientes costumam er chamados de Pythonistas.




## Por que estudar Python?

Em 2017, o Stack Overflow, website de perguntas e respostas destinado a desenvolvedores, publicou um estudo sobre o rápido crescimento no interesse pela linguagem Python {cite}`robinsonBlog2017`. O estudo considerou apenas o interesse de usuários de países de alta renda e naturalmente avaliou apenas resultados até a sua publicação. A {numref}`python-growth`, obtida por meio da ferramenta [Stack Overflow Trends](https://insights.stackoverflow.com/trends), apresenta as curvas para as mesmas linguagens, considerando usuários de todo o mundo (o que muda as curvas em relação ao estudo citado) e resultados até o meio de 2019. Até o meio de 2012, Python era a sexta linguagem menos buscada das 7 analisadas, tornando-se a linguagem de maior interesse apenas 6 anos depois, no meio de 2018.


:::{figure-md} python-growth
<img src="images/python-growth.svg" alt="Crescimento da porcentagem de perguntas de várias linguagens de programação no Stack Overflow"/>

Crescimento da porcentagem de perguntas de várias linguagens de programação no Stack Overflow.
:::

Esse crescimento do interesse por Python extremamente acentuado a partir de 2012 está conectado ao avanço da área de ciência de dados e conhecimentos relacionados, como aprendizagem de máquina, big data, business analytics, entre outras. Python e R costumam ser as linguagens **mais citadas** por cientistas de dados em seus perfis em redes sociais como LinkedIn. Segundo análise da Initiative for Analytics and Data Science Standards (IADSS) {cite}`fayyadSkill2019`, **100%** dos cientistas de dados mencionam conhecimento de Python em seus perfis, enquanto 84% mencionam R. Além disso, como mostra a {numref}`job-listings`, o mercado de trabalho abraçou essas duas linguagens, com **mais de 70%** dos anúncios de vagas para cientistas de dados, retirados de sites como LinkedIn, Indeed, SimplyHired e Monster em outubro de 2018, mencionando Python e mais de 60% mencionando R.

:::{figure-md} job-listings
<img src="images/job-listings.png" alt="20 habilidades mais mencionadas em anúncios de vagas para cientistas de dados"/>

20 habilidades mais mencionadas em anúncios de vagas para cientistas de dados {cite}`haleSkill2018`.
:::

Para completar esta motivação, geramos a tabela abaixo usando Python e a biblioteca _pandas_, dando um gostinho do que vem por aí. Os dados foram obtidos por meio da plataforma [Google Trends](https://trends.google.com.br/trends/) e representam o interesse mundial por quatro tópicos de buscas no Google: Python, R, aprendizagem de máquina e ciência de dados. A quantidade de buscas de cada tópico foi medida semanalmente. O código abaixo calcula o índice de correlação de Spearman do interesse semanal de cada um dos tópicos e todos os outros. Os valores calculados indicam que há relação entre o crescimento do interesse em ciência de dados e aprendizagem de máquina e a quantidade de buscas relacionadas a R e Python. Esta última apresentou correlações quase perfeitas com ciência de dados e aprendizagem de máquina, mostrando que o seu crescimento nos últimos 5 anos está **diretamente conectado** ao crescimento da importância dessas áreas.

import pandas as pd
url = 'https://tmfilho.github.io/pyestbook/data/google-trends-timeline.csv'
trends = pd.read_csv(url, index_col=0, parse_dates=True)

trends.corr(method='spearman')

O código abaixo gera um gráfico com as quatro séries temporais de interesse. Os valores são relativos ao maior valor de interesse no período, que nesse caso equivale ao interesse por Python em setembro de 2019.

import matplotlib.pyplot as plt

plot = trends.plot()
plt.xlabel('Semana', fontsize=16)
plt.show()




```{toctree}
:hidden:
:titlesonly:
:numbered: True

guide/01_first
objects/01_first
math/01_first
solutions/intro
references
```
